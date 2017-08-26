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
    print('3 RAISE ON POSSESS PAIR')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 128:
        sys.exit('bet is not 128 but {}'.format(bet))

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

with open('test_case11.json') as test_case:
    print('11 STRAIGHT')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 670:
        sys.exit('bet is not 670 but {}'.format(bet))

with open('test_case12.json') as test_case:
    print('12 CASE STUDY #1')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 0:
        sys.exit('bet is not 0 but {}'.format(bet))

with open('test_case13.json') as test_case:
    print('13 STRAIGHT FLUSH')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 871:
        sys.exit('bet is not 871 but {}'.format(bet))

#with open('test_case14.json') as test_case:
#    print('14 CAP ON PAIRS')
#    bet = Player().betRequest(json.loads(test_case.read()))
#    if bet != 333:
#        sys.exit('bet is not 333 but {}'.format(bet))

with open('test_case15.json') as test_case:
    print('15 FULL HOUSE')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 672:
        sys.exit('bet is not 672 but {}'.format(bet))

with open('test_case16.json') as test_case:
    print('16 FLUSH IS CORRECT')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 506:
        sys.exit('bet is not 506 but {}'.format(bet))

with open('test_case17.json') as test_case:
    print('17 TRIPLE')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 256:
        sys.exit('bet is not 256 but {}'.format(bet))

with open('test_case18.json') as test_case:
    print('18 HIGH PAIR')
    bet = Player().betRequest(json.loads(test_case.read()))
    if bet != 131:
        sys.exit('bet is not 131 but {}'.format(bet))

print('ALL TESTS ARE GOOD!')

