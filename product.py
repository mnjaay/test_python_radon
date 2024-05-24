import unittest

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

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.get_name() == product_name:
                self.products.remove(product)
                return
        print("Product not found")

    def update_quantity(self, product_name, new_quantity):
        for product in self.products:
            if product.get_name() == product_name:
                product.set_quantity(new_quantity)
                return
        print("Product not found")

    def get_product_price(self, product_name):
        for product in self.products:
            if product.get_name() == product_name:
                return product.get_price()
        print("Product not found")
        return None

    def sell_product(self, product_name, quantity):
        for product in self.products:
            if product.get_name() == product_name:
                if quantity <= product.get_quantity():
                    product.set_quantity(product.get_quantity() - quantity)
                    return True
                else:
                    return False
        print("Product not found")
        return False

    def get_total_stock_value(self):
        total = 0
        for product in self.products:
            total = total + (product.get_price() * product.get_quantity())
        return total


    def get_available_products(self):
        for product in self.products:
            if product.get_quantity() >0:
                print(product)





class TestProductStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.store.add_product(Product("bonbon", 1200.0, 50))
        self.store.add_product(Product("Maad", 500.0, 50))

    def test_get_product_price(self):
        self.assertEqual(self.store.get_product_price("bonbon"), 1200.0)

    def test_sell_product(self):
        self.assertTrue(self.store.sell_product("bonbon", 10))
        self.assertFalse(self.store.sell_product("bonbon", 51))

    def test_remove_product(self):
        self.store.remove_product("Maad")
        self.assertNotIn("Daakar", [product.name for product in self.store.products])


