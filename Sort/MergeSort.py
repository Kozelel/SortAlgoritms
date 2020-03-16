from Sort.LabSort import LabSort
class MergeSort(LabSort):
    def __init__(self, len, type):
        super().__init__(len, type)
    def mainSort(self):
        self.mergeSort(self.getArray(),0)
    def mergeSort(self,array,arrayId):
        mainArray=array.getArrayById(arrayId)
        length=len(mainArray)
        if length==1:
            return array.getArrayById(arrayId)
        leftArrayId=array.newArray()
        rightArrayId=array.newArray()
        leftArray=array.getArrayById(leftArrayId)
        rightArray=array.getArrayById(rightArrayId)
        for i in range(0,int(length/2)):
            leftArray.push(mainArray.getById(i))
        for i in range(int(length/2),length):
            rightArray.push(mainArray.getById(i))
        leftArray=self.mergeSort(array,leftArrayId)
        rightArray=self.mergeSort(array,rightArrayId)
        leftIterator=0
        rightIterator=0
        for i in range(0,length):
            if leftIterator<len(leftArray) and rightIterator<len(rightArray):
                if leftArray.isLowerNumber(leftIterator,rightArray.getById(rightIterator)):
                    mainArray.setById(i,leftArray.getById(leftIterator))
                    leftIterator+=1
                else:
                    mainArray.setById(i,rightArray.getById(rightIterator))
                    rightIterator+=1
            elif leftIterator<len(leftArray):
                mainArray.setById(i, leftArray.getById(leftIterator))
                leftIterator += 1
            elif rightIterator<len(rightArray):
                mainArray.setById(i, rightArray.getById(rightIterator))
                rightIterator += 1
            else:
                raise Exception("Blad dlugosci tablic tworzonych")
        return mainArray

