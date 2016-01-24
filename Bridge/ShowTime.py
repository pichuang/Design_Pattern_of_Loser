#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Phil Huang <pichuang@cs.nctu.edu.tw>

# pylint: disable=missing-docstring, line-too-long, too-few-public-methods

"""
Bridge

a client-provider middleman to soften interface changes

Reference
http://xyz.cinc.biz/2013/07/bridge-pattern.html
https://gist.github.com/pazdera/1173009
"""


class ShowTimeImplentationInterface(object):
    """
    Interface for the background implementation

    This class defines how the Bridge communicates with various background implementations.
    """

    def show_time(self):
        raise NotImplementedError


class LinuxSystem(ShowTimeImplentationInterface):
    """
    Concrete background implementation - Linux
    """

    def show_time(self):
        print("Linux Time!")


class WindowsSystem(ShowTimeImplentationInterface):
    def show_time(self):
        print("Windows Time!")


class ShowTimeAbstractInterface(object):
    """
    Target Interface

    This is the target interface, that clients use.
    """

    def i_want_know_time(self):
        raise NotImplementedError


class Bridge(ShowTimeAbstractInterface):
    """
    Bridge class

    This class forms a bridge between the target interface and background implementation.
    """

    def __init__(self):
        self.__implementation = None


class TimeCommand(Bridge):
    """
    Variant of the target interface
    """

    def __init__(self, implementation):
        self.__implementation = implementation

    def i_want_know_time(self):
        print("Use `show time` Command:")
        self.__implementation.show_time()


def main():
    linux = LinuxSystem()
    windows = WindowsSystem()

    mm = TimeCommand(linux)
    mm.i_want_know_time()

    mm = TimeCommand(windows)
    mm.i_want_know_time()


if __name__ == '__main__':
    main()
