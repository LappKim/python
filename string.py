a = "I ate 1 apples. so I was sick for \"three\" days."

print("a => " + a)

a = """
I ate 1 apples.
so I was sick for \"three\" days.
"""

print("a => " + a)

a = "I ate 1 apples. so I was sick for \"three\" days."
#    0123456789
# 문자열 개수 세기
print("a.count('I') => " + str(a.count('I')))

# 위치 알려주기
print("a.find('a') => " + str(a.find('a')))

# 위치 알려주기
print("a.find('a', 1) => " + str(a.find('a', 1)))

# 위치 알려주기
print("a.find('a', 2) => " + str(a.find('a', 2)))
# 위치 알려주기
print("a.find('a', 3) => " + str(a.find('a', 3)))
# 위치 알려주기
print("a.find('a', 7) => " + str(a.find('a', 7)))

# 위치 알려주기2
print("a.index('a') => " + str(a.index('a')))

# 위치 알려주기2
print("a.index('a', 1) => " + str(a.index('a', 1)))

# 위치 알려주기2
print("a.index('a', 2) => " + str(a.index('a', 2)))
# 위치 알려주기2
print("a.index('a', 3) => " + str(a.index('a', 3)))
# 위치 알려주기2
print("a.index('a', 7) => " + str(a.index('a', 7)))

# find 못찾으면 -1, index 못찾으면 오류

# join
a = ",".join("abcd")
print("a => " + a)

a = "!!!".join("abcd")
print("a => " + a)

a = ",".join(["a","b","c","d"])
print("a => " + a)

a = ",".join("abcd")
print("a * 10 => " + a * 10)
