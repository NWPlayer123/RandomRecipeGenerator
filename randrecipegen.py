#TODO: 
#    - make text a lot more random(random letters that kind of look like words)
import random, os, sys
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
#all the empty strings at the beginning are
#just to increase the likelyhood of choosing
#an empty. I have no idea how to weight randoms in python.
randwords = [" ", " ", " ", " ", " ", "the", "cat ", "dog ", "banana ", "purple ", "apple ", "picachu ", "wrong ",
"can ", "family ", "data ", "knife ", "trick ", "script "]
count = input('Enter recipe count: ')
if(len(count) > 0):
    try:
        count=int(count)
    except ValueError:
        print('Invalid number entered, going with default of 10')
        count=10;
if not os.path.exists("recipeGibberized"):
    os.makedirs("recipeGibberized")
for w in range(1, count+1):
    
    outformatted = open(str(w) + ".txt", "w")
    outrandomized = open("recipeGibberized/"+str(w)+".txt", "w")
    outformatted.write("Ingredients: \n\n")
    intingr = random.randint(3, 16)
    ingredientmerp = [""]*intingr
    ingredientgibberish = [""]*intingr;
    
    for x in range(0, intingr):
        ingredientgibberish[x] = str(ingredientlist[random.randint(0,len(ingredientlist)-1)].lower())
        outrandomized.write(str(units[random.randint(0,len(units)-1)]) + " " + units[random.randint(0, len(units)-1)] +
        randwords[random.randint(0, len(randwords)-1)] + ingredientlist[x] + "\n")

        ingredientmerp[x] = str(ingredientlist[random.randint(0,len(ingredientlist)-1)].lower())
        outformatted.write(str(units[random.randint(0,len(units)-1)]) + " " + ingredientlist[x] + "\n")
    
    outformatted.write("\nDirections: \n\n")
    outformatted.write("Preheat oven to " + str(random.randrange(300,500,5)) + " degrees Farenheit\n")
    
    for z in range(0, intingr):
        outformatted.write(str(actions[random.randint(0,len(actions)-1)]) + " the " + str(ingredientmerp[z]) + " for " + str(random.randint(3, 90)) + " minutes\n")
    outformatted.write("Bake for " + str(random.randint(3, 90)) + " minutes\n")
    
    outrandomized.write("\nDirections: \n\n")
    outrandomized.write("Preheat oven to " + str(random.randrange(300,500,5)) + " degrees Farenheit\n")
    
    for z in range(0, intingr):
        outformatted.write(str(actions[random.randint(0,len(actions)-1)]) + " the " + str(ingredientmerp[z]) + " for " + str(random.randint(3, 90)) + " minutes\n")
    outrandomized.write("Bake for " + str(random.randint(3, 90)) + " minutes\n")
    outformatted.close();
    outrandomized.close();
