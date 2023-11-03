class Coffee:
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if self._name == None:
            if isinstance(name, str) and len(name) >= 3:
                self._name = name
        
    def orders(self):
        all_orders = []
        for orders in Order.all:
            if orders.coffee == self:
                all_orders.append(orders)
        return all_orders
        
    
    def customers(self):
        all_customers = set()
        for orders in Order.all:
            if orders.coffee == self:
                all_customers.add(orders.customer)
        return list(all_customers)
    
    def num_orders(self):
        all_orders = 0
        for orders in Order.all:
            if orders.coffee == self:
                all_orders += 1
        return all_orders
    
    def average_price(self):
        price_sum = 0
        for orders in Order.all:
            if orders.coffee == self:
                price_sum += orders.price
        average = price_sum / self.num_orders()
        return average

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(1, 16):
            self._name = name
        
    def orders(self):
        all_orders = []
        for orders in Order.all:
            if orders.customer == self:
                all_orders.append(orders)
        return all_orders
    
    def coffees(self):
        all_coffees = set()
        for orders in Order.all:
            if orders.customer == self:
                all_coffees.add(orders.coffee)
        return list(all_coffees)
    
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = None
        self.price = price
        self.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if self._price == None:
            if isinstance(price, float) and price in range(1,11):
                self._price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee

