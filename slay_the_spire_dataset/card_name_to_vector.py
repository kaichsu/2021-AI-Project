import json
import re
import pandas as pd
import numpy as np

def spilt_card_class(df):
  #declaration
  cut_index = []
  dfs = {}

  #find cut index
  for str in Card_class:
    cut_index.append(df.index[df['Name'] == str].tolist())

  cut_index.append([len(df)])

  #cut
  for i in range(len(Card_class)):
    dfs[Card_class[i]] = df[df.keys()[0:6]].iloc[cut_index[i][0] + 1:cut_index[i + 1][0],:]

  return dfs

def clean_text(text):
    return re.sub(r'[.,()]', '', text).casefold()

def get_card(card_name, upgraded=False, cur_cost=-1, cur_engery=0):
    card = next(filter(lambda card: card_name.casefold() == card['Name'].casefold(), cards))

    try:
        cost = int(card['Cost'])
    except Exception as e:
        cost = card['Cost']

    if type(cost) == int and cur_cost != -1:
        cost = cur_cost

    elif cost == 'X':
        cost = cur_engery

    elif cost == 'Unplayable':
        cost = -1

    elif type(cost) != int:
        if cur_cost == -1:
            cost = int(re.sub(r'[()]', '', card['Cost']).split()[1] if upgraded else
                re.sub(r'[()]', '', card['Cost']).split()[0])
        else:
            cost = cur_cost



    if upgraded and card['Description (Upgraded)']:
        text = card['Description (Upgraded)']

    else:
        text = card['Description']

        text = re.sub(r'[0-9]+ \([0-9]+\)', lambda match:
            (re.sub(r'[()]', '', match.group(0)).split()[1] if upgraded else
             re.sub(r'[()]', '', match.group(0)).split()[0]), text)

    text = re.sub(r' X ', ' '+str(cur_engery)+' ', text)
    text = re.sub(r' X\+1 ', ' '+str(cur_engery+1)+' ', text)

    return cost, text

def get_attribute(text):
    int_value_substring = [
        #for attack
        r'deal [0-9]+ damage',
        r'deals [0-9]+ additional damage',
        r'[0-9]+ time',

        r'take [0-9]+ damage',
        #for player statue
        r'gain [0-9]+ artifact',
        r'gain [0-9]+ block',
        r'gain [0-9]+ gold',
        r'gain [0-9]+ intangible',
        r'gain [0-9]+ plated armor',
        r'gain [0-9]+ strength',
        r'gain [0-9]+ weak',

        r'heal [0-9]+ hp',

        r'lose [0-9]+ hp',
        r'lose [0-9]+ max hp',
        r'lose [0-9]+ strength',
        r'lose [0-9] energy',
        #for enemy buff
        r'apply [0-9]+ vulnerable',
        r'apply [0-9]+ [a-z]+ and vulnerable',
        r'apply [0-9]+ weak',

        r'loses [0-9]+ strength',
        #for cards
        r'draw [0-9]+ card',
        r'discard [0-9]+ card',
        r'exhaust [0-9]+ card',
        r'play [0-9] card',
        #other
        r'by [0-9]+',
        r'up to [0-9]+'
    ]

    int_value_substring_e = [
        r'add [0-9a]+',
        r'shuffle [0-9a]+',
        r'next [0-9]*'
    ]

    bool_value_substring = [
        #value
        r'damage',
        r'block',
        #target
        r'all',
        r'random',
        r'this',
        r'top',
        r'bottom',
        #arithmetic
        r'affect',
        r'double',
        r'twice',
        r'equal',
        r'number of',
        #card attribute
        r'unplayable',
        r'innate',
        r'retain',
        r'exhaust',
        r'ethereal',
        r'play',
        r'upgrade',
        #card pile
        r'hand',
        r'draw pile',
        r'discard pile',
        r'exhaust pile',
        #card type
        r'colorless',
        r'status',
        r'curse',
        r'attack',
        r'power',
        r'skill',
        r'non-attack',
        #card name
        r'burn',
        r'dazed',
        r'wound',
        r'slimed',
        r'void',
        r'bleed',
        r'omega',
        r'strike',
        #condition
        r'if',
        r'no',
        r'for',
        r'have',
        r'whenever',
        r'every',
        r'contain',
        r'each',
        r'fatal',
        r'vulnerable',
        r'not removed',
        r'played',
        r'exhausted',
        #result
        r'cannot draw',
        r'cannot play',
        r'increase',
        r'reduce',
        r'costs* 0',
        r'put a',
        r'put any',
        r'permanently',
        r'raise your max hp',
        #player
        r'attacked',
        r'lose hp',
        r'heal hp',
        #enemy
        r'intends',
        #turn
        r'turn',
        r'start',
        r'end'
    ]

    v = []
    for substring in int_value_substring:
        value = 0
        object = re.findall(substring, text)
        if object:
            value = int(re.sub(substring, lambda match:
                re.sub(r'[a-z ]+', '', match.group(0)), object[0]))
        v.append(value)

    value = 0
    object = re.findall(r'\[[a-z]\]', text)
    if object:
        value = len(object)
    v.append(value)


    for substring in int_value_substring_e:
        value = 0
        object = re.findall(substring, text)
        if object:
            try:
                value = int(re.sub(substring, lambda match:
                    re.sub(r'[a-z ]+', '', match.group(0)), object[0]))
            except Exception as e:
                value = 1
        v.append(value)

    for substring in bool_value_substring:
        value = 0
        object = re.findall(substring, text)
        if object:
            value = 1
        v.append(value)

    return v

def card_name_to_vector(card_name, cur_cost=-1, cur_engery=0):
    upgraded = False
    print(card_name)

    if card_name[-1] == '+':
        card_name = card_name[:-1]
        upgraded = True

    cost, text = get_card(card_name, upgraded, cur_cost, cur_engery)

    print('Cost: ' + str(cost) + '\nDescription: ' + clean_text(text))

    return [cost] + get_attribute(clean_text(text))

raw = pd.read_excel('Slay_the_Spire_Reference.xlsx', sheet_name='Cards', engine='openpyxl')

Card_class = ['Ironclad Cards', 'Silent Cards', 'Defect Cards', 'Watcher Cards', 'Colorless Cards', 'Curse Cards', 'Status Cards']
df = spilt_card_class(raw)

Choosed_class = ['Ironclad Cards', 'Colorless Cards', 'Curse Cards', 'Status Cards']
choosed_df = df[Choosed_class[0]]

for c in Choosed_class[1:]:
    choosed_df = choosed_df.append(df[c], ignore_index=True)

cards = json.loads(choosed_df.to_json(orient="records"))

for card in cards:
    card_name = card['Name']
    print(card_name_to_vector(card_name, cur_engery=1000))
    print(card_name_to_vector(card_name+'+', cur_engery=1000))

# while True:
#     id = int(input('card_id: '))
#     if(id < 0 or id >= len(cards)):
#         break
#     card = cards[id]
#     card_name = card['Name']
#     print(card_name)
#     vector = card_name_to_vector(input('card name: '), cur_engery=int(input('current engery: ')))
