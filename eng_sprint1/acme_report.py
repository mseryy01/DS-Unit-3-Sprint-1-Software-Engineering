import random
from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(num_products=30):
    """Generate random products"""
    products = []
    for _ in range(num_products):
        adject = sample(ADJECTIVES, 1)
        noun = sample(NOUNS, 1)
        name = adject[0] + ' ' + noun[0]
        price  = round(random.uniform(5,100),2)
        weight = round(random.uniform(5,100),2)
        flammability = round(random.uniform(0,2.5),2)
        products.append(Product(name, price, weight, flammability))
    return products

def inventory_report(products):
    """Generate inventory report of products"""
    names = []
    prices = []
    weights = []
    flames = []
    for p in products:
        names.append(p.name)
        prices.append(p.price)
        weights.append(p.weight)
        flames.append(p.flammability)

    print("Number of unique product names in the list is ", len(set(names)))
    print("Average product price is ", sum(prices) / len(prices))
    print("Average product weight is ", sum(weights) / len(weights))
    print("Average product flammability is ", sum(flames) / len(flames))

if __name__ == '__main__':
    inventory_report(generate_products())
