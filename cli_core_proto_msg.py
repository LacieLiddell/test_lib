from msg_int_field import *
from msg_enum_field import *
from msg_struct_field import *
from msg_array_field import *
from msg_float_field import *
from msg import *

####################################################################################################
# Type aliases.
####################################################################################################

####################################################################################################
# Constant definitions.
####################################################################################################

INFO_CH_FRAME_SIZE = int(112)

####################################################################################################
# Enum definitions.
####################################################################################################

####################################################################################################
class ErrLevel(Enum16):
	ERR_LEVEL_OK = 0x0000
	ERR_LEVEL_CORE = 0x0001
	ERR_LEVEL_TKPA = 0x0002
	ERR_LEVEL_BE = 0x0003

	nameDict = {
			ERR_LEVEL_OK: "ERR_LEVEL_OK",
			ERR_LEVEL_CORE: "ERR_LEVEL_CORE",
			ERR_LEVEL_TKPA: "ERR_LEVEL_TKPA",
			ERR_LEVEL_BE: "ERR_LEVEL_BE",
	}

	def __init__(self, code=ERR_LEVEL_OK, name="ErrLevel"):
		Enum16.__init__(self, code)
		self.setName(name)

####################################################################################################
class Status(Enum16):
	STATUS_OK = 0x0000
	STATUS_ERROR = 0x0001
	STATUS_UNKNOWN_REQ = 0x0002
	STATUS_INVALID_REQ = 0x0003
	STATUS_MKO_ERROR = 0x0004
	STATUS_CONF_TIMEOUT = 0x0005
	STATUS_INVALID_CONF = 0x0006
	STATUS_PK_NOT_DONE = 0x0007
	STATUS_KPA_CONNECTION_CONN_ERROR = 0x0010
	STATUS_KPA_CONNECTION_SEND_ERROR = 0x0011
	STATUS_KPA_CONNECTION_RECEIVE_ERROR = 0x0012
	STATUS_CORE_REQ_HANDLING_TIMEOUT = 0x0080
	STATUS_CORE_COREPARAMS_APPLY_ERROR = 0x0081
	STATUS_MKO_WRITE_CRC_ERROR = 0x0100
	STATUS_MKO_READ_CRC_ERROR = 0x0101
	STATUS_TECHN_UNKNOWN_REQ = 0x0102
	STATUS_TECHN_ACCESS_DENIED = 0x0103
	STATUS_TECHN_REQ_PARAM_ERROR = 0x0104
	STATUS_TECHN_RESP_PARAM_ERROR = 0x0105
	STATUS_TECHN_RESP_TIMEOUT = 0x0106
	STATUS_TECHN_UNKNOWN_STATUS = 0x0107

	nameDict = {
			STATUS_OK: "STATUS_OK",
			STATUS_ERROR: "STATUS_ERROR",
			STATUS_UNKNOWN_REQ: "STATUS_UNKNOWN_REQ",
			STATUS_INVALID_REQ: "STATUS_INVALID_REQ",
			STATUS_MKO_ERROR: "STATUS_MKO_ERROR",
			STATUS_CONF_TIMEOUT: "STATUS_CONF_TIMEOUT",
			STATUS_INVALID_CONF: "STATUS_INVALID_CONF",
			STATUS_PK_NOT_DONE: "STATUS_PK_NOT_DONE",
			STATUS_KPA_CONNECTION_CONN_ERROR: "STATUS_KPA_CONNECTION_CONN_ERROR",
			STATUS_KPA_CONNECTION_SEND_ERROR: "STATUS_KPA_CONNECTION_SEND_ERROR",
			STATUS_KPA_CONNECTION_RECEIVE_ERROR: "STATUS_KPA_CONNECTION_RECEIVE_ERROR",
			STATUS_CORE_REQ_HANDLING_TIMEOUT: "STATUS_CORE_REQ_HANDLING_TIMEOUT",
			STATUS_CORE_COREPARAMS_APPLY_ERROR: "STATUS_CORE_COREPARAMS_APPLY_ERROR",
			STATUS_MKO_WRITE_CRC_ERROR: "STATUS_MKO_WRITE_CRC_ERROR",
			STATUS_MKO_READ_CRC_ERROR: "STATUS_MKO_READ_CRC_ERROR",
			STATUS_TECHN_UNKNOWN_REQ: "STATUS_TECHN_UNKNOWN_REQ",
			STATUS_TECHN_ACCESS_DENIED: "STATUS_TECHN_ACCESS_DENIED",
			STATUS_TECHN_REQ_PARAM_ERROR: "STATUS_TECHN_REQ_PARAM_ERROR",
			STATUS_TECHN_RESP_PARAM_ERROR: "STATUS_TECHN_RESP_PARAM_ERROR",
			STATUS_TECHN_RESP_TIMEOUT: "STATUS_TECHN_RESP_TIMEOUT",
			STATUS_TECHN_UNKNOWN_STATUS: "STATUS_TECHN_UNKNOWN_STATUS",
	}

	def __init__(self, code=STATUS_OK, name="Status"):
		Enum16.__init__(self, code)
		self.setName(name)

####################################################################################################
class SwVerType(Enum8):
	SW_VER_TYPE_CORE = 0x01
	SW_VER_TYPE_TKPA = 0x02
	SW_VER_TYPE_BE = 0x03

	nameDict = {
			SW_VER_TYPE_CORE: "SW_VER_TYPE_CORE",
			SW_VER_TYPE_TKPA: "SW_VER_TYPE_TKPA",
			SW_VER_TYPE_BE: "SW_VER_TYPE_BE",
	}

	def __init__(self, code=SW_VER_TYPE_CORE, name="SwVerType"):
		Enum8.__init__(self, code)
		self.setName(name)

####################################################################################################
class KpaMode(Enum8):
	KPA_MODE_MANUAL = 0x00
	KPA_MODE_SIM = 0x01
	KPA_MODE_REAL = 0x02
	KPA_MODE_MOCKUP = 0x03

	nameDict = {
			KPA_MODE_MANUAL: "KPA_MODE_MANUAL",
			KPA_MODE_SIM: "KPA_MODE_SIM",
			KPA_MODE_REAL: "KPA_MODE_REAL",
			KPA_MODE_MOCKUP: "KPA_MODE_MOCKUP",
	}

	def __init__(self, code=KPA_MODE_MANUAL, name="KpaMode"):
		Enum8.__init__(self, code)
		self.setName(name)

####################################################################################################
class MkoPk(Enum8):
	MKO_PK_VO = 1
	MKO_PK_VO1 = 2
	MKO_PK_VO2 = 3
	MKO_PK_OO = 4
	MKO_PK_VOBH = 5
	MKO_PK_OOBH = 6
	MKO_PK_RR = 7
	MKO_PK_DR = 8
	MKO_PK_TST1 = 9
	MKO_PK_TST2 = 10
	MKO_PK_TST3 = 11
	MKO_PK_RAZM = 12
	MKO_PK_ZARM = 13
	MKO_PK_RAZS = 14
	MKO_PK_ZARS = 15
	MKO_PK_RAZRH = 16
	MKO_PK_KBO = 17
	MKO_PK_KBZ = 18
	MKO_PK_OTO = 19
	MKO_PK_L1 = 20
	MKO_PK_L2 = 21
	MKO_PK_L3 = 22
	MKO_PK_ORPM = 23
	MKO_PK_ROPM = 24
	MKO_PK_ORZM = 25
	MKO_PK_ROZM = 26
	MKO_PK_URK1 = 29
	MKO_PK_URK2 = 30
	MKO_PK_URK3 = 31
	MKO_PK_OS = 32
	MKO_PK_VAT = 33
	MKO_PK_OAT = 34
	MKO_PK_OFPKT = 35
	MKO_PK_VFPKT = 36

	nameDict = {
			MKO_PK_VO: "MKO_PK_VO",
			MKO_PK_VO1: "MKO_PK_VO1",
			MKO_PK_VO2: "MKO_PK_VO2",
			MKO_PK_OO: "MKO_PK_OO",
			MKO_PK_VOBH: "MKO_PK_VOBH",
			MKO_PK_OOBH: "MKO_PK_OOBH",
			MKO_PK_RR: "MKO_PK_RR",
			MKO_PK_DR: "MKO_PK_DR",
			MKO_PK_TST1: "MKO_PK_TST1",
			MKO_PK_TST2: "MKO_PK_TST2",
			MKO_PK_TST3: "MKO_PK_TST3",
			MKO_PK_RAZM: "MKO_PK_RAZM",
			MKO_PK_ZARM: "MKO_PK_ZARM",
			MKO_PK_RAZS: "MKO_PK_RAZS",
			MKO_PK_ZARS: "MKO_PK_ZARS",
			MKO_PK_RAZRH: "MKO_PK_RAZRH",
			MKO_PK_KBO: "MKO_PK_KBO",
			MKO_PK_KBZ: "MKO_PK_KBZ",
			MKO_PK_OTO: "MKO_PK_OTO",
			MKO_PK_L1: "MKO_PK_L1",
			MKO_PK_L2: "MKO_PK_L2",
			MKO_PK_L3: "MKO_PK_L3",
			MKO_PK_ORPM: "MKO_PK_ORPM",
			MKO_PK_ROPM: "MKO_PK_ROPM",
			MKO_PK_ORZM: "MKO_PK_ORZM",
			MKO_PK_ROZM: "MKO_PK_ROZM",
			MKO_PK_URK1: "MKO_PK_URK1",
			MKO_PK_URK2: "MKO_PK_URK2",
			MKO_PK_URK3: "MKO_PK_URK3",
			MKO_PK_OS: "MKO_PK_OS",
			MKO_PK_VAT: "MKO_PK_VAT",
			MKO_PK_OAT: "MKO_PK_OAT",
			MKO_PK_OFPKT: "MKO_PK_OFPKT",
			MKO_PK_VFPKT: "MKO_PK_VFPKT",
	}

	def __init__(self, code=MKO_PK_DR, name="MkoPk"):
		Enum8.__init__(self, code)
		self.setName(name)

####################################################################################################
class Fk(Enum32):
	FK_VIP1F1 = 1
	FK_VIP1NF2 = 2
	FK_VIP2F3 = 3
	FK_VIP2NF4 = 4
	FK_RAZF5 = 5
	FK_ZARF6 = 6
	FK_RRF7 = 7
	FK_DRF8 = 8
	FK_VOF9 = 9
	FK_OOF10 = 10
	FK_STRF11 = 11
	FK_STRNF12 = 12
	FK_RLF13 = 13
	FK_OLF14 = 14
	FK_RPPTF15 = 15
	FK_OPPTF16 = 16
	FK_RZ1F17 = 17
	FK_OZ1F18 = 18
	FK_VOF19 = 19
	FK_VO2F20 = 20
	FK_RURFF21 = 21
	FK_OURFF22 = 22
	FK_TMI1F23 = 23
	FK_TMI2F24 = 24
	FK_OSF25 = 25
	FK_VATF26 = 26
	FK_OATF27 = 27
	FK_TST1F28 = 28
	FK_TST2F29 = 29
	FK_TST3F30 = 30
	FK_KU1F31 = 31
	FK_KU2F32 = 32
	FK_KU3F33 = 33
	FK_PK1F34 = 34
	FK_PK2F35 = 35
	FK_PK3F36 = 36
	FK_KOS1F37 = 37
	FK_KOS2F38 = 38
	FK_ACT1F39 = 39
	FK_ACT2F40 = 40
	FK_MIT1F41 = 41
	FK_MIT2F42 = 42
	FK_MIT3F43 = 43
	FK_PO1F44 = 44
	FK_PO2F45 = 45
	FK_PO3F46 = 46
	FK_PO4F47 = 47
	FK_BFKCF48 = 48
	FK_BFKSF49 = 49
	FK_BUDRF50 = 50
	FK_BUDOF51 = 51
	FK_BOPRF52 = 52
	FK_BOPOF53 = 53
	FK_BSTRF54 = 54
	FK_BSTOF55 = 55

	nameDict = {
			FK_VIP1F1: "FK_VIP1F1",
			FK_VIP1NF2: "FK_VIP1NF2",
			FK_VIP2F3: "FK_VIP2F3",
			FK_VIP2NF4: "FK_VIP2NF4",
			FK_RAZF5: "FK_RAZF5",
			FK_ZARF6: "FK_ZARF6",
			FK_RRF7: "FK_RRF7",
			FK_DRF8: "FK_DRF8",
			FK_VOF9: "FK_VOF9",
			FK_OOF10: "FK_OOF10",
			FK_STRF11: "FK_STRF11",
			FK_STRNF12: "FK_STRNF12",
			FK_RLF13: "FK_RLF13",
			FK_OLF14: "FK_OLF14",
			FK_RPPTF15: "FK_RPPTF15",
			FK_OPPTF16: "FK_OPPTF16",
			FK_RZ1F17: "FK_RZ1F17",
			FK_OZ1F18: "FK_OZ1F18",
			FK_VOF19: "FK_VOF19",
			FK_VO2F20: "FK_VO2F20",
			FK_RURFF21: "FK_RURFF21",
			FK_OURFF22: "FK_OURFF22",
			FK_TMI1F23: "FK_TMI1F23",
			FK_TMI2F24: "FK_TMI2F24",
			FK_OSF25: "FK_OSF25",
			FK_VATF26: "FK_VATF26",
			FK_OATF27: "FK_OATF27",
			FK_TST1F28: "FK_TST1F28",
			FK_TST2F29: "FK_TST2F29",
			FK_TST3F30: "FK_TST3F30",
			FK_KU1F31: "FK_KU1F31",
			FK_KU2F32: "FK_KU2F32",
			FK_KU3F33: "FK_KU3F33",
			FK_PK1F34: "FK_PK1F34",
			FK_PK2F35: "FK_PK2F35",
			FK_PK3F36: "FK_PK3F36",
			FK_KOS1F37: "FK_KOS1F37",
			FK_KOS2F38: "FK_KOS2F38",
			FK_ACT1F39: "FK_ACT1F39",
			FK_ACT2F40: "FK_ACT2F40",
			FK_MIT1F41: "FK_MIT1F41",
			FK_MIT2F42: "FK_MIT2F42",
			FK_MIT3F43: "FK_MIT3F43",
			FK_PO1F44: "FK_PO1F44",
			FK_PO2F45: "FK_PO2F45",
			FK_PO3F46: "FK_PO3F46",
			FK_PO4F47: "FK_PO4F47",
			FK_BFKCF48: "FK_BFKCF48",
			FK_BFKSF49: "FK_BFKSF49",
			FK_BUDRF50: "FK_BUDRF50",
			FK_BUDOF51: "FK_BUDOF51",
			FK_BOPRF52: "FK_BOPRF52",
			FK_BOPOF53: "FK_BOPOF53",
			FK_BSTRF54: "FK_BSTRF54",
			FK_BSTOF55: "FK_BSTOF55",
	}

	def __init__(self, code=FK_VIP1F1, name="Fk"):
		Enum32.__init__(self, code)
		self.setName(name)

####################################################################################################
class ArrId(Enum16):
	ARR_BI = 0x0001
	ARR_BS = 0x0002
	ARR_RH = 0x0003

	nameDict = {
			ARR_BI: "ARR_BI",
			ARR_BS: "ARR_BS",
			ARR_RH: "ARR_RH",
	}

	def __init__(self, code=ARR_BI, name="ArrId"):
		Enum16.__init__(self, code)
		self.setName(name)

####################################################################################################
class DriveId(Enum16):
	PPM = 0x00000001
	PKM = 0x00000002
	ARR1_BI = 0x00000003
	ARR2_BI = 0x00000004
	PPZS1 = 0x00000005
	PPZS2 = 0x00000006
	ARR1_BS = 0x00000007
	ARR2_BS = 0x00000008

	nameDict = {
			PPM: "PPM",
			PKM: "PKM",
			ARR1_BI: "ARR1_BI",
			ARR2_BI: "ARR2_BI",
			PPZS1: "PPZS1",
			PPZS2: "PPZS2",
			ARR1_BS: "ARR1_BS",
			ARR2_BS: "ARR2_BS",
	}

	def __init__(self, code=PPM, name="DriveId"):
		Enum16.__init__(self, code)
		self.setName(name)

####################################################################################################
class HeatId(Enum16):
	HEAT_BI1 = 1
	HEAT_BI2 = 2
	HEAT_BI3 = 3
	HEAT_BI4 = 4
	HEAT_BI5 = 5
	HEAT_BI6 = 6
	HEAT_BI7 = 7
	HEAT_BI8 = 8
	HEAT_BI9 = 9
	HEAT_BI10 = 10
	HEAT_KOEB1 = 11
	HEAT_KOEB2 = 12
	HEAT_KOEB3 = 13
	HEAT_KOEB4 = 14
	HEAT_KOEB5 = 15
	HEAT_KOEB6 = 16
	HEAT_BS1 = 17
	HEAT_BS2 = 18
	HEAT_RH1 = 19
	HEAT_RH2 = 20
	HEAT_BH = 21
	HEAT_BCHT1 = 22
	HEAT_BCHT2 = 23

	nameDict = {
			HEAT_BI1: "HEAT_BI1",
			HEAT_BI2: "HEAT_BI2",
			HEAT_BI3: "HEAT_BI3",
			HEAT_BI4: "HEAT_BI4",
			HEAT_BI5: "HEAT_BI5",
			HEAT_BI6: "HEAT_BI6",
			HEAT_BI7: "HEAT_BI7",
			HEAT_BI8: "HEAT_BI8",
			HEAT_BI9: "HEAT_BI9",
			HEAT_BI10: "HEAT_BI10",
			HEAT_KOEB1: "HEAT_KOEB1",
			HEAT_KOEB2: "HEAT_KOEB2",
			HEAT_KOEB3: "HEAT_KOEB3",
			HEAT_KOEB4: "HEAT_KOEB4",
			HEAT_KOEB5: "HEAT_KOEB5",
			HEAT_KOEB6: "HEAT_KOEB6",
			HEAT_BS1: "HEAT_BS1",
			HEAT_BS2: "HEAT_BS2",
			HEAT_RH1: "HEAT_RH1",
			HEAT_RH2: "HEAT_RH2",
			HEAT_BH: "HEAT_BH",
			HEAT_BCHT1: "HEAT_BCHT1",
			HEAT_BCHT2: "HEAT_BCHT2",
	}

	def __init__(self, code=HEAT_BI1, name="HeatId"):
		Enum16.__init__(self, code)
		self.setName(name)

####################################################################################################
class PpmZoneId(Enum8):
	ZONE_1 = 0x0000
	ZONE_2 = 0x0001

	nameDict = {
			ZONE_1: "ZONE_1",
			ZONE_2: "ZONE_2",
	}

	def __init__(self, code=ZONE_1, name="PpmZoneId"):
		Enum8.__init__(self, code)
		self.setName(name)

####################################################################################################
# Struct definitions.
####################################################################################################

####################################################################################################
# Array definitions.
####################################################################################################

####################################################################################################
class VarSizeHex16Array(Array):
	def __init__(self, array=None):
		Array.__init__(self, array=array, itemType=Hex16, isVarSize=True)

####################################################################################################
class InfoChFrameArray(Array):
	def __init__(self, array=None):
		Array.__init__(self, array=array, itemType=Hex8, fixedSize=INFO_CH_FRAME_SIZE)

####################################################################################################
# Message definitions.
####################################################################################################

####################################################################################################
class UnknownReqInd(Msg):
	def __init__(self, errLevel=ErrLevel(), id=Hex32(0)):
		Msg.__init__(self, name = "Unknown request", id = Hex32(0x30000fe))
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "id", fieldType = Hex32, field = id)

####################################################################################################
class GetSwVersionReq(Msg):
	def __init__(self, verType=SwVerType()):
		Msg.__init__(self, name = "Get SW version request", id = Hex32(0x1000001))
		Msg.addField(self, fieldName = "verType", fieldType = SwVerType, field = verType)

####################################################################################################
class GetSwVersionConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), verType=SwVerType(), ver=Hex32(0)):
		Msg.__init__(self, name = "Get SW version confirm", id = Hex32(0x2000001))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "verType", fieldType = SwVerType, field = verType)
		Msg.addField(self, fieldName = "ver", fieldType = Hex32, field = ver)

####################################################################################################
class OpenTkpaConnReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Open TKPA connection request", id = Hex32(0x10000fe))

####################################################################################################
class OpenTkpaConnConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Open TKPA connection confirm", id = Hex32(0x20000fe))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class CloseTkpaConnReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Close TKPA connection request", id = Hex32(0x10000ff))

####################################################################################################
class CloseTkpaConnConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Close TKPA connection confirm", id = Hex32(0x20000ff))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class TkpaConnStatusInd(Msg):
	def __init__(self, isConnected=Uint8()):
		Msg.__init__(self, name = "TKPA connection status indication", id = Hex32(0x30000fd))
		Msg.addField(self, fieldName = "isConnected", fieldType = Uint8, field = isConnected)

####################################################################################################
class SetBePowerReq(Msg):
	def __init__(self, on=Uint16(0), res=Uint16(0)):
		Msg.__init__(self, name = "Set BE power request", id = Hex32(0x1000002))
		Msg.addField(self, fieldName = "on", fieldType = Uint16, field = on)
		Msg.addField(self, fieldName = "res", fieldType = Uint16, field = res)

####################################################################################################
class SetBePowerConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Set BE power confirm", id = Hex32(0x2000002))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class GetKpaModeReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Get KPA mode request", id = Hex32(0x1000003))

####################################################################################################
class GetKpaModeConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), mode=KpaMode()):
		Msg.__init__(self, name = "Get KPA mode confirm", id = Hex32(0x2000003))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "mode", fieldType = KpaMode, field = mode)

####################################################################################################
class SetKpaModeReq(Msg):
	def __init__(self, mode=KpaMode()):
		Msg.__init__(self, name = "Set KPA mode request", id = Hex32(0x1000004))
		Msg.addField(self, fieldName = "mode", fieldType = KpaMode, field = mode)

####################################################################################################
class SetKpaModeConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Set KPA mode confirm", id = Hex32(0x2000004))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class SetCoreParamsReq(Msg):
	def __init__(self, transmitFramesToClients=Uint8()):
		Msg.__init__(self, name = "Set Core parameters request", id = Hex32(0x1000005))
		Msg.addField(self, fieldName = "transmitFramesToClients", fieldType = Uint8, field = transmitFramesToClients)

####################################################################################################
class SetCoreParamsConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Set Core parameters confirm", id = Hex32(0x2000005))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class GetCoreParamsReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Get Core parameters request", id = Hex32(0x1000006))

####################################################################################################
class GetCoreParamsConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), transmitFramesToClients=Uint8()):
		Msg.__init__(self, name = "Get Core parameters confirm", id = Hex32(0x2000006))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "transmitFramesToClients", fieldType = Uint8, field = transmitFramesToClients)

####################################################################################################
class WriteMkoMsgReq(Msg):
	def __init__(self, channel=Uint8(), addr=Uint8(), subaddr=Uint8(), dataSize=Uint8(0), data=VarSizeHex16Array()):
		Msg.__init__(self, name = "Write MKO message request", id = Hex32(0x1010001))
		Msg.addField(self, fieldName = "channel", fieldType = Uint8, field = channel)
		Msg.addField(self, fieldName = "addr", fieldType = Uint8, field = addr)
		Msg.addField(self, fieldName = "subaddr", fieldType = Uint8, field = subaddr)
		Msg.addField(self, fieldName = "dataSize", fieldType = Uint8, field = dataSize)
		Msg.addField(self, fieldName = "data", fieldType = VarSizeHex16Array, field = data, isVarSize = True)

####################################################################################################
class WriteMkoMsgConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Write MKO message confirm", id = Hex32(0x2010001))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class ReadMkoMsgReq(Msg):
	def __init__(self, channel=Uint8(), addr=Uint8(), subaddr=Uint8(), dataSize=Uint8()):
		Msg.__init__(self, name = "Read MKO message request", id = Hex32(0x1010002))
		Msg.addField(self, fieldName = "channel", fieldType = Uint8, field = channel)
		Msg.addField(self, fieldName = "addr", fieldType = Uint8, field = addr)
		Msg.addField(self, fieldName = "subaddr", fieldType = Uint8, field = subaddr)
		Msg.addField(self, fieldName = "dataSize", fieldType = Uint8, field = dataSize)

####################################################################################################
class ReadMkoMsgConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), dataSize=Uint32(0), data=VarSizeHex16Array()):
		Msg.__init__(self, name = "Read MKO message confirm", id = Hex32(0x2010002))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "dataSize", fieldType = Uint32, field = dataSize)
		Msg.addField(self, fieldName = "data", fieldType = VarSizeHex16Array, field = data, isVarSize = True)

####################################################################################################
class SoftBeResetReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Soft BE reset request", id = Hex32(0x1010003))

####################################################################################################
class SoftBeResetConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Soft BE reset confirm", id = Hex32(0x2010003))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class HardBeResetReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Hard BE reset request", id = Hex32(0x1010004))

####################################################################################################
class HardBeResetConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Hard BE reset confirm", id = Hex32(0x2010004))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class EnableBeAddrSpaceAccessReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Enable BE address space access request", id = Hex32(0x1010005))

####################################################################################################
class EnableBeAddrSpaceAccessConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Enable BE address space access confirm", id = Hex32(0x2010005))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class WriteBeReg16Req(Msg):
	def __init__(self, addr=Uint16(), access=Uint8(), data=VarSizeHex16Array()):
		Msg.__init__(self, name = "Write BE 16 bit register request", id = Hex32(0x1010006))
		Msg.addField(self, fieldName = "addr", fieldType = Uint16, field = addr)
		Msg.addField(self, fieldName = "access", fieldType = Uint8, field = access)
		Msg.addField(self, fieldName = "data", fieldType = VarSizeHex16Array, field = data, isVarSize = True)

####################################################################################################
class WriteBeReg16Conf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Write BE 16 bit register confirm", id = Hex32(0x2010006))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class ReadBeReg16Req(Msg):
	def __init__(self, addr=Uint16(), access=Uint8(), dataSize=Uint8(0)):
		Msg.__init__(self, name = "Read BE 16 bit register request", id = Hex32(0x1010007))
		Msg.addField(self, fieldName = "addr", fieldType = Uint16, field = addr)
		Msg.addField(self, fieldName = "access", fieldType = Uint8, field = access)
		Msg.addField(self, fieldName = "dataSize", fieldType = Uint8, field = dataSize)

####################################################################################################
class ReadBeReg16Conf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), data=VarSizeHex16Array()):
		Msg.__init__(self, name = "Read BE 16 bit register confirm", id = Hex32(0x2010007))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "data", fieldType = VarSizeHex16Array, field = data, isVarSize = True)

####################################################################################################
class WriteMkoPkReq(Msg):
	def __init__(self, pk=MkoPk()):
		Msg.__init__(self, name = "Write MKO PK request", id = Hex32(0x1010008))
		Msg.addField(self, fieldName = "pk", fieldType = MkoPk, field = pk)

####################################################################################################
class WriteMkoPkConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Write MKO PK confirm", id = Hex32(0x2010008))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class MovePpmToZoneReq(Msg):
	def __init__(self, ZoneId=PpmZoneId()):
		Msg.__init__(self, name = "Move PPM to Zone MKO request", id = Hex32(0x1010009))
		Msg.addField(self, fieldName = "ZoneId", fieldType = PpmZoneId, field = ZoneId)

####################################################################################################
class MovePpmToZoneConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Move PPM to Zone MKO confirm", id = Hex32(0x2010009))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class MkoTmiInd(Msg):
	def __init__(self, SD1_2_BShV=Uint32(0), SD3_testErrorCode=Uint8(0), SD3_testNum=Uint8(0), SD3_1Hz_2=Uint8(0), SD3_1Hz_1=Uint8(0), SD3_1Hz_0=Uint8(0), SD3_STR=Uint8(0), SD3_DAT=Uint8(0), SD4_requestedMode=Uint8(0), SD4_currentMode=Uint8(0), SD4_OMBSet=Uint8(0), SD4_BESet=Uint8(0), SD4_stateVIP=Uint8(0), SD5_indicationPK=Uint8(0), SD5_lastPK=Uint16(0), SD6_7_cntRecievedMsg=Uint32(0), SD8_BL3=Uint8(0), SD8_BL2=Uint8(0), SD8_BL1=Uint8(0), SD8_PKMR=Uint8(0), SD8_PKMO=Uint8(0), SD8_PPMR=Uint8(0), SD8_PPMO=Uint8(0), SD8_VIP3V=Uint8(0), SD8_VIP2V=Uint8(0), SD8_VIP1V=Uint8(0), SD8_5VIP3=Uint8(0), SD8_5VIP2=Uint8(0), SD8_5VIP1=Uint8(0), SD8_VIP3P=Uint8(0), SD8_VIP2P=Uint8(0), SD8_VIP1P=Uint8(0), SD9_ZONA2=Uint8(0), SD9_ZONA1=Uint8(0), SD9_KOP=Uint8(0), SD9_DNPBS=Uint8(0), SD9_DAT=Uint8(0), SD9_STR2=Uint8(0), SD9_STR1=Uint8(0), SD9_PU=Uint8(0), SD9_URK3=Uint8(0), SD9_URK2=Uint8(0), SD9_URK1=Uint8(0), SD10_ARH=Uint8(0), SD10_ARMS=Uint8(0), SD10_ARM=Uint8(0), SD10_TEST=Uint8(0), SD10_MODE=Uint8(0), SD11_MACP1=Uint8(0), SD11_MPSTR2=Uint8(0), SD11_MPSTR1=Uint8(0), SD11_MVIP=Uint8(0), SD11_MP=Uint8(0), SD11_BE=Uint8(0), SD11_RKR=Uint8(0), SD11_RKO=Uint8(0), SD12_MUSTR2=Uint8(0), SD12_MUSTR1=Uint8(0), SD12_MUD2=Uint8(0), SD12_MUD1=Uint8(0), SD12_MACP2=Uint8(0), SD13_NRH2=Uint8(0), SD13_NRH1=Uint8(0), SD13_NBChT2=Uint8(0), SD13_NBChT1=Uint8(0), SD13_NBS2=Uint8(0), SD13_NBS1=Uint8(0), SD13_NBI10=Uint8(0), SD13_NBI9=Uint8(0), SD13_NBI8=Uint8(0), SD13_NBI7=Uint8(0), SD13_NBI6=Uint8(0), SD13_NBI5=Uint8(0), SD13_NBI4=Uint8(0), SD13_NBI3=Uint8(0), SD13_NBI2=Uint8(0), SD13_NBI1=Uint8(0), SD14_DTKOEB4=Uint8(0), SD14_DTKOEB3=Uint8(0), SD14_DTKOEB2=Uint8(0), SD14_DTKOEB1=Uint8(0), SD14_DTRH2=Uint8(0), SD14_DTRH1=Uint8(0), SD14_DTBChT2=Uint8(0), SD14_DTBChT1=Uint8(0), SD14_NBH=Uint8(0), SD14_NKOEB6=Uint8(0), SD14_NKOEB5=Uint8(0), SD14_NKOEB4=Uint8(0), SD14_NKOEB3=Uint8(0), SD14_NKOEB2=Uint8(0), SD14_NKOEB1=Uint8(0), SD15_DTBH=Uint8(0), SD15_DTDV=Uint8(0), SD15_DTSV=Uint8(0), SD15_DTKV=Uint8(0), SD15_DTBS2=Uint8(0), SD15_DTBS1=Uint8(0), SD15_DTBI10=Uint8(0), SD15_DTBI9=Uint8(0), SD15_DTBI8=Uint8(0), SD15_DTBI7=Uint8(0), SD15_DTBI6=Uint8(0), SD15_DTBI5=Uint8(0), SD15_DTBI4=Uint8(0), SD15_DTBI3=Uint8(0), SD15_DTBI2=Uint8(0), SD15_DTBI1=Uint8(0)):
		Msg.__init__(self, name = "Mko telemetry indication", id = Hex32(0x3010001))
		Msg.addField(self, fieldName = "SD1_2_BShV", fieldType = Uint32, field = SD1_2_BShV)
		Msg.addField(self, fieldName = "SD3_testErrorCode", fieldType = Uint8, field = SD3_testErrorCode)
		Msg.addField(self, fieldName = "SD3_testNum", fieldType = Uint8, field = SD3_testNum)
		Msg.addField(self, fieldName = "SD3_1Hz_2", fieldType = Uint8, field = SD3_1Hz_2)
		Msg.addField(self, fieldName = "SD3_1Hz_1", fieldType = Uint8, field = SD3_1Hz_1)
		Msg.addField(self, fieldName = "SD3_1Hz_0", fieldType = Uint8, field = SD3_1Hz_0)
		Msg.addField(self, fieldName = "SD3_STR", fieldType = Uint8, field = SD3_STR)
		Msg.addField(self, fieldName = "SD3_DAT", fieldType = Uint8, field = SD3_DAT)
		Msg.addField(self, fieldName = "SD4_requestedMode", fieldType = Uint8, field = SD4_requestedMode)
		Msg.addField(self, fieldName = "SD4_currentMode", fieldType = Uint8, field = SD4_currentMode)
		Msg.addField(self, fieldName = "SD4_OMBSet", fieldType = Uint8, field = SD4_OMBSet)
		Msg.addField(self, fieldName = "SD4_BESet", fieldType = Uint8, field = SD4_BESet)
		Msg.addField(self, fieldName = "SD4_stateVIP", fieldType = Uint8, field = SD4_stateVIP)
		Msg.addField(self, fieldName = "SD5_indicationPK", fieldType = Uint8, field = SD5_indicationPK)
		Msg.addField(self, fieldName = "SD5_lastPK", fieldType = Uint16, field = SD5_lastPK)
		Msg.addField(self, fieldName = "SD6_7_cntRecievedMsg", fieldType = Uint32, field = SD6_7_cntRecievedMsg)
		Msg.addField(self, fieldName = "SD8_BL3", fieldType = Uint8, field = SD8_BL3)
		Msg.addField(self, fieldName = "SD8_BL2", fieldType = Uint8, field = SD8_BL2)
		Msg.addField(self, fieldName = "SD8_BL1", fieldType = Uint8, field = SD8_BL1)
		Msg.addField(self, fieldName = "SD8_PKMR", fieldType = Uint8, field = SD8_PKMR)
		Msg.addField(self, fieldName = "SD8_PKMO", fieldType = Uint8, field = SD8_PKMO)
		Msg.addField(self, fieldName = "SD8_PPMR", fieldType = Uint8, field = SD8_PPMR)
		Msg.addField(self, fieldName = "SD8_PPMO", fieldType = Uint8, field = SD8_PPMO)
		Msg.addField(self, fieldName = "SD8_VIP3V", fieldType = Uint8, field = SD8_VIP3V)
		Msg.addField(self, fieldName = "SD8_VIP2V", fieldType = Uint8, field = SD8_VIP2V)
		Msg.addField(self, fieldName = "SD8_VIP1V", fieldType = Uint8, field = SD8_VIP1V)
		Msg.addField(self, fieldName = "SD8_5VIP3", fieldType = Uint8, field = SD8_5VIP3)
		Msg.addField(self, fieldName = "SD8_5VIP2", fieldType = Uint8, field = SD8_5VIP2)
		Msg.addField(self, fieldName = "SD8_5VIP1", fieldType = Uint8, field = SD8_5VIP1)
		Msg.addField(self, fieldName = "SD8_VIP3P", fieldType = Uint8, field = SD8_VIP3P)
		Msg.addField(self, fieldName = "SD8_VIP2P", fieldType = Uint8, field = SD8_VIP2P)
		Msg.addField(self, fieldName = "SD8_VIP1P", fieldType = Uint8, field = SD8_VIP1P)
		Msg.addField(self, fieldName = "SD9_ZONA2", fieldType = Uint8, field = SD9_ZONA2)
		Msg.addField(self, fieldName = "SD9_ZONA1", fieldType = Uint8, field = SD9_ZONA1)
		Msg.addField(self, fieldName = "SD9_KOP", fieldType = Uint8, field = SD9_KOP)
		Msg.addField(self, fieldName = "SD9_DNPBS", fieldType = Uint8, field = SD9_DNPBS)
		Msg.addField(self, fieldName = "SD9_DAT", fieldType = Uint8, field = SD9_DAT)
		Msg.addField(self, fieldName = "SD9_STR2", fieldType = Uint8, field = SD9_STR2)
		Msg.addField(self, fieldName = "SD9_STR1", fieldType = Uint8, field = SD9_STR1)
		Msg.addField(self, fieldName = "SD9_PU", fieldType = Uint8, field = SD9_PU)
		Msg.addField(self, fieldName = "SD9_URK3", fieldType = Uint8, field = SD9_URK3)
		Msg.addField(self, fieldName = "SD9_URK2", fieldType = Uint8, field = SD9_URK2)
		Msg.addField(self, fieldName = "SD9_URK1", fieldType = Uint8, field = SD9_URK1)
		Msg.addField(self, fieldName = "SD10_ARH", fieldType = Uint8, field = SD10_ARH)
		Msg.addField(self, fieldName = "SD10_ARMS", fieldType = Uint8, field = SD10_ARMS)
		Msg.addField(self, fieldName = "SD10_ARM", fieldType = Uint8, field = SD10_ARM)
		Msg.addField(self, fieldName = "SD10_TEST", fieldType = Uint8, field = SD10_TEST)
		Msg.addField(self, fieldName = "SD10_MODE", fieldType = Uint8, field = SD10_MODE)
		Msg.addField(self, fieldName = "SD11_MACP1", fieldType = Uint8, field = SD11_MACP1)
		Msg.addField(self, fieldName = "SD11_MPSTR2", fieldType = Uint8, field = SD11_MPSTR2)
		Msg.addField(self, fieldName = "SD11_MPSTR1", fieldType = Uint8, field = SD11_MPSTR1)
		Msg.addField(self, fieldName = "SD11_MVIP", fieldType = Uint8, field = SD11_MVIP)
		Msg.addField(self, fieldName = "SD11_MP", fieldType = Uint8, field = SD11_MP)
		Msg.addField(self, fieldName = "SD11_BE", fieldType = Uint8, field = SD11_BE)
		Msg.addField(self, fieldName = "SD11_RKR", fieldType = Uint8, field = SD11_RKR)
		Msg.addField(self, fieldName = "SD11_RKO", fieldType = Uint8, field = SD11_RKO)
		Msg.addField(self, fieldName = "SD12_MUSTR2", fieldType = Uint8, field = SD12_MUSTR2)
		Msg.addField(self, fieldName = "SD12_MUSTR1", fieldType = Uint8, field = SD12_MUSTR1)
		Msg.addField(self, fieldName = "SD12_MUD2", fieldType = Uint8, field = SD12_MUD2)
		Msg.addField(self, fieldName = "SD12_MUD1", fieldType = Uint8, field = SD12_MUD1)
		Msg.addField(self, fieldName = "SD12_MACP2", fieldType = Uint8, field = SD12_MACP2)
		Msg.addField(self, fieldName = "SD13_NRH2", fieldType = Uint8, field = SD13_NRH2)
		Msg.addField(self, fieldName = "SD13_NRH1", fieldType = Uint8, field = SD13_NRH1)
		Msg.addField(self, fieldName = "SD13_NBChT2", fieldType = Uint8, field = SD13_NBChT2)
		Msg.addField(self, fieldName = "SD13_NBChT1", fieldType = Uint8, field = SD13_NBChT1)
		Msg.addField(self, fieldName = "SD13_NBS2", fieldType = Uint8, field = SD13_NBS2)
		Msg.addField(self, fieldName = "SD13_NBS1", fieldType = Uint8, field = SD13_NBS1)
		Msg.addField(self, fieldName = "SD13_NBI10", fieldType = Uint8, field = SD13_NBI10)
		Msg.addField(self, fieldName = "SD13_NBI9", fieldType = Uint8, field = SD13_NBI9)
		Msg.addField(self, fieldName = "SD13_NBI8", fieldType = Uint8, field = SD13_NBI8)
		Msg.addField(self, fieldName = "SD13_NBI7", fieldType = Uint8, field = SD13_NBI7)
		Msg.addField(self, fieldName = "SD13_NBI6", fieldType = Uint8, field = SD13_NBI6)
		Msg.addField(self, fieldName = "SD13_NBI5", fieldType = Uint8, field = SD13_NBI5)
		Msg.addField(self, fieldName = "SD13_NBI4", fieldType = Uint8, field = SD13_NBI4)
		Msg.addField(self, fieldName = "SD13_NBI3", fieldType = Uint8, field = SD13_NBI3)
		Msg.addField(self, fieldName = "SD13_NBI2", fieldType = Uint8, field = SD13_NBI2)
		Msg.addField(self, fieldName = "SD13_NBI1", fieldType = Uint8, field = SD13_NBI1)
		Msg.addField(self, fieldName = "SD14_DTKOEB4", fieldType = Uint8, field = SD14_DTKOEB4)
		Msg.addField(self, fieldName = "SD14_DTKOEB3", fieldType = Uint8, field = SD14_DTKOEB3)
		Msg.addField(self, fieldName = "SD14_DTKOEB2", fieldType = Uint8, field = SD14_DTKOEB2)
		Msg.addField(self, fieldName = "SD14_DTKOEB1", fieldType = Uint8, field = SD14_DTKOEB1)
		Msg.addField(self, fieldName = "SD14_DTRH2", fieldType = Uint8, field = SD14_DTRH2)
		Msg.addField(self, fieldName = "SD14_DTRH1", fieldType = Uint8, field = SD14_DTRH1)
		Msg.addField(self, fieldName = "SD14_DTBChT2", fieldType = Uint8, field = SD14_DTBChT2)
		Msg.addField(self, fieldName = "SD14_DTBChT1", fieldType = Uint8, field = SD14_DTBChT1)
		Msg.addField(self, fieldName = "SD14_NBH", fieldType = Uint8, field = SD14_NBH)
		Msg.addField(self, fieldName = "SD14_NKOEB6", fieldType = Uint8, field = SD14_NKOEB6)
		Msg.addField(self, fieldName = "SD14_NKOEB5", fieldType = Uint8, field = SD14_NKOEB5)
		Msg.addField(self, fieldName = "SD14_NKOEB4", fieldType = Uint8, field = SD14_NKOEB4)
		Msg.addField(self, fieldName = "SD14_NKOEB3", fieldType = Uint8, field = SD14_NKOEB3)
		Msg.addField(self, fieldName = "SD14_NKOEB2", fieldType = Uint8, field = SD14_NKOEB2)
		Msg.addField(self, fieldName = "SD14_NKOEB1", fieldType = Uint8, field = SD14_NKOEB1)
		Msg.addField(self, fieldName = "SD15_DTBH", fieldType = Uint8, field = SD15_DTBH)
		Msg.addField(self, fieldName = "SD15_DTDV", fieldType = Uint8, field = SD15_DTDV)
		Msg.addField(self, fieldName = "SD15_DTSV", fieldType = Uint8, field = SD15_DTSV)
		Msg.addField(self, fieldName = "SD15_DTKV", fieldType = Uint8, field = SD15_DTKV)
		Msg.addField(self, fieldName = "SD15_DTBS2", fieldType = Uint8, field = SD15_DTBS2)
		Msg.addField(self, fieldName = "SD15_DTBS1", fieldType = Uint8, field = SD15_DTBS1)
		Msg.addField(self, fieldName = "SD15_DTBI10", fieldType = Uint8, field = SD15_DTBI10)
		Msg.addField(self, fieldName = "SD15_DTBI9", fieldType = Uint8, field = SD15_DTBI9)
		Msg.addField(self, fieldName = "SD15_DTBI8", fieldType = Uint8, field = SD15_DTBI8)
		Msg.addField(self, fieldName = "SD15_DTBI7", fieldType = Uint8, field = SD15_DTBI7)
		Msg.addField(self, fieldName = "SD15_DTBI6", fieldType = Uint8, field = SD15_DTBI6)
		Msg.addField(self, fieldName = "SD15_DTBI5", fieldType = Uint8, field = SD15_DTBI5)
		Msg.addField(self, fieldName = "SD15_DTBI4", fieldType = Uint8, field = SD15_DTBI4)
		Msg.addField(self, fieldName = "SD15_DTBI3", fieldType = Uint8, field = SD15_DTBI3)
		Msg.addField(self, fieldName = "SD15_DTBI2", fieldType = Uint8, field = SD15_DTBI2)
		Msg.addField(self, fieldName = "SD15_DTBI1", fieldType = Uint8, field = SD15_DTBI1)

####################################################################################################
class ResetInfoChCntReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Reset info channel counters request", id = Hex32(0x1020001))

####################################################################################################
class ResetInfoChCntConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Reset info channel counters confirm", id = Hex32(0x2020001))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class SetInfoChTestModeReq(Msg):
	def __init__(self, subCh0TestMode=Uint16(), subCh1TestMode=Uint16(), subCh0TestFrameNumb=Uint16(), subCh1TestFrameNumb=Uint16()):
		Msg.__init__(self, name = "Set info channel test mode request", id = Hex32(0x1020002))
		Msg.addField(self, fieldName = "subCh0TestMode", fieldType = Uint16, field = subCh0TestMode)
		Msg.addField(self, fieldName = "subCh1TestMode", fieldType = Uint16, field = subCh1TestMode)
		Msg.addField(self, fieldName = "subCh0TestFrameNumb", fieldType = Uint16, field = subCh0TestFrameNumb)
		Msg.addField(self, fieldName = "subCh1TestFrameNumb", fieldType = Uint16, field = subCh1TestFrameNumb)

####################################################################################################
class SetInfoChTestModeConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Set info channel test mode confirm", id = Hex32(0x2020002))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class GetInfoChTestModeReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Get info channel test mode request", id = Hex32(0x1020003))

####################################################################################################
class GetInfoChTestModeConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), subCh0TestMode=Uint16(), subCh1TestMode=Uint16(), subCh0TestFrameNumb=Uint16(), subCh1TestFrameNumb=Uint16()):
		Msg.__init__(self, name = "Get info channel test mode confirm", id = Hex32(0x2020003))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "subCh0TestMode", fieldType = Uint16, field = subCh0TestMode)
		Msg.addField(self, fieldName = "subCh1TestMode", fieldType = Uint16, field = subCh1TestMode)
		Msg.addField(self, fieldName = "subCh0TestFrameNumb", fieldType = Uint16, field = subCh0TestFrameNumb)
		Msg.addField(self, fieldName = "subCh1TestFrameNumb", fieldType = Uint16, field = subCh1TestFrameNumb)

####################################################################################################
class InfoChCntInd(Msg):
	def __init__(self, subCh0FrameCnt=Uint32(), subCh0FrameErrCnt=Uint32(), subCh1FrameCnt=Uint32(), subCh1FrameErrCnt=Uint32(), ifgPckCnt=Uint32(), ifgPckErrCnt=Uint32(), ifgPckTmCnt=Uint32(), ifgPckTmErrCnt=Uint32(), srvPckTmCnt=Uint32(), srvPckTmErrCnt=Uint32()):
		Msg.__init__(self, name = "Info channel counters indication", id = Hex32(0x3020001))
		Msg.addField(self, fieldName = "subCh0FrameCnt", fieldType = Uint32, field = subCh0FrameCnt)
		Msg.addField(self, fieldName = "subCh0FrameErrCnt", fieldType = Uint32, field = subCh0FrameErrCnt)
		Msg.addField(self, fieldName = "subCh1FrameCnt", fieldType = Uint32, field = subCh1FrameCnt)
		Msg.addField(self, fieldName = "subCh1FrameErrCnt", fieldType = Uint32, field = subCh1FrameErrCnt)
		Msg.addField(self, fieldName = "ifgPckCnt", fieldType = Uint32, field = ifgPckCnt)
		Msg.addField(self, fieldName = "ifgPckErrCnt", fieldType = Uint32, field = ifgPckErrCnt)
		Msg.addField(self, fieldName = "ifgPckTmCnt", fieldType = Uint32, field = ifgPckTmCnt)
		Msg.addField(self, fieldName = "ifgPckTmErrCnt", fieldType = Uint32, field = ifgPckTmErrCnt)
		Msg.addField(self, fieldName = "srvPckTmCnt", fieldType = Uint32, field = srvPckTmCnt)
		Msg.addField(self, fieldName = "srvPckTmErrCnt", fieldType = Uint32, field = srvPckTmErrCnt)

####################################################################################################
class InfoChFrameInd(Msg):
	def __init__(self, data=InfoChFrameArray()):
		Msg.__init__(self, name = "Info channel frame indication", id = Hex32(0x3020002))
		Msg.addField(self, fieldName = "data", fieldType = InfoChFrameArray, field = data, isVarSize = False)

####################################################################################################
class InfoChIfgPacketInd(Msg):
	def __init__(self, rcvNum=Uint8(1), pixNum=Uint8(1), pointNum=Uint16(0), bitPerPoint=Uint8(16), lowIfgBase=Uint16(0), ifgId=Uint32(0), ifgEnd=Uint8(1), highIfgBase=Uint8(0), disp=Uint16(0), points=VarSizeHex16Array()):
		Msg.__init__(self, name = "Info channel IFG packet indication", id = Hex32(0x3020003))
		Msg.addField(self, fieldName = "rcvNum", fieldType = Uint8, field = rcvNum)
		Msg.addField(self, fieldName = "pixNum", fieldType = Uint8, field = pixNum)
		Msg.addField(self, fieldName = "pointNum", fieldType = Uint16, field = pointNum)
		Msg.addField(self, fieldName = "bitPerPoint", fieldType = Uint8, field = bitPerPoint)
		Msg.addField(self, fieldName = "lowIfgBase", fieldType = Uint16, field = lowIfgBase)
		Msg.addField(self, fieldName = "ifgId", fieldType = Uint32, field = ifgId)
		Msg.addField(self, fieldName = "ifgEnd", fieldType = Uint8, field = ifgEnd)
		Msg.addField(self, fieldName = "highIfgBase", fieldType = Uint8, field = highIfgBase)
		Msg.addField(self, fieldName = "disp", fieldType = Uint16, field = disp)
		Msg.addField(self, fieldName = "points", fieldType = VarSizeHex16Array, field = points, isVarSize = True)

####################################################################################################
class InfoChVeloPacketInd(Msg):
	def __init__(self, ifgId=Uint32(0), pointNum=Uint16(0), points=VarSizeHex16Array()):
		Msg.__init__(self, name = "Info channel velocity packet indication", id = Hex32(0x3020004))
		Msg.addField(self, fieldName = "ifgId", fieldType = Uint32, field = ifgId)
		Msg.addField(self, fieldName = "pointNum", fieldType = Uint16, field = pointNum)
		Msg.addField(self, fieldName = "points", fieldType = VarSizeHex16Array, field = points, isVarSize = True)

####################################################################################################
class SetStrPowerReq(Msg):
	def __init__(self, str1=Uint16(0), str2=Uint16(0)):
		Msg.__init__(self, name = "Set STR power request", id = Hex32(0x1030001))
		Msg.addField(self, fieldName = "str1", fieldType = Uint16, field = str1)
		Msg.addField(self, fieldName = "str2", fieldType = Uint16, field = str2)

####################################################################################################
class SetStrPowerConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Set STR power confirm", id = Hex32(0x2030001))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class GetStrHeatVoltReq(Msg):
	def __init__(self, heatId=HeatId(), isUnderLoad=Uint16(0)):
		Msg.__init__(self, name = "Get STR heat voltage request", id = Hex32(0x1030002))
		Msg.addField(self, fieldName = "heatId", fieldType = HeatId, field = heatId)
		Msg.addField(self, fieldName = "isUnderLoad", fieldType = Uint16, field = isUnderLoad)

####################################################################################################
class GetStrHeatVoltConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), heatId=HeatId(), isUnderLoad=Uint16(0), heatVolt=Uint16(0), heatVoltLd=Uint16(0)):
		Msg.__init__(self, name = "Get STR heat voltage confirm", id = Hex32(0x2030002))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "heatId", fieldType = HeatId, field = heatId)
		Msg.addField(self, fieldName = "isUnderLoad", fieldType = Uint16, field = isUnderLoad)
		Msg.addField(self, fieldName = "heatVolt", fieldType = Uint16, field = heatVolt)
		Msg.addField(self, fieldName = "heatVoltLd", fieldType = Uint16, field = heatVoltLd)

####################################################################################################
class StrHeatVoltInd(Msg):
	def __init__(self, nbi1=Uint16(0), nbi2=Uint16(0), nbi3=Uint16(0), nbi4=Uint16(0), nbi5=Uint16(0), nbi6=Uint16(0), nbi7=Uint16(0), nbi8=Uint16(0), nbi9=Uint16(0), nbi10=Uint16(0), nkoeb1=Uint16(0), nkoeb2=Uint16(0), nkoeb3=Uint16(0), nkoeb4=Uint16(0), nkoeb5=Uint16(0), nkoeb6=Uint16(0), nbs1=Uint16(0), nbs2=Uint16(0), nrh1=Uint16(0), nrh2=Uint16(0), nbh=Uint16(0), nbcht1=Uint16(0), nbcht2=Uint16(0), res=Uint16(0)):
		Msg.__init__(self, name = "STR heat voltage indication", id = Hex32(0x3030001))
		Msg.addField(self, fieldName = "nbi1", fieldType = Uint16, field = nbi1)
		Msg.addField(self, fieldName = "nbi2", fieldType = Uint16, field = nbi2)
		Msg.addField(self, fieldName = "nbi3", fieldType = Uint16, field = nbi3)
		Msg.addField(self, fieldName = "nbi4", fieldType = Uint16, field = nbi4)
		Msg.addField(self, fieldName = "nbi5", fieldType = Uint16, field = nbi5)
		Msg.addField(self, fieldName = "nbi6", fieldType = Uint16, field = nbi6)
		Msg.addField(self, fieldName = "nbi7", fieldType = Uint16, field = nbi7)
		Msg.addField(self, fieldName = "nbi8", fieldType = Uint16, field = nbi8)
		Msg.addField(self, fieldName = "nbi9", fieldType = Uint16, field = nbi9)
		Msg.addField(self, fieldName = "nbi10", fieldType = Uint16, field = nbi10)
		Msg.addField(self, fieldName = "nkoeb1", fieldType = Uint16, field = nkoeb1)
		Msg.addField(self, fieldName = "nkoeb2", fieldType = Uint16, field = nkoeb2)
		Msg.addField(self, fieldName = "nkoeb3", fieldType = Uint16, field = nkoeb3)
		Msg.addField(self, fieldName = "nkoeb4", fieldType = Uint16, field = nkoeb4)
		Msg.addField(self, fieldName = "nkoeb5", fieldType = Uint16, field = nkoeb5)
		Msg.addField(self, fieldName = "nkoeb6", fieldType = Uint16, field = nkoeb6)
		Msg.addField(self, fieldName = "nbs1", fieldType = Uint16, field = nbs1)
		Msg.addField(self, fieldName = "nbs2", fieldType = Uint16, field = nbs2)
		Msg.addField(self, fieldName = "nrh1", fieldType = Uint16, field = nrh1)
		Msg.addField(self, fieldName = "nrh2", fieldType = Uint16, field = nrh2)
		Msg.addField(self, fieldName = "nbh", fieldType = Uint16, field = nbh)
		Msg.addField(self, fieldName = "nbcht1", fieldType = Uint16, field = nbcht1)
		Msg.addField(self, fieldName = "nbcht2", fieldType = Uint16, field = nbcht2)
		Msg.addField(self, fieldName = "res", fieldType = Uint16, field = res)

####################################################################################################
class AnalogTmiInd(Msg):
	def __init__(self, VIP1PT1=Uint8(0), VIP2PT2=Uint8(0), V5VIP1T3=Uint8(0), V5VIP2T4=Uint8(0), VIP1VT5=Uint8(0), VIP2VT6=Uint8(0), ARRT7=Uint8(0), ARZT8=Uint8(0), PDAT9=Uint8(0), ZO1T10=Uint8(0), SB11T11=Uint8(0), ZO2T12=Uint8(0), SB1013=Uint8(0), DOPT14=Uint8(0), OPRT15=Uint8(0), PPTOT16=Uint8(0), PPTRT17=Uint8(0), NSTRT18=Uint8(0), LOT19=Uint8(0), LRT20=Uint8(0), URFOT21=Uint8(0), URFRT22=Uint8(0), RKOT23=Uint8(0), RKRT24=Uint8(0), SB1T25=Uint8(0), SB2T26=Uint8(0), SB3T27=Uint8(0), SB4T28=Uint8(0), SB5T29=Uint8(0), SB6T30=Uint8(0), SB7T31=Uint8(0), SB8T32=Uint8(0), SB9T33=Uint8(0), TLOT34=Uint8(0), TLRT35=Uint8(0), SB12T36=Uint8(0), SB13T37=Uint8(0), TTR1T38=Uint32(0), TTR2T39=Uint32(0), TMI3T40=Uint32(0), TMI4T41=Uint32(0), TTKT42=Uint32(0), DATT43=Uint32(0)):
		Msg.__init__(self, name = "Analog telemetry indication", id = Hex32(0x3040001))
		Msg.addField(self, fieldName = "VIP1PT1", fieldType = Uint8, field = VIP1PT1)
		Msg.addField(self, fieldName = "VIP2PT2", fieldType = Uint8, field = VIP2PT2)
		Msg.addField(self, fieldName = "V5VIP1T3", fieldType = Uint8, field = V5VIP1T3)
		Msg.addField(self, fieldName = "V5VIP2T4", fieldType = Uint8, field = V5VIP2T4)
		Msg.addField(self, fieldName = "VIP1VT5", fieldType = Uint8, field = VIP1VT5)
		Msg.addField(self, fieldName = "VIP2VT6", fieldType = Uint8, field = VIP2VT6)
		Msg.addField(self, fieldName = "ARRT7", fieldType = Uint8, field = ARRT7)
		Msg.addField(self, fieldName = "ARZT8", fieldType = Uint8, field = ARZT8)
		Msg.addField(self, fieldName = "PDAT9", fieldType = Uint8, field = PDAT9)
		Msg.addField(self, fieldName = "ZO1T10", fieldType = Uint8, field = ZO1T10)
		Msg.addField(self, fieldName = "SB11T11", fieldType = Uint8, field = SB11T11)
		Msg.addField(self, fieldName = "ZO2T12", fieldType = Uint8, field = ZO2T12)
		Msg.addField(self, fieldName = "SB1013", fieldType = Uint8, field = SB1013)
		Msg.addField(self, fieldName = "DOPT14", fieldType = Uint8, field = DOPT14)
		Msg.addField(self, fieldName = "OPRT15", fieldType = Uint8, field = OPRT15)
		Msg.addField(self, fieldName = "PPTOT16", fieldType = Uint8, field = PPTOT16)
		Msg.addField(self, fieldName = "PPTRT17", fieldType = Uint8, field = PPTRT17)
		Msg.addField(self, fieldName = "NSTRT18", fieldType = Uint8, field = NSTRT18)
		Msg.addField(self, fieldName = "LOT19", fieldType = Uint8, field = LOT19)
		Msg.addField(self, fieldName = "LRT20", fieldType = Uint8, field = LRT20)
		Msg.addField(self, fieldName = "URFOT21", fieldType = Uint8, field = URFOT21)
		Msg.addField(self, fieldName = "URFRT22", fieldType = Uint8, field = URFRT22)
		Msg.addField(self, fieldName = "RKOT23", fieldType = Uint8, field = RKOT23)
		Msg.addField(self, fieldName = "RKRT24", fieldType = Uint8, field = RKRT24)
		Msg.addField(self, fieldName = "SB1T25", fieldType = Uint8, field = SB1T25)
		Msg.addField(self, fieldName = "SB2T26", fieldType = Uint8, field = SB2T26)
		Msg.addField(self, fieldName = "SB3T27", fieldType = Uint8, field = SB3T27)
		Msg.addField(self, fieldName = "SB4T28", fieldType = Uint8, field = SB4T28)
		Msg.addField(self, fieldName = "SB5T29", fieldType = Uint8, field = SB5T29)
		Msg.addField(self, fieldName = "SB6T30", fieldType = Uint8, field = SB6T30)
		Msg.addField(self, fieldName = "SB7T31", fieldType = Uint8, field = SB7T31)
		Msg.addField(self, fieldName = "SB8T32", fieldType = Uint8, field = SB8T32)
		Msg.addField(self, fieldName = "SB9T33", fieldType = Uint8, field = SB9T33)
		Msg.addField(self, fieldName = "TLOT34", fieldType = Uint8, field = TLOT34)
		Msg.addField(self, fieldName = "TLRT35", fieldType = Uint8, field = TLRT35)
		Msg.addField(self, fieldName = "SB12T36", fieldType = Uint8, field = SB12T36)
		Msg.addField(self, fieldName = "SB13T37", fieldType = Uint8, field = SB13T37)
		Msg.addField(self, fieldName = "TTR1T38", fieldType = Uint32, field = TTR1T38)
		Msg.addField(self, fieldName = "TTR2T39", fieldType = Uint32, field = TTR2T39)
		Msg.addField(self, fieldName = "TMI3T40", fieldType = Uint32, field = TMI3T40)
		Msg.addField(self, fieldName = "TMI4T41", fieldType = Uint32, field = TMI4T41)
		Msg.addField(self, fieldName = "TTKT42", fieldType = Uint32, field = TTKT42)
		Msg.addField(self, fieldName = "DATT43", fieldType = Uint32, field = DATT43)

####################################################################################################
class SliKpaInd(Msg):
	def __init__(self, pwrBE_current=Uint16(0), pwrBE_voltage=Uint16(0), pwrBE_state=Uint8(0), pwrBE_bit_PwrOnLimitEx=Uint8(0), pwrBE_bit_Overcurrent=Uint8(0), pwrBE_bit_Overvoltage=Uint8(0), pwrBE_bit_PowerGood=Uint8(0), pwrBE_bit_KS=Uint8(0), pwrSTR1_current=Uint16(0), pwrSTR1_voltage=Uint16(0), pwrSTR1_state=Uint8(0), pwrSTR1_bit_PwrOnLimitEx=Uint8(0), pwrSTR1_bit_Overcurrent=Uint8(0), pwrSTR1_bit_Overvoltage=Uint8(0), pwrSTR1_bit_PowerGood=Uint8(0), pwrSTR2_current=Uint16(0), pwrSTR2_voltage=Uint16(0), pwrSTR2_state=Uint8(0), pwrSTR2_bit_PwrOnLimitEx=Uint8(0), pwrSTR2_bit_Overcurrent=Uint8(0), pwrSTR2_bit_Overvoltage=Uint8(0), pwrSTR2_bit_PowerGood=Uint8(0)):
		Msg.__init__(self, name = "SlI KPA indication", id = Hex32(0x3040002))
		Msg.addField(self, fieldName = "pwrBE_current", fieldType = Uint16, field = pwrBE_current)
		Msg.addField(self, fieldName = "pwrBE_voltage", fieldType = Uint16, field = pwrBE_voltage)
		Msg.addField(self, fieldName = "pwrBE_state", fieldType = Uint8, field = pwrBE_state)
		Msg.addField(self, fieldName = "pwrBE_bit_PwrOnLimitEx", fieldType = Uint8, field = pwrBE_bit_PwrOnLimitEx)
		Msg.addField(self, fieldName = "pwrBE_bit_Overcurrent", fieldType = Uint8, field = pwrBE_bit_Overcurrent)
		Msg.addField(self, fieldName = "pwrBE_bit_Overvoltage", fieldType = Uint8, field = pwrBE_bit_Overvoltage)
		Msg.addField(self, fieldName = "pwrBE_bit_PowerGood", fieldType = Uint8, field = pwrBE_bit_PowerGood)
		Msg.addField(self, fieldName = "pwrBE_bit_KS", fieldType = Uint8, field = pwrBE_bit_KS)
		Msg.addField(self, fieldName = "pwrSTR1_current", fieldType = Uint16, field = pwrSTR1_current)
		Msg.addField(self, fieldName = "pwrSTR1_voltage", fieldType = Uint16, field = pwrSTR1_voltage)
		Msg.addField(self, fieldName = "pwrSTR1_state", fieldType = Uint8, field = pwrSTR1_state)
		Msg.addField(self, fieldName = "pwrSTR1_bit_PwrOnLimitEx", fieldType = Uint8, field = pwrSTR1_bit_PwrOnLimitEx)
		Msg.addField(self, fieldName = "pwrSTR1_bit_Overcurrent", fieldType = Uint8, field = pwrSTR1_bit_Overcurrent)
		Msg.addField(self, fieldName = "pwrSTR1_bit_Overvoltage", fieldType = Uint8, field = pwrSTR1_bit_Overvoltage)
		Msg.addField(self, fieldName = "pwrSTR1_bit_PowerGood", fieldType = Uint8, field = pwrSTR1_bit_PowerGood)
		Msg.addField(self, fieldName = "pwrSTR2_current", fieldType = Uint16, field = pwrSTR2_current)
		Msg.addField(self, fieldName = "pwrSTR2_voltage", fieldType = Uint16, field = pwrSTR2_voltage)
		Msg.addField(self, fieldName = "pwrSTR2_state", fieldType = Uint8, field = pwrSTR2_state)
		Msg.addField(self, fieldName = "pwrSTR2_bit_PwrOnLimitEx", fieldType = Uint8, field = pwrSTR2_bit_PwrOnLimitEx)
		Msg.addField(self, fieldName = "pwrSTR2_bit_Overcurrent", fieldType = Uint8, field = pwrSTR2_bit_Overcurrent)
		Msg.addField(self, fieldName = "pwrSTR2_bit_Overvoltage", fieldType = Uint8, field = pwrSTR2_bit_Overvoltage)
		Msg.addField(self, fieldName = "pwrSTR2_bit_PowerGood", fieldType = Uint8, field = pwrSTR2_bit_PowerGood)

####################################################################################################
class FkReq(Msg):
	def __init__(self, fk=Fk()):
		Msg.__init__(self, name = "FK request", id = Hex32(0x1090001))
		Msg.addField(self, fieldName = "fk", fieldType = Fk, field = fk)

####################################################################################################
class FkConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "FK confirm", id = Hex32(0x2090001))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class SetBiZoneReq(Msg):
	def __init__(self, zone1=Uint8(), zone2=Uint8(), zone1Res=Uint8(), zone2Res=Uint8()):
		Msg.__init__(self, name = "Set BI zone request", id = Hex32(0x10a0001))
		Msg.addField(self, fieldName = "zone1", fieldType = Uint8, field = zone1)
		Msg.addField(self, fieldName = "zone2", fieldType = Uint8, field = zone2)
		Msg.addField(self, fieldName = "zone1Res", fieldType = Uint8, field = zone1Res)
		Msg.addField(self, fieldName = "zone2Res", fieldType = Uint8, field = zone2Res)

####################################################################################################
class SetBiZoneConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Set BI zone confirm", id = Hex32(0x20a0001))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class GetBiZoneReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Get BI zone request", id = Hex32(0x10a0002))

####################################################################################################
class GetBiZoneConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), zone1=Uint8(), zone2=Uint8(), zone1Res=Uint8(), zone2Res=Uint8()):
		Msg.__init__(self, name = "Get BI zone confirm", id = Hex32(0x20a0002))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "zone1", fieldType = Uint8, field = zone1)
		Msg.addField(self, fieldName = "zone2", fieldType = Uint8, field = zone2)
		Msg.addField(self, fieldName = "zone1Res", fieldType = Uint8, field = zone1Res)
		Msg.addField(self, fieldName = "zone2Res", fieldType = Uint8, field = zone2Res)

####################################################################################################
class SetArrReq(Msg):
	def __init__(self, arrId=ArrId(), zar=Uint8(), raz=Uint8()):
		Msg.__init__(self, name = "Set arretir request", id = Hex32(0x10a0003))
		Msg.addField(self, fieldName = "arrId", fieldType = ArrId, field = arrId)
		Msg.addField(self, fieldName = "zar", fieldType = Uint8, field = zar)
		Msg.addField(self, fieldName = "raz", fieldType = Uint8, field = raz)

####################################################################################################
class SetArrConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Set arretir confirm", id = Hex32(0x20a0003))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class GetArrReq(Msg):
	def __init__(self, arrId=ArrId()):
		Msg.__init__(self, name = "Get arretir request", id = Hex32(0x10a0004))
		Msg.addField(self, fieldName = "arrId", fieldType = ArrId, field = arrId)

####################################################################################################
class GetArrConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), arrId=ArrId(), zar=Uint8(), raz=Uint8()):
		Msg.__init__(self, name = "Get arretir confirm", id = Hex32(0x20a0004))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "arrId", fieldType = ArrId, field = arrId)
		Msg.addField(self, fieldName = "zar", fieldType = Uint8, field = zar)
		Msg.addField(self, fieldName = "raz", fieldType = Uint8, field = raz)

####################################################################################################
class GetDkpmPowerReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Get DKPM power request", id = Hex32(0x10a0005))

####################################################################################################
class GetDkpmPowerConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), zone1=Uint16(), zone2=Uint16(), zone1Res=Uint16(), zone2Res=Uint16()):
		Msg.__init__(self, name = "Get DKPM power confirm", id = Hex32(0x20a0005))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "zone1", fieldType = Uint16, field = zone1)
		Msg.addField(self, fieldName = "zone2", fieldType = Uint16, field = zone2)
		Msg.addField(self, fieldName = "zone1Res", fieldType = Uint16, field = zone1Res)
		Msg.addField(self, fieldName = "zone2Res", fieldType = Uint16, field = zone2Res)

####################################################################################################
class GetDrivePowerReq(Msg):
	def __init__(self, driveId=DriveId(), isUnderLoad=Uint16(0)):
		Msg.__init__(self, name = "Get drive power request", id = Hex32(0x10a0006))
		Msg.addField(self, fieldName = "driveId", fieldType = DriveId, field = driveId)
		Msg.addField(self, fieldName = "isUnderLoad", fieldType = Uint16, field = isUnderLoad)

####################################################################################################
class GetDrivePowerConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), driveId=DriveId(), isUnderLoad=Uint16(0), pos=Uint16(), posLd=Uint16(), neg=Uint16(), res=Uint16()):
		Msg.__init__(self, name = "Get drive power confirm", id = Hex32(0x20a0006))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "driveId", fieldType = DriveId, field = driveId)
		Msg.addField(self, fieldName = "isUnderLoad", fieldType = Uint16, field = isUnderLoad)
		Msg.addField(self, fieldName = "pos", fieldType = Uint16, field = pos)
		Msg.addField(self, fieldName = "posLd", fieldType = Uint16, field = posLd)
		Msg.addField(self, fieldName = "neg", fieldType = Uint16, field = neg)
		Msg.addField(self, fieldName = "res", fieldType = Uint16, field = res)

####################################################################################################
class GetRefChPowerReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Get referential channel power request", id = Hex32(0x10a0007))

####################################################################################################
class GetRefChPowerConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), pos=Uint16(), neg=Uint16()):
		Msg.__init__(self, name = "Get referential channel power confirm", id = Hex32(0x20a0007))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "pos", fieldType = Uint16, field = pos)
		Msg.addField(self, fieldName = "neg", fieldType = Uint16, field = neg)

####################################################################################################
class GetDnpsPowerReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Get DNPS power request", id = Hex32(0x10a0008))

####################################################################################################
class GetDnpsPowerConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), value=Uint16(), res=Uint16()):
		Msg.__init__(self, name = "Get DNPS power confirm", id = Hex32(0x20a0008))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "value", fieldType = Uint16, field = value)
		Msg.addField(self, fieldName = "res", fieldType = Uint16, field = res)

####################################################################################################
class GetDnpsReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Get DNPS request", id = Hex32(0x10a0009))

####################################################################################################
class GetDnpsConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), value=Uint32()):
		Msg.__init__(self, name = "Get DNPS confirm", id = Hex32(0x20a0009))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "value", fieldType = Uint32, field = value)

####################################################################################################
class SetDnpsReq(Msg):
	def __init__(self, value=Uint32()):
		Msg.__init__(self, name = "Set DNPS request", id = Hex32(0x10a000a))
		Msg.addField(self, fieldName = "value", fieldType = Uint32, field = value)

####################################################################################################
class SetDnpsConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel()):
		Msg.__init__(self, name = "Set DNPS confirm", id = Hex32(0x20a000a))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)

####################################################################################################
class GetSkvtPowerReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Get SKVT power request", id = Hex32(0x10a000b))

####################################################################################################
class GetSkvtPowerConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), rudeAmp=Uint16(), rudeFreq=Uint16(), fineAmp=Uint16(), fineFreq=Uint16()):
		Msg.__init__(self, name = "Get SKVT power confirm", id = Hex32(0x20a000b))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "rudeAmp", fieldType = Uint16, field = rudeAmp)
		Msg.addField(self, fieldName = "rudeFreq", fieldType = Uint16, field = rudeFreq)
		Msg.addField(self, fieldName = "fineAmp", fieldType = Uint16, field = fineAmp)
		Msg.addField(self, fieldName = "fineFreq", fieldType = Uint16, field = fineFreq)

####################################################################################################
class GetBpuPowerReq(Msg):
	def __init__(self):
		Msg.__init__(self, name = "Get preamplifier block power request", id = Hex32(0x10a000c))

####################################################################################################
class GetBpuPowerConf(Msg):
	def __init__(self, status=Status(), errLevel=ErrLevel(), posValue=Uint16(), negValue=Uint16()):
		Msg.__init__(self, name = "Get preamplifier block power confirm", id = Hex32(0x20a000c))
		Msg.addField(self, fieldName = "status", fieldType = Status, field = status)
		Msg.addField(self, fieldName = "errLevel", fieldType = ErrLevel, field = errLevel)
		Msg.addField(self, fieldName = "posValue", fieldType = Uint16, field = posValue)
		Msg.addField(self, fieldName = "negValue", fieldType = Uint16, field = negValue)

