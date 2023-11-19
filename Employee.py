# Author: Preethi_Gutha
# Date: 11/18
# Description: Employee class

class Employee:
    """
    A class to represent an employee.
    
    Attributes:
        _name (str): Employee's name
        _id_num (int): Employee's ID number
        _pay_rate (float): Employee's pay rate
    """
    def __init__(self, name, id_num, pay_rate):
        self._name = name
        self._id_num = id_num
        self._pay_rate = pay_rate

    def calcPay(self, hours_worked):
        return self._pay_rate * hours_worked

    # Getters and setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def id_num(self):
        return self._id_num

    @id_num.setter
    def id_num(self, id_num):
        self._id_num = id_num

    @property
    def pay_rate(self):
        return self._pay_rate

    @pay_rate.setter
    def pay_rate(self, pay_rate):
        self._pay_rate = pay_rate
