import unittest
from Product import Product
from Store import Store

#help(unittest)
class TestProductStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()
        self.store.add_product(Product("bonbon",1200.0,50))
        self.store.add_product(Product("Maad",500.0,50))



    def test_get_product_price(self):
        self.assertEqual(self.store.get_product_price("bonbon"),1200.0)

    def test_sell_product(self):
        self.assertTrue(self.store.sell_product("bonbon",10))
        self.assertFalse(self.store.sell_product("bonbon",51))

    def test_remove_product(self):
        self.store.remove_product("Maad")
        self.assertNotIn("Daakar",[product.name for product in self.store.products])


if __name__ == '__main__' :
    unittest.main()
