from shoeClass import shoe

class stockKnowingShoeClass():

    def __init__(self):
        self.stock = []
        return None
    
    # get methods: methods to access the attribus.
    def getStock(self):
        return self.stock
        
    # set methods: methods to modify values, in case menaingfull for the use case
    # change value of the price of the shoe
    def setStock(self, newStock: list):
        self.stock = newStock
        return 1
    
    # general methods
    def addShoe(self, newShoeColor: str, newShoeModel: str, newShoePrice: int):
        newShoe = shoe(newShoeColor, newShoePrice, newShoeModel)
        self.stock.append(newShoe)
        return 1
    
    def existShoe(self, newShoeColor: str, newShoeModel: str, newShoePrice: int):
        isShoeThere = False
        for i in self.stock:
            if newShoeColor ==  i.shoeColor and newShoeModel == i.shoeModel and newShoePrice == i.shoePrice:
                isShoeThere = True
                pass
        return isShoeThere
    
    def indexShoe(self, newShoeColor: str, newShoeModel: str, newShoePrice: int):
        isShoeThere = self.existShoe(newShoeColor, newShoeModel, newShoePrice)
        indexLocation = -1
        if isShoeThere:
            for i in self.stock:
                if newShoeColor ==  i.shoeColor and newShoeModel == i.shoeModel and newShoePrice == i.shoePrice:
                    indexLocation = self.stock.index(i)
                    pass
        return indexLocation
    
    def removeShoe(self, newShoeColor: str, newShoeModel: str, newShoePrice: int):
            isShoeThere = self.existShoe(newShoeColor, newShoeModel, newShoePrice)
            if isShoeThere:
                indexLocation = self.indexShoe(newShoeColor, newShoeModel, newShoePrice)
                self.stock.remove(self.stock[indexLocation])
                return 1
            else:
                return 0
    
    def sellShoe(self, newShoeColor: str, newShoeModel: str, newShoePrice: int, newBuyer: str):
        isShoeThere = self.existShoe(newShoeColor, newShoeModel, newShoePrice)
        if isShoeThere:
            for i in self.stock:
                indexLocation = self.indexShoe(newShoeColor, newShoeModel, newShoePrice)
                self.stock[indexLocation].shoebuyer = newBuyer
                pass
        return 1
    
    def numShoesInStock(self):
        return len(self.stock)
