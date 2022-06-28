# Python小技巧#9：实例方法，类方法，静态方法的区别？
#https://www.bilibili.com/video/BV13741167D8/?spm_id_from=pageDriver&vd_source=82b424d5825df6f0aeee022464bec1ab
class Dog():
	dogbook = {'黄色':30, '黑色':20, '白色':0}

	def __init__(self, name, color, weight):
		self.name = name
		self.color = color
		self.weight = weight
		#此处省略若干行，应该更新dogbook的数量

    #实例方法: 定义时,必须把self作为第一个参数，可以访问实例变量，只能通过实例名访问
	def bark(self):
		print(f'{self.name} 叫了起来')

    #类方法：定义时,必须把类作为第一个参数，可以访问类变量，可以通过实例名或类名访问
	@classmethod
	def dog_num(cls):
		num = 0
		for v in cls.dogbook.values():
			num = num + v
		return num

    #静态方法：不强制传入self或者cls, 他对类和实例都一无所知。不能访问类变量，也不能访问实例变量；可以通过实例名或类名访问
	@staticmethod
	def total_weights(dogs):
		total = 0
		for o in dogs:
			total = total + o.weight
		return total
if __name__ == '__main__':

	print(f'共有 {Dog.dog_num()} 条狗')
	d1 = Dog('大黄', '黄色', 10)
	d1.bark()
	print(f'共有 {d1.dog_num()} 条狗')
	d2 = Dog('旺财', '黑色', 8)
	d2.bark()
	print(f'狗共重 {Dog.total_weights([d1, d2])} 公斤')


