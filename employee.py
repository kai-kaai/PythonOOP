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
