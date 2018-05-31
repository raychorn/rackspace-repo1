import os, sys
import StringIO

import unittest

'''
You must validate your input for all cases and respond appropriately.
The port number must be an integer between 1 and 65535 (including 1 and 65535).
Write sufficient unit tests using the standard Python unit test library for your method.
'''
class Connector(object):
    def __init__(self, is_silent=False):
        self.is_silent = is_silent
    
    def set_port(self, port):
        if (port >= 1) and (port <= 65535):
            self.port = port
        else:
            self.port = None
            if (not self.is_silent):
                raise ValueError('The port number must be an integer between 1 and 65535 (including 1 and 65535).')

    def get_port(self):
        return self.port
    
class MyUnitTests(unittest.TestCase):
    def test1(self):
        c = Connector(is_silent=True)
        p = -1
        try:
            c.set_port(-1)
            p = c.get_port()
        except ValueError:
            pass
        self.assertEqual(p, None)

    def test2(self):
        c = Connector(is_silent=True)
        p = -1
        try:
            c.set_port(1)
            p = c.get_port()
        except ValueError:
            pass
        self.assertEqual(p, 1)

    def test3(self):
        c = Connector(is_silent=True)
        p = -1
        try:
            c.set_port(65535)
            p = c.get_port()
        except ValueError:
            pass
        self.assertEqual(p, 65535)

    def test4(self):
        c = Connector(is_silent=True)
        p = -1
        try:
            c.set_port(99999)
            p = c.get_port()
        except ValueError:
            pass
        self.assertEqual(p, None)


if (__name__ == '__main__'):
    print 'First we run a few tests apart from the unit tests to help level-set expectations.'
    c = Connector(is_silent=True)
    c.set_port(-1)
    print c.get_port()
    c.set_port(1)
    print c.get_port()
    c.set_port(65535)
    print c.get_port()
    c.set_port(99999)
    print c.get_port()
    
    print 'Now we run the unit tests.'
    unittest.main()
