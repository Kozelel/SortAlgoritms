from Sort.LabSort import LabSort
from time import sleep
class StaticQuickSort(LabSort):
    def __init__(self, len, type):
        super().__init__(len, type)
    def mainSort(self):
        self.quickMain(0,len(self.getArray().getArrayById(0))-1,self.getArray().getArrayById(0))
    def quickMain(self,start,stop,array):
        stack=[[start,stop]]
        while 1>0:
            pointer=self.quickSelect(stack[0][0],stack[0][1],array)
            if (pointer-1)-stack[0][0]>1:
                stack.append([stack[0][0],pointer-1])
            if stack[0][1]-(pointer+1)>1:
                stack.append([pointer+1,stack[0][1]])
            stack.remove(stack[0])
            if len(stack)==0:
                break
    def quickSelect(self,start,stop,array):
        pointer=array.getById(stop)
        lowest=start-1
        for i in range(start,stop,1):
            if array.isLowerNumber(i,pointer):
                lowest+=1
                array.swap(lowest,i)
        array.swap(lowest+1,stop)
        return lowest+1
