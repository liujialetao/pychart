from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts import add

cc = add(3,4)
x = range(1, 8)
y = [114, 55, 27, 101, 125, 27, 105]

bar = Bar()
bar.add_xaxis(list(x))
bar.add_yaxis('name', y)
bar.set_global_opts(title_opts=opts.TitleOpts(subtitle="ssss"))

bar.render()

print('ss')