#Overloading Method
class Employee:
    # class variable (ต้องประกาศตัวแปรเป็น public หรือ protected)
    minSalary = 12000
    maxSalary = 50000
    companyname = "บริษัท xyz จํากัด"

    def __init__(self, name, salary, department): 
        # instance variable
        self.__name = name
        self.__salary = salary
        self._department = department
    
    # แสดงข้อมูล
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหน่ง = {}".format(self._department))

    #รายได้ต่อปี
    def _getIncome(self):
        return self.__salary * 12
    
    def __str__(self):
        return ("ชื่อพนักงาน = {} ,แผนก {} , เงินเดือน = {} , รายได้ต่อปี = {}".format(self.__name,self._department,self.__salary,self._getIncome()))

class Accounting(Employee):
    __departmentName ="บัญชี"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentName)
        self.age = age

class Programmer(Employee):
    __departmentName ="พัฒนาโปรแกรม"
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self.__departmentName)
        self.exp = experience
        self.skill = skill
        

class Sale(Employee):
    __departmentName ="ฝ่ายขาย"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentName)
        self.area = area
        


account = Accounting("chaw",20000,30)
account._showdata()
programmer = Programmer("kai",50000,2,"python")
sale = Sale("siri",50000,"กรุงเทพ")

