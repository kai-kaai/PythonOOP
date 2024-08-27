#Getter Setter Method
class Employee:
    def __init__(self,name,salary,department):
        self.__name = name
        self.__salary = salary
        self.__department = department
    
    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.getName()))
        print("เงินเดือน = {}".format(self.getSalary()))
        print("ตำแหน่ง = {}".format(self.getDepartment()))

    # Setter method
    def setName(self, newname):
        self.__name = newname

    def setSalary(self, newsalary):
        self.__salary = newsalary

    def setDepartment(self, department):
        self.__department = department

    # Getter method
    def getName(self):
        return self.__name
    
    def getSalary(self):
        return self.__salary
    
    def getDepartment(self):
        return self.__department

obj1 = Employee("ไก่",50000,"บัญชี")
print(obj1.getName())