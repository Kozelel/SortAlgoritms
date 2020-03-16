from Lab.LabArrays import LabArrays
from random import randint
import time
class LabSort:
    #rosnąco
    def __init__(self,len,type):
        self.__time=0
        self.__array=LabArrays()
        self.__array.newArray()
        array=self.__array.getArrayById(0)
        if type=='random':
            for i in range(len):
                array.push(randint(-999999,999999))
        elif type=='sorted':
            for i in range(len):
                array.push(i)
        elif type=='unsorted':
            for i in range(len):
                array.push(len-i)
    def stat(self):
        pom=self.__array.stat()
        pom['time']=self.__time
        return pom
    def getArray(self):
        return self.__array
    def run(self):
        start_time = time.time()
        self.mainSort()
        self.__time=time.time() - start_time