a = "I eat %d apples." % 3
b = "I eat " +str(3)+ " apples."

print("a => " + a)
print("b => " + b)


# %s
# %c
# %d
# %f
# %o
# %x
# % % : %
number = 10
day = "three"

a = "I ate %d apples. so I was sick for \"%s\" days." % (number, day)
print("a => " + a)

a = "I ate %s apples. so I was sick for \"%s\" days." % (number, day)
print("a => " + a)

a = "I ate {} apples.".format(number)
print("a => " + a)

a = "I ate {} apples. so I was sick for \"{}\" days.".format(number, day)
print("a => " + a)

a = "My name is {name}.".format(name="김현석")
print("a => " + a)

a = "My name is {name}. I'm {age} old.".format(age=30, name="김현석")
print("a => " + a)

name="김현석"
a = f"My name is {name}."
print("a => " + a)
