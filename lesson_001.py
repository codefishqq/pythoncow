'''
basic python:-
1. comment
2. string
'''
# remake for coding, not programming issue
# multi-line coding
print ("1>>hello \
world")
# u can run/test python program online in browser !!

# section 1
# line comment :- #
# comment block :- '''

# section 2

print ("2>> hello line 1")
print ('3>>hello line 2')

# print no new line
print ("4>>same ---", end='')
print ("line")

# need to print ' , use "", or otherwise
print ("5>>He's a boy")
print ('6>>He said "hello"')

# want print both ', "
print ("7>>he said \"he\'s a boy\" ")

# you can break string into multi string
print ("8>>this is"
        " one "
        "line")

# want to print multi-line (line block)
# **search  "escape" character table for details
#e.g.  http://daniel-hug.github.io/characters/
# e.g. https://mateam.net/html-escape-characters/

# '\n' :- new line
# '\t' :- tab
print (" ** ** \n*  *  *\n *   *\n  * *\n   *")

# or ie use + to append strings, or without '+'
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

#print pi char
print ("9>>\u03C0 = 3.1415...")

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
