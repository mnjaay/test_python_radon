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

