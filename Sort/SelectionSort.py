from Sort.LabSort import LabSort
class SelectionSort(LabSort):
    def __init__(self, len, type):
        super().__init__(len, type)
    def mainSort(self):
        array=self.getArray().getArrayById(0)
        for i in range(len(array)-1,0,-1):
            max=i
            for j in range(i-1,-1,-1):
                if array.isBigger(j,i):
                    max=j
            array.swap(i,max)
