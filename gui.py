from tkinter import *
from tkinter import filedialog,messagebox
from tkinter.ttk import *
from typing import Dict

import file2img  

class WinGUI(Tk):
    widget_dic: Dict[str, Widget] = {}
    def __init__(self):
        super().__init__()
        self.__win()
        self.widget_dic["tk_label_lb1"] = self.__tk_label_lb1(self)
        self.widget_dic["tk_button_select_file"] = self.__tk_button_select_file(self)
        self.widget_dic["tk_label_select_file_label"] = self.__tk_label_select_file_label(self)
        self.widget_dic["tk_button_convert_file"] = self.__tk_button_convert_file(self)
        self.widget_dic["tk_label_lb2"] = self.__tk_label_lb2(self)
        self.widget_dic["tk_button_select_image"] = self.__tk_button_select_image(self)
        self.widget_dic["tk_label_select_image_label"] = self.__tk_label_select_image_label(self)
        self.widget_dic["tk_button_convert_image"] = self.__tk_button_convert_image(self)

    def __win(self):
        self.title("File2IMG")
        # 设置窗口大小、居中
        width = 300
        height = 220
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

        # 自动隐藏滚动条
    def scrollbar_autohide(self,bar,widget):
        self.__scrollbar_hide(bar,widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
    
    def __scrollbar_show(self,bar,widget):
        bar.lift(widget)

    def __scrollbar_hide(self,bar,widget):
        bar.lower(widget)
        
    def __tk_label_lb1(self,parent):
        label = Label(parent,text="任意文件转换为图片",anchor="center",font=("微软雅黑",16))
        label.place(x=0, y=0, width=300, height=40)
        return label

    def __tk_button_select_file(self,parent):
        btn = Button(parent, text="选择文件")
        btn.place(x=0, y=40, width=80, height=30)
        return btn

    def __tk_label_select_file_label(self,parent):
        label = Label(parent,text="未选择文件",anchor="center")
        label.place(x=80, y=40, width=220, height=29)
        return label

    def __tk_button_convert_file(self,parent):
        btn = Button(parent, text="开始转换",state="disabled")
        btn.place(x=0, y=70, width=300, height=30)
        return btn

    def __tk_label_lb2(self,parent):
        label = Label(parent,text="图片还原为文件",anchor="center",font=("微软雅黑",16))
        label.place(x=0, y=120, width=300, height=40)
        return label

    def __tk_button_select_image(self,parent):
        btn = Button(parent, text="选择图片")
        btn.place(x=0, y=160, width=80, height=30)
        return btn

    def __tk_label_select_image_label(self,parent):
        label = Label(parent,text="未选择图片",anchor="center")
        label.place(x=80, y=160, width=220, height=30)
        return label

    def __tk_button_convert_image(self,parent):
        btn = Button(parent, text="开始还原",state="disabled")
        btn.place(x=0, y=190, width=300, height=30)
        return btn

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def handler_select_file(self,evt):
        path = filedialog.askopenfilename()
        lb = self.widget_dic["tk_label_select_file_label"]
        btn = self.widget_dic["tk_button_convert_file"]
        if path != "":
            lb.configure(text=path)
            btn.configure(state="active")
        else:
            lb.configure(text="未选择文件")
            btn.configure(state="disabled")
        
    def handler_convert_file(self,evt):
        btn = self.widget_dic["tk_button_convert_file"]
        if str(btn["state"])=="disabled":
            return
        
        lb = self.widget_dic["tk_label_select_file_label"]
        file_path = lb["text"]
        path = filedialog.asksaveasfilename(title="选择保存的路径",initialfile="修改此处文件名_后缀要为png.png",filetypes=[("PNG图像",".png")])
        if path=="":
            messagebox.showerror("失败","未选择保存的路径")
        else:
            try:
                file2img.encode_file_to_image(file_path,path)
                messagebox.showinfo("成功",f"保存至 {path}")
            except Exception as e:
                messagebox.showerror("错误",e)
            

        
    def handler_select_image(self,evt):
        path = filedialog.askopenfilename(filetypes=[("PNG图像",".png")])
        lb = self.widget_dic["tk_label_select_image_label"]
        btn = self.widget_dic["tk_button_convert_image"]
        if path != "":
            lb.configure(text=path)
            btn.configure(state="active")
        else:
            lb.configure(text="未选择文件")
            btn.configure(state="disabled")

        
    def handler_convert_image(self,evt):
        btn = self.widget_dic["tk_button_convert_image"]
        if str(btn["state"])=="disabled":
            return

        lb = self.widget_dic["tk_label_select_image_label"]
        file_path = lb["text"]
        path = filedialog.asksaveasfilename(title="选择保存的路径",initialfile="修改此处文件名及后缀")
        if path=="":
            messagebox.showerror("失败","未选择保存的路径")
        else:
            try:
                file2img.decode_image_to_file(file_path,path)
                messagebox.showinfo("成功",f"保存至 {path}")
            except Exception as e:
                messagebox.showerror("错误",e)
        
    def __event_bind(self):
        self.widget_dic["tk_button_select_file"].bind('<Button-1>',self.handler_select_file)
        self.widget_dic["tk_button_convert_file"].bind('<Button-1>',self.handler_convert_file)
        self.widget_dic["tk_button_select_image"].bind('<Button-1>',self.handler_select_image)
        self.widget_dic["tk_button_convert_image"].bind('<Button-1>',self.handler_convert_image)
        
if __name__ == "__main__":
    win = Win()
    win.mainloop()
