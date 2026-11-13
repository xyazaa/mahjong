import inspect

# Assune that the given parameters are in the right format.-> not modular, should include basic checks and edge cases for direct use.
# assume sorted into melds and melds are sorted.
# where to calculate fu? with the yaku or seperate
# maybe include all methods from mahjong in here, for it to be a more inclusive and self reliant class


class CountYaku:
    def __init__(self, pHand, pDora, pRiichi, pTsuron, pOpen, pSeat):
        self.hand = pHand
        self.dora = pDora
        self.riichi = pRiichi
        self.tsuron = pTsuron
        self.open = pOpen
        self.seat = pSeat
        self.achievedYaku = []
        self.yaku = ['riichi', 'menzentsumo', 'pinfu', 'iipeikou', 'ryanpeikou', 'chiitoitsu', 'yakuhai', 'shousangen', 'daisangen', 'shousuushi', 'daisuushi', 'tanyao', 'sanshokudoujun', 'ittsu', 'chanta', 'junchan', 'honroutou', 'chinroutou', 'tsuuiisou', 'toitoi', 'sanankou', 'suuankou', 'sankantsu', 'suukantsu', 'sanshokudoukou', 'honitsu', 'chinitsu', 'ryuuiisou', 'chuurenpoutou']
        self.han = 0
        self.fu = 0

    def isSequence(meld):
        if len(meld)==3 and int(meld[0][1])+1==int(meld[1][1]) and int(meld[1][1])+1==int(meld[2][1]):
            return True
        return False

    def score(self):
        cYaku = self.yaku.copy()
        if self.open:
            cYaku = [x for x in cYaku if x not in ['riichi', 'menzentsumo', 'pinfu', 'iipeikou', 'ryanpeikou', 'chiitoitsu']]

        while len(cYaku)!=0:
            currentYaku = cYaku.pop(0)
            getattr(self, currentYaku)(cYaku)
                

    def riichi(self, yaku):
        if riichi:
            self.han +=1
            self.achievedYaku.append('Riichi')
            return True
        return False
        
    def menzentsumo(self, yaku):
        if not self.open and self.tsuron[0] == 'tsumo':
            self.han+=1
            self.achievedYaku.append('Menzen Tsumo')
            return True
        return False
    
    # need to check where the double is and if the winning tile is a side wait on each meld.
    def pinfu(self, yaku):
        for meld in self.hand: #checks if the hand contains anything that will eliminate it from pinfu
            if len(meld)==2 and meld[1]==self.tsuron[1]: #double check
                return False
            elif not isSequence(meld):
                return False
            elif tsuron[1] in meld and meld.index(tsuron[1])==1::
                return False
        self.han +=1
        self.achievedYaku.append('Pinfu')
        # Remove all yaku which cannot be achieved if pinfu is achieved
        yaku[:] = [x for x in yaku if x not in ['chiitoitsu', 'yakuhai','shousangen', 'daisangen', 'shousuushi', 'daisuushi', 'honroutou', 'chinroutou', 'tsuuiisou', 'toitoi', 'sanankou', 'suuankou', 'sankantsu', 'suukantsu', 'sanshokudoukou', 'honitsu','ryuuiisou', 'chuurenpoutou']]
        return True

    def iipeikou(self, yaku): 
        for meld in self.hand:
            if self.hand.count(meld) == 2:
                self.han += 1
                self.achievedYaku.append('Iipeikou')
                ryanpeikou()
                return True
        return False

    def ryanpeikou(self, yaku):
        firstPair = None
        for meld in self.hand:
            if firstPair == None and self.hand.count(meld) == 2:
                firstPair = meld
            elif not meld == firstPair and self.hand.count(meld) == 2:
                # ryanpeikou found
                if 'Iipeikou' in self.achievedYaku: # Case where Iipeikou calls Ryanpeikou or iipeikou is added from somewhere
                    self.achievedYaku.remove('Iipeikou')
                    self.han += 2
                else:
                    self.han += 3
                self.achievedYaku.append('Ryanpeikou')
                return True
        return False


    def chiitoitsu(self, yaku): # the current format cannot deal with chiitoitsu here
        return

    def yakuhai(self,yaku):
        return
    
    def shousangen(self, yaku)
        return
