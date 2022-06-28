# https://www.bilibili.com/video/BV1JW411i7HR?spm_id_from=333.337.search-card.all.click&vd_source=82b424d5825df6f0aeee022464bec1ab
def arg_func(c):# c装饰器函数的参数
    def func2(func):
        def func1(a, b):
            print(a, b)
            a = a+c
            b = b+c
            print(a, b)
            return func(a,b)
        return func1

    return func2





@arg_func(c = 5)  #装饰器实现，将a,b的值都加上5
def mysum(a, b):
    return a+b




sum1 = mysum(1, 2)
print(sum1)
mysum(1, 2)