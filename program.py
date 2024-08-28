from accounting import Accounting
from programmer import Programmer
from sale import Sale


account = Accounting("chaw",10000,30)
print(account.__str__())
print("แผนกบัญชีรายได้ต่อปี = "+str(account._getIncome(5000))+" บาท")

programmer = Programmer("kai",50000,2,"python")
print(programmer.__str__())
print("แผนกพัฒนาโปรแกรมรายได้ต่อปี = "+str(programmer._getIncome(10000,500))+" บาท")

sale = Sale("siri",50000,"กรุงเทพ")
print(sale.__str__())
print("แผนกฝ่ายขายรายได้ต่อปี = "+str(sale._getIncome())+" บาท")
