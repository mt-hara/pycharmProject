import tkinter as tk
import tkinter.font as font


class AppView():
    def __init__(self, master, model) -> None:
        self.master = master
        self.model = model
        self.controller = None

    def register(self, controller):
        self.controller = controller

    def top_view(self):
        self.topframe = tk.Frame(self.master,width=self.model.t_width,height=self.model.t_height)
        self.topframe.grid(row=0, column=0,padx=(0,0), pady=(0,0),sticky=tk.W)
        self.txtframe = tk.Frame(self.master, width=500, height=200, bg="white")
        self.txtframe.grid(row=1, column=0, padx=(0,0), pady=(0,0), sticky=tk.W)
        # ボタンフレーム作成
        self.topbtnframe = tk.Frame(self.master, width = 150, height = 200)
        self.topbtnframe.grid(row=1, column=1, padx=(0,0),pady=(0,0), sticky=tk.W + tk.E + tk.N +
                                                                             tk.S)


        self.toplbl = tk.Label(self.topframe, text="対象ファイル")
        self.toplbl.pack()

        self.sclbar = tk.Scrollbar(self.txtframe)
        self.sclbar.pack(side="right", fill="y")
        self.txtfld = tk.Text(self.txtframe, width=85, height=10, bd=1, relief="groove",
                              font=("",9))
        self.txtfld.pack(side="left", padx=(5,0), pady=(5,5))
        self.txtfld["yscrollcommand"]=self.sclbar.set
