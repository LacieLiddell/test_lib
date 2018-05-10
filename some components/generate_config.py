import random

class generate_config():
    # def __init__(self):
    #     """
    #     by default all blocks is primary
    #     setters set actually value (now it's random)
    #     getters returns it
    #     1 - means primary
    #     0 - reserve
    #     """
    #     self.vip = 1
    #     self.bud = 1
    #     self.bustr = 1
    #     self.bpop = 1
    #     self.bfk = 1

    def set_vip(self):
        if ((random.randint(0, 100)  % 2 ) == 0):
            self.vip = 1
        else:
            self.vip = 0

    def set_bfk(self):
        if ((random.randint(0, 100)  % 2 ) == 0):

            self.bfk = 1
        else:
            self.bfk = 0

    def set_bpop(self):
        if ((random.randint(0, 100)  % 2 ) == 0):
            self.bpop = 1
        else:
            self.bpop = 0

    def set_bustr(self):
        if ((random.randint(0, 100)  % 2 ) == 0):
            self.bustr = 1
        else:
            self.bustr = 0

    def set_bud(self):
        if ((random.randint(0, 100)  % 2 ) == 0):
            self.bud = 1
        else:
            self.bud = 0

    def gen_conf(self):
        self.set_vip()
        self.set_bud()
        self.set_bustr()
        self.set_bfk()
        self.set_bpop()
        print str(self.vip) + " vip"
        print str(self.bud) + " bud"
        print str(self.bustr) + " bustr"
        print str(self.bfk) + " bfk"
        print str(self.bpop) + " bpop"

    def get_vip(self):
        return self.vip

    def get_bud(self):
        return self.bud

    def get_bustr(self):
        return self.bustr

    def get_bfk(self):
        return self.bfk

    def get_bpop(self):
        return self.bpop

if __name__ == '__main__':
    g = generate_config()
    g.gen_conf()