import socket
import sys
import select
import threading
import Queue


# append many paths...
import time

sys.path.append("C:\Users\lacie\PycharmProjects\\test_lib\\client.py")
sys.path.append("../api")
sys.path.append("../api/py_lib/bsc")
sys.path.append("../api/py_lib/cstruct")
sys.path.append("../api/core/")
sys.path.append("../api/py_lib/msg/msg")
sys.path.append("../api/TPO/Core.i3/src")
sys.path.append("some components/")
import msg_parser
import bsc
import info_ch_params
import msg_int_field
import analog_tmi_params
import sli_kpa_tmi_params

from time_srv import *
from constants_table import *


class client(threading.Thread):
    def __init__(self):
        # inherits this class for multithreading
        threading.Thread.__init__(self)
        self.timeSrv = TimeSrv()
        self.bscEngine = bsc.Bsc()
        self.stopEvent = threading.Event()

        self.cliCoreProtoMsgParser = msg_parser.MsgParser("../api/core/cli_core_proto_msg.xml")
        self.cliCoreProtoMsgMod = self.cliCoreProtoMsgParser.getMsgModule()
        # Core msg stuff.
        self.coreReq = None
        self.coreConf = None
        self.reqStartTime = None
        self.fromCoreMsgQueue = Queue.Queue()
        self.toCoreReqQueue = Queue.Queue()
        self.isTkpaConn = False

        # MKO telemetry
        self.tmiMko = None

        # Analog telemetry
        self.analogTmi = None

        # SlI Kpa telemetry
        self.sliKpaTmi = None

        # Info channel stuff.
        self.infoChFrameQueue = Queue.Queue()
        self.InfoChIfgPacketQueue = Queue.Queue()
        self.InfoChVeloPacketQueue = Queue.Queue()


    def stop(self):
        """
        """
        self.stopEvent.set()


    def waitForStop(self):
        """
        """
        self.join()
        self.sckt.close()


    def run(self):
        """
        redefined method of class Thread. it called then starts second thread.
        connect to core and launch loop (while not stopped) to get and handle messages from core
        """
        #  init socket and connect to core
        self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # try:
        self.sckt.connect(("localhost", CORE_PORT))
        print "connect"
        while not self.stopEvent.isSet():
            # await for message. if get data or pass 10 msec - try to get this message and parse it
            rdSockList, wrSockList, excList = select.select([self.sckt], [], [], 0.01)
            if len(rdSockList):
                try:
                    data = self.sckt.recv(1024)
                except:
                    data = None
                if not data:
                    self.sckt.close()
                    self.stop()
                else:
                    # Parse BSC stream.
                    coreMsgStrList = self.bscEngine.parseRxData(data)
                    for coreMsgStr in coreMsgStrList:
                        # Make primitive from string.
                        try:
                            coreMsg = self.cliCoreProtoMsgParser.deserialize(coreMsgStr)
                            # print coreMsg
                        except Exception, e:
                            print ("Core msg parsing error:\n" + str(e))
                        else:
                            # if all is ok - parse message
                            self.handleCoreMsg(coreMsg=coreMsg)


    def connTkpa(self):
        """
        """
        req = self.cliCoreProtoMsgMod.OpenTkpaConnReq()
        print "conn tkpa"
        print req
        self.sendCoreReq(req)
        self.getCoreConf(self.cliCoreProtoMsgMod.OpenTkpaConnConf)

    def disconnTkpa(self):
        """
        """
        req = self.cliCoreProtoMsgMod.CloseTkpaConnReq()
        self.sendCoreReq(req)
        self.getCoreConf(self.cliCoreProtoMsgMod.CloseTkpaConnConf)

    def handleCoreMsg(self, coreMsg):
        """
        handle message from core. this thing scare me, but looks not very complicated
        """
        if (coreMsg.isType(self.cliCoreProtoMsgMod.GetSwVersionConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.OpenTkpaConnConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.CloseTkpaConnConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.GetKpaModeConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.SetKpaModeConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.WriteMkoMsgConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.ReadMkoMsgConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.WriteMkoPkConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.SetBiZoneConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.GetBiZoneConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.SetArrConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.GetArrConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.GetDkpmPowerConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.GetDrivePowerConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.ReadBeReg16Conf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.WriteBeReg16Conf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.GetRefChPowerConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.GetDnpsPowerConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.GetDnpsConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.SetDnpsConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.GetSkvtPowerConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.SetBePowerConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.SetStrPowerConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.GetBpuPowerConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.SetCoreParamsConf) or
                # coreMsg.isType(self.cliCoreProtoMsgMod.GetCoreParamsConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.FkConf)): #or
                # coreMsg.isType(self.cliCoreProtoMsgMod.GetStrHeatVoltConf)):

            self.coreConf = coreMsg

        elif coreMsg.isType(self.cliCoreProtoMsgMod.TkpaConnStatusInd):
            # Handle TKPA connection status.
            isConnected = int(coreMsg.getField("isConnected"))
            if isConnected:
                ### Connection with TKPA set.
                self.isTkpaConn = True
            else:
                ### Connection with TKPA lost.
                self.isTkpaConn = False

        elif coreMsg.isType(self.cliCoreProtoMsgMod.InfoChCntInd):
            # Info channel counters.
            pass

        elif coreMsg.isType(self.cliCoreProtoMsgMod.InfoChFrameInd):
            # Info channel frame.
            strDataList = coreMsg.getField("data").getList()
            dataList = []
            for item in strDataList:
                dataList.append(int(item))
            self.infoChFrameQueue.put(dataList)

        elif coreMsg.isType(self.cliCoreProtoMsgMod.InfoChIfgPacketInd):
            # Info channel IFG packet.
            strPointList = coreMsg.getField("points").getList()
            pointList = []
            for item in strPointList:
                pointList.append(int(item))
            ifgPacketParams = info_ch_params.InfoChIfgPacketParams(pointList=pointList)
            ifgPacketParams["rcvNum"] = int(coreMsg.getField("rcvNum"))
            ifgPacketParams["pixNum"] = int(coreMsg.getField("pixNum"))
            ifgPacketParams["bitPerPoint"] = int(coreMsg.getField("bitPerPoint"))
            ifgPacketParams["pointNum"] = int(coreMsg.getField("pointNum"))
            ifgPacketParams["highIfgBase"] = int(coreMsg.getField("highIfgBase"))
            ifgPacketParams["ifgEnd"] = int(coreMsg.getField("ifgEnd"))
            ifgPacketParams["ifgId"] = int(coreMsg.getField("ifgId"))
            ifgPacketParams["lowIfgBase"] = int(coreMsg.getField("lowIfgBase"))
            ifgPacketParams["disp"] = int(coreMsg.getField("disp"))
            self.InfoChIfgPacketQueue.put(ifgPacketParams)

        elif coreMsg.isType(self.cliCoreProtoMsgMod.InfoChVeloPacketInd):
            # Info channel velocity packet.
            strPointList = coreMsg.getField("points").getList()
            pointList = []
            for item in strPointList:
                pointList.append(int(item))
            veloPacketParams = info_ch_params.InfoChVeloPacketParams(pointList=pointList)
            veloPacketParams["ifgId"] = int(coreMsg.getField("ifgId"))
            veloPacketParams["pointNum"] = int(coreMsg.getField("pointNum"))
            self.InfoChVeloPacketQueue.put(veloPacketParams)

        #not need now
        # elif coreMsg.isType(self.cliCoreProtoMsgMod.MkoTmiInd):
        #     # Handle MKO telemetry indication.
        #     self.handler_tmiMko(coreMsg)
        #
        elif coreMsg.isType(self.cliCoreProtoMsgMod.AnalogTmiInd):
            # Handle analog telemetry indication.
            self.handler_analogTmi(coreMsg)

        elif coreMsg.isType(self.cliCoreProtoMsgMod.SliKpaInd):
            # Handle SlI Kpa telemetry indication.
            self.handler_SliKpaTmi(coreMsg)

        else:
            # Unknown confirm or indication.
            print "Unknown confirm or indication:\n" + str(coreMsg)
            # self.log("Unknown confirm or indication:\n" + str(coreMsg))


    def get_sw_version(self, verType):
        """
        get core version. it's take request type (SW_VER_TYPE_CORE = 0x01), then send through socket and get confirm,
        parse it and return version
        """
        req = self.cliCoreProtoMsgMod.GetSwVersionReq(verType=self.cliCoreProtoMsgMod.SwVerType(verType))
        print req
        self.sendCoreReq(req)
        print "send request"
        conf = self.getCoreConf(self.cliCoreProtoMsgMod.GetSwVersionConf)
        print "get request"
        ver = int(conf.getField("ver"))
        print ver
        return ver


    def sendCoreReq(self, coreReq):
        """
        this method just send command to core.
        """
        # parse (deparse?.. it's serialize. just serialize) message
        s = self.bscEngine.makeMsg(self.cliCoreProtoMsgParser.serialize(coreReq))
        # send message through socket
        self.sckt.sendall(s)
        self.coreConf = None
        # start clock
        self.reqStartTime = self.timeSrv.clock()


    def getCoreConf(self, confType):
        """
        this method return request from core. while data is empty - infinitive loop and await for data.
        if time ends (imeSrv = 20 sec) - exception. if status != ok, then another exception.
        if all is ok - return confirm
        """
        while True:
            if self.coreConf != None:
                status = int(self.coreConf.getField("status").code)
                if status == self.cliCoreProtoMsgMod.Status.STATUS_OK:
                    break
                else:
                    print "Core confirm status error\n" + str(self.coreConf)
            if (self.timeSrv.clock() - self.reqStartTime) > CORE_REQ_TIMEOUT:
                print "Core request timeout\n" + str(self.coreReq)
        return self.coreConf


    def getAnalogTmi(self):
        """
        """
        return self.analogTmi


    def getSliKpaTmi(self):
        """
        """
        return self.sliKpaTmi


    def setBePower(self, on):
        """
        """
        req = self.cliCoreProtoMsgMod.SetBePowerReq(on = msg_int_field.Uint16(on))
        self.sendCoreReq(req)
        self.getCoreConf(self.cliCoreProtoMsgMod.SetBePowerConf)


    def writeFk(self, fk):
        """
        """
        req = self.cliCoreProtoMsgMod.FkReq(fk = self.cliCoreProtoMsgMod.Fk(fk))
        self.sendCoreReq(req)
        self.getCoreConf(self.cliCoreProtoMsgMod.FkConf)

    ####################################################################################################################


    def handler_analogTmi(self, coreMsg):
        """
        """
        analogTmiParams = analog_tmi_params.AnalogTmiParams()

        analogTmiParams["VIP1PT1"] = int(coreMsg.getField("VIP1PT1"))
        analogTmiParams["VIP2PT2"] = int(coreMsg.getField("VIP2PT2"))
        analogTmiParams["V5VIP1T3"] = int(coreMsg.getField("V5VIP1T3"))
        analogTmiParams["V5VIP2T4"] = int(coreMsg.getField("V5VIP2T4"))
        analogTmiParams["VIP1VT5"] = int(coreMsg.getField("VIP1VT5"))
        analogTmiParams["VIP2VT6"] = int(coreMsg.getField("VIP2VT6"))
        analogTmiParams["ARRT7"] = int(coreMsg.getField("ARRT7"))
        analogTmiParams["ARZT8"] = int(coreMsg.getField("ARZT8"))
        analogTmiParams["PDAT9"] = int(coreMsg.getField("PDAT9"))
        analogTmiParams["ZO1T10"] = int(coreMsg.getField("ZO1T10"))
        analogTmiParams["SB11T11"] = int(coreMsg.getField("SB11T11"))
        analogTmiParams["ZO2T12"] = int(coreMsg.getField("ZO2T12"))
        analogTmiParams["SB1013"] = int(coreMsg.getField("SB1013"))
        analogTmiParams["DOPT14"] = int(coreMsg.getField("DOPT14"))
        analogTmiParams["OPRT15"] = int(coreMsg.getField("OPRT15"))
        analogTmiParams["PPTOT16"] = int(coreMsg.getField("PPTOT16"))
        analogTmiParams["PPTRT17"] = int(coreMsg.getField("PPTRT17"))
        analogTmiParams["NSTRT18"] = int(coreMsg.getField("NSTRT18"))
        analogTmiParams["LOT19"] = int(coreMsg.getField("LOT19"))
        analogTmiParams["LRT20"] = int(coreMsg.getField("LRT20"))
        analogTmiParams["URFOT21"] = int(coreMsg.getField("URFOT21"))
        analogTmiParams["URFRT22"] = int(coreMsg.getField("URFRT22"))
        analogTmiParams["RKOT23"] = int(coreMsg.getField("RKOT23"))
        analogTmiParams["RKRT24"] = int(coreMsg.getField("RKRT24"))
        analogTmiParams["SB1T25"] = int(coreMsg.getField("SB1T25"))
        analogTmiParams["SB2T26"] = int(coreMsg.getField("SB2T26"))
        analogTmiParams["SB3T27"] = int(coreMsg.getField("SB3T27"))
        analogTmiParams["SB4T28"] = int(coreMsg.getField("SB4T28"))
        analogTmiParams["SB5T29"] = int(coreMsg.getField("SB5T29"))
        analogTmiParams["SB6T30"] = int(coreMsg.getField("SB6T30"))
        analogTmiParams["SB7T31"] = int(coreMsg.getField("SB7T31"))
        analogTmiParams["SB8T32"] = int(coreMsg.getField("SB8T32"))
        analogTmiParams["SB9T33"] = int(coreMsg.getField("SB9T33"))
        analogTmiParams["TLOT34"] = int(coreMsg.getField("TLOT34"))
        analogTmiParams["TLRT35"] = int(coreMsg.getField("TLRT35"))
        analogTmiParams["SB12T36"] = int(coreMsg.getField("SB12T36"))
        analogTmiParams["SB13T37"] = int(coreMsg.getField("SB13T37"))
        analogTmiParams["TTR1T38"] = int(coreMsg.getField("TTR1T38"))
        analogTmiParams["TTR2T39"] = int(coreMsg.getField("TTR2T39"))
        analogTmiParams["TMI3T40"] = int(coreMsg.getField("TMI3T40"))
        analogTmiParams["TMI4T41"] = int(coreMsg.getField("TMI4T41"))
        analogTmiParams["TTKT42"] = int(coreMsg.getField("TTKT42"))
        analogTmiParams["DATT43"] = int(coreMsg.getField("DATT43"))

        self.analogTmi = analogTmiParams

        ####################################################################################################################


    def handler_SliKpaTmi(self, coreMsg):
        """
        """
        sliKpaTmiParams = sli_kpa_tmi_params.SliKpaTmiParams()

        sliKpaTmiParams["pwrBE_current"] = int(coreMsg.getField("pwrBE_current"))
        sliKpaTmiParams["pwrBE_voltage"] = int(coreMsg.getField("pwrBE_voltage"))
        sliKpaTmiParams["pwrBE_state"] = int(coreMsg.getField("pwrBE_state"))

        sliKpaTmiParams["pwrBE_bit_PwrOnLimitEx"] = int(coreMsg.getField("pwrBE_bit_PwrOnLimitEx"))
        sliKpaTmiParams["pwrBE_bit_Overcurrent"] = int(coreMsg.getField("pwrBE_bit_Overcurrent"))
        sliKpaTmiParams["pwrBE_bit_Overvoltage"] = int(coreMsg.getField("pwrBE_bit_Overvoltage"))
        sliKpaTmiParams["pwrBE_bit_PowerGood"] = int(coreMsg.getField("pwrBE_bit_PowerGood"))
        sliKpaTmiParams["pwrBE_bit_KS"] = int(coreMsg.getField("pwrBE_bit_KS"))

        sliKpaTmiParams["pwrSTR1_current"] = int(coreMsg.getField("pwrSTR1_current"))
        sliKpaTmiParams["pwrSTR1_voltage"] = int(coreMsg.getField("pwrSTR1_voltage"))
        sliKpaTmiParams["pwrSTR1_state"] = int(coreMsg.getField("pwrSTR1_state"))

        sliKpaTmiParams["pwrSTR1_bit_PwrOnLimitEx"] = int(coreMsg.getField("pwrSTR1_bit_PwrOnLimitEx"))
        sliKpaTmiParams["pwrSTR1_bit_Overcurrent"] = int(coreMsg.getField("pwrSTR1_bit_Overcurrent"))
        sliKpaTmiParams["pwrSTR1_bit_Overvoltage"] = int(coreMsg.getField("pwrSTR1_bit_Overvoltage"))
        sliKpaTmiParams["pwrSTR1_bit_PowerGood"] = int(coreMsg.getField("pwrSTR1_bit_PowerGood"))

        sliKpaTmiParams["pwrSTR2_current"] = int(coreMsg.getField("pwrSTR2_current"))
        sliKpaTmiParams["pwrSTR2_voltage"] = int(coreMsg.getField("pwrSTR2_voltage"))
        sliKpaTmiParams["pwrSTR2_state"] = int(coreMsg.getField("pwrSTR2_state"))

        sliKpaTmiParams["pwrSTR2_bit_PwrOnLimitEx"] = int(coreMsg.getField("pwrSTR2_bit_PwrOnLimitEx"))
        sliKpaTmiParams["pwrSTR2_bit_Overcurrent"] = int(coreMsg.getField("pwrSTR2_bit_Overcurrent"))
        sliKpaTmiParams["pwrSTR2_bit_Overvoltage"] = int(coreMsg.getField("pwrSTR2_bit_Overvoltage"))
        sliKpaTmiParams["pwrSTR2_bit_PowerGood"] = int(coreMsg.getField("pwrSTR2_bit_PowerGood"))

        self.sliKpaTmi = sliKpaTmiParams
