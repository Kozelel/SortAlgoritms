from Sort.LabSort import LabSort
class HeapSort(LabSort):
    def __init__(self, len, type):
        super().__init__(len, type)
    def mainSort(self):
        array=self.getArray().getArrayById(0)
        self.firstRow(array)
        for i in range(len(array)-1,0,-1):
            array.swap(i,0)
            self.nextRows(array,i-1)
    def firstRow(self,array):
        for i in range(1,len(array)+1):
            pivot=i
            while int(pivot/2)>=1:
                if array.isBigger(pivot-1,int(pivot/2)-1):
                    array.swap(pivot-1,int(pivot/2)-1)
                    pivot=int(pivot/2)
                else:
                    break

    def nextRows(self,array,last):
       last+=1
       pivot=1
       while (pivot*2)<=last:
            bigger=pivot*2
            if bigger+1<=last and array.isBigger(bigger+1-1,bigger-1):
               bigger+=1
            if array.isBigger(bigger-1,pivot-1):
                array.swap(bigger-1,pivot-1)
                pivot=bigger
            else:
                break

