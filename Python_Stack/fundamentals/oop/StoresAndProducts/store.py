from product import Product


class Store:
    def __init__(self, store_name):
        self.name = store_name
        self.products_list = []

    def add_product(self, new_product):
        if new_product not in self.products_list:
            self.products_list.append(new_product)

    def sell_product(self, id_number):
        if id_number < len(self.products_list):
            del self.products_list[id_number]

    def inflation(self, percent_increase):
        for product in self.products_list:
            product.update_price(percent_increase, True)

    def set_clearance(self, category, percent_decrease):
        for product in self.products_list:
            if product.category == category:
                product.update_price(percent_decrease, False)


if __name__ == '__main__':
    "Lets Test this code"
    store_name = input("What is the name of your store --> ")
    store = Store(store_name)
    number_of_products = int(input("How many products in the store --> "))
    for _ in range(number_of_products):
        product_name = input("Nanme of the product --> ")
        product_category = input("Product Category --> ")
        product_price = float(input("Product Price --> "))
        store.add_product(Product(product_name, product_price, product_category))

    store.sell_product(2)
    store.inflation(15)

    for product in store.products_list:
        print(product)

    store.set_clearance("food", 3)

    for product in store.products_list:
        print(product)
