
def average():

    li = []

    def inner(value):
        li.append(value)
        return sum(li) / len(li)

    return inner

avg = average()
print(avg(6000))
print(avg(7000))
print(avg(8000))