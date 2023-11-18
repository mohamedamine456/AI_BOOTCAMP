from vector import Vector

v1 = Vector([4, 77, 88, 9, 32, 32, 2])
v2 = Vector(7)
print(v2)
v3 = v1 - v2
print(v3)
v3 = v1 + v2
print(v3)
v3 = v1 * v2
print(v3)
v3 = 44.1 + v1
print(v3)
v3 = 2.03 - v2
print(v3)
v3 = v2 / 2
print(v3)
print(str(v3))
print(repr(v3))

v7 = Vector([[0.0], [1.0], [2.0], [3.0]])
v7 = v7 * 5
print(v7)
