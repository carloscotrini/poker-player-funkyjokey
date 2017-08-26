
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def isPair(our_cards, community_cards):
    rank_counts = {rank:0 for rank in ranks}
    for card in our_cards + community_cards:
        rank_counts[card["rank"]] += 1

    return len(list(filter(lambda r : rank_counts[r] > 1, rank_counts.keys())))

def possessPair(our_cards, community_cards):
    rank_counts = {rank: 0 for rank in ranks}
    for card in our_cards + community_cards:
        rank_counts[card["rank"]] += 1

    multiple_ranks = list(filter(lambda r: rank_counts[r] > 1, rank_counts.keys()))
    our_ranks = [card["rank"] for card in our_cards]
    return isPair(our_cards, [])  or set(our_ranks) ^ set(multiple_ranks) != set()