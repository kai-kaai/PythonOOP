from employee import Employee

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
