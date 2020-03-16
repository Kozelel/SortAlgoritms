from Sort.LabSort import LabSort
class InsertSort(LabSort):
    def __init__(self, len, type):
        super().__init__(len, type)
    def mainSort(self):
        array =self.getArray().getArrayById(0)
        count=len(array)
        for i in range(1,count):
            pom=array.getById(i)
            for j in range(i-1,-1,-1):
                if array.isBiggerNumber(j,pom):
                    array.setById(j+1,array.getById(j))
                else:
                    array.setById(j+1,pom)
                    break

