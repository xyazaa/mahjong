#hand = [s1,s2,s3,s4,s5.. we,ws,ww,wn, dr,dw,dg]

suit = ["s", "m", "p"]
honours= ["w", "d"]

example = ["s1", "s2", "s3", "m4", "m4", "m4", "we", "we", "we", "p6", "p7", "p8", "dr", "dr"]
exampleKokushi = ["s1", "s9", "m1", "m9", "p1", "p9", "we", "ws", "ww", "wn", "dr", "dg", "dw", "dw"]


def checkFormat(hand): #assert if the hand is a valid winning hand, ignoring if there is a valid yaku
    if len(hand) < 14: #kan?
        return False
    
    for tile in hand:
        if len(tile) != 2:
            return False
        if tile[0] in suit:
            if not 0<int(tile[1])<10:
                return False
        elif tile[0] in honours:
             match tile[0]:
                case "d":
                    if not tile[1] in ["r", "g" "w"]:
                        return False
                case "w":
                    if not tile[1] in ["e", "s", "w", "n"]:
                        return False
        else:
            return False

    return True

def checkKokushi(hand):
    if len(hand)!=14:
        return False

    kokushi = ["s1", "s9", "m1", "m9", "p1", "p9", "we", "ws", "ww", "wn", "dr", "dg", "dw"]

    fHand = hand.copy() #prevent hand from being changed inside the function

    for tile in kokushi:
        if tile in fHand:
            fHand.remove(tile)

    if len(fHand)!=1:
        return False
    
    if set(fHand).issubset(kokushi):
        return True
    else:
        return False

# sort hand into 4 melds and a pair, what about yakumans? ->  only kokushi is special (not conforming to standard)
# what about open hands?
def scoreHand(hand, open):
    #for every permutation of a winnable hand, calculate the score and then return highest scoring hand.
    groups = []
    hand.sort()
    copyHand = hand.copy()
    while True:
        for i in range(4):
            if len(copyHand)!=2:
                if copyHand[0][0] in suit:


if checkKokushi(exampleKokushi):
    print("true")
    print(exampleKokushi)
else:
    print("false")