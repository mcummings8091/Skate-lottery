import random

def skate_lottery():
    for i in range(3):
        yield random.choice(skateproduct)

    yield random.choice(specialprize)


skateproduct = ['Indy Trucks', 'Spitfire FF', 'Bones Bearings', 'Skate Wax', 'Slide Gloves']
specialprize = ['Spitfire Hoodie', 'Second Sun Deck', 'Cadillac Swingers', 'Downhill Freeride Deck']

for random_product in skate_lottery():
    print(f"and you win...{random_product}! ")