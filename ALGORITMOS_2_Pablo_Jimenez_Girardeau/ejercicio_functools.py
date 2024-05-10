import functools

class SimpleOperations:
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""
        if not (0 <= discount <= 1):
            raise ValueError("El descuento debe estar entre 0 y 1.")
        return price * (1 - discount)

    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""
        if not (0 <= tax_rate <= 1):
            raise ValueError("El impuesto debe estar entre 0 y 1.")
        return price * (1 + tax_rate)

# Crear una instancia de SimpleOperations
operations = SimpleOperations()

# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
twenty_percent_discount = functools.partial(operations.apply_discount, discount=0.20)
vat_tax = functools.partial(operations.calculate_tax, tax_rate=0.21)

# Usar las funciones preconfiguradas
price_with_discount = twenty_percent_discount(100)  # Precio original: 100
price_with_vat = vat_tax(100)                       # Precio original: 100


precio_original = 100
print(f"Precio original: {precio_original}")
print(f"Precio después de aplicar 20% de descuento: {price_with_discount}")
print(f"Precio después de agregar un impuesto del 21%: {price_with_vat}")
