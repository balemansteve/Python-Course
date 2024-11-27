'''
La sobrescritura permite redefinir un método de una clase base en una subclase para cambiar su comportamiento.
'''

# Clase base Employee
class Employee:
    def __init__(self, name, salary):
        self.name = name  # Nombre del empleado
        self.salary = salary  # Salario del empleado

    def get_details(self):
        # Método que imprime los detalles del empleado
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

# Subclase Manager
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        # Inicializamos los atributos de la superclase
        super().__init__(name, salary)
        self.team_size = team_size  # Tamaño del equipo

    def get_details(self):
        # Sobrescribimos el método para incluir el tamaño del equipo
        print(f"Manager Name: {self.name}, Salary: {self.salary}, Team Size: {self.team_size}")

# Crear instancias de Employee y Manager
employee = Employee("John", 50000)
manager = Manager("Alice", 80000, 10)

# Llamar a get_details()
employee.get_details()
manager.get_details()
