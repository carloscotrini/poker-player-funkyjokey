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

        our_cards = [{"rank": "Q"}, {"rank": "8"}]
        community_cards = []
        self.assertTrue(strategies.possessHighCard(our_cards, community_cards))

    def test_possessFlush(self):

        our_cards = [{"suit": "hearts"}, {"suit": "spades"}]
        community_cards = [{"suit": "clubs"}, {"suit": "clubs"}]
        self.assertFalse(strategies.possessFlush(our_cards, community_cards))

        our_cards = [{"suit": "spades"}, {"suit": "spades"}]
        community_cards = []
        self.assertFalse(strategies.possessFlush(our_cards, community_cards))

        our_cards = [{"suit": "hearts"}, {"suit": "hearts"}]
        community_cards = [{"suit": "hearts"}, {"suit": "hearts"}, {"suit": "hearts"}]
        self.assertTrue(strategies.possessFlush(our_cards, community_cards))

        our_cards = [{"suit": "hearts"}, {"suit": "spades"}]
        community_cards = [{"suit": "hearts"}, {"suit": "hearts"}, {"suit": "hearts"}]
        self.assertFalse(strategies.possessFlush(our_cards, community_cards))

        our_cards = [{"suit": "hearts"}, {"suit": "spades"}]
        community_cards = [{"suit": "hearts"}, {"suit": "hearts"}, {"suit": "hearts"}, {"suit": "hearts"}, {"suit": "hearts"}]
        self.assertFalse(strategies.possessFlush(our_cards, community_cards))

        our_cards = [{"suit": "hearts"}, {"suit": "hearts"}]
        community_cards = [{"suit": "hearts"}, {"suit": "hearts"}, {"suit": "hearts"}, {"suit": "hearts"}, {"suit": "hearts"}]
        self.assertTrue(strategies.possessFlush(our_cards, community_cards))

    def test_possessPoker(self):

        our_cards = [{"rank": "2"}, {"rank": "3"}]
        community_cards = [{"rank": "4"}, {"rank": "5"}]
        self.assertFalse(strategies.possessPoker(our_cards, community_cards))

        our_cards = [{"rank": "5"}, {"rank": "5"}]
        community_cards = [{"rank": "5"}, {"rank": "5"}]
        self.assertTrue(strategies.possessPoker(our_cards, community_cards))

        our_cards = [{"rank": "Q"}, {"rank": "Q"}]
        community_cards = [{"rank": "Q"}, {"rank": "Q"}, {"rank": "K"}]
        self.assertTrue(strategies.possessPoker(our_cards, community_cards))

        our_cards = [{"rank": "Q"}, {"rank": "K"}]
        community_cards = [{"rank": "Q"}, {"rank": "Q"}, {"rank": "Q"}, {"rank": "Q"}]
        self.assertFalse(strategies.possessPoker(our_cards, community_cards))

    def test_possessStraight(self):
        our_cards = [{"rank": "2"}, {"rank": "3"}]
        community_cards = [{"rank": "4"}, {"rank": "5"}]
        self.assertFalse(strategies.possessStraight(our_cards, community_cards))

        our_cards = [{"rank": "5"}, {"rank": "7"}]
        community_cards = [{"rank": "6"}, {"rank": "8"}, {"rank": "4"}]
        self.assertTrue(strategies.possessStraight(our_cards, community_cards))

        our_cards = [{"rank": "A"}, {"rank": "Q"}]
        community_cards = [{"rank": "J"}, {"rank": "K"}, {"rank": "10"}, {"rank": "K"}, {"rank": "10"}]
        self.assertTrue(strategies.possessStraight(our_cards, community_cards))

        our_cards = [{"rank": "2"}, {"rank": "Q"}]
        community_cards = [{"rank": "J"}, {"rank": "K"}, {"rank": "10"}, {"rank": "K"}, {"rank": "10"}]
        self.assertFalse(strategies.possessStraight(our_cards, community_cards))

    def test_possessStraightFlush(self):
        our_cards = [{"rank": "2", "suit":"hearts"}, {"rank": "3" , "suit":"hearts"}]
        community_cards = [{"rank": "4", "suit":"hearts"}, {"rank": "5", "suit":"hearts"}, {"rank": "6", "suit":"spades"}]
        self.assertFalse(strategies.possessStraightFlush(our_cards, community_cards))

        our_cards = [{"rank": "2", "suit":"hearts"}, {"rank": "3" , "suit":"hearts"}]
        community_cards = [{"rank": "4", "suit":"hearts"}, {"rank": "5", "suit":"hearts"}, {"rank": "6", "suit":"hearts"}]
        self.assertTrue(strategies.possessStraightFlush(our_cards, community_cards))

        our_cards = [{"rank": "5", "suit":"hearts"}, {"rank": "7", "suit":"spades"}]
        community_cards = [{"rank": "6", "suit":"clubs"}, {"rank": "8", "suit":"diamonds"}, {"rank": "4", "suit":"hearts"}]
        self.assertFalse(strategies.possessStraightFlush(our_cards, community_cards))

        our_cards = [{"rank": "5", "suit":"clubs"}, {"rank": "7", "suit":"clubs"}]
        community_cards = [{"rank": "6", "suit":"clubs"}, {"rank": "8", "suit":"clubs"}, {"rank": "4", "suit":"clubs"}]
        self.assertTrue(strategies.possessStraightFlush(our_cards, community_cards))

        our_cards = [{"rank": "5", "suit":"clubs"}, {"rank": "7", "suit":"spades"}]
        community_cards = [{"rank": "6", "suit":"clubs"}, {"rank": "8", "suit":"clubs"}, {"rank": "4", "suit":"clubs"}]
        self.assertFalse(strategies.possessStraightFlush(our_cards, community_cards))


if __name__ == "__main__":
    unittest.main()