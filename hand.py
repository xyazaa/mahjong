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


    def score():
        if self.open:
            self.yaku = [x for x in self.yaku if x not in ['riichi', 'menzentsumo', 'pinfu', 'iipeikou', 'ryanpeikou', 'chiitoitsu']]

        while len(self.yaku)!=0:
            currentYaku = self.yaku.pop(0)
            getattr(self, currentYaku)
                

    def riichi():
        if riichi:
            self.han +=1
            achievedYaku.append('riichi')
        
    def menzentsumo():