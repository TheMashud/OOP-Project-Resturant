from Menu import Pizza, Burger, Drinks, Menu

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
    coffee = Drinks('mocha', 300, False)
    menu.add_menu_item('drinks', coffee)
    
    #Show Menu
    menu.show_menu()





#call the main
if __name__ == '__main__':
    main()