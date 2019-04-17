"""
list = [x * x for x in range(3)]                #列表生成式

for i in list:
    print(i)
"""
def square():
    for x in range(4):
        yield x ** 2                           
#循环至yield处时停止，然后在主循环出继续迭代，
#不需在函数中循环出全部的值再进行主循环，节省内存

square_gen = square()
for x in square_gen:
    print(x)