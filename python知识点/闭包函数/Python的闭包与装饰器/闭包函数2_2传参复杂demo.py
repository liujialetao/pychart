# https://www.bilibili.com/video/BV1JW411i7HR?spm_id_from=333.337.search-card.all.click&vd_source=82b424d5825df6f0aeee022464bec1ab
def arg_func(sex):
    def func1(func):
        def func2():

            if sex == 'man':
                print('你不可以生娃')
            if sex == 'woman':
                print('你可以生娃')
            return func()

        return func2

    return func1




@arg_func(sex='man')
def man():
    print('我是男人')


@arg_func(sex='woman')
def woman():
    print('我是女人')


man()
woman()