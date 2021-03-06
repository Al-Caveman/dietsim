# simulation to see how much food i need to stockpile
import random
import json
import sys

# todo food
#   rich cereal serving for 60 days
#   popcorn servings

# raw food items
def template(quantity, unit, calories, protein, carbs, fat):
    return {
            'name'          : sys._getframe(1).f_code.co_name,
            'quantity'      : quantity,
            'unit'          : unit,
            'calories'      : calories,
            'protein'       : protein,
            'carbs'         : carbs,
            'fat'           : fat,
    }

def banana(num):
    return template(
        quantity    = num,
        unit        = 'medium bananas',
        calories    = num * 105,
        protein     = num * 1.3,
        carbs       = num * 27,
        fat         = num * .4,
    )

def cheese(spoons):
    spoon_g = 9.375
    return template(
        quantity    = spoon_g * spoons,
        unit        = 'grams',
        calories    = spoon_g * (249 / 100),
        protein     = spoon_g * (9.9 / 100),
        carbs       = spoon_g * (3 / 100),
        fat         = spoon_g * (22 / 100),
    )

def bread(pitas):
    return template(
        quantity    = pitas,
        unit        = 'pitas',
        calories    = pitas * 165,
        protein     = pitas * 5.5,
        carbs       = pitas * 33.4,
        fat         = pitas * 0.7,
    )

def fool(servings):
    can_servings = 3
    cans_num = servings / can_servings
    return template(
        quantity    = cans_num,
        unit        = 'cans',
        calories    = 110 * servings,
        protein     = 8 * servings,
        carbs       = 7 * servings,
        fat         = 6 * servings,
    )

def canned_fruit(servings):
    can_servings = 3
    cans_num = servings / can_servings
    return template(
        quantity    = cans_num,
        unit        = 'cans',
        calories    = 72 * servings,
        protein     = 0 * servings,
        carbs       = 5 * servings,
        fat         = 0 * servings,
    )

def smoked_chicken(slices):
    package_slices = 7
    package_netweight_g = 250
    packs_num = slices / package_slices
    serving_g = 54
    slices_g = package_netweight_g / package_slices * slices
    return template(
        quantity    = packs_num,
        unit        = 'packs',
        calories    = 60 * (slices_g / serving_g),
        protein     = 10 * (slices_g / serving_g),
        carbs       = 3 * (slices_g / serving_g),
        fat         = 1.5 * (slices_g / serving_g),
    )

def smoked_beef(slices):
    package_slices = 6
    package_netweight_g = 250
    packs_num = slices / package_slices
    serving_g = 100
    slices_g = package_netweight_g / package_slices * slices
    return template(
        quantity    = packs_num,
        unit        = 'packs',
        calories    = 116 * (slices_g / serving_g),
        protein     = 14 * (slices_g / serving_g),
        carbs       = 4 * (slices_g / serving_g),
        fat         = 6 * (slices_g / serving_g),
    )

def hummus(scoops):
    scoop_g = 16
    return template(
        quantity    = scoops * scoops,
        unit        = 'scoop',
        calories    = scoops * (37 / scoop_g),
        protein     = scoops * (1.2 / scoop_g),
        carbs       = scoops * (2.3 / scoop_g),
        fat         = scoops * (2.8 / scoop_g),
    )

def protein_powder(spoons):
    return template(
        quantity    = spoons,
        unit        = 'spoon',
        calories    = spoons * 160,
        protein     = spoons * 30,
        carbs       = spoons * 4,
        fat         = spoons * 2.5,
    )

def milk(ml):
    return template(
        quantity    = ml,
        unit        = 'ml',
        calories    = ml * 600/1000,
        protein     = ml * 31/1000,
        carbs       = ml * 47/1000,
        fat         = ml * 31/1000,
    )

def boiled_eggs(eggs):
    return template(
        quantity    = eggs,
        unit        = 'eggs',
        calories    = eggs * 78,
        protein     = eggs * 6.3,
        carbs       = eggs * .6,
        fat         = eggs * 5.3,
    )

def protein_shake(scoops):
    if scoops == 1:
        ml = 250
    elif scoops == 2:
        ml = 300
    else:
        ml = scoops*150
    value_powder = protein_powder(scoops)
    value_milk = protein_powder(ml)
    return template(
        quantity    = 1,
        unit        = 'shake: {}scoops prot + {}ml milk'.format(scoops, ml),
        calories    = value_powder['calories'] + value_milk['calories'],
        protein     = value_powder['protein'] + value_milk['protein'],
        carbs       = value_powder['carbs'] + value_milk['carbs'],
        fat         = value_powder['fat'] + value_milk['fat'],
    )

# run sim
random.seed(0)
DAYS = 30
FOODS = [
    [banana         , 0, 10     ],
    [cheese         , 0, 20     ],
    [bread          , 0, 10     ],
    [fool           , 0, 12     ],
    [canned_fruit   , 0, 6      ],
    [smoked_chicken , 0, 14     ],
    [smoked_beef    , 0, 12     ],
    [hummus         , 0, 800    ],
    [protein_shake  , 0, 4      ],
    [milk           , 0, 1000   ],
    [boiled_eggs    , 0, 10     ],
]
CALORIES_MAX = 1900
CALORIES_MIN = 1500
PROTEIN_MIN = 120
PROTEIN_MAX = 200
CARBS_MAX = 77
FAT_MAX = 69
stockpiled_meals = []
while(len(stockpiled_meals) < DAYS):
    calories = 0
    proteins = 0
    carbs = 0
    fat = 0
    random.shuffle(FOODS)
    picked_meals = []
    for food, arg_min, arg_max in FOODS:
        arg = random.randint(arg_min, arg_max)
        if arg == 0:
            continue
        value = food(arg)
        calories += value['calories']
        proteins += value['protein']
        carbs    += value['carbs']
        fat      += value['fat']

        if (
            calories <= CALORIES_MAX
            and carbs <= CARBS_MAX
            and fat <= FAT_MAX
        ):
            picked_meals.append(value)
            if proteins >= PROTEIN_MAX:
                break
            elif proteins >= PROTEIN_MIN and calories >= CALORIES_MIN:
                stockpiled_meals.append(list(picked_meals))
        else:
            break

# do some stats
grand_calories = 0
grand_proteins = 0
grand_carbs    = 0
grand_fat      = 0
stockpile = {}
for meal in stockpiled_meals:
    calories = 0
    proteins = 0
    carbs    = 0
    fat      = 0
    for value in meal:
        if value['name'] in stockpile:
            stockpile[value['name']]['quantity'] += value['quantity']
            stockpile[value['name']]['calories'] += value['calories']
            stockpile[value['name']]['protein' ] += value['protein']
            stockpile[value['name']]['carbs'   ] += value['carbs']
            stockpile[value['name']]['fat'     ] += value['fat']
        else:
            stockpile[value['name']] = {
                'quantity'  : value['quantity'],
                'unit'      : value['unit'],
                'calories'  : value['calories'],
                'protein'   : value['protein'],
                'carbs'     : value['carbs'],
                'fat'       : value['fat'],
            }
        calories += value['calories']
        proteins += value['protein']
        carbs    += value['carbs']
        fat      += value['fat']
    print('\n==================================================')
    print('kcals:{:.2f}  prot:{:.2f}  carbs:{:.2f}  fat:{:.2f}'.format(
        calories, proteins, carbs, fat
    ))
    print(json.dumps(meal, indent=4))
    grand_calories += calories
    grand_proteins += proteins
    grand_carbs    += carbs
    grand_fat      += fat

print('\n==================================================')
print('average macros:')
print('kcals:{:.2f}  prot:{:.2f}  carbs:{:.2f}  fat:{:.2f}'.format(
        grand_calories / len(stockpiled_meals),
        grand_proteins / len(stockpiled_meals),
        grand_carbs / len(stockpiled_meals),
        grand_fat / len(stockpiled_meals)
    ))

print('\n==================================================')
print('stockpile:')
print(json.dumps(stockpile, indent=4))
