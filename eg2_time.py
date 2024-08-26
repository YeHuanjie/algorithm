# coding=utf-8
# different functions cost different time
from timeit import Timer


def test1():
    li = []
    for i in range(1000):
        li.append(i)


def test2():
    li = []
    for i in range(1000):
        li += [i]
        # li = li + [i]
        # need more time


def test3():
    li = [i for i in range(1000)]


def test4():
    li = list(range(1000))


def test5():
    li = []
    for i in range(1000):
        li.extend([i])


t1 = Timer("test1()", "from __main__ import test1")
print("append  {:.4f}".format(t1.timeit(number=1000)), " seconds")
t2 = Timer("test2()", "from __main__ import test2")
print("+  {:.4f}".format(t2.timeit(number=1000)), " seconds")
t3 = Timer("test3()", "from __main__ import test3")
print("[i for i in range]  {:.4f}".format(t3.timeit(number=1000)), " seconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list(range)  {:.4f}".format(t4.timeit(number=1000)), " seconds")
t5 = Timer("test5()", "from __main__ import test5")
print("extend  {:.4f}".format(t5.timeit(number=1000)), " seconds")

# result:
# append  0.1045  seconds
# +  0.1500  seconds
# [i for i in range]  0.0395  seconds
# list(range)  0.0169  seconds
# extend  0.1958  seconds


def test6():
    li = []
    for i in range(1000):
        li.append(i)


def test7():
    li = []
    for i in range(1000):
        li.insert(0, i)


t6 = Timer("test6()", "from __main__ import test6")
print("append  {:.4f}".format(t6.timeit(number=1000)), " seconds")
t7 = Timer("test7()", "from __main__ import test7")
print("insert  {:.4f}".format(t7.timeit(number=1000)), " seconds")
# result:
# append  0.0962  seconds
# insert  0.3779  seconds
