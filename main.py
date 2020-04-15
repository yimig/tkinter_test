import tkinter
#from poker_soldier import *


def poker_soldier_jump():
    ps.jump()


def poker_soldier_blink():
    ps.blink()


def poker_soldier_fill():
    ps.fill()


try:
    from poker_soldier import *
except ImportError:
    print("抱歉，这个实验用到了线性变换，需要安装numpy库才能运行。")
else:
    root = tkinter.Tk()
    frm1 = tkinter.Frame(root)
    frm1.pack()
    title_frm = tkinter.Frame(frm1)
    title_frm.pack()
    tkinter.Label(title_frm, text="使用Tkinter绘制扑克牌士兵").pack()
    tkinter.Label(title_frm, text="author:https://github.com/yimig").pack()
    canvas = tkinter.Canvas(root, width=800, height=600, bg="white")
    canvas.pack()
    ps = PokerSoldier(canvas)
    frm2 = tkinter.Frame(root)
    frm2.pack()
    func_frm = tkinter.Frame(frm2)
    func_frm.pack(side="bottom")
    tkinter.Button(func_frm, text="眨眼", command=ps.blink).grid(row=0, column=0)
    tkinter.Button(func_frm, text="运动四肢", command=ps.jump).grid(row=0, column=1)
    tkinter.Button(func_frm, text="色彩装饰", command=ps.fill).grid(row=0, column=2)
    tkinter.mainloop()
