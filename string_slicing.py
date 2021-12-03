
a = "Life is too short, You need python"

print("a => " + a)

print("a[0:4] => " + a[0:4])

# a[     :     :      ]
#   이상 : 미만 : 간격
#    <=  x  <
a = "20010831Rainy"

print("a => " + a)

print("a[:8] => " + a[:8])

print("a[8:] => " + a[8:])

a = "0123456789"

print("a[0:8:2] => " + a[0:8:2])

print("a => " + a)

# 9876543210
print("a[::-1] => " + a[::-1])

# 97531
print("a[::-2] => " + a[::-2])



def is_pl(s):
    "Check whether a string is a palindrome"""
    return s == s[::-1]

# TypeError: can only concatenate str (not "bool") to str
print("is_pl(a) => " + str(is_pl(a)))
