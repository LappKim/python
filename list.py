
a = [ 1, 2, 3, 4 ]
print("a => " + str(a))

a = [ 1, 2, 3, 4, [5, 6]]
print("a => " + str(a))

print("a[4] => " + str(a[4]))

print("a[4][0] => " + str(a[4][0]))
print("a[4][1] => " + str(a[4][1]))

a = [ 1, 2, 3 ]
b = [ 4, 5, 6 ]
# a+b => [1, 2, 3, 4, 5, 6]
print("a + b => " + str(a+b))

# a * 5 => [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# a 5번 반복
print("a * 5 => " + str(a * 5))

a.append(4)

print("a => " + str(a))

del a[0]

print("a => " + str(a))
