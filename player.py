import strategies

import random

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        players = game_state['players']
        current_buy_in = game_state['current_buy_in']
        in_action = game_state['in_action']
        our_cards = players[in_action]['hole_cards']
        community_cards = game_state['community_cards']
        bet = players[in_action]['bet']
        stack = players[in_action]['stack']
        minimum_to_play = current_buy_in - bet
        print(str(our_cards), str(community_cards))
        if strategies.possessStraightFlush(our_cards, community_cards):
            print("PICKED STRATEGY: possessStraightFlush")
            return stack
        if strategies.possessPoker(our_cards, community_cards):
            print("PICKED STRATEGY: possessPoker")
            minimum_raise = int(stack) / 4 * 3
            return minimum_to_play + minimum_raise
        if strategies.possessFlush(our_cards, community_cards):
            print("PICKED STRATEGY: possessFlush")
            minimum_raise = int(stack) / 2
            return minimum_to_play + minimum_raise
        if strategies.possessStraight(our_cards, community_cards):
            print("PICKED STRATEGY: possessStraight")
            minimum_raise = int(stack) / 3 * 2
            return minimum_to_play + minimum_raise
        if strategies.possessFullHouse(our_cards, community_cards):
            print("PICKED STRATEGY: possessFullHouse")
            minimum_raise = int(stack) / 3 * 2
            return minimum_to_play + minimum_raise
        if strategies.possessTriple(our_cards, community_cards):
            print("PICKED STRATEGY: possessTriple")
            minimum_raise = int(stack) / 4
            return minimum_to_play + minimum_raise
        if strategies.possessPair(our_cards, community_cards):
            #cap = int(stack) / 3
            threshold = int(stack) / 6
            if minimum_to_play >= threshold:
                print("PICKED STRATEGY: foldForHighStakes PAIR")
                return 0
            print("PICKED STRATEGY: possessPair")
            minimum_raise = int(stack) / 8
            to_bet = minimum_to_play + minimum_raise
            #if to_bet > cap:
            #    to_bet = cap
            return to_bet
        if strategies.possessHighCard(our_cards, community_cards):
            threshold = int(stack) / 10
            if minimum_to_play >= threshold:
                print("PICKED STRATEGY: foldForHighStakes HIGH CARD")
                return 0
            print("PICKED STRATEGY: possessHighCard")
            return minimum_to_play
        #if random.randint(1, 10) <= 3 and stack >= 1000 and len(community_cards) >= 3:
        #    print("PICKED_STRATEGY: scareThemOff")
        #    minimum_raise = int(stack) / 4
        #    return minimum_to_play + minimum_raise
        print("NO STRATEGY, WE ARE CHECKING OR FOLDING")
        return 0

    def showdown(self, game_state):
        pass

