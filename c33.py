### Conditionals and comparators

"""
def older(num):
    if num >= 18:
        return True
    else:
        return False
        

age = input("Give your age: ") 

if older(int(age)):
    print("You are adult")

else:
    print("You are not adult")

"""

########## 👆 ages

######## 👇 What is the number

"""""
def elder (n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    if n2 >= n1 and n2 >= n3:
        return n2
    if n3 >= n1 and n3 >= n2:
        return n3
    else:
        return n3

nume = (elder(100, 66, 104))
print(nume)
"""