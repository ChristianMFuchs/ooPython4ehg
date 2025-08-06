from shoeClass import shoe

def main():
    christianShoe = shoe('red', 50, 'NB')
    print(christianShoe.getShoeModel())
    print(christianShoe.getShoeColor())
    print(christianShoe.getShoePrice())
    print(christianShoe.getShoeBuyer())
    print('-----')
    print(christianShoe.shoeModel)
    print(christianShoe.shoeColor)
    print(christianShoe.shoePrice)
    print(christianShoe.shoeBuyer)
    print('-----')
    christianShoe.setShoeBuyer('Christian')
    print(christianShoe.getShoeBuyer())
    return 1

main()