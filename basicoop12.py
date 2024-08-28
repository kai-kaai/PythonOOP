#Overiding Overloading Method
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
    
    # แสดงข้อมูล (Overiding Method)
    def _showdata(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหน่ง = {}".format(self._department))

    #รายได้ต่อปี (Overloading Method)
    def _getIncome(self,bonus=0,overtime=0):
        return (self.__salary * 12)+bonus+overtime
    
    # แสดงข้อมูล (Overriding Method)
    def __str__(self):
        return ("ชื่อพนักงาน = {} ,แผนก {} , เงินเดือน = {} , รายได้ต่อปี = {}".format(self.__name,self._department,self.__salary,self._getIncome()))

class Accounting(Employee):
    __departmentName ="บัญชี"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmentName)
        self.__age = age
    
    def _showdata(self):
        super()._showdata()
        print("อายุ = {}".format(self.__age))
        print("##################")

    def __str__(self):
        return (super().__str__()+" , อายุ = {}".format(self.__age))


class Programmer(Employee):
    __departmentName ="พัฒนาโปรแกรม"
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self.__departmentName)
        self.__exp = experience
        self.__skill = skill

    def _showdata(self):
        super()._showdata()
        print("ประสบการณ์ = {}".format(self.__exp))
        print("ทักษะ = {}".format(self.__skill))
        print("##################")
    
    def __str__(self):
        return (super().__str__()+" , ประสบการณ์ = {} ปี , ทักษะ = {}".format(self.__exp,self.__skill))
        

class Sale(Employee):
    __departmentName ="ฝ่ายขาย"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmentName)
        self.__area = area

    def _showdata(self):
        super()._showdata()
        print("พื้นที่ = {}".format(self.__area))
        print("##################")
    
    def __str__(self):
        return (super().__str__()+" , พื้นที่รับผิดชอบ = {}".format(self.__area))

        


account = Accounting("chaw",10000,30)
print(account.__str__())
print("แผนกบัญชีรายได้ต่อปี = "+str(account._getIncome(5000))+" บาท")
programmer = Programmer("kai",50000,2,"python")
print(programmer.__str__())
print("แผนกพัฒนาโปรแกรมรายได้ต่อปี = "+str(programmer._getIncome(10000,500))+" บาท")
sale = Sale("siri",50000,"กรุงเทพ")
print(sale.__str__())
print("แผนกฝ่ายขายรายได้ต่อปี = "+str(sale._getIncome())+" บาท")