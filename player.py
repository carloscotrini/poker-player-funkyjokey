
class Player:
    VERSION = "Default Python folding player"

    """
    game state:
        - players
          [
           - name
             stack int
             status
             bet int
             hole_cards
             [
               - rank 2-10 or J Q K A
               - suit [hearts diamonds clubs spades]
             ]
             version
             id
          ]
        - tournament_id
        - game_id
        - round int
        - bet_index int
        - small_blind int
        - orbits
        - dealer
        - community_cards [cards]
        - current buy in
        - pot
    """

    def isPair():
        return

    def betRequest(self, game_state):
        """
        return integer: amount of chips to be bet
        0 means check
        """
        players = game_state['players']
        current_buy_in = game_state['current_buy_in']
        in_action = game_state['in_action']
        our_cards = players[in_action]['hole_cards']
        community_cards = game_state['community_cards']
        bet = players[in_action]['bet']
        minimum_to_play = current_buy_in - bet
        
        return 0

    def showdown(self, game_state):
        pass

