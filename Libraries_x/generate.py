import random

# When I use the "shuffle" func i want literally shuffle the array
cards = ["jack", "quenn", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

# func "randint" for create a numbe with 10% probability 
# number = random.randint(1, 10)
# print(number)

# program used "choice" func from librari randon for flip a coin
# coin = random.choice(["heads", "tails"])
# print(coin)