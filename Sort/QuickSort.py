from Sort.LabSort import LabSort
class QuickSort(LabSort):
    def __init__(self, len, type):
        super().__init__(len, type)
    def mainSort(self):
        self.quickMain(0,len(self.getArray().getArrayById(0))-1,self.getArray().getArrayById(0))
    def quickMain(self,start,stop,array):
        pointer=self.quickSelect(start,stop,array)
        if (pointer-1)-start>1:
            self.quickMain(start,pointer-1,array)
        if stop-(pointer+1)>1:
            self.quickMain(pointer+1,stop,array)
    def quickSelect(self,start,stop,array):
        pointer=array.getById(stop)
        lowest=start-1
        for i in range(start,stop,1):
            if array.isLowerNumber(i,pointer):
                lowest+=1
                array.swap(lowest,i)
        array.swap(lowest+1,stop)
        return lowest+1

