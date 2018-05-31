import os, sys
import StringIO

import unittest

class html_tag(object):

    def __init__(self,tag_name):
        self.tag_name = tag_name

    def __enter__(self):
        print '<%s>' % (self.tag_name)

    def __exit__(self,  type, value, traceback):
        print '<%s>' % (self.tag_name)

class MyUnitTests(unittest.TestCase):
    def test1(self):
        old_stdout = sys.stdout
        buffer = StringIO.StringIO()
        sys.stdout = buffer
        with html_tag("h1"):
            print("foo")
    
        with html_tag("p"):
            print("bar")
            
        sys.stdout = old_stdout
        
        buffer.flush()
        
        s = buffer.getvalue()
        toks = [t for t in s.split('\n') if (len(t) > 0)]
        self.assertEqual(toks, ['<h1>', 'foo', '<h1>', '<p>', 'bar', '<p>'])


if (__name__ == '__main__'):
    old_stdout = sys.stdout
    buffer = StringIO.StringIO()
    sys.stdout = buffer
    with html_tag("h1"):
        print("foo")

    with html_tag("p"):
        print("bar")
        
    sys.stdout = old_stdout
    
    buffer.flush()
    
    print 'First we run a few tests apart from the unit tests to help level-set expectations.'
    s = buffer.getvalue()
    print '='*30
    toks = [t for t in s.split('\n') if (len(t) > 0)]
    print toks
    print '='*30
    
    print 'Now we run the unit tests.'
    unittest.main()
