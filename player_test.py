from player import Player
import sys
import json

with open('test_case1.json') as test_case:
    print('BASIC PARSING')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 0:
        sys.exit('problem in parsing')

with open('test_case2.json') as test_case:
    print('SHOULD NOT BET ON NOTHING')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 0:
        sys.exit('betting on nothing')

with open('test_case3.json') as test_case:
    print('RAISE HALF ON POSSESS PAIR')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 503:
        sys.exit('bet is not 503 but {}'.format(bet))

with open('test_case4.json') as test_case:
    print('FOLD IF NO PAIR')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 0:
        sys.exit('bet is not 0 but {}'.format(bet))

with open('test_case5.json') as test_case:
    print('CALL IF HIGH CARD')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 3:
        sys.exit('bet is not 3 but {}'.format(bet))

with open('test_case6.json') as test_case:
    print('DO NOT RAISE ON MISSING COMMUNITY CARDS')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 0:
        sys.exit('bet is not 0 but {}'.format(bet))

with open('test_case7.json') as test_case:
    print('RAISE HARD ON FLUSH')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 753:
        sys.exit('bet is not 753 but {}'.format(bet))

print('ALL TESTS ARE GOOD!')

