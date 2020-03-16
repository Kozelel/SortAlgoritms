from tkinter import *
class MyFrame:
    def __init__(self,root):
        self.__frame=Frame(root)
        self.__widgets=[]
        self.__spinBoxes=[]
        self.__checBoxes=[]
        self.__buttons=[]
    def addButton(self,button):
        self.__buttons.append(button)
    def addWidget(self,widget):
        if widget not in self.__widgets:
            self.__widgets.append(widget)
    def addSpinBox(self,add):
        self.__spinBoxes.append(add)
    def addCheckBox(self, add):
        self.__checBoxes.append(add)
    def getFrame(self):
        return self.__frame
    def getStats(self):
        stats={}
        for i in self.__checBoxes:
            stats[i[0]]=bool(i[2].get())
        for i in self.__spinBoxes:
            stats[i[0]]=int(i[1].get())
        return stats
    def deleteWidgets(self):
        for i in range(len(self.__widgets)):
            self.__widgets[i].destroy()
        for i in range(len(self.__widgets)):
            self.__widgets.remove(self.__widgets[0])