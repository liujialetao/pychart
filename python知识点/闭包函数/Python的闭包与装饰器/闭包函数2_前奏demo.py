# https://www.bilibili.com/video/BV1JW411i7HR?spm_id_from=333.337.search-card.all.click&vd_source=82b424d5825df6f0aeee022464bec1ab

# def func1(func):
#     def func2():
#         print('aaabbb')
#         return func()
#     return func2
#
#
# def myprint():
#     print('你好，我是myprint')
#
# myprint()
# myprint()



def func1(func):
    def func2(str_a):
        print('aaabbb')
        return func(str_a)
    return func2

@func1
def myprint(str_a):
    print(str_a)

myprint('你好，我是myprint')
# myprint()
# myprint()