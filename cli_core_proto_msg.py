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
# Struct definitions.
####################################################################################################

####################################################################################################
# Array definitions.
####################################################################################################

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
class AnalogTmiInd(Msg):
	def __init__(self, VIP1PT1=Uint8(0), VIP2PT2=Uint8(0), VIP1T3_5=Uint8(0), VIP2T4_5=Uint8(0), VIP1VT5=Uint8(0), VIP2VT6=Uint8(0), ARRT7=Uint8(0), ARZT8=Uint8(0), PDAT9=Uint8(0), ZO1T10=Uint8(0), SB11T11=Uint8(0), ZO2T12=Uint8(0), SB1013=Uint8(0), DOPT14=Uint8(0), OPRT15=Uint8(0), PPTOT16=Uint8(0), PPTRT17=Uint8(0), NSTRT18=Uint8(0), LOT19=Uint8(0), LRT20=Uint8(0), URFOT21=Uint8(0), URFRT22=Uint8(0), RKOT23=Uint8(0), RKRT24=Uint8(0), SB1T25=Uint8(0), SB2T26=Uint8(0), SB3T27=Uint8(0), SB4T28=Uint8(0), SB5T29=Uint8(0), SB6T30=Uint8(0), SB7T31=Uint8(0), SB8T32=Uint8(0), SB9T33=Uint8(0), TLOT34=Uint8(0), TLRT35=Uint8(0), SB12T36=Uint8(0), SB13T37=Uint8(0), TTR1T38=Uint32(0), TTR2T39=Uint32(0), TMI3T40=Uint32(0), TMI4T41=Uint32(0), TTKT42=Uint32(0), DATT43=Uint32(0)):
		Msg.__init__(self, name = "Analog telemetry indication", id = Hex32(0x3040001))
		Msg.addField(self, fieldName = "VIP1PT1", fieldType = Uint8, field = VIP1PT1)
		Msg.addField(self, fieldName = "VIP2PT2", fieldType = Uint8, field = VIP2PT2)
		Msg.addField(self, fieldName = "VIP1T3_5", fieldType = Uint8, field = VIP1T3_5)
		Msg.addField(self, fieldName = "VIP2T4_5", fieldType = Uint8, field = VIP2T4_5)
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
	def __init__(self, pwrBE_current=Uint16(0), pwrBE_voltage=Uint16(0), pwrBE_state=Uint8(0), pwrBE_bit_PwrOnLimitEx=Uint8(0), pwrBE_bit_Overcurrent=Uint8(0), pwrBE_bit_Overvoltage=Uint8(0), pwrBE_bit_PowerGood=Uint8(0), pwrBE_bit_KS=Uint8(0)):
		Msg.__init__(self, name = "SlI KPA indication", id = Hex32(0x3040002))
		Msg.addField(self, fieldName = "pwrBE_current", fieldType = Uint16, field = pwrBE_current)
		Msg.addField(self, fieldName = "pwrBE_voltage", fieldType = Uint16, field = pwrBE_voltage)
		Msg.addField(self, fieldName = "pwrBE_state", fieldType = Uint8, field = pwrBE_state)
		Msg.addField(self, fieldName = "pwrBE_bit_PwrOnLimitEx", fieldType = Uint8, field = pwrBE_bit_PwrOnLimitEx)
		Msg.addField(self, fieldName = "pwrBE_bit_Overcurrent", fieldType = Uint8, field = pwrBE_bit_Overcurrent)
		Msg.addField(self, fieldName = "pwrBE_bit_Overvoltage", fieldType = Uint8, field = pwrBE_bit_Overvoltage)
		Msg.addField(self, fieldName = "pwrBE_bit_PowerGood", fieldType = Uint8, field = pwrBE_bit_PowerGood)
		Msg.addField(self, fieldName = "pwrBE_bit_KS", fieldType = Uint8, field = pwrBE_bit_KS)

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

