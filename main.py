from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from Userss import Chef, Customer, Server, Manager
from order import Order

def main():
    menu = Menu()
    pizza_1 = Pizza('Shutki pizz', 600, 'learge', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('alor bortar pizz', 400, 'large',['potato', 'onion'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('dal pizza', 500, 'large',['dal', 'piyazo'])
    menu.add_menu_item('pizza', pizza_3)

    # add burger to the menu
    burger_1 = Burger('naga burger', 1000, 'chicken',['bread', 'chili'])
    menu.add_menu_item('burger',burger_1)
    burger_2 = Burger('beff burger', 2000, 'beff',['goru', 'haddi'])
    menu.add_menu_item('burger',burger_2)

    # add drinks to the menu
    coke = Drinks('coke', 50, True)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('Mocha cofee', 300, False)
    menu.add_menu_item('drinks', coffee)
    
    #Show Menu
    # menu.show_menu()

    #add employees
    restaurant = Restaurant("Sai Baba Restaurant",2000, menu)
    manager = Manager('Mashudul hoque', 18, 'mashud@mail.com','ctg',30000, 'Jan 01 2022', "core")
    restaurant.add_employee('manager', manager)

    chef = Chef('Siddik baburchi', 82, 'siddk@maill.com', 'baskali',2000,'fab 02 2022', 'chef', 'evreything')
    restaurant.add_employee('chef', chef)

    server = Server('alam bodda', 19, 'bodda@mail.com', 'baskali', 5000, 'jan 2, 2022', 'staff' )
    restaurant.add_employee('server', server)

    # restaurant.Show_employees()

    #customer 1 placing an order
    customer_1 = Customer('opi',12, 'opi@com','ctg', 10000)
    order_1 = Order(customer_1, [pizza_3, coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)
    #custome 1 paying for order_1
    restaurant.recive_payment(order_1, 2000, customer_1)
    print(f'revenue and balace after first cudtomer ', restaurant.revenue, restaurant.balance)

   #customer 2 placing an order
    customer_2 = Customer('rafi',12, 'opi@com','ctg', 50000)
    order_2 = Order(customer_2, [pizza_2, burger_2, coke, coffee])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)
    #custome 1 paying for order_1
    restaurant.recive_payment(order_2, 4000, customer_2)
    print(f'revenue and balace after 2nd cudtomer ', restaurant.revenue, restaurant.balance)

    #pay rent
    restaurant.pay_expense(restaurant.rent, 'Rent')
    print(f'After Rent ', restaurant.revenue, restaurant.expense)

    restaurant.pay_salary(chef)
    print(f'After salary ', restaurant.revenue, restaurant.balance, restaurant.expense)









#call the main
if __name__ == '__main__':
    main()