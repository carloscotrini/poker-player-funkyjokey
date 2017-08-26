
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
val_of_rank = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}
suits = ["clubs","spades","hearts","diamonds"]

class Card:

    def __init__(self, card):
        self.rank = card["rank"] if "rank" in card.keys() else "1"
        self.suite = card["suit"] if "suit" in card.keys() else "none"

    def __str__(self):
        return "[[" + self.rank + " " + self.suite + "]]"

def isPair(our_cards, community_cards):
    rank_counts = {rank:0 for rank in ranks}
    for card in our_cards + community_cards:
        rank_counts[card["rank"]] += 1

    return len(list(filter(lambda r : rank_counts[r] > 1, rank_counts.keys())))

def possessPair(our_cards, community_cards):
    our_ranks = [card["rank"] for card in our_cards]
    comm_ranks = [card["rank"] for card in community_cards]
    return isPair(our_cards, []) or set(our_ranks) & set(comm_ranks) != set()

def possessHighCard(our_cards, community_cards):
    return {"J", "Q", "K", "A"} & set(map(lambda card : card["rank"], our_cards)) != set()

def possessFlush(our_cards, community_cards):
    our_cards = [Card(c) for c in our_cards]
    community_cards = [Card(c) for c in community_cards]

    if len(our_cards) < 2:
        return False
    elif our_cards[0].suite == our_cards[1].suite:
        comm_suites = [c.suite for c in community_cards]
        comm_suite_counts = {r : 0 for r in suits}
        for suite in comm_suites:
            comm_suite_counts[suite] += 1
        if comm_suite_counts[our_cards[0].suite] >= 3:
            return True
    else:
        return False

def get_rank_freq(cards):
    map = {r : 0 for r in ranks}
    for c in cards:
        map[c.rank] += 1
    return map

def get_suit_freq(cards):
    map = {r : 0 for r in ranks}
    for c in cards:
        map[c.suite] += 1
    return map

def isPoker(cards):
    cards = [Card(c) for c in cards]

    map = get_rank_freq(cards)
    return len(list(filter(lambda val : val >= 4, map.values()))) > 0

def possessPoker(our_cards, community_cards):
    return isPoker(our_cards + community_cards) and (not isPoker(community_cards))

def isStraight(cards):
    cards = [Card(c) for c in cards]

    map = get_rank_freq(cards)
    ranks_in_cards = []
    for rank, freq in map.items():
        if freq > 0:
            ranks_in_cards.append(rank)

    val_ranks = [False for r in range(20)]
    for rank in ranks_in_cards:
        val_ranks[val_of_rank[rank]] = True
    for i in [2,3,4,5,6,7,8,9,10]:
        straight_found = True
        for j in [0,1,2,3,4]:
            if not val_ranks[i + j]:
                straight_found = False
        if straight_found:
            return True

    return False

def possessStraight(our_cards, community_cards):
    return isStraight(our_cards + community_cards) and (not isStraight(community_cards))

def isStraightFlush(cards):
    for suit in suits:
        suit_cards = list(filter(lambda c : c["suit"] == suit, cards))
        if isStraight(suit_cards):
            return True

    return False

def possessStraightFlush(our_cards, community_cards):
    return isStraightFlush(our_cards + community_cards) and (not isStraightFlush(community_cards))

def hasFullHouse(cards):
    triple_rank = None
    for rank in ranks:
        rank_cards = list(filter(lambda c : c["rank"] == rank, cards))
        if len(rank_cards) >= 3:
            triple_rank = rank
            break

    if triple_rank:
        for rank in ranks:
            if rank != triple_rank:
                rank_cards = list(filter(lambda c : c["rank"] == rank, cards))
                if len(rank_cards) >= 2:
                    return True

    return False

def possessFullHouse(our_cards, community_cards):
    return hasFullHouse(our_cards + community_cards) and (not hasFullHouse(community_cards))