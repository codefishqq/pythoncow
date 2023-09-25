'''
basic python:-
1. comment
2. string
'''
# section 1
# linr comment :- #
# comment block :- '''

# section 2

print ("hello line 1")
print ('hello line 2')

# multi-line coding
print ("hello \
world")

# print no new line
print ("same ---", end='')
print ("line")

# need to print ' , use "", or otherwise
print ("He's a boy")
print ('He said "hello"')

# want print both ', "
print ("he said \"he\'s a boy\" ")

# want to print multi-line (line block)
# **search  "escape" character table for details
# e.g. https://mateam.net/html-escape-characters/
# '\n' :- new line
# '\t' :- tab
print (" ** ** \n*  *  *\n *   *\n  * *\n   *")
# or ie use + to append strings
print (" ** ** \n"+
       "*  *  *\n"+
       " *   * \n"+
       "  * *  \n"+
       "   *     ")

#tab :- notes 'time table' to long,
# 2 tabs is needed below
print ("time table\tmon \ttue \twed")
print ("1:00\t\tEng \tMaths \tComp")
print ("2:00\t\tMusic \tArts \tSci")

# line block :- '''
print (
'''
*************
|   ^    ^  |
|     ##    |
*************
    hi !
'''
)
