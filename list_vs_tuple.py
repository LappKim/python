
# 리스트 - 리스트에 추가 삭제 가능
# a = [ 1, 2, 3 ]

# 튜플 (tuple) - 추가, 변경, 삭제 불가능
# a = ( 1, 2, 3 )

t1 = (1, 2, 'a', 'b')

# 삭제 불가능
# del t1[0] # TypeError: 'tuple' object doesn't support item deletion

# t1[0] = 2 # TypeError: 'tuple' object does not support item assignment   

# indexing 가능
print("t1[1] -> {value}, address => {address}".format(value=t1[1], address=id(t1)))

# slicing 가능
print("t1[0:2] -> {value}, address => {address}".format(value=t1[0:2], address=id(t1)))

# 더하기
t2 = (3, 4)
print("t2 -> {value}, address => {address}".format(value=t2, address=id(t2)))

t3 = t1 + t2
print("t3 -> {value}, address => {address}".format(value=t3, address=id(t3)))

# 곱하기
t4 = t1 * 3
print("t4 -> {value}, address => {address}".format(value=t4, address=id(t4)))
