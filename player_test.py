from player import Player
import sys
import json

with open('test_case1.json') as test_case:
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 0:
        sys.exit('problem in parsing')

with open('test_case2.json') as test_case:
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 0:
        sys.exit('betting on nothing')

with open('test_case3.json') as test_case:
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 503:
        sys.exit('bet is not 503 but {}'.format(bet))

with open('test_case4.json') as test_case:
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 0:
        sys.exit('bet is not 0 but {}'.format(bet))

with open('test_case5.json') as test_case:
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 3:
        sys.exit('bet is not 3 but {}'.format(bet))

print('ALL TESTS ARE GOOD!')

