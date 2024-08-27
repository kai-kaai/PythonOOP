#ฟังก์ชั่นเสริม
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
obj2 = Employee("Kong",40000,"Manager")
obj3 = Employee("Nut",100000,"Director")

print(isinstance(obj1,Employee))
print(dir(obj1))
print(obj1.__class__)