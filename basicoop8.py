#class Variable
class Employee:
    # class variable (ต้องประกาศตัวแปรเป็น public หรือ protected)
    _minSalary = 12000
    _maxSalary = 50000
    _companyname = "บริษัท xyz จํากัด"

    def __init__(self, name, salary, department): 
        # instance variable
        self.__name = name
        self.__salary = salary
        self._department = department
    
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหน่ง = {}".format(self._department))

obj1 = Employee("Kai",50000,"Programmer")
print("เงินเดือนต่ำสุดของพนักงาน = "+str(Employee._minSalary))
print(Employee._companyname)
