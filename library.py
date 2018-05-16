import sys
sys.path.append("some components/")

from client import client
from constants_table import *
import time
from generate_config import generate_config
INIT_CONFIG = 0
SWITCH_CONFIG = 1
CURR_CONFIG = 2
# global variable for correct tests
test_lib = client()
conf = generate_config()


#############################################
# procedures
#############################################
def get_analog_tmi(tmi):
    for i in xrange(3):
        time.sleep(1)
        raw_value = test_lib.getAnalogTmi()[tmi]
        fin_value = raw_value * 5.0 / 256.0
        print "Analog TMI", tmi, ": ", i, "sec: ", fin_value, "V"
    return fin_value

def check_em_config(tmi, fk):
    # vip1 = get_analog_tmi('VIP1PT1')
    # vip2 = get_analog_tmi('VIP2PT2')
    # bfk = get_analog_tmi('SB1T25')
    # bud = get_analog_tmi('SB2T26')
    # bpop = get_analog_tmi('SB3T27')
    # bustr = get_analog_tmi('SB4T28')
    print "tmi: ", tmi, ", fk: ", fk
    value = get_analog_tmi(tmi)
    if (tmi == "VIP1PT1"):
        if (fk == FK_VIP1F1 and value >= 0 and value <= 0.5):
            return SWITCH_CONFIG
    elif (tmi == "VIP2PT2"):
        if (fk == FK_VIP2F3 and value >= 0 and value <= 0.5):
            return SWITCH_CONFIG
    elif (tmi == "SB1T25"):
        vip1 = get_analog_tmi('VIP1PT1')
        vip2 = get_analog_tmi('VIP2PT2')
        # check main vip and foreign bfk
        if ((vip1 >= 2.1) and (value >= 1.8) and (value <= 2.2)):
            if (fk == FK_BFKCF48):
                return SWITCH_CONFIG
            elif (fk == FK_BFKSF49):
                return CURR_CONFIG
        #     Check main vip and own bfk
        if ((vip1 >= 2.1) and (value >= 3.8) and (value <= 4.2)):
            if (fk == FK_BFKCF48):
                return CURR_CONFIG
            elif (fk == FK_BFKSF49):
                return SWITCH_CONFIG
            # Check res vip and foreign bfk
            if ((vip2 >= 2.1) and (value >= 1.8) and (value <= 2.2)):
                if (fk == FK_BFKCF48):
                    return SWITCH_CONFIG
                elif (fk == FK_BFKSF49):
                    return CURR_CONFIG
            #     Check res vip and own bfk
            if ((vip2 >= 2.1) and (value >= 3.8) and (value <= 4.2)):
                if (fk == FK_BFKCF48):
                    return CURR_CONFIG
                elif (fk == FK_BFKSF49):
                    return SWITCH_CONFIG
    elif (tmi == "SB2T26"):
        if (fk == FK_BUDRF50 and (value >= 3.8) and (value <= 4.2)):
            return SWITCH_CONFIG
        elif (fk == FK_BUDOF51 and (value >= 1.8) and (value <= 2.2)):
            return SWITCH_CONFIG
        else: return CURR_CONFIG
    elif (tmi == 'SB3T27'):
        if (fk == FK_BOPRF52 and (value >= 3.8) and (value <= 4.2)):
            return SWITCH_CONFIG
        elif (fk == FK_BOPOF53 and (value >= 1.8) and (value <= 2.2)):
            return SWITCH_CONFIG
        else:
            return CURR_CONFIG
    elif (tmi == 'SB4T28'):
        if (fk == FK_BSTRF54 and (value >= 3.8) and (value <= 4.2)):
            return SWITCH_CONFIG
        elif (fk == FK_BSTOF55 and (value >= 1.8) and (value <= 2.2)):
            return SWITCH_CONFIG
        else:
            return CURR_CONFIG
    return INIT_CONFIG

def set_me_to_init_config():
    test_lib.setBePower(POWER_OFF)
    test_lib.writeFk(FK_VIP1F1)
    time.sleep(4)
    test_lib.writeFk(FK_VIP2NF4)
    time.sleep(4)


def change_config():
    pass

def switch_block(fk, tmi):
    config = check_em_config(tmi, fk)
    print config
    time.sleep(4)
    if config == CURR_CONFIG:
        return None
        # pass
    if config == SWITCH_CONFIG:
        me = get_analog_tmi("SB5T29")
        test_lib.writeFk(fk)
        time.sleep(4)
        value = get_analog_tmi(tmi)
    if config == INIT_CONFIG:
        # TODO switch config x_x
        set_me_to_init_config()
    # return value, me



#############################################
# tests
#############################################

def get_sw_version_test():
    ver = test_lib.get_sw_version(SW_VER_TYPE_CORE)
    return ver


def get_be_version_test():
    ver = test_lib.get_sw_version(SW_VER_TYPE_BE)
    return ver


def check_em_power_supply():
    """
    this method check electronic module power supply. library method
    """
    test_lib.setBePower(POWER_ON)
    sliKpaTmi = test_lib.getSliKpaTmi()
    print 'getSliKpaTmi'
    print sliKpaTmi
    return sliKpaTmi


def check_inside_resources():
    test_lib.writeFk(FK_TMI1F23)
    value = get_analog_tmi("SB7T31")
    # for i in xrange(3):
    #     time.sleep(1)
    #     sb7t31 = test_lib.getAnalogTmi()["SB7T31"]
    #     value = sb7t31 * 5.0 / 256.0
    #     print "Analog TMI SB7T31, ", i, "sec: ", value, "V"
    return value


def check_block_change(fk_opposite, fk_init, telemetry):
    save_conf = get_analog_tmi(telemetry)
    # save_conf = test_lib.getAnalogTmi()
    time.sleep(4)
    # for i in xrange(4):
    #     time.sleep(1)
    #     save_value = test_lib.getAnalogTmi()[telemetry]
    #     save_conf = save_value * 5.0 / 256.0
    #     print "Analog TMI save_conf, ", i, "sec: ", save_conf, "V"

    # save_conf = get_analog_tmi(telemetry)
    # test_lib.writeFk(fk_opposite)
    # time.sleep(4)
    # test_lib.writeFk(fk_init)
    # time.sleep(4)
    print "switch to opposite, if needed"
    switch_block(fk_opposite, telemetry)
    print "switch to init"
    switch_block(fk_init, telemetry)
    # for i in xrange(4):
    #     time.sleep(1)
    #     tmi_value = test_lib.getAnalogTmi()[telemetry]
    #     value = tmi_value * 5.0 / 256.0
    #     print "Analog TMI tmi_value, ", i, "sec: ", value, "V"
    # analogTmi = test_lib.getAnalogTmi()
    value = get_analog_tmi(telemetry)
    return value, save_conf


def check_vip_turnoff(fk_opposite):
    test_lib.setBePower(POWER_OFF)
    test_lib.writeFk(fk_opposite)
    test_lib.setBePower(POWER_ON)
    analogTmi = test_lib.getAnalogTmi()
    return analogTmi


# def check_bustr_change(fk_init, fk_opposite):
#     test_lib = connect()
#     # TODO: 54 - FK_BSTRF54, 55 - FK_BSTOF55
#     test_lib.writeFk(fk_opposite)
#     test_lib.writeFk(fk_init)
#     analogTmi = test_lib.getAnalogTmi()
#     disconnect(test_lib)
#     return analogTmi


# def check_bud_change(fk_init, fk_opposite):
#     test_lib = connect()
#     # TODO: 50 - FK_BUDRF50, 51 - FK_BUDOF51
#     test_lib.writeFk(fk_opposite)
#     test_lib.writeFk(fk_init)
#     analogTmi = test_lib.getAnalogTmi()
#     disconnect(test_lib)
#     return analogTmi


# def check_bpop_change(fk_init, fk_opposite):
#     test_lib = connect()
#     # TODO: 52 - FK_BOPRF52, 53 - FK_BOPOF53
#     test_lib.writeFk(fk_opposite)
#     test_lib.writeFk(fk_init)
#     analogTmi = test_lib.getAnalogTmi()
#     disconnect(test_lib)
#     return analogTmi


def check_change_mode():
    test_lib = connect()
    test_lib.writeFk(FK_RRF7)
    rrTmi = test_lib.getAnalogTmi()
    test_lib.writeFk(FK_DRF8)
    drTmi = test_lib.getAnalogTmi()
    test_lib.writeFk(FK_VOF9)
    voTmi = test_lib.getAnalogTmi()
    test_lib.writeFk(FK_DRF8)
    test_lib.getAnalogTmi()
    test_lib.writeFk(FK_VOF9)
    test_lib.getAnalogTmi()
    test_lib.writeFk(FK_OOF10)
    test_lib.getAnalogTmi()
    return rrTmi, drTmi, voTmi

#############################################
# /tests
#############################################


# def check_laser_change(fk_init, fk_opposite):
#     test_lib = connect()
#     # TODO: 19 - VOF19, 20 - VO2F20
#     test_lib.writeFk(fk_opposite)
#     test_lib.writeFk(fk_init)
#     analogTmi = test_lib.getAnalogTmi()
#     disconnect(test_lib)
#     return analogTmi

#############################################
# connect and disconnect
#############################################
def connect():
    # create and start second thread for connection to core
    test_lib.start()
    time.sleep(1)
    # delay. it need to init socket
    test_lib.connTkpa()
    # conf.gen_conf()



def disconnect():
    test_lib.disconnTkpa()
    time.sleep(0.5)
    test_lib.stop()
    test_lib.waitForStop()
    print "stop"

def set_config(fk):
    test_lib.writeFk(fk)

#############################################
# /connect and disconnect
#############################################


#############################################
# service procedures
#############################################
# def check_me_config():
#     i dont know .______________.

# def init_me():
#     test_lib.setBePower(POWER_OFF)
#     test_lib.writeFk(FK_VIP2NF1)
#     test_lib.writeFk(FK_VIP2NF4)




#############################################
# /service procedures
#############################################


if __name__ == '__main__':
    connect()
    # get_sw_version_test()
    test_lib.writeFk(FK_BFKCF48)
    time.sleep(4)
    test_lib.writeFk(FK_VIP2F3)
    time.sleep(4)
    get_analog_tmi('SB1T25')
    # test_lib.writeFk(FK_BUDRF50)
    check_block_change(FK_BUDRF50, FK_BUDOF51, 'SB2T26')
    # get_analog_tmi('SB2T26')
    # test_lib.writeFk(FK_TMI1F23)
    # analogTmi = test_lib.getAnalogTmi()
    # print analogTmi
    # for i in xrange(8):
    #     time.sleep(1)
    #     sb7t31 = test_lib.getAnalogTmi()["VIP1PT1"]
    #     value = sb7t31 * 5.0 / 256.0
    #     print "Analog TMI SB7T31, ", i, "sec: ", value, "V"
    test_lib.disconnTkpa()
    disconnect()
