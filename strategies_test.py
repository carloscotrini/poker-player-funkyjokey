import strategies
import unittest

class StrategyTester(unittest.TestCase):

    def test_isPair(self):
        our_cards = [{"rank": "3"}, {"rank":"3"}]
        community_cards = []

        self.assertTrue(strategies.isPair(our_cards, community_cards))
        self.assertTrue(strategies.possessPair(our_cards, community_cards))

        our_cards = [{"rank": "3"}, {"rank":"5"}]

        self.assertFalse(strategies.isPair(our_cards, community_cards))
        self.assertFalse(strategies.possessPair(our_cards, community_cards))

        our_cards = [{"rank": "3"}, {"rank":"5"}]
        community_cards = [{"rank" : "4"}, {"rank": "5"}]

        self.assertTrue(strategies.isPair(our_cards, community_cards))
        self.assertTrue(strategies.possessPair(our_cards, community_cards))

        our_cards = [{"rank": "3"}, {"rank":"5"}]
        community_cards = [{"rank" : "4"}, {"rank": "A"}]

        self.assertFalse(strategies.isPair(our_cards, community_cards))
        self.assertFalse(strategies.isPair(our_cards, community_cards))

        our_cards = [{"rank": "3"}, {"rank": "5"}]
        community_cards = [{"rank": "A"}, {"rank": "A"}]

        self.assertTrue(strategies.isPair(our_cards, community_cards))
        self.assertFalse(strategies.possessPair(our_cards, community_cards))

    def test_possesHighCard(self):

        our_cards = [{"rank": "A"}, {"rank": "5"}]
        community_cards = [{"rank": "A"}, {"rank": "A"}]
        self.assertTrue(strategies.possessHighCard(our_cards, community_cards))

        our_cards = [{"rank": "1"}, {"rank": "5"}]
        community_cards = [{"rank": "A"}, {"rank": "A"}]
        self.assertFalse(strategies.possessHighCard(our_cards, community_cards))

        our_cards = [{"rank": "J"}, {"rank": "5"}]
        community_cards = [{"rank": "A"}, {"rank": "A"}]
        self.assertTrue(strategies.possessHighCard(our_cards, community_cards))

        our_cards = [{"rank": "2"}, {"rank": "5"}]
        community_cards = [{"rank": "1"}, {"rank": "1"}]
        self.assertFalse(strategies.possessHighCard(our_cards, community_cards))

        our_cards = [{"rank": "1"}, {"rank": "3"}]
        community_cards = [{"rank": "A"}, {"rank": "A"}]
        self.assertFalse(strategies.possessHighCard(our_cards, community_cards))

if __name__ == "__main__":
    unittest.main()