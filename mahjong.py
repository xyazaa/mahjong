#hand = [s1,s2,s3,s4,s5.. we,ws,ww,wn, dr,dw,dg]

suit = ["s", "m", "p"]
honours= ["w", "d"]

example = ["s1", "s2", "s3", "m4", "m4", "m4", "we", "we", "we", "p6", "p7", "p8", "dr", "dr"]
example2 = ["s2", "s2", "s2", "s3", "s4", "m3", "m3", "m3", "m4", "m5", "m6", "p7", "p8", "p9"]
example3 = ["m1", "m1", "m2", "m2", "m3", "m3", "p1", "p2", "p2", "p3","p3", "p4", "we", "we"]
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

# sort hand into 4 melds and a pair, what about yakumans? ->  only kokushi is special (not conforming to standard) + chitoitsu
def sortHand(hand, open):
    #Can refactor so that only hand is needed, no meld variable 
    groups = []
    look = 0
    hand.sort()
    print(hand)
    while True:
        if look+2>len(hand): #if there still exist hand[look] and hand[look+1] there must be a double error
            break
        meld = hand[look:look+3]
        print(meld)
        if not meld[0][0]==meld[1][0]:
            break
            #wrong hand, how can the first tile suit not be equal to the second?
        if len(meld)==2 or not meld[1][0]==meld[2][0]:
            #minimum double
            if meld[0]==meld[1]:
                #double
                groups.append(meld[0:2])
                look+=2
            elif int(meld[0][1])+1 == int(meld[1][1]):
                groups[-1].pop(-1)
                look-=1
        elif meld[0]==meld[1] and meld[1]==meld[2]:
            groups.append(meld)
            look+=3
        elif int(meld[0][1])+1 == int(meld[1][1]) and int(meld[1][1])+1 == int(meld[2][1]):
            groups.append(meld)
            look+=3
        elif all(int(hand[look+offset][1])+1 == int(hand[look+2+offset][1]) and int(hand[look+2+offset][1])+1 == int(hand[look+4+offset][1]) for offset in [0,1]):
            groups.append(hand[look:look+6:2])
            groups.append(hand[look+1:look+7:2])
            look+=6
    return groups


def scoreHand(melds, dora, riichi, tsuron, open, dealer):
    han=0
    fu=0
        
    for m in melds:
        for t in m:
            if t == dora:
                han += 1

print(sortHand(example3, 1))
