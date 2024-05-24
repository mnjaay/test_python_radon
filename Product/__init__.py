class Product:
    # Création d'une classe Product
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Méthode pour retourner le nom
    def get_name(self):
        return self.name

    # Méthode pour retourner le prix
    def get_price(self):
        return self.price

    # Méthode pour retourner la quantité
    def get_quantity(self):
        return self.quantity

    # Méthode pour modifier la quantité
    def set_quantity(self, qty):
        self.quantity = qty

    # Méthode pour représenter l'objet sous forme de chaîne
    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
