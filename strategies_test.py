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

        our_cards = [{"rank": "3"}, {"rank":"5"}]
        community_cards = [{"rank" : "4"}, {"rank": "5"}]

        self.assertTrue(strategies.isPair(our_cards, community_cards))

        our_cards = [{"rank": "3"}, {"rank":"5"}]
        community_cards = [{"rank" : "4"}, {"rank": "A"}]

        self.assertFalse(strategies.isPair(our_cards, community_cards))

if __name__ == "__main__":
    unittest.main()