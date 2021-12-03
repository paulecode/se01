"""
Water sort

0: free space
1: green
2: red
"""

beakers = {
    "1": [1, 0, 0],
    "2": [2, 1, 2],
    "3": [2, 1, 0]
}

# print (beakers)

def getTopLiquid(beaker):
    beaker = beaker.copy()
    while beaker:
        topLiquid = beaker.pop()
        if topLiquid == 0:
            continue
        else:
            return topLiquid
    
    return "Its empty"

def checkSpace(beaker):
    beaker = beaker.copy()
    emptySpace = 0
    while beaker:
        topLiquid = beaker.pop()
        if topLiquid == 0:
            emptySpace += 1
        else:
            break
    return emptySpace

def getTopLiquidLength(beaker):
    beaker = beaker.copy()
    length = 0
    color = getTopLiquid(beaker)
    while beaker:
        topLiquid = beaker.pop()
        if topLiquid == 0:
            continue
        if topLiquid == color:
            length += 1
        else: 
            break
    return length

def checkMove(sourceselector, targetselector):

    source = beakers[sourceselector]
    target = beakers[targetselector]
    
    print (getTopLiquid(target))
    print (getTopLiquid(source))

    print (source)
    print (target)

    # print (getTopLiquid(source) == getTopLiquid(target))
    print (checkSpace(target))
    print (getTopLiquidLength(source))


    #TODO Exception upon not available

    if (checkSpace(target) >=  getTopLiquidLength(source)):
        # Enough Space
        if (getTopLiquid(source) == getTopLiquid(target)):
            print ("Legal")
            
        else: 
            print ("Illegal not the same")
    else:
        print ("Illegal no space")

checkMove(sourceselector = input("Source: "), targetselector = input("Target: "))

# print (getTopLiquidLength([2, 1, 2])) 
# source = input()


# print (getTopLiquid([1,0,0]))
# print (getTopLiquid([2,1,0]))

# print (getTopLiquid([2,1,0]) == getTopLiquid([1,0,0]))


# print (getTopLiquidLength([1, 0, 0]))
# print (checkSpace([2, 1, 0]))

# print (checkSpace([2, 1, 0]) >= getTopLiquidLength([1,0,0]))