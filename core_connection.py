import Queue
import socket
import sys
import time
import traceback
import  select
import  threading
import  Queue

sys.path.append("../api")
sys.path.append("../api/py_lib/bsc")
sys.path.append("../api/py_lib/cstruct")
sys.path.append("../api/core/")
sys.path.append("../api/py_lib/msg/msg")
sys.path.append("../api/TPO/Core.i3/src")
import msg_parser
import bsc
import info_ch_params

CORE_VER = 0x00000001  # Core version.
CORE_PORT = 50004  # TCP/IP port for core.
SW_VER_TYPE_CORE = 0x01
CORE_REQ_TIMEOUT = 20.0

sys.path.insert(0, "dir_test")
from duck import *

class TestLib(threading.Thread):
    def __init__(self):
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

    ####################################################################################################################
    def waitForStop(self):
        """
        """
        self.join()
        self.sckt.close()


    def run(self):
        self.sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # try:
        self.sckt.connect(("localhost", CORE_PORT))
        print 'connect'
        while not self.stopEvent.isSet():
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
                            print "pechalka"
                            # self.log("Core msg parsing error:\n" + str(e))
                        else:
                            self.handleCoreMsg(coreMsg=coreMsg)

    def handleCoreMsg(self, coreMsg):
        """
        """
        if (coreMsg.isType(self.cliCoreProtoMsgMod.GetSwVersionConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.OpenTkpaConnConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.CloseTkpaConnConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.GetKpaModeConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.SetKpaModeConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.WriteMkoMsgConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.ReadMkoMsgConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.WriteMkoPkConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.SetBiZoneConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.GetBiZoneConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.SetArrConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.GetArrConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.GetDkpmPowerConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.GetDrivePowerConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.ReadBeReg16Conf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.WriteBeReg16Conf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.GetRefChPowerConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.GetDnpsPowerConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.GetDnpsConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.SetDnpsConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.GetSkvtPowerConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.SetBePowerConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.SetStrPowerConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.GetBpuPowerConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.SetCoreParamsConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.GetCoreParamsConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.FkConf) or
                coreMsg.isType(self.cliCoreProtoMsgMod.GetStrHeatVoltConf)):

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
        # elif coreMsg.isType(self.cliCoreProtoMsgMod.AnalogTmiInd):
        #     # Handle analog telemetry indication.
        #     self.handler_analogTmi(coreMsg)
        #
        # elif coreMsg.isType(self.cliCoreProtoMsgMod.SliKpaInd):
        #     # Handle SlI Kpa telemetry indication.
        #     self.handler_SliKpaTmi(coreMsg)

        else:
            # Unknown confirm or indication.
            print "Unknown confirm or indication:\n" + str(coreMsg)
            # self.log("Unknown confirm or indication:\n" + str(coreMsg))

    def getSwVersion(self, verType):
        """
        """
        req = self.cliCoreProtoMsgMod.GetSwVersionReq(verType=self.cliCoreProtoMsgMod.SwVerType(verType))
        print req
        self.sendCoreReq(req)
        print "send request"
        conf = self.getCoreConf(self.cliCoreProtoMsgMod.GetSwVersionConf)
        print "get request"
        ver = int(conf.getField("ver"))
        print  ver
        return ver

    def sendCoreReq(self, coreReq):
        """
        """
        s = self.bscEngine.makeMsg(self.cliCoreProtoMsgParser.serialize(coreReq))
        self.sckt.sendall(s)
        self.coreConf = None
        self.reqStartTime = self.timeSrv.clock()


    def getCoreConf(self, confType):
        """
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



if __name__ == '__main__':
    testLib = TestLib()
    testLib.start()
    time.sleep(0.5)
    testLib.getSwVersion(SW_VER_TYPE_CORE)


