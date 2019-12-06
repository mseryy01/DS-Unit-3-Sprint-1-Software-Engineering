#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10"""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20"""
        prod = Product("Test Product 1")
        self.assertEqual(prod,weight, 20)

    def test_explode_method(self):
        """Ensure explode method works"""
        prod = Product("Test Product 2")
        self.assertEqual(prod.explode(), "...BABOOM!!")

    def test_stealability_method(self):
        """Ensure stealability method works"""
        prod = Product("Test Product 3")
        self.assertEqual(prod.stealability(), "Kinda stealable.")

class AcmeReportTests(unittest, TestCase):
    """Check report outputs"""
    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
        prods = generate_products()
        for p in prods:
            self.assertEqual(p.name.count(" "), 1)
            self.assertIn(p.name.split(" ")[0], ADJECTIVES)
            self.assertIn(p.name.split(" ")[-1], NOUNS)
        
if __name__ == '__main__':
    unittest.main()
