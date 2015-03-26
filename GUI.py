#coding=utf-8
from Tkinter import *
import tkMessageBox
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel=Label(self,text='hello,world')
		self.helloLabel.pack()
		self.quitButton=Button(self,text='quit',command=self.quit)
		self.quitButton.pack()

	def createWidgets(self):
		self.nameInput=Entry(self)
		self.nameInput.pack()
		self.alertButton=Button(self,text='hello',command=self.hello)
		self.alertButton.pack()

	def hello(self):
		name=self.nameInput.get() or 'world'
		tkMessageBox.showinfo('杜志丽','hello,%s' % name)

app=Application()
#设置窗口主题
app.master.title('hello')
#主消息循环
app.mainloop()
