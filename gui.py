from Tkinter import *
import os
sys.path.append('some components')
import tkMessageBox as mbox
import db_parser as parser


class gui(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.s = 'call robot ' + os.getcwd() + '/someTest.robot'
        # self.root = Frame
        # frame = Frame(root, relief=RAISED, borderwidth=1)
        # frame.pack(fill= "both", expand=True)
        # root.pack(fill= 'both', expand=True)
        self.f = None
        self.var = BooleanVar()

        run_all_btn = Button(root, text="run all")
        run_all_btn.bind("<Button-1>", self.bat_test)
        run_all_btn.pack(side="left", padx=5, pady=5)

        frame = Frame(root, relief=RAISED, borderwidth=1)
        frame.pack(fill="both", expand=True, side="right")

        select_btn = Button(frame, text="select tests")
        select_btn.bind("<Button-1>", self.select_test)
        select_btn.pack(side="right", padx=5, pady=5)


    def bat_test(self, event):
        self.f = open('./script.bat', 'w')
        self.f.write(self.s)
        self.f.close()
        os.system(os.getcwd() + './script.bat')
        mbox.showinfo("Done!", "Testing completed. You can look info about results in log or report.")



    def select_test(self, event):
        t = Toplevel(root)
        t.geometry('400x300')

        core_version_cb = Checkbutton(t, text="Check core version",
                         variable=self.var, command = self.onClick)
        # cb.select()
        core_version_cb.grid(column = 1, row = 1)
        em_cb = Checkbutton(t, text="Check EM power supply",
                                      variable=self.var, command=self.onClick)
        # cb.select()
        em_cb.grid(column=1, row=2)

        run_select = Button(t, text="select tests")
        run_select.bind("<Button-1>", self.bat_test)
        run_select.grid(column = 0, row = 5, padx=5, pady=5)


    def onClick(self):
        print self.s
        if self.var.get() is True:
            # f = open('./script.bat', 'w')
            # f.write('call robot ' + '"Check core version" '+ os.getcwd() + '/someTest.robot')
            # f.close()
            # os.system(os.getcwd() + './script.bat')
            self.s = 'call robot ' + '-t "Check core version" '+ os.getcwd() + '/someTest.robot'
        else:
            self.s = 'call robot ' + os.getcwd() + '/someTest.robot'

    # def check_selected(self):
    #     print 's'
    #     cb.cget('text')



# if __name__ == '__main__':
#     root = Tk()
#     root.geometry( '200x150' )
#     app = gui(root)
#     parser.parse()
#     root.mainloop()

