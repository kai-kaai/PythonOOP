#Encapsulation
class Employee: #การสร้างคลาส(ชื่อคลาสให้ตัวแรกเป็นตัวพิมพ์ใหญ่)
    def __init__(self, name, salary, department): #จะระบุหรือไม่ระบุก็ได้ ถ้าไม่ระบุจะเป็นคำสั่ง default
        #private attribute
        self._name = name #protected
        self.__salary = salary
        self.__department = department
        self.__showdata()
        #private method
    def __showdata(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self.__salary))
        print("ตำแหน่ง = {}".format(self.__department))
        
#การสร้างวัตถุ
obj1 = Employee("Kai",50000,"Programmer")
obj1._name = "Chawakorn Pimsarn"
obj1.__salary = 99999
obj1.__department = "Director"


