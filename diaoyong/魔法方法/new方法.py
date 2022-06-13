# 通俗的讲解Python中的__new__()方法
# https://blog.csdn.net/sj2050/article/details/81172022
class A:
    pass


class B(A):
    def __new__(cls):
        print("__new__方法被执行")
        return super().__new__(cls)

    def __init__(self):
        print("__init__方法被执行")

print('开始流程')
b = B()


class CapStr(str):
    def __new__(cls, string):
        self_in_init = super().__new__(cls, string)
        print(id(self_in_init))
        return self_in_init

    def __init__(self, string):
        print(id(self))


a = CapStr("I love China!")
print(id(a))
