import sys
list1 = sys.path
print(list1)
print('=========')

from pyecharts import charts, commons, components, datasets, options, render, scaffold
from pyecharts.charts.chart_lj. chart_add import add
from pyecharts._version import __author__, __version__

list2 = sys.path
print(list2)


for i in list2:
    if i not in list1:
        print('list1没有',i)

for i in list1:
    if i not in list2:
        print('list2没有',i)
print('欢迎调用pyecharts_lj')