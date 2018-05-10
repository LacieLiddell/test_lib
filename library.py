import sys
sys.path.append("some components/")

from client import client
from constants_table import *
import time
from generate_config import generate_config
# global variable for correct tests
test_lib = client()
conf = generate_config()


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
    analogTmi = test_lib.getAnalogTmi()
    return analogTmi


def check_block_change(fk_init, fk_opposite):
    save_conf = test_lib.getAnalogTmi()
    test_lib.writeFk(fk_opposite)
    test_lib.writeFk(fk_init)
    analogTmi = test_lib.getAnalogTmi()
    return analogTmi, save_conf


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
    get_sw_version_test()

    # test_lib.connTkpa()
    # get_be_version_test(test_lib)
    # check_em_power_supply(test_lib)
    # test_lib.setBePower(POWER_OFF)
    # test_lib.writeFk(FK_VIP1F1)
    # test_lib.setBePower(POWER_ON)
    # analogTmi = test_lib.getAnalogTmi()
    # print analogTmi
    # test_lib.disconnTkpa()
    # disconnect(test_lib)
