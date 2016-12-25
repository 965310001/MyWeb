#coding:utf-8

from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *

#方法
def menu_author():
    showinfo('作者','我是作者')

def menu_copyright():
    showinfo('版权','我是版权')


def newFile():
    asksaveasfilename(defaultextension='.txt',initialfile='未命名.txt')




root=Tk()
root.title('郭枫记事本')
root.geometry('500x500+50+50')
# root.iconbitmap('')

#menu
menuBar=Menu(root)
root.config(menu=menuBar)

fileMenu=Menu(menuBar,tearoff=0)
fileMenu.add_command(label='新建',accelerator='Ctrl+N',command=newFile)
fileMenu.add_command(label='打开',accelerator='Ctrl+O')
fileMenu.add_command(label='保存',accelerator='Ctrl+S')
fileMenu.add_command(label='另存为',accelerator='Ctrl+Shift+S')
fileMenu.add_command(label='退出')
menuBar.add_cascade(label='文件',menu=fileMenu)

editMenu=Menu(root,tearoff=0)
editMenu.add_command(label='撤销',accelerator='Ctrl+Z')
editMenu.add_command(label='重做',accelerator='Ctrl+y')
editMenu.add_separator()
editMenu.add_command(label='剪切',accelerator='Ctrl+X')
editMenu.add_command(label='复制',accelerator='Ctrl+C')
editMenu.add_command(label='粘贴',accelerator='Ctrl+V')
editMenu.add_separator()
editMenu.add_command(label='查找',accelerator='Ctrl+F')
editMenu.add_command(label='全选',accelerator='Ctrl+A')
menuBar.add_cascade(label='编辑',menu=editMenu)

aboutMenu=Menu(root,tearoff=0)
aboutMenu.add_command(label='作者',command=menu_author)
aboutMenu.add_command(label='版权',command=menu_copyright)
menuBar.add_cascade(label='关于',menu=aboutMenu)

toolBar=Frame(root,height=25,bg='light sea green')
shortButton=Button(toolBar,text='打开',width=6)
shortButton.pack(side=LEFT,padx=5,pady=5)
shortButton=Button(toolBar,text='保存',width=6)
shortButton.pack(side=LEFT,padx=5,pady=5)
toolBar.pack(expand=NO,fill=X)

statusBar=Label(root,text='Ln20',relief=SUNKEN,anchor=W)
statusBar.pack(side=BOTTOM,fill=X)

root.mainloop()