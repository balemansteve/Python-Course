'''
La abstracción se logra con clases abstractas que definen métodos obligatorios para sus subclases.
'''

from abc import ABC, abstractmethod  # Importamos clases abstractas

# Clase abstracta Payment
class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass  # Método abstracto

# Subclase CreditCardPayment
class CreditCardPayment(Payment):
    def process_payment(self):
        print("Processing credit card payment...")

# Subclase PayPalPayment
class PayPalPayment(Payment):
    def process_payment(self):
        print("Processing PayPal payment...")

# Función para procesar un pago
def process_payment_method(payment_method):
    payment_method.process_payment()

# Crear instancias de métodos de pago
credit_card = CreditCardPayment()
paypal = PayPalPayment()

# Procesar pagos
process_payment_method(credit_card)
process_payment_method(paypal)
