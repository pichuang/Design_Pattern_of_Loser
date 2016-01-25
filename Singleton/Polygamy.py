#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Phil Huang <pichuang@cs.nctu.edu.tw>

# pylint: disable=missing-docstring, line-too-long, too-few-public-methods

"""
Singleton

Reference
http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Singleton.html
http://openhome.cc/Gossip/DesignPattern/SingletonPattern.htm
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Husband(metaclass=Singleton):
    def __init__(self):
        self.name = "pichuang"


class Wife(object):
    def __init__(self, name, husband):
        self.name = name
        self.husband = husband

    def love(self):
        print("{0} love {1} (object id is {2})".format(self.name, self.husband.name, id(self.husband)))


def main():
    wife_1 = Wife(name="Arimura Kasumi", husband=Husband())  # https://www.instagram.com/kasumi_arimura/
    wife_2 = Wife(name="Hashimoto Kanna", husband=Husband())  # https://en.wikipedia.org/wiki/Kanna_Hashimoto
    wife_1.love()
    wife_2.love()


if __name__ == '__main__':
    main()
