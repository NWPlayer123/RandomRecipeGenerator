import random
ingredientlist = ["lemon juice", "mayonnaise", "ground black pepper", "onion powder", 'apricots', 'asparagus', 'mango', 'carrots', 'Swiss cheese', 'button mushrooms',
'parsley', 'artichoke', 'water chestnuts', 'radicchio', 'pears', 'endive', 'beef', 'mozzarella', 'carrots', 'apricots', 'black beans', 'Ricotta cheese', 'beef',
'cabbage', 'radicchio', 'mango', 'ham', 'sardines', 'blueberries', 'beet greens', 'red beans', 'celery', 'parsley', 'leeks', 'cucumber', 'kiwi', 'broccoli', 'cranberries',
'cauliflower', 'celery', 'clams', 'black-eyed peas']
measurements = ["teaspoons", "tablespoons", "ounces", "pints", "quarts", "liters", "gallons", "cups", "pounds"]
units = ["3/4", "1/2", "1/3", "1/4", "2/3", "1", "2", "3", "4", "5", "6", '7', '8', '9', '10']
actions = ['add','bake','batter','beat','bind','blacken','blanch','blend','boil','braise','broil','brown','brush','butterfly','caramelize','chiffron','chop','coat','core','cream',
'crimp','crisp','cure','deep-fry','deglaze','dice','dot','dredge','drizzle','dust','fillet','flan','fold','fry','garnish','glaze','grate','grease','grill','grind','knead',
'marinate','mash','mince','mix','moisten','parchment','poach','pressure cook','puree','reduce','roast','saute','scald','score','sear','season','shred','sift','simmer',
'skim','stir-fry','thin','toss','unleaven','vinaigrette','water bath','whip','whisk','zest']

for w in range(1, 111):
    outfoo = open(str(w) + ".txt", "w")
    outfoo.write("Ingredients: \n\n")
    intingr = random.randint(3, 16)
    ingredientmerp = [""]*intingr
    for x in range(0, intingr):
        ingredientmerp[x] = str(ingredientlist[random.randint(0,len(ingredientlist)-1)].lower())
        outfoo.write(str(units[random.randint(0,len(units)-1)]) + " " + str(measurements[random.randint(0,len(measurements)-1)]) +
        " " + ingredientlist[x] + "\n")

    outfoo.write("\nDirections: \n\n")
    outfoo.write("Preheat oven to " + str(random.randrange(300,500,5)) + " degrees Farenheit\n")
    for z in range(0, intingr):
        outfoo.write(str(actions[random.randint(0,len(actions)-1)]) + " the " + str(ingredientmerp[z]) + " for " + str(random.randint(3, 90)) + " minutes\n")
    outfoo.write("Bake for " + str(random.randint(3, 90)) + " minutes\n")
