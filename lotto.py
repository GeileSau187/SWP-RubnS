import random

# 1) Define constants (same style as lotto example)
SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

CARDS_PER_SUIT = 13
TOTAL_CARDS = 52
CARDS_PER_HAND = 5
SIM_DRAWS = 100000  # 100k simulations as required

# Reference probabilities from standard 5-card poker math (in %)
# Flush = excl. Straight Flush; Straight Flush includes Royal.
REFERENCE_PCT = {
  "Straight Flush": 0.001539,
  "Vierling": 0.024010,
  "Full House": 0.144058,
  "Flush": 0.196540,
  "Straight": 0.392465,
  "Drilling": 2.112845,
  "Zwei Paare": 4.753902,
  "Zwilling": 42.256903,
  "Nichts": 50.117739
}

# 2) Create deck (0..51 → suit via //13, rank via %13)
def buildDeck():
  deck = []
  for i in range(TOTAL_CARDS):
    suitIndex = i // CARDS_PER_SUIT
    rankIndex = i % CARDS_PER_SUIT
    suit = SUITS[suitIndex]
    rank = RANKS[rankIndex]
    deck.append((suit, rank))
  return deck

# Draw one 5-card hand WITHOUT replacement using in-place swap
# (strictly same technique as in your lottery code)
def drawHand():
  # numbers 0..51 as indices into deck
  numbers = [i for i in range(0, TOTAL_CARDS)]
  n = TOTAL_CARDS
  drawnIdx = []
  for _ in range(CARDS_PER_HAND):
    idx = random.randrange(n)
    drawnIdx.append(numbers[idx])
    numbers[idx], numbers[n - 1] = numbers[n - 1], numbers[idx]
    n -= 1
  # map indices to (suit, rank) using same math as buildDeck
  hand = []
  for i in drawnIdx:
    suitIndex = i // CARDS_PER_SUIT
    rankIndex = i % CARDS_PER_SUIT
    hand.append((SUITS[suitIndex], RANKS[rankIndex]))
  return hand

def formatHand(hand):
  out = ""
  for i in range(len(hand)):
    suit, rank = hand[i]
    out += str(rank) + str(suit)
    if i < len(hand) - 1:
      out += ", "
  return out



def isFlush(hand):
  firstSuit = hand[0][0]
  for (s, r) in hand:
    if s != firstSuit:
      return False
  return True

def rankValues(hand):
  vals = []
  for (s, r) in hand:
    if r == "A":
      vals.append(14)
    elif r == "K":
      vals.append(13)
    elif r == "Q":
      vals.append(12)
    elif r == "J":
      vals.append(11)
    else:
      vals.append(int(r))
  return vals

def isStraight(vals):
  # check 5 distinct consecutive values
  # 1) normal check
  distinct = []
  for v in vals:
    if v not in distinct:
      distinct.append(v)
  if len(distinct) != 5:
    return False
  # find min
  minV = distinct[0]
  for v in distinct:
    if v < minV:
      minV = v
  ok = True
  for k in range(1, 5):
    if (minV + k) not in distinct:
      ok = False
      break
  if ok:
    return True
  # 2) wheel straight A-2-3-4-5 (treat A as 1)
  # convert A(14) to 1 in a temp list and re-check
  wheel = []
  for v in vals:
    if v == 14:
      wheel.append(1)
    else:
      wheel.append(v)
  distinct2 = []
  for v in wheel:
    if v not in distinct2:
      distinct2.append(v)
  if len(distinct2) != 5:
    return False
  minW = distinct2[0]
  for v in distinct2:
    if v < minW:
      minW = v
  ok2 = True
  for k in range(1, 5):
    if (minW + k) not in distinct2:
      ok2 = False
      break
  return ok2

def rankCounts(hand):
  # returns dict rank -> count using only basics
  counts = {}
  for (s, r) in hand:
    if r in counts:
      counts[r] += 1
    else:
      counts[r] = 1
  return counts

# 5) Search for combinations (simple, memory-light)
def evaluateHand(hand):
  flush = isFlush(hand)
  vals = rankValues(hand)
  straight = isStraight(vals)

  counts = rankCounts(hand)
  # gather multiplicities
  maxCount = 1
  pairCount = 0
  hasThree = False
  for k in counts:
    c = counts[k]
    if c > maxCount:
      maxCount = c
    if c == 2:
      pairCount += 1
    if c == 3:
      hasThree = True

  if straight and flush:
    return "Straight Flush"
  if maxCount == 4:
    return "Vierling"
  if hasThree and pairCount == 1:
    return "Full House"
  if flush:
    return "Flush"
  if straight:
    return "Straight"
  if maxCount == 3:
    return "Drilling"
  if pairCount == 2:
    return "Zwei Paare"
  if maxCount == 2:
    return "Zwilling"
  return "Nichts"

# 6) Simulate many draws and compute percentages
def generateStatistics(draws=SIM_DRAWS):
  categories = [
    "Straight Flush", "Vierling", "Full House",
    "Flush", "Straight", "Drilling", "Zwei Paare",
    "Zwilling", "Nichts"
  ]
  stats = {name: 0 for name in categories}

  for _ in range(draws):
    hand = drawHand()
    cat = evaluateHand(hand)
    if cat in stats:
      stats[cat] += 1
    else:
      stats["Nichts"] += 1

  pct = {}
  for k in stats:
    pct[k] = (stats[k] * 100.0) / float(draws)
  return stats, pct

def printComparison(simPct):
  print("\nComparison (Simulation vs Reference)")
  keys = [
    "Straight Flush", "Vierling", "Full House",
    "Flush", "Straight", "Drilling", "Zwei Paare",
    "Zwilling", "Nichts"
  ]
  for k in keys:
    sp = simPct.get(k, 0.0)
    rp = REFERENCE_PCT.get(k, 0.0)
    diff = sp - rp
    print(f"{k:15s}  sim={sp:8.5f}%   ref={rp:8.5f}%   diff={diff:+8.5f}%")

if __name__ == "__main__":
  sample = drawHand()
  print("Your poker hand:")
  print(formatHand(sample))
  print("Result:", evaluateHand(sample))

  stats, pct = generateStatistics()
  print("\nCounts after", SIM_DRAWS, "hands:")
  print(stats)

  print("\nPercentages (%):")
  print(pct)

  printComparison(pct)
