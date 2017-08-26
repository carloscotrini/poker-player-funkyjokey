from player import Player
import sys
import json

with open('test_case1.json') as test_case:
    print('1 BASIC PARSING')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 0:
        sys.exit('problem in parsing')

with open('test_case2.json') as test_case:
    print('2 SHOULD NOT BET ON NOTHING')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 0:
        sys.exit('betting on nothing')

with open('test_case3.json') as test_case:
    print('3 RAISE HALF ON POSSESS PAIR')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 253:
        sys.exit('bet is not 253 but {}'.format(bet))

with open('test_case4.json') as test_case:
    print('4 FOLD IF NO PAIR')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 0:
        sys.exit('bet is not 0 but {}'.format(bet))

with open('test_case5.json') as test_case:
    print('5 CALL IF HIGH CARD')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 3:
        sys.exit('bet is not 3 but {}'.format(bet))

with open('test_case6.json') as test_case:
    print('6 DO NOT RAISE ON MISSING COMMUNITY CARDS')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 0:
        sys.exit('bet is not 0 but {}'.format(bet))

with open('test_case7.json') as test_case:
    print('7 RAISE HARD ON FLUSH')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 503:
        sys.exit('bet is not 503 but {}'.format(bet))

with open('test_case8.json') as test_case:
    print('8 FOLD FOR HIGH STAKES WITH HIGH CARD')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 0:
        sys.exit('bet is not 0 but {}'.format(bet))

with open('test_case9.json') as test_case:
    print('9 FOLD FOR HIGH STAKES WITH PAIR')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 0:
        sys.exit('bet is not 0 but {}'.format(bet))

with open('test_case10.json') as test_case:
    print('10 POKER')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 1250:
        sys.exit('bet is not 1250 but {}'.format(bet))

print('ALL TESTS ARE GOOD!')

