'''
lesson 2
A. variables
B. more print(), with variable
'''
#*********************************
'''A. basic variable, 4 types:-
1. string
2. integer
3. float
4. boolean
'''
# *** integer/ float(non-integer)
v1 = 5
v2 = 3
#pure integer calc results in integer, except
print ("1>>", v1+(v2*2)-1)     # ans : 10
# division always result in floats
print ("2>>4/2=", 4/2)        # ans :2.0

# any calc involves float will result in float
print ("3>>3+1.0 = ",v2 + 1.0 )    #ans :4.0

# float calc might not precise as expect
print ("4>>0.1 + 0.2 = ", 0.1 + 0.2)  #ans: 0.30000000001

#boolean
# multi-assign
b1, b2 = True, False
b3 = not(b1)
#for comparison
b4 = (1 == 2)
b5 = (v1 != 2)

#print multi-output
print("5>>boolean :-", b1, b2, b3, b4, b5 )

# type conversion, casting
# string to number
s1 = "3"
s2 = "2.1"
i1 = 4
f1 = 5.1231
print ("6>>", int(s1)+float(s2))
#float string cannot convert to integer directly
# print (int(s1)+int(s2))    #error
print ("7>>", int(s1)+int(float(s2)))

#number to string
#in the following, i print the same string with diff method :-
#format string: m1
print ("08>>i have " + str(i1) + " apple and " +
       str(f1)+" orange")

#B. more print()
#format string: m2a, seen before
#note that comma auto put space between
print ("09>>i have" ,str(i1) ,"apple and" ,
       str(f1), "orange")
#format string: m3a , use of format(), positional arguement
print ("10>>i have {0} apple and {1} orange".format(i1,f1))
#format string : m3b, key word arguement
print ("11>>i have {vname1} apple and {vname2} orange".
       format(vname1=i1,vname2=f1))
#format string: m4
print (f"12>>i have {i1} apple and {f1} orange")

#format string :m5 , old c language format
#'c Format Specifier' : %d, %f, %s
# few people choose this one
print("13>>i have %d apple and %.4f orange" %(i1,f1) )

