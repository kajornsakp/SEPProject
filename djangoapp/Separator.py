

class Separator:

    def __init__(self):
        self.keyword = ['reminder','calendar','note','hw']

    def findKeyword(self,keyword):
        if keyword in self.keyword:
            return keyword

