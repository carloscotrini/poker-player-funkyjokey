import strategies

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        players = game_state['players']
        current_buy_in = game_state['current_buy_in']
        in_action = game_state['in_action']
        our_cards = players[in_action]['hole_cards']
        community_cards = game_state['community_cards']
        bet = players[in_action]['bet']
        minimum_to_play = current_buy_in - bet
        print(str(our_cards), str(community_cards))
        if (strategies.isPair(our_cards, community_cards)):
            print("PICKED STRATEGY: isPair")
            return minimum_to_play
        print("NO STRATEGY, WE ARE CHECKING OR FOLDING")
        return 0

    def showdown(self, game_state):
        pass

