from shoeClass import shoe
from stockClass_NOT_Knowing_shoeClass import stock_NOT_KnowingShoeClass

def main():
    jg2ShowStock =  stock_NOT_KnowingShoeClass()

    shoeA = shoe('Blue', 150, 'ADIDAS')
    shoeB = shoe('White', 160, 'ADIDAS')
    shoeC = shoe('Red', 170, 'ADIDAS')
    shoeD = shoe('Red', 170, 'ADIDAS')

    jg2ShowStock.addShoes(shoeA)
    jg2ShowStock.addShoes(shoeB)
    jg2ShowStock.addShoes(shoeC)
    
    print('Number of shoes in stock: ', jg2ShowStock.numShoesInStock())
    jg2ShowStock.removeShoe(shoeD)
    print('Number of shoes in stock after removal: ', jg2ShowStock.numShoesInStock())
    return 1

main()