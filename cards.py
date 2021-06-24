import json
name = input('name:')

type = ['Attack', 'Skill', 'Power', 'Curse', 'Status']
print('\n',list(enumerate(type)))
_type = input('type:')

rarity = ['Starter', 'Common', 'Uncommon', 'Rare', 'Other']
print('\n',list(enumerate(rarity)))
_rarity = input('rarity:')

cost = input('cost:')

info = {
    'name': name,
    'type': type[int(_type)],
    'rarity': rarity[int(_rarity)],
    'cost': cost
}

damage = {}

if input('deal damage?') == '1':
    monster = {}
    if input('deal damage to monster?') == '1':

        target = ['choosed', 'all', 'random', 'random all', 'other']
        print('\n',list(enumerate(target)))
        _target = input('target:')

        time = input('time:')

        amount = input('amount:')

        condition = input('have condition?')

        monster = {
            'target': target[int(_target)],
            'time': time,
            'amount': amount,
            'condition': condition
        }

    player = {}

    if input('deal damage to player?') == '1':

        time = input('time:')

        amount = input('amount:')

        condition = input('have condition?')

        player = {
            'target': 'self',
            'time': time,
            'amount': amount,
            'condition': condition
        }

    damage = {
        'monster': monster,
        'player': player
    }

block = input('block:')

energy = input('energy:')

buff = {}

if input('have buff?') == '1':

    monster = []

    for i in range(int(input('monster buff num?'))):

        name = input('name:')

        amount = input('amount:')

        monster.append({'name': name, 'amount': amount})

    player = []

    for i in range(int(input('player buff num?'))):

        name = input('name:')

        amount = input('amount:')

        player.append({'name': name, 'amount': amount})

    buff = {
        'monster': monster,
        'player': player
    }

card = {}
if input('have add or upgrade or play cards?') == '1':

    draw_pile = {}
    if input('draw pile?') == '1':

        _from = ['discard pile', 'exhaust pile', 'hand', 'other']
        print('\n',list(enumerate(_from)))
        __from = input('from:')

        target = ['choosed', 'all', 'ramdom', 'self', 'other']
        print('\n',list(enumerate(target)))
        _target = input('target:')

        place = ['random', 'top', 'bottom']
        print('\n',list(enumerate(place)))
        _place = input('place:')

        amount = input('amount:')

        draw_pile = {
            'from': _from[int(__from)],
            'target': target[int(_target)],
            'place': place[int(_place)],
            'amount': amount
        }

    discard_pile = {}
    if input('discard pile?') == '1':

        _from = ['draw pile', 'exhaust pile', 'hand', 'other']
        print('\n',list(enumerate(_from)))
        __from = input('from:')

        target = ['choosed', 'all', 'ramdom', 'self', 'other']
        print('\n',list(enumerate(target)))
        _target = input('target:')

        place = ['random', 'top', 'bottom']
        print('\n',list(enumerate(place)))
        _place = input('place:')

        amount = input('amount:')

        discard_pile = {
            'from': _from[int(__from)],
            'target': target[int(_target)],
            'place': place[int(_place)],
            'amount': amount
        }

    exhaust_pile = {}
    if input('exhaust pile?') == '1':

        _from = ['draw pile', 'discard pile', 'hand', 'other']
        print('\n',list(enumerate(_from)))
        __from = input('from:')

        target = ['choosed', 'all', 'ramdom', 'self', 'other']
        print('\n',list(enumerate(target)))
        _target = input('target:')

        place = ['random', 'top', 'bottom']
        print('\n',list(enumerate(place)))
        _place = input('place:')

        amount = input('amount:')

        exhaust_pile = {
            'from': _from[int(__from)],
            'target': target[int(_target)],
            'place': place[int(_place)],
            'amount': amount
        }

    hand = {}
    if input('hand?') == '1':

        _from = ['draw pile', 'discard pile', 'exhaust pile', 'other']
        print('\n',list(enumerate(_from)))
        __from = input('from:')

        target = ['choosed', 'all', 'ramdom', 'self', 'other']
        print('\n',list(enumerate(target)))
        _target = input('target:')

        place = ['random', 'top', 'bottom']
        print('\n',list(enumerate(place)))
        _place = input('place:')

        amount = input('amount:')

        hand = {
            'from': _from[int(__from)],
            'target': target[int(_target)],
            'place': place[int(_place)],
            'amount': amount
        }

    play = {}
    if input('play?') == '1':

        _from = ['draw pile', 'discard pile', 'exhaust pile', 'hand', 'other']
        print('\n',list(enumerate(_from)))
        __from = input('from:')

        target = ['choosed', 'all', 'ramdom', 'self', 'other']
        print('\n',list(enumerate(target)))
        _target = input('target:')

        place = ['random', 'top', 'bottom']
        print('\n',list(enumerate(place)))
        _place = input('place:')

        amount = input('amount:')

        play = {
            'from': _from[int(__from)],
            'target': target[int(_target)],
            'place': place[int(_place)],
            'amount': amount
        }

    upgrade = {}
    if input('upgrade?') == '1':

        _from = ['draw pile', 'discard pile', 'exhaust pile', 'hand', 'other']
        print('\n',list(enumerate(_from)))
        __from = input('from:')

        target = ['choosed', 'all', 'ramdom', 'self', 'other']
        print('\n',list(enumerate(target)))
        _target = input('target:')

        amount = input('amount:')

        upgrade = {
            'from': _from[int(__from)],
            'target': target[int(_target)],
            'amount': amount
        }

    card = {
        'draw pile': draw_pile,
        'discard pile': discard_pile,
        'exhaust pile': exhaust_pile,
        'hand': hand,
        'play': play,
        'upgrade': upgrade
    }

cards = {
    'info': info,
    'damage': damage,
    'block': block,
    'energy': energy,
    'buff': buff,
    'card': card
}

with open("card.json", "w") as write_file:
    json.dump(cards, write_file)
