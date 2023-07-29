class Restaurant:
    def __init__(self, name ) -> None:
        self.name = name
        self.chef = None
        self.server = None
        self.manager = None
        self.menu = []
        self.revenue = 0
        self.expense = 0
        self.balance = 0
        self.profit = 0

    def add_employee(self, employee_type, empployee):
        if employee_type == "chep":
            self.chef = empployee
        elif employee_type == 'server':
            self.server = empployee
        elif employee_type == 'manager':
            self.manager = empployee

    def recive_payment(self, order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        
    def pay_expense(self, amount, description):
        if amount <self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expense {amount} for {description}')
        else:
            print(f'not enough money to pay {amount}')

    
    def pay_salary(self, employee):
        if employee.salary < self.balance:
            employee.receive_salary()