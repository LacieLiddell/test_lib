from client import *
from constats_table import *
import time


def get_sw_version_test():
    '''
    needs like test library method. test suite file call this to connect to core and start second thread,
    because test suite file ignore __main__ method
    '''
    test_lib = connect()
    ver = test_lib.get_sw_version(SW_VER_TYPE_CORE)
    disconnect(test_lib)
    return ver


def check_em_power_supply():
    """
    this method check electronic module power supply. library method
    """
    test_lib = connect()
    # 1 - on, 0 - off power
    test_lib.setBePower(POWER_ON)
    sliKpaTmi = test_lib.getSliKpaTmi()
    print 'getSliKpaTmi'
    disconnect(test_lib)
    return sliKpaTmi


def check_inside_resources():
    test_lib = connect()
    # TODO
    # FK_TMI1F23
    test_lib.writeFk(FK_TMI1F23)
    analogTmi = test_lib.getAnalogTmi()
    disconnect(test_lib)
    return analogTmi


# def check_bfk(fk):
#     # TODO
#     # 48 - FK_BFKCF48, 49 - FK_BFKSF49
#     test_lib = connect()
#     test_lib.writeFk(fk)
#     disconnect(test_lib)


# def check_vip_change(fk_init, fk_opposite):
#     # TODO - fk mast be an argumnt
#     # 1 - FK_VIP1F1, 3 - FK_VIP2F3
#     test_lib = connect()
#     test_lib.writeFk(fk_opposite)
#     test_lib.writeFk(fk_init)
#     disconnect(test_lib)

def check_block_change(fk_init, fk_opposite):
    test_lib = connect()
    test_lib.writeFk(fk_opposite)
    test_lib.writeFk(fk_init)
    analogTmi = test_lib.getAnalogTmi()
    disconnect(test_lib)
    return analogTmi


def check_vip_turnoff(fk_opposite):
    # TODO. fk mast be an argument.then it can doing two tests between one
    # 2 - FK_VIP1NF2
    # and this method can take argument 4 - FK_VIP2NF4
    test_lib = connect()
    test_lib.setBePower(POWER_OFF)
    test_lib.writeFk(fk_opposite)
    test_lib.setBePower(POWER_ON)
    analogTmi = test_lib.getAnalogTmi()
    disconnect(test_lib)
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
    # TODO: 7 - FK_RRF7, 8 - FK_DRF8, 9 - FK_VOF9, 10 - FK_OOF10
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
    disconnect(test_lib)


# def check_laser_change(fk_init, fk_opposite):
#     test_lib = connect()
#     # TODO: 19 - VOF19, 20 - VO2F20
#     test_lib.writeFk(fk_opposite)
#     test_lib.writeFk(fk_init)
#     analogTmi = test_lib.getAnalogTmi()
#     disconnect(test_lib)
#     return analogTmi


def connect():
    # create and start second thread for connection to core
    test_lib = client()
    test_lib.start()
    # delay. it need to init socket
    time.sleep(0.5)
    return test_lib


def disconnect(test_lib):
    time.sleep(0.5)
    test_lib.stop()
    test_lib.waitForStop()
    print "stop"