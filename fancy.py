"""
Classiness Scorer

Created by Jeffery Ansah
py3


"""


class Classy(object):
    def __init__(self):
        self.items = [] # list hold items
        self.lookup = {"tophat" : 2,
                       "bowtie": 4,
                       "monocle" : 5
                        }    #hash table to map items  to the wieghted score
        self.scores = 0   # initialise the score to zero
        
    def addItem(self,item):
        """
        This function will accept the item and append it to the items list.
        The function will keep track of the last value of the score value and calculate the new score base on the most
        recent item to be added
        """
        self.items.append(item)   
        if item in self.lookup.keys():
            self.scores = self.lookup[item] + self.scores


        
    def getClassiness(self):
        return self.scores



# Test cases
me = Classy()
#should be 0
print me.getClassiness()

me.addItem("tophat")
#should be 2
print me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
#should be 11
print me.getClassiness()


me.addItem("bowtie")
#should be 15
print me.getClassiness()