from Employee import Employee
from temp5 import Person

mars = Employee("px", 30, 0)

print(issubclass(Employee, Person))
print(isinstance(mars, Employee))
print(isinstance(mars, Person))

print(mars.__repr__())
print(mars.__str__())

eleven = Employee("px", 30, 0)
print(mars == eleven)

print("-"*50)
print(mars.counter)
# print(Employee._Employee__counter)

a = [1, 2]
print(a)
# next(a)
b = iter(a)
print(next(b))
print(next(b))
# print(next(b))
