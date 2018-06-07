from temp5 import Person


class Employee(Person):
    """一个雇员"""

    __counter = 0

    @property
    def counter(self):
        print("--getter--")
        return self.__counter

    @counter.setter
    def counter(self, newCounter):
        print("--setter--")
        self.__counter = newCounter

    # counter = property(getCounter, setCounter)

    def __init__(self, name, age, work_id):
        Person.__init__(self, name, age)
        self.work_id = work_id
        Employee.__counter += 1

    def __str__(self):
        return "Employee"

    def __eq__(self, other):
        return self.name == other.name and \
               self.age == other.age and \
               self.work_id == other.work_id
