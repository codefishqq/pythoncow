'''
lesson 4
1. swap 2 variables
2. decision :- if-statement
3. loop :- while
'''
# 1. swap 2 variables
v1 = 4
v2 = 10
# programming language without multi assignment
# to swap variable v1 <--> v2
tmp = v1
v1 = v2
v2 = tmp
print('v1>>', v1, ' v2>>', v2)
#for python
v1, v2 = v2, v1
print('v1>>', v1, ' v2>>' , v2)

# if statement

# negative :- not
# connect caomparison with :- and , or
# comparison operator : ==,  !=, >, >=, <, <=

# eg 1
if (v1 == v2):
    print('the same')
else:
    print('not the same')

#eg2
if ((v2 < 50) and (v2 > 0)):
    print('fail')
elif (v2 < 80):
    print('pass')
elif (v2 < 90):
    print('good')
elif (v2 < 100):
    print('excellent')
else:
    print('error : out of range')

#number as boolean
# 0 == False
# non 0 == True
print('04>>',bool(0))
print('05>>',bool(23))

#string comparison




