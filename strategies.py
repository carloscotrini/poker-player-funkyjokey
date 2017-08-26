
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suites = ["clubs","spades","hearts","diamonds"]

class Card:

    def __init__(self, card):
        self.rank = card["rank"] if "rank" in card.keys() else "1"
        self.suite = card["suite"] if "suite" in card.keys() else "none"

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

    if our_cards[0].suite == our_cards[1].suite:
        comm_suites = [c.suite for c in community_cards]
        comm_suite_counts = {r : 0 for r in suites}
        for suite in comm_suites:
            comm_suite_counts[suite] += 1
        if comm_suite_counts[our_cards[0].suite] >= 3:
            return True
    else:
        return False