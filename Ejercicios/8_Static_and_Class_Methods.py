'''
Métodos estáticos: no dependen de la instancia ni de la clase, actúan como funciones regulares dentro del contexto de una clase.
Métodos de clase: reciben como primer argumento la clase (cls) y se usan para modificar o crear instancias de la clase.
'''

# Clase Calculator
class Calculator:
    def __init__(self, default_value=0):
        self.value = default_value  # Valor predeterminado

    @staticmethod
    def add(a, b):
        # Método estático para sumar dos números
        return a + b

    @classmethod
    def create_default(cls):
        # Método de clase para crear una instancia predeterminada
        return cls(default_value=100)

# Uso del método estático
result = Calculator.add(5, 7)
print(f"Static method result: {result}")

# Uso del método de clase
default_calculator = Calculator.create_default()
print(f"Class method result: Default value is {default_calculator.value}")
