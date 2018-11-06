class Employee:
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number


class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):
        Employee.__init__(self, employee_name, employee_number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

