# coding=utf-8
# assume a+b+c=1000, find all the possible values of (a,b,c) satisfying a^2+b^2=c^2 is
import time

# solution one
print("solution one")
start = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print("a, b, c = %d ,%d, %d" % (a, b, c))
end = time.time()
print("time: %d" % (end - start))
# T(n) = O(n ** 3)
# result:
# a, b, c = 0 ,500, 500
# a, b, c = 200 ,375, 425
# a, b, c = 375 ,200, 425
# a, b, c = 500 ,0, 500
# time: 145

# solution two
print("solution two")
start = time.time()
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print("a, b, c = %d ,%d, %d" % (a, b, c))
end = time.time()
print("time: %d" % (end - start))
# T(n) = O(n ** 2)
# result:
# a, b, c = 0 ,500, 500
# a, b, c = 200 ,375, 425
# a, b, c = 375 ,200, 425
# a, b, c = 500 ,0, 500
# time: 1
