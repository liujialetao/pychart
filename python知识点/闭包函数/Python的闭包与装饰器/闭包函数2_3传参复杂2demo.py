# https://www.bilibili.com/video/BV1JW411i7HR?spm_id_from=333.337.search-card.all.click&vd_source=82b424d5825df6f0aeee022464bec1ab
def arg_func(func):  #外部函数接收 mysum被装饰函数
    def func1(a, b): #内部函数接收mysum的参数
        print(a, b)
        a = a+5
        b = b+5
        print(a, b)
        return func(a,b)

    return func1




@arg_func  #装饰器实现，将a,b的值都加上5
def mysum(a, b):
    return a+b




sum1 = mysum(1, 2)
mysum(1, 2)