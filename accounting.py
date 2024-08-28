from employee import Employee
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
