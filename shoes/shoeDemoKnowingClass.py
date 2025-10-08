from shoeClass import shoe
from stockClass_Knowing_shoeClass import stockKnowingShoeClass

def main():
    jg2ShowStock =  stockKnowingShoeClass()

    jg2ShowStock.addShoe('Blue', 'Alpha', 150)
    jg2ShowStock.addShoe('Red', 'Beta', 200)
    jg2ShowStock.addShoe('Yellow', 'Gamma', 100)
    print('Number of shoes in stock: ', jg2ShowStock.numShoesInStock())
    jg2ShowStock.removeShoe('Blue', 'Alpha', 150)
    print('Number of shoes in stock after removal: ', jg2ShowStock.numShoesInStock())
    jg2ShowStock.sellShoe('Blue', 'Alpha', 150, 'Person')
    print('Number of shoes in stock after selling: ', jg2ShowStock.numShoesInStock())
    return 1


main()