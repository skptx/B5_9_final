import time

# использование функции декоратора с параметром
def time_this(num_runs):
	def decorator(func):
		def wrap():
			avg_time = 0
			for _ in range(num_runs):
				t0 = time.time()
				func()
				t1 = time.time()
			avg_time += (t1 - t0)
			avg_time /= num_runs
			print("\nИспользование функции декоратора с параметром")
			print("Выполнение заняло %.5f секунд" % avg_time)
		return wrap
	return decorator


@time_this(num_runs=10)
def f():
    for j in range(10000000):
        pass    
f()


# использование функции декоратора внутри класса
class c_time_this:
	def __init__(self, num_runs=10):
	 	self.num_runs = num_runs
	def __call__(self, func):
		def wrap(*args):
			avg_time = 0
			for _ in range(self.num_runs):
				t0 = time.time()
				func()
				t1 = time.time()
			avg_time += (t1 - t0)
			avg_time /= self.num_runs
			print("\n*Использование функции декоратора в виде класса")
			print("Выполнение заняло %.5f секунд" % avg_time)
		return wrap

t = c_time_this(10)

@t
def fc():
    for j in range(10000000):
        pass    

fc()


# использование функции декоратора внутри класса с контекстным менеджером.
class cw_time_this:
	def __init__(self, num_runs=10):
	 	self.num_runs = num_runs
	def __enter__(self):
		return self
	def __exit__(self, type, value, traceback):
		pass
	def __call__(self, func):
		def wrap(*args):
			avg_time = 0
			for _ in range(self.num_runs):
				t0 = time.time()
				func()
				t1 = time.time()
			avg_time += (t1 - t0)
			avg_time /= self.num_runs
			print("\n**Использование функции декоратора в виде класса с контестным менеджером.")
			print("Выполнение заняло %.5f секунд" % avg_time)
		return wrap

with cw_time_this(10) as cw:
	@cw
	def fcw():
	    for j in range(10000000):
	        pass    

fcw()