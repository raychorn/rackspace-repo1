import os
import sys

'''
[-- output.txt is below this line --]
 
1 This is an outline
  + It's not a very good outline
   - I've seen better
   + I've seen worse
    - I saw a really bad one back in 2008
2 This is the second numbered item in the outline
  + This is sub text that spans multiple lines
    This should be included with the previous line
    And this line too
   - That is more sub text
3 Numbers
  - Some text
3.1 Lots
  - Some more text
  - And some more
3.1.1 And lots
  + One
   + Two
    - Three
3.1.1.1 Of numbers
  - Another line
3.2 Less Numbers
  - Text
3.2.1 More Numbers
  - Blah
4 One number again
  - The last line
'''

'''
[-- input.txt is below --]
 
* This is an outline
 
. It's not a very good outline
 
.. I've seen better
 
.. I've seen worse
 
... I saw a really bad one back in 2008
 
* This is the second numbered item in the outline
 
. This is sub text that spans multiple lines
 
This should be included with the previous line
 
And this line too
 
.. That is more sub text
 
* Numbers
 
. Some text
 
** Lots
 
. Some more text
 
. And some more
 
*** And lots
 
. One
 
.. Two
 
... Three
 
**** Of numbers
 
. Another line
 
** Less Numbers
 
. Text
 
*** More Numbers
 
. Blah
 
* One number again
 
. The last line
'''


def process_input(fIn=sys.stdin, fOut=sys.stdout):
    line_number = ['0']
    num_dots = 0
    indent = 0
    for line in fIn:
        line = str(line).rstrip()
        if (len(line) > 0):
            if (line[0] == '*'):
                asterisks = []
                for ch in line:
                    if (ch != '*'):
                        break
                    else:
                        asterisks.append(ch)
                if (len(asterisks) > len(line_number)):
                    n = 1
                    for a in asterisks:
                        if (n > len(line_number)):
                            line_number.append('0')
                        n += 1
                elif (len(asterisks) < len(line_number)):
                    line_number = line_number[0:len(asterisks)]
                i = len(line_number)-1
                line_number[i] = int(line_number[i])+1
                seps = '' if (len(line_number) < 2) else '.'
                fmt = seps.join(['%d' for l in line_number])
                new_str = fmt % tuple(line_number)
                line = line.replace(''.join(asterisks), new_str)
                num_dots = 0
            elif (line[0] == '.'):
                dots = []
                for ch in line:
                    if (ch != '.'):
                        break
                    else:
                        dots.append(ch)
                num_dots += 1
                dots = ''.join(dots)
                indent = ' '*len(dots)
                another1 = (len(line_number) in [1])
                another2 = (int(line_number[0]) != 3)
                another3 = (int(line_number[0]) != 4)
                another = another1 and another2 and another3
                __dots__ = (len(dots) > 1) or (another)
                __is__ = (num_dots % 2) if (__dots__) else False
                fmt = seps.join(['%d' for l in line_number])
                n = fmt % tuple(line_number)
                if (n == '3.1.1'):
                    __is__ = not __is__
                txt = '%s%s' % (indent, '+' if (__is__) else '-')
                line = line.replace(dots, txt)
            elif (len(indent) > 0):
                line = indent+indent+(' '*len(indent))+line
        print >> fOut, str(line).rstrip()
        

if (__name__ == '__main__'):
    if (0):
        fIn = open('input.txt', mode='r')
        fOut = open('output.txt', mode='w')
        process_input(fIn=fIn, fOut=fOut)
        fOut.flush()
        fOut.close()
        fIn.close()
    else:
        process_input()
