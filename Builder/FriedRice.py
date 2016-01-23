#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Phil Huang <pichuang@cs.nctu.edu.tw>

# pylint: disable=missing-docstring, line-too-long, too-few-public-methods

"""
Builder

instead of using multiple constructors, builder object receives parameters and returns constructed objects

Reference:
http://rockssdlog.blogspot.tw/2012/05/design-pattern-builder-pattern.html
https://sourcemaking.com/design_patterns/builder
https://github.com/faif/python-patterns/blob/master/builder.py
"""


class Director(object):
    """
    Counter Service or Waiter
    """
    builder = None

    def __init__(self, builder):
        self.builder = builder

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_main_meal()
        self.builder.build_sauce()
        self.builder.build_drink()

    def get_building(self):
        return self.builder.building


class Builder(object):
    """
    Chef
    """

    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = FriedRice()


class BeefBuilder(Builder):
    def build_main_meal(self):
        self.building.main_meal = "Beef"

    def build_sauce(self):
        self.building.sauce = "XO"

    def build_drink(self):
        self.building.drink = "Coca"


class ChieckenBuilder(Builder):
    def build_main_meal(self):
        self.building.main_meal = "Chicken"

    def build_sauce(self):
        self.building.sauce = "BBQ"

    def build_drink(self):
        self.building.drink = "Water"


class FriedRice(object):
    """
    Base Product
    """

    def __init__(self):
        self.main_meal = None
        self.sauce = None
        self.drink = None
        self.rice = "Koshihikari" # https://en.wikipedia.org/wiki/Koshihikari

    def __repr__(self):
        return "{main_meal} + {sauce} + {rice} + {drink}".format(main_meal=self.main_meal, sauce=self.sauce, rice=self.rice, drink=self.drink)


def main():
    """Order Beef Fried Rice"""
    director = Director(BeefBuilder())
    director.construct_building()
    beef_fired_rice = director.get_building()
    print("Order `Beef Fried Rice`, include {0}".format(beef_fired_rice))

    """Order Chicken Fried Rice"""
    director.builder = ChieckenBuilder()
    director.construct_building()
    chicken_fired_rice = director.get_building()
    print("Order `Chicken Fried Rice`, include {0}".format(chicken_fired_rice))


if __name__ == '__main__':
    main()
