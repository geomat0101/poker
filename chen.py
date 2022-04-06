#!/usr/bin/env python

# chen formula calculator
# http://www.thepokerbank.com/strategy/basic/starting-hand-selection/chen-formula/

import math
import sys

if len(sys.argv) < 2:
    print "Usage: %s cardOne cardTwo ['s' for suited]" % sys.argv[0]
    sys.exit(1)

cardOne, cardTwo = (_.lower() for _ in sys.argv[1:3])
suited = False
if len(sys.argv) == 4:
    if cardOne == cardTwo:
        print "WARNING: pairs cannot be suited.  disabling suited flag."
    elif sys.argv[3].lower() == 's':
        suited = True

# base scores for face cards
cardScores = {
        'a': 10,
        'k': 8,
        'q': 7,
        'j': 6,
        't': 5
        }

# ordinal scoreues for face cards
cardOrds = {
        'a': 14,
        'k': 13,
        'q': 12,
        'j': 11,
        't': 10
        }


def getBaseScore (card):
    if card in cardScores:
        return cardScores[card]
    
    return int(card)/2.


def getOrd (card):
    if card in cardOrds:
        return cardOrds[card]

    return int(card)


result = 0
scoreOne = getBaseScore(cardOne)
scoreTwo = getBaseScore(cardTwo)
ordOne = getOrd(cardOne)
ordTwo = getOrd(cardTwo)
gap = 0

# score highest card, compute gap
if scoreOne > scoreTwo:
    result += scoreOne
    gap = ordOne - ordTwo - 1
elif scoreOne == scoreTwo:
    pairScore = scoreOne + scoreTwo
    if pairScore < 5:
        result += 5
    else:
        result += pairScore
else:
    result += scoreTwo
    gap = ordTwo - ordOne - 1

# suited bonus
if suited:
    result += 2

# penalty for gaps between cards
if gap < 3:
    result -= gap
elif gap == 3:
    result -= 4
else:
    result -= 5

# black magic bonus
if (cardOne != cardTwo and
        scoreOne < cardScores['q'] and
        scoreTwo < cardScores['q'] and
        gap < 2):
    result += 1

# round up
result = int(math.ceil(result))
early, mid, late = 'fold', 'fold', 'fold'

if result >= 10:
    early, mid, late = 'raise', 'raise', 'raise'
elif result == 9:
    mid, late = 'raise', 'raise'
elif result >= 7:
    late = 'raise'

print "%d: early/mid/late %s/%s/%s" % (result, early, mid, late)





















