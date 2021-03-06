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
        pot = game_state['pot']
        print(str(our_cards), str(community_cards))
        if strategies.possessStraightFlush(our_cards, community_cards):
            print("PICKED STRATEGY: possessStraightFlush")
            return stack
        if strategies.possessPoker(our_cards, community_cards):
            print("PICKED STRATEGY: possessPoker")
            return stack
        if strategies.possessFlush(our_cards, community_cards):
            print("PICKED STRATEGY: possessFlush")
            minimum_raise = int(stack) / 4 * 3
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
        if strategies.possessHighPair(our_cards, community_cards):
            print("PICKED STRATEGY: possessHighPair")
            minimum_raise = int(stack) / 8
            return minimum_to_play + minimum_raise
        if strategies.possessPair(our_cards, community_cards):
            print("PICKED STRATEGY: possessPair")
            minimum_raise = int(stack) / 8
            return minimum_to_play + minimum_raise
        if strategies.possessHighCard(our_cards, community_cards):
            print("PICKED STRATEGY: possessHighCard")
            return minimum_to_play
        print("NO STRATEGY, WE ARE CHECKING OR FOLDING")
        return 0

    def showdown(self, game_state):
        pass

