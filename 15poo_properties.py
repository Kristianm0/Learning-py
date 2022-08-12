#Properties

class Worker:
    def __init__(self, name, salary):
        self.__name = name 
        self.__salary = salary
    
    def __getname(self):
        return self.__name
    def __getsalary(self):
        return self.__salary

    def __setname(self):
        self.__name = name
    def __setsalary(self, salary):
        self.__salary = salary 

    def __delname(self):
        del self.__name
    def __delsalary(self):
        del self.__salary

    name = property(fget=__getname, fget= __setname, fdel= __delname, doc = "I am the property of the name")
    salary = property(fget=__getsalary)

Worker_one = Worker('Amoka', 3000)
Worker_one.name = "Rodo"
print(Worker_one.name, Worker_one.salary)

#worker_one = Worker("Victor", 2000)
#print(worker_one.getname(),",",worker_one.getsalary())

#worker_one = Worker("Raul", 1000)
#print(worker_one.getname(),',',worker_one.getsalary())


