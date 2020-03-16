class LabArray:
    def __init__(self):
        self.__array=[]
        self.__accessToArray=0
        self.__comparisions=0
        self.__swaps=0
        self.__sets=0
    def __len__(self):
        return len(self.__array)
    def push(self,new):
        self.__array.append(new)
    def getById(self,id):
        self.__accessToArray+=1
        return self.__array[id]
    def setById(self,id,new):
        self.__sets+=1
        self.__accessToArray+=1
        self.__array[id]=new
    def isBigger(self,a,b):
        self.__comparisions+=1
        if self.getById(a)>self.getById(b):
            return 1
        return 0
    def isBiggerNumber(self,index,number):
        self.__comparisions+=1
        if self.getById(index)>number:
            return 1
        return 0
    def isLower(self,a,b):
        self.__comparisions += 1
        if self.getById(a) < self.getById(b):
            return 1
        return 0
    def isLowerNumber(self,index,number):
        self.__comparisions+=1
        if self.getById(index)<number:
            return 1
        return 0
    def getArray(self):
        return self.__array
    def swap(self,a,b):
        self.__swaps+=1
        pom=self.getById(a)
        self.setById(a,self.getById(b))
        self.setById(b,pom)
    def stat(self):
        dir ={}
        dir['swaps']=self.__swaps
        dir['comparisions']=self.__comparisions
        dir['accessToArray']=self.__accessToArray
        dir['sets']=self.__sets-(2*self.__swaps)
        return dir