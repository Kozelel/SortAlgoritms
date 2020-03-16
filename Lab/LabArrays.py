from Lab.LabArray import LabArray
class LabArrays:
    def __init__(self):
        self.__arrays=[]
        self.__arraysCount=0
    def newArray(self):
        self.__arraysCount+=1
        self.__arrays.append(LabArray())
        return self.__arraysCount-1
    def getArrayById(self,id):
        return self.__arrays[id]
    def stat(self):
        dir={}
        dir['countOfArrays']=self.__arraysCount
        dir['swaps']=0
        dir['comparisions']=0
        dir['accessToArray']=0
        dir['sets']=0
        for i in range(self.__arraysCount):
            stat=self.__arrays[i].stat()
            dir['swaps']+=stat['swaps']
            dir['comparisions']+=stat['comparisions']
            dir['accessToArray']+=stat['accessToArray']
            dir['sets']+=stat['sets']
        return dir
    def printArray(self):
        print(self.getArrayById(0).getArray())



