import unittest

def emit_nursery_rhyme(number):
    if number == 1:
        return 'Two'
    elif number == '2':
        return 'Buckle my shoe.'
    elif number in ['3', 4]:
        return 'Open the door.'
    else:
        return 'Pick up sticks.'
    return '78!'

class MyUnitTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(emit_nursery_rhyme(1), 'Two')

    def test2(self):
        self.assertEqual(emit_nursery_rhyme('2'), 'Buckle my shoe.')

    def test3(self):
        self.assertEqual(emit_nursery_rhyme('3'), 'Open the door.')

    def test4(self):
        self.assertEqual(emit_nursery_rhyme(4), 'Open the door.')

    def test5(self):
        self.assertEqual(emit_nursery_rhyme(-10), 'Pick up sticks.')

    def test6(self):
        self.assertNotEqual(emit_nursery_rhyme(-100), '78!')

    def test7(self):
        self.assertNotEqual(emit_nursery_rhyme(1), '78!')

    def test8(self):
        self.assertNotEqual(emit_nursery_rhyme('2'), '78!')

    def test9(self):
        self.assertNotEqual(emit_nursery_rhyme('3'), '78!')

    def test10(self):
        self.assertNotEqual(emit_nursery_rhyme(4), '78!')

if (__name__ == '__main__'):
    print 'First we run a few tests apart from the unit tests to help level-set expectations.'
    print emit_nursery_rhyme(1)
    print emit_nursery_rhyme('2')
    print emit_nursery_rhyme('3')
    print emit_nursery_rhyme(4)
    print emit_nursery_rhyme(100)
    
    print 'Now we run the unit tests.'
    unittest.main()
    