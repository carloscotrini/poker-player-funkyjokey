from player import Player
import sys

bet = Player().betRequest(
    {
        "players":[
            {
                "name":"Player 1",
                "stack":1000,
                "status":"active",
                "bet":0,
                "hole_cards":[{
                    'rank': '2',
                    'suit': 'hearts'
                }, {
                    'rank': '2',
                    'suit': 'spades'
                }],
                "version":"Version name 1",
                "id":0
            },
            {
                "name":"Player 2",
                "stack":1000,
                "status":"active",
                "bet":0,
                "hole_cards":[],
                "version":"Version name 2",
                "id":1
            }
        ],
        "tournament_id":"550d1d68cd7bd10003000003",
        "game_id":"550da1cb2d909006e90004b1",
        "round":0,
        "bet_index":0,
        "small_blind":10,
        "orbits":0,
        "dealer":0,
        "in_action":0,
        "community_cards":[],
        "current_buy_in":3,
        "pot":0
    }
)

if bet is not 3:
    sys.exit('bet is not 3')

print('this did not crash :)')

