# # 例子1
# class Foo():
#
#     def __iter__(self):
#         print('111')
#         yield 1
#         print('222')
#         yield 2
#         print('333')
#
# obj = Foo()
#
# for item in obj:
#     print(item)


# 例子2


# B站视频地址
# https://www.bilibili.com/video/BV1BT4y1P7nn?spm_id_from=333.880.my_history.page.click&vd_source=82b424d5825df6f0aeee022464bec1ab
class Xrange(object):
    '''
    模拟range
    '''
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        num = 0
        print('第一次进入')
        while(num < self.max_num):
            print('返回num:', num)
            yield num
            num += 1
            print('计算下次的num:', num)

obj = Xrange(100)
for item in obj:
    print('生成器中的值为', item)
    print(item)