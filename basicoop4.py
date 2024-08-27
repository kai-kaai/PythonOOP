# การสร้าง constructor
class Employee: #การสร้างคลาส(ชื่อคลาสให้ตัวแรกเป็นตัวพิมพ์ใหญ่)

    def __init__(self, name, salary, department): #จะระบุหรือไม่ระบุก็ได้ ถ้าไม่ระบุจะเป็นคำสั่ง default
        self.name = name
        self.salary = salary
        self.department = department
    
    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))
        
#การสร้างวัตถุ
obj1 = Employee("Kai",50000,"Programmer")
obj1.salary = 99999
obj1.name = "Chawakorn Pimsarn"
obj1.showdata()

obj2 = Employee("Kong",40000,"Manager")
obj2.showdata()

obj3 = Employee("Nut",100000,"Director")
obj3.showdata()



