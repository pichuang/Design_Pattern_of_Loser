#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Phil Huang <pichuang@cs.nctu.edu.tw>

# pylint: disable=missing-docstring, line-too-long, too-few-public-methods

"""
Factory

delegate a specialized function/method to create instances

Reference:
https://github.com/gennad/Design-Patterns-in-Python/blob/master/factory.py
https://gist.github.com/pazdera/1099559
https://github.com/faif/python-patterns/blob/master/factory_method.py
"""


class Chicken(object):
    price = None

    def get_price(self):
        return self.price


class KFC(Chicken):
    def __init__(self):
        self.price = 100


class MCDonald(Chicken):
    def __init__(self):
        self.price = 80


class ChickenFactory(object):
    # The factory method

    @staticmethod
    def order_chicken(chicken_type):
        if chicken_type == "KFC":
            return KFC()
        elif chicken_type == "MCDonald":
            return MCDonald()


def main():
    # Get KFC Chicken
    kfc_chicken = ChickenFactory.order_chicken("KFC")
    print("Price of {chicken_type} is {price}".format(chicken_type=kfc_chicken.__class__.__name__,
                                                      price=kfc_chicken.get_price()))

    # Get McDonald_Chicken
    mcdonald_chicken = ChickenFactory.order_chicken("MCDonald")
    print("Price of {chicken_type} is {price}".format(chicken_type=mcdonald_chicken.__class__.__name__,
                                                      price=mcdonald_chicken.get_price()))


if __name__ == '__main__':
    main()
