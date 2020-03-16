from Sort.LabSort import LabSort
class BubbleSort(LabSort):
    def __init__(self, len, type):
        super().__init__(len, type)
    def mainSort(self):
        unsorted = 1
        iter = -1
        array =self.getArray().getArrayById(0)
        while unsorted == 1:
            unsorted = 0
            iter += 1
            for i in range(len(array) - iter - 1):
                if array.isBigger(i, i + 1):
                    array.swap(i, i + 1)
                    unsorted = 1

