from player import Player
import sys
import json

with open('test_case1.json') as test_case:
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet is not 0:
        sys.exit('bet is not 0')

with open('test_case2.json') as test_case:
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet is not 0:
        sys.exit('bet is not 0')

with open('test_case3.json') as test_case:
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet is not 3:
        sys.exit('bet is not 3')

with open('test_case4.json') as test_case:
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet is not 0:
        sys.exit('bet is not 0')

print('this did not crash :)')

