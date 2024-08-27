# โปรแกรมจัดการข้อมูลของพนักงาน ชื่อ, เงินเดือน

class Employee: #การสร้างคลาส(ชื่อคลาสให้ตัวแรกเป็นตัวพิมพ์ใหญ่)
    #การสร้าง method
    def detail(self, name, salary, department):
        self.name = name #Astribute  มีself แสดงว่าเราทำงานกับตัว object
        self.salary = salary
        self.department = department
    
    def showdata(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("ตำแหน่ง = {}".format(self.department))



#การสร้างวัตถุ
obj1 = Employee()
obj1.detail("Kai",50000,"Programmer")
obj2 = Employee()
obj2.detail("Kong",40000,"Manager")
obj3 = Employee()
obj3.detail("Nut",100000,"Director")

obj1.showdata()
obj2.showdata()
obj3.showdata()