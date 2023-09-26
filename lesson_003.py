'''
lesson 3
1. more example of print output
2. input
'''
# format the variable output {}
# search python string format() method
# e.g. w3school, realpython
i1, f1, s1 = 4123, 13.44532, "3.445"
# {:a} :- a = length of proint
# number : right align, string : left align
print(f'==={i1:10}===')
print(f'==={f1:10}===')
print(f'==={s1:10}===')
# force left align < , right align >, center ^
print(f'==={f1:<10}===')
print(f'==={s1:>10}===')

# for float
# 2 decimal point, flosting point
# ** must have f (change to float),
# otherwise  significant value of the number
print(f'==={f1:10.2f}===')

#fill
print('sdf'.zfill(7))

