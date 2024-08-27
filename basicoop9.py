#Inher itance
class Employee:
    # class variable (ต้องประกาศตัวแปรเป็น public หรือ protected)
    __minSalary = 12000
    maxSalary = 50000
    companyname = "บริษัท xyz จํากัด"

    def __init__(self, name, salary, department): 
        # instance variable
        self.__name = name
        self.__salary = salary
        self._department = department
    
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหน่ง = {}".format(self._department))

class Accounting(Employee):
    __departmentName ="บัญชี"
    def __init__(self):
        pass
class Programmer(Employee):
    __departmentName ="พัฒนาโปรแกรม"
    def __init__(self):
        pass
class Sale(Employee):
    __departmentName ="ฝ่ายขาย"
    def __init__(self):
        pass

account = Accounting()


programmer = Programmer()
print(Programmer._Employee__minSalary)

sale = Sale()

