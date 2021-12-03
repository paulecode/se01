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
    
    # print (getTopLiquid(target))
    # print (getTopLiquid(source))

    # print (source)
    # print (target)

    # # print (getTopLiquid(source) == getTopLiquid(target))
    # print (checkSpace(target))
    # print (getTopLiquidLength(source))


    #TODO Exception upon not available

    if (checkSpace(target) >=  getTopLiquidLength(source)):
        # Enough Space
        if (getTopLiquid(source) == getTopLiquid(target)):
            print ("Legal")
            return True
        else: 
            print ("Illegal not the same")
    else:
        print ("Illegal no space")



def makeMove(sourceselector, targetselector):
    source = beakers[sourceselector]
    target = beakers[targetselector]

    topLiquid = getTopLiquid(source)
    topLiquidLength = getTopLiquidLength(source)

    # source.reverse()
    target.reverse()

    for x in range(topLiquidLength):
        source[x] = 0

    for x in range(topLiquidLength):
        target[x] = topLiquid

    target.reverse()
    print (source)
    print (target)

    print (beakers)

    return beakers

def play():
    sourceselector = input("Source: ")
    targetselector = input("Target: ")

    legal = checkMove(sourceselector, targetselector)
    if legal:
        makeMove(sourceselector, targetselector)

play()