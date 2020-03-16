class Config:
    def __init__(self,name,type='random',xStart=10000,xStop=100001,Step=10000,maxTime=5):
        self.__name=name
        self.__type=type
        self.__xStart=xStart
        self.__xStop=xStop
        self.__Step=Step
        self.__maxTime=maxTime
    def getType(self):
        return self.__type
    def getName(self):
        return self.__name
    def getXStart(self):
        return self.__xStart
    def getXStop(self):
        return self.__xStop
    def getStep(self):
        return self.__Step
    def getMaxTime(self):
        return self.__maxTime