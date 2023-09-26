'''
lesson 3
1. more example of print output
2. more string and number manipulation
3. input function
'''
# format the variable output :- {}
# ref:- search python string format() method
# e.g. w3school, realpython
i1, f1, s1 = 4123, 13.44532, "3.445"
# {:a} :- a = length of proint
# number : right align, string : left align
print(f'01>>==={i1:10}===')
print(f'02>>==={f1:10}===')
print(f'03>>==={s1:10}===')
# force left align < , right align >, center ^
print(f'04>>==={f1:<10}===')
print(f'05>>==={s1:>10}===')

# for float
# 2 decimal point, flosting point
# ** must have f (change to float),
# otherwise  significant value of the number
print(f'06>>==={f1:10.2f}===')

# 2a. number manipulation
# trunc , ceil method is in the math library
# not default, must load before use it
import math

ff1 = 2.4
ff2 = -2.9

# round to the nearest integer:-
# if over decimal 5, to the greater value,
# 1.5 --> 2 , 1.49 --> 1
# -2.51 --> -3, -2.5 --> -2
print('07>>', round(ff1))
print('08>>', round(ff2))

# to round down a number (to integer)
# trunc/cast int :- just cut off the decimal
# trunc/ int() :- 2.3 --> 2, -2.3 --> -2
# floor :- round to the nearest smaller integer
# floor :- 2.3 --> 2, -2.3 --> -3
print('09>>', math.trunc(ff1))
print('10>>', math.floor(ff1))
print('11>>', math.trunc(ff2))
print('12>>', math.floor(ff2))

# to round a float to 2 decimal point
print('13>>', round(ff1,2))

# to round up a number (to the nearest larger integer)
# 2.3 --> 3, -2.3 --> -2
print('14>>', math.ceil(ff1))
print('15>>', math.ceil(ff2))

# 3b. string manipulation (just few examples)
# string case change
ss1 = 'liTTle minG'
# first letter to be capital letter
print('16>>'+ss1.title())
# change all to upper or lower case
print('17>>'+ss1.lower())
print('18>>'+ss1.upper())

# stripping whiltespaces, ie. space , new line, tab etc
# use len() to show length of the string
ss2 = '   hello again    '
print('19>>', len(ss2))
# strip both end
print('20>>', len(ss2.strip()))
# strip left
print('21>>', len(ss2.lstrip()))
# strip right
print('22>>', len(ss2.rstrip()))

#remove prefix
ss3  = 'name :cow cow'
print('23>>', ss3.removeprefix('name :'))
print('24>>', ss3.removesuffix('cow cow'))

# 2. input function:-
# always return  string
# use type() to show the type of the variable
aa = input('pls input:-')
print ('25>>', type(aa))
# if u expect number to be input , case string into float
# i.e. if invalide input, error and program break down !!
bb = input("input a number :-")
print ("26>>" , float(bb) *2)

