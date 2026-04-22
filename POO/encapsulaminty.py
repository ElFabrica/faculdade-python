class Employee:
    def __init__(self, name, role, time_worked_value):
        self.name = name
        self.role = role
        self.time_worked_value = time_worked_value
        self.__worked_time = 0
        self.__salary = 0

    def register_time_worked(self):
        self.__worked_time += 1

    def calc_salary(self):
        self.__salary = self.__salary * self.time_worked_value

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, new_salary):
        raise ValueError("Impossível alterar salário diretamente. Use a funcao calcula_salario()")


pedro = Employee('Pedro', 'Gerente de vendas', 50)
pedro.salary = 100000

print(pedro.salary)