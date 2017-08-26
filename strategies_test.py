import strategies

our_cards = [{"rank": "3"}, {"rank":"3"}]
community_cards = []

print(str(strategies.isPair(our_cards, community_cards)) + " == 1")

our_cards = [{"rank": "3"}, {"rank":"5"}]

print(str(strategies.isPair(our_cards, community_cards)) + " == 0")

our_cards = [{"rank": "3"}, {"rank":"5"}]
community_cards = [{"rank" : "4"}, {"rank": "5"}]

print(str(strategies.isPair(our_cards, community_cards)) + " == 1")

our_cards = [{"rank": "3"}, {"rank":"5"}]
community_cards = [{"rank" : "4"}, {"rank": "A"}]

print(str(strategies.isPair(our_cards, community_cards)) + " == 0")