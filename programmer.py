from employee import Employee
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
   