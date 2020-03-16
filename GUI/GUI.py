from tkinter import *
from tkinter.font import *
from Engine.Engine import *
from Lab.Config import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from GUI.MyFrame import MyFrame
class GUI:
    def __init__(self):
        self.__window=Tk(className="Sorting Alghoritms Comparision")
        self.__window.geometry("1000x700")
        self.__massagess=[]
        self.__opctionFrame=MyFrame(self.__window)
        self.__plotsFrames=[]
        self.__actualFrame=0
        self.__plotFrame=MyFrame(self.__window)
        self.opctionFrameSetup()
    def run(self):
        self.__opctionFrame.getFrame().pack(side=TOP)
        self.__window.mainloop()
    def runSimulation(self):
        entries=self.__opctionFrame.getStats()
        self.__opctionFrame.getFrame().destroy()
        #print(entries)
        cfg=[]
        for i in ['BubbleSort','SelectionSort','InsertSort','MergeSort','HeapSort','QuickSort','QuickSortWithMedianPointer','StaticQuickSort','StaticQuickSortWithMedianPointer']:
            if entries[i]:
                if entries['random']:
                    cfg.append(Config(i,'random',entries['Start Step'],entries['Last Step']+1,entries['Step'],entries['MaxTime']))
                if entries['sorted']:
                    cfg.append(Config(i,'sorted',entries['Start Step'],entries['Last Step']+1,entries['Step'],entries['MaxTime']))
                if entries['unsorted']:
                    cfg.append(Config(i,'unsorted',entries['Start Step'],entries['Last Step']+1,entries['Step'],entries['MaxTime']))
        engine=Engine(cfg)
        engine.mainLab()

        dataForPlots=engine.statForPlot()
        df=[]
        frames=self.__plotsFrames
        for i in dataForPlots.keys():
            for j in dataForPlots[i].keys():
                df.append({'title':i+" "+j,'mainColumn':'n','columns':dataForPlots[i][j].keys(),'data':DataFrame(dataForPlots[i][j],columns=dataForPlots[i][j].keys())})
        for i in range(len(df)):
            frames.append(Frame(self.__plotFrame.getFrame()))
            figure2 = plt.Figure(figsize=(11, 11), dpi=60)
            ax2 = figure2.add_subplot(111)
            line2 = FigureCanvasTkAgg(figure2, frames[i])
            line2.get_tk_widget().pack(side=LEFT, fill=BOTH)
            df2 = df[i]['data'][df[i]['columns']].groupby(df[i]['mainColumn']).sum()
            df2.plot(kind='line', legend=True, ax=ax2, fontsize=10)
            ax2.set_title(df[i]['title'])
        self.printPlot(self.__actualFrame)

    def previous(self):
        if self.__actualFrame > 0:
            self.__actualFrame-=1
            self.__plotsFrames[self.__actualFrame+1].grid_remove()
            self.__plotsFrames[self.__actualFrame].grid(row=1, column=2)
            self.__plotFrame.addWidget(self.__plotsFrames[self.__actualFrame])

    def next(self):
        if self.__actualFrame < (len(self.__plotsFrames)-1):
            self.__actualFrame += 1
            self.__plotsFrames[self.__actualFrame - 1].grid_remove()
            self.__plotsFrames[self.__actualFrame].grid(row=1, column=2)
            self.__plotFrame.addWidget(self.__plotsFrames[self.__actualFrame])
    def printPlot(self,number):
        frame = self.__plotFrame
        graps = self.__plotsFrames

        button=Button(frame.getFrame(),text="previous",command=self.previous)
        button.grid(row=2,column=1)
        frame.addButton(button)
        button = Button(frame.getFrame(), text="next",command=self.next)
        button.grid(row=2, column=3)
        frame.addButton(button)
        button = Button(frame.getFrame(), text="quit", command=quit)
        button.grid(row=2, column=2)
        frame.addButton(button)

        graps[number].grid(row=1,column=2)
        frame.addWidget(graps[number])

        frame.getFrame().pack(side=TOP)

    def opctionFrameSetup(self):
        frame=self.__opctionFrame
        label = Label(frame.getFrame(), text="Chose opctions",font=Font(size=20))
        label.grid(row=1, column=3)
        frame.addWidget(label)

        button=Button(frame.getFrame(),text="Start Simulation",command=self.runSimulation)
        button.grid(row=11,column=3)
        frame.addWidget(button)
        j=2
        for i in ['BubbleSort','SelectionSort','InsertSort','MergeSort','HeapSort','QuickSort','QuickSortWithMedianPointer','StaticQuickSort','StaticQuickSortWithMedianPointer']:
            label=Label(frame.getFrame(),text=i)
            label.grid(row=j,column=1)
            value=BooleanVar()
            value.set(False)
            checkBox=Checkbutton(frame.getFrame(),var=value)
            checkBox.grid(row=j,column=2)
            frame.addCheckBox([i,checkBox,value])
            frame.addWidget(label)
            j+=1
        j=2
        for i in [['Start Step',[10,100,1000,10000]],['Last Step',[100,1000,10000,100000]],['Step',[10,100,1000,10000]],['MaxTime',[1,2,5,10,15,60]]]:
            label = Label(frame.getFrame(), text=i[0])
            label.grid(row=j, column=4)
            spinBox=Spinbox(frame.getFrame(),values=i[1])
            spinBox.grid(row=j, column=5)
            frame.addSpinBox([i[0], spinBox])
            frame.addWidget(label)
            j += 1
        j = 7
        for i in ['random','sorted','unsorted']:
            label = Label(frame.getFrame(), text=i)
            label.grid(row=j, column=4)
            value = BooleanVar()
            value.set(False)
            checkBox = Checkbutton(frame.getFrame(),var=value)
            checkBox.grid(row=j, column=5)
            frame.addCheckBox([i, checkBox,value])
            frame.addWidget(label)
            j += 1
