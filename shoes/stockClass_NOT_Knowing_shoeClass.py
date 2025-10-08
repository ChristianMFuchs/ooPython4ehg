from shoeClass import shoe

class stock_NOT_KnowingShoeClass():

    def __init__(self):
        self.stock = []
        return None
    
    # get methods: methods to access the attribus.
    def getStock(self):
        return self.stock
        
    # set methods: methods to modify values, in case menaingfull for the use case
    # change value of the price of the shoe
    def setStock(self, newStock: int):
        self.stock = newStock
        return 1
    
    # add a pair of shoes to the stock
    def addShoes(self, newPair: shoe):
        self.stock.append(newPair)
        return 1
    
    def isAvailable(self, compareShoe: shoe):
        isShoeThere = False
        for i in self.stock:
            if (compareShoe.shoeColor ==  i.shoeColor and 
                compareShoe.shoeModel == i.shoeModel and 
                compareShoe.shoePrice == i.shoePrice):
                isShoeThere = True
                pass
        return isShoeThere
    
    def indexLocation(self, compareShoe: shoe):
        isShoeThere = self.isAvailable(compareShoe)
        indexLocation = -1
        if isShoeThere:
            for i in self.stock:
                indexLocation += 1
                if (compareShoe.shoeColor ==  i.shoeColor and 
                    compareShoe.shoeModel == i.shoeModel and 
                    compareShoe.shoePrice == i.shoePrice):
                    pass
        return indexLocation
    
    def removeShoe(self, removeShoe: shoe):
        isShoeThere = self.isAvailable(removeShoe)
        if isShoeThere:
            indexLocation = self.indexLocation(removeShoe)
            self.stock.remove(self.stock[indexLocation])
            return 1
        else:
            return 0
    
    def sellShoe(self, sellShoe: shoe, buyer:str):
        for i in self.stock:
            #
            if self.isAvailable(sellShoe):
                
                pass
            #
        return 1
    
    def numShoesInStock(self):
        return len(self.stock)