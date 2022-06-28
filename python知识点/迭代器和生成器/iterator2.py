class Reverse():
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    # 如果一个类中有__iter__方法，且返回迭代器对象；则我们称这个类创建的对象为可迭代对象
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise  StopIteration

        self.index = self.index - 1
        return self.data[self.index]

# r = Reverse('abc')

class Foo():
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return Reverse(self.data)
# for循环内部在循环时，先执行__iter__方法，获取一个迭代器对象，然后不断执行next取值
# 如果取值结束，抛出StopIteration
obj = Foo('abc')
for i in obj:
    print(i)

print('3434')