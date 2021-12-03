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
    while beaker:
        topLiquid = beaker.pop()
        if topLiquid == 0:
            continue
        else:
            return topLiquid
    
    return "Its empty"

def checkSpace(beaker):
    emptySpace = 0
    while beaker:
        topLiquid = beaker.pop()
        if topLiquid == 0:
            emptySpace += 1
        else:
            break
    return emptySpace

def getTopLiquidLength(beaker):
    length = 1
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

def checkMove():
    source = input('Sourcebeaker: ')
    target = input('Targetbeaker: ')
    print (beakers[target])

    #TODO Exception upon not available

    if (checkSpace(beakers[target]) >=  getTopLiquidLength(beakers[source])):
        # Enough Space
        if (getTopLiquid(beakers[source]) == getTopLiquid(beakers[target])):
            print ("Legal")
            
        else: 
            print ("Illegal not the same")
    else:
        print ("Illegal no space")

# checkMove()

print (getTopLiquidLength([2, 1, 2]))

# print (getTopLiquid([1,0,0]))
# print (getTopLiquid([2,1,0]))

# print (getTopLiquid([2,1,0]) == getTopLiquid([1,0,0]))


# print (getTopLiquidLength([1, 0, 0]))
# print (checkSpace([2, 1, 0]))

# print (checkSpace([2, 1, 0]) >= getTopLiquidLength([1,0,0]))