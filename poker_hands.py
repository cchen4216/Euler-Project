
CARDS = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def isFlush1(hand):
    if len(hand) != 5:
        print 'error in issamesuit'
        quit()
    if hand[0][1]==hand[1][1]==hand[2][1]==hand[3][1]==hand[4][1]:
        return True
    return False

def isStraight(hand):
    global CARDS
    nums = []
    for i in sorted(hand, key=sortkey):
        nums.append(i[0])
    for i in range(len(CARDS)-4):
        if nums == CARDS[i:i+5]:
            return True, CARDS[i+4]
    return False, None

def is4Kind(hand):
    hand = sorted(hand, key=sortkey)
    if len(hand) != 5:
        print 'Error in is4Kind'
        quit()
    for i in range(len(hand)-3):
        if hand[i][0]==hand[i+1][0]==hand[i+2][0]==hand[i+3][0]:
            return True, hand[i][0]
    return False, None

def is3Kind(hand):
    hand = sorted(hand, key=sortkey)
    if len(hand) != 5:
        print 'Error in is4Kind'
        quit()
    for i in range(len(hand)-2):
        if hand[i][0]==hand[i+1][0]==hand[i+2][0]:
            return True, hand[i][0]
    return False, -1

#temp = ['2H', '3H', '2D', '4D', '2D']
#print is3Kind(temp)
#quit()

def is2Kind(hand):
    hand = sorted(hand, key=sortkey)
    if len(hand) != 5:
        print 'Error in is4Kind'
        quit()
    for i in range(len(hand)-1):
        if hand[i][0]==hand[i+1][0]: #!=hand[i+2][0]:
            if i < 2:
                for j in range(i+2,len(hand)-1):
                    if hand[j][0]==hand[j+1][0]:
                        return True, hand[i][0], hand[j][0]
            return True, hand[i][0], -1
    return False, -1, -1

#temp = ['2H', '3H', '4D', '7D', '5D']
#print is2Kind(temp)
#quit()

def sortkey(str):
    global CARDS
    return CARDS.index(str[0])

def compareHands(hand1, hand2):
    flush1 = isFlush1(hand1)
    flush2 = isFlush1(hand2)
    straight1, cardS1 = isStraight(hand1)
    straight2, cardS2 = isStraight(hand2)

    # At least one hand is straight flush
    if (flush1 and straight1) and (flush2 and straight2):
        if CARDS.index(cardS1) > CARDS.index(cardS2):
            return 1      # hand1 larger
        elif CARDS.index(cardS1) < CARDS.index(cardS2):
            return 2      # hand2 larger
        else:
            return 0      # tie
    elif (flush1 and straight1) and not (flush2 and straight2):
        return 1         # hand1 straight flush, hand2 not
    elif not (flush1 and straight1) and (flush2 and straight2):
        return 2

    # Both are not straight flush
    # At least one hand is 4kind
    kind41, card41 = is4Kind(hand1)
    kind42, card42 = is4Kind(hand2)
    if kind41 and kind42:
        if CARDS.index(card41) > CARDS.index(card42):
            return 1
        elif CARDS.index(card41) < CARDS.index(card42):
            return 2
        else:
            temp1 = sorted(hand1, key=sortkey, reverse=True)
            temp2 = sorted(hand2, key=sortkey, reverse=True)
            for i in range(len(temp1)):
                if CARDS.index(temp1[i][0]) < CARDS.index(temp2[i][0]):
                    return 2
                elif CARDS.index(temp1[i][0]) > CARDS.index(temp2[i][0]):
                    return 1
            return 0
    elif kind41 and not kind42:
        return 1
    elif not kind41 and kind42:
        return 2

    # Both are not straight flush
    # Both hands are not 4kind
    # At least one is Full-house
    kind31, card31 = is3Kind(hand1)
    kind32, card32 = is3Kind(hand2)
    kind21, card21, card211 = is2Kind(hand1)
    kind22, card22, card222 = is2Kind(hand2)
    bool1 = kind31 and card211 != -1
    bool2 = kind32 and card222 != -1
    if bool1 and bool2:
        if CARDS.index(card31) > CARDS.index(card32):
            return 1
        elif CARDS.index(card31) < CARDS.index(card32):
            return 2
        else:
            temp1 = max(card21, card211)
            temp2 = max(card22, card222)
            if temp1 > temp2:
                return 1
            elif temp1 < temp2:
                return 2
            else:
                return 0
    elif bool1 and not bool2:
        return 1
    elif not bool1 and bool2:
        return 2

    # At least one is flush
    if flush1 and flush2:
        temp1 = sorted(hand1, key=sortkey, reverse=True)
        temp2 = sorted(hand2, key=sortkey, reverse=True)
        for i in range(len(temp1)):
            if CARDS.index(temp1[i][0]) < CARDS.index(temp2[i][0]):
                return 2
            elif CARDS.index(temp1[i][0]) > CARDS.index(temp2[i][0]):
                return 1
        return 0
    elif flush1 and not flush2:
        return 1
    elif not flush1 and flush2:
        return 2

    # At least one is straight
    if straight1 and straight2:
        if CARDS.index(cardS1) > CARDS.index(cardS2) :
            return 1
        elif CARDS.index(cardS1) < CARDS.index(cardS2):
            return 2
        else:
            return 0
    elif straight1 and not straight2:
        return 1
    elif not straight1 and straight2:
        return 2

    # At least one is 3kind
    if kind31 and kind32:
        if CARDS.index(card31) > CARDS.index(card32):
            return 1
        elif CARDS.index(card31) < CARDS.index(card32):
            return 2
        else:
            temp1 = sorted(hand1, key=sortkey, reverse=True)
            temp2 = sorted(hand2, key=sortkey, reverse=True)
            for i in range(len(temp1)):
                if CARDS.index(temp1[i][0]) < CARDS.index(temp2[i][0]):
                    return 2
                elif CARDS.index(temp1[i][0]) > CARDS.index(temp2[i][0]):
                    return 1
            return 0
    elif kind31 and not kind32:
        return 1
    elif not kind31 and kind32:
        return 2

    # At least one is two pairs
    bool1 = kind21 and card211!=-1
    bool2 = kind22 and card222!=-1
    if bool1 and bool2 :
        temp1 = sorted(hand1, key=sortkey, reverse=True)
        temp2 = sorted(hand2, key=sortkey, reverse=True)
        for i in range(len(temp1)):
            if CARDS.index(temp1[i][0]) < CARDS.index(temp2[i][0]):
                return 2
            elif CARDS.index(temp1[i][0]) > CARDS.index(temp2[i][0]):
                return 1
        return 0
    elif bool1 and not bool2 :
        return 1
    elif not bool1 and bool2:
        return 2

    # At least one is one pair
    if kind21 and kind22:
        if CARDS.index(card21) > CARDS.index(card22):
            return 1
        elif CARDS.index(card21) < CARDS.index(card22):
            return 2
        else:
            temp1 = sorted(hand1, key=sortkey, reverse=True)
            temp2 = sorted(hand2, key=sortkey, reverse=True)
            for i in range(len(temp1)):
                if CARDS.index(temp1[i][0]) < CARDS.index(temp2[i][0]):
                    return 2
                elif CARDS.index(temp1[i][0]) > CARDS.index(temp2[i][0]):
                    return 1
            return 0
    elif kind21 and not kind22:
        return 1
    elif not kind21 and kind22:
        return 2

    # only compare the values of cards from large to small
    temp1 = sorted(hand1, key=sortkey, reverse=True)
    temp2 = sorted(hand2, key=sortkey, reverse=True)

    for i in range(len(temp1)):
        if CARDS.index(temp1[i][0]) < CARDS.index(temp2[i][0]):
            #print 'a'
            return 2
        elif CARDS.index(temp1[i][0]) > CARDS.index(temp2[i][0]):
            #print 'b'
            return 1
    return 0

#test1 = ['2D', '9C', 'AS', 'AH', 'AC']
#test2 = ['3D', '6D', '7D', 'TD', 'QD']
#test1 = ['4D', '8H', '5D', '6D', 'TD']
#test2 = ['7D', '9H', '4C', '3B', '2D']
#test1 = ['4D', '6S', '9H', 'QH', 'QC']
#test2 = ['3D', '6D', '7H', 'QD', 'QS']
#test1 = ['2H', '2D', '4C', '4D', '4S']
#test2 = ['3C', '3D', '3S', '9S', '9D']
#test1 = ['5H', '5C', '6S', '7S', 'KD']
#test2 = ['2C', '3S', '8S', '8D', 'TD']
#test1 = ['5D', '8C', '9S', 'JS', 'AC']
#test2 = ['2C', '5C', '7D', '8S', 'QH']
#print compareHands(test1, test2)
#quit()

fobj = open('p054_poker.txt')
hands = fobj.readlines()

player1 = []
player2 = []
count = 0
count2 = 0
for i in hands[:]:
    temp = i.split()
    #player1.append(sorted(temp[:5]))
    #player2.append(sorted(temp[5:]))
    hand1 = sorted(temp[:5], key=sortkey)
    hand2 = sorted(temp[5:], key=sortkey)
    result = compareHands(hand1,hand2)
    #print hand1, hand2, result
    if result == 1:
        count += 1
    elif result == 2:
        count2 += 1

print count, count2
#print player1[0]
#print player2[0]
