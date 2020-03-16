from Lab.Config import Config
from Sort.BubbleSort import BubbleSort
from Sort.InsertSort import InsertSort
from Sort.SelectionSort import SelectionSort
from Sort.QuickSort import QuickSort
from Sort.HeapSort import HeapSort
from Sort.QuickSortWithMedianPointer import QuickSortWithMedianPointer
from Sort.StaticQuickSort import StaticQuickSort
from Sort.StaticQuickSortWithMedianPointer import StaticQuickSortWithMedianPointer
from Sort.MergeSort import MergeSort

class Engine:
    def __init__(self,cfg):
        self.__cfg=cfg
        self.__dir={}
    def singleSort(self,alghoritm,count,type):
        a=0
        if alghoritm=="BubbleSort":
            a=BubbleSort(count,type)
        elif alghoritm=="InsertSort":
            a=InsertSort(count,type)
        elif alghoritm=="SelectionSort":
            a=SelectionSort(count,type)
        elif alghoritm=="QuickSort":
            a=QuickSort(count,type)
        elif alghoritm=="HeapSort":
            a=HeapSort(count,type)
        elif alghoritm=="QuickSortWithMedianPointer":
            a=QuickSortWithMedianPointer(count,type)
        elif alghoritm=="StaticQuickSortWithMedianPointer":
            a=StaticQuickSortWithMedianPointer(count,type)
        elif alghoritm == "StaticQuickSort":
            a = StaticQuickSort(count, type)
        elif alghoritm == "MergeSort":
            a = MergeSort(count, type)
        else:
            print(F"Nie znaleziono algorytmu o nazwie {alghoritm}")
            return
        a.run()
        return a.stat()
    def mainLab(self):
        dir={}
        for i in self.__cfg:
            if i.getType() not in dir.keys():
                dir[i.getType()]={}
            if i.getName() not in dir[i.getType()].keys():
                dir[i.getType()][i.getName()]={}
                for j in range(i.getXStart(),i.getXStop(),i.getStep()):
                    #print(i.getXStart(),i.getXStop(),i.getStep())
                    if j not in dir[i.getType()][i.getName()].keys():
                        dir[i.getType()][i.getName()][j]={}
                    print(f"{i.getType()}:{i.getName()}:{j}")
                    try:
                        dir[i.getType()][i.getName()][j]=self.singleSort(i.getName(),j,i.getType())
                        if dir[i.getType()][i.getName()][j]['time'] > i.getMaxTime():
                            break
                    except:
                        break
        self.__dir=dir


        self.__dir=dir
    def printInt(self,data):
        data=str(data)
        output=""
        for i in range(len(data)):
            if i%3==0 and i!=0:
                output="."+output
            output=data[len(data)-1-i]+output
        return output

            
    def stat(self):
        #print(self.__dir)

        dir=self.__dir
        for i in dir.keys():
            print()
            for j in dir[i].keys():
                for k in dir[i][j].keys():
                    try:
                        #print(f"{i}:{j}:{k} time: {dir[i][j][k]['time']:0.2f} Arrays:{dir[i][j][k]['countOfArrays']} Comp:{dir[i][j][k]['comparisions']} Access:{dir[i][j][k]['accessToArray']} Swaps:{dir[i][j][k]['swaps']} Sets:{dir[i][j][k]['sets']}")
                        print(f"{i}:{j}:{k} time: {dir[i][j][k]['time']:0.2f} Arrays:{self.printInt(dir[i][j][k]['countOfArrays'])} Comp:{self.printInt(dir[i][j][k]['comparisions'])} Access:{self.printInt(dir[i][j][k]['accessToArray'])} Swaps:{self.printInt(dir[i][j][k]['swaps'])} Sets:{self.printInt(dir[i][j][k]['sets'])}")
                    except:
                        pass
    def statForPlot(self):
        dir=self.__dir
        cfg=self.__cfg
        output={}
        for i in cfg:
            if i.getType() not in output.keys():
                output[i.getType()]={}
                for j in ['time','countOfArrays','comparisions','accessToArray','swaps','sets']:
                    output[i.getType()][j]={}
                    output[i.getType()][j]['n']=[]
                    for k in range(i.getXStart(),i.getXStop(),i.getStep()):
                        output[i.getType()][j]['n'].append(k)
            if i.getName() not in output[i.getType()]['time'].keys():
                for j in ['time','countOfArrays','comparisions','accessToArray','swaps','sets']:
                    output[i.getType()][j][i.getName()]=[]
                    for k in range(i.getXStart(),i.getXStop(),i.getStep()):
                        try:
                            output[i.getType()][j][i.getName()].append(dir[i.getType()][i.getName()][k][j])
                        except:
                            output[i.getType()][j][i.getName()].append(None)

        return output



