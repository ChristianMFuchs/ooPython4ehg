#
#
class shoe():

    def __init__(self, shoeColor: str, shoePrice: int, shoeModel: str):
        self.shoeColor = shoeColor
        self.shoeModel = shoeModel
        self.shoePrice = shoePrice
        self.shoeBuyer = "-"
        return None
    
    # get methods: methods to access the attribus.
    def getShoeColor(self):
        return self.shoeColor
    
    def getShoeModel(self):
        return self.shoeModel
    
    def getShoePrice(self):
        return self.shoePrice
    
    def getShoeBuyer(self):
        return self.shoeBuyer
    
    # set methods: methods to modify values, in case menaingfull for the use case
    # change value of the price of the shoe
    def setShoePrice(self, newShoePrice: int):
        self.setShowPrice = newShoePrice
        return 1

    # define the name of the buyer, when the show is sold
    def setShoeBuyer(self, newBuyer: str):
        self.shoeBuyer = newBuyer
        return 1

    # provide easy method to find out, whether a show is sold or not
    def isShowSold(self):
        if self.buyer == '-':
             isSold = False
        else:
            isSold = True
        return isSold
    #
    #
