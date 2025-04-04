class Item:
    def __init__(self, name, quantity, category, price):
        self.name = name
        self.quantity = quantity
        self.category = category
        self.price = price
        self.purchased = False

    def mark_as_purchased(self):
        self.purchased = True

    def __str__(self):
        return f"{'[✔]' if self.purchased else '[ ]'} {self.name} - {self.quantity} шт, {self.category}, {self.price} грн"


class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def update_item(self, name, new_name, new_quantity, new_category, new_price):
        for item in self.items:
            if item.name.lower() == name.lower():
                item.name = new_name
                item.quantity = new_quantity
                item.category = new_category
                item.price = new_price
                print("Товар оновлено!")
                return
        print("Товар не знайдено!")

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name.lower() != name.lower()]
        print("Товар видалено!")

    def mark_as_purchased(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                item.mark_as_purchased()
                print("Товар позначено як куплений!")
                return
        print("Товар не знайдено!")

    def filter_by_category(self, category):
        print(f"Товари у категорії: {category}")
        for item in self.items:
            if item.category.lower() == category.lower():
                print(item)

    def sort_items_by_name(self):
        def get_name(item):
            return item.name.lower()

        self.items.sort(key=get_name)

    def sort_items_by_category(self):
        def get_category(item):
            return item.category.lower()

        self.items.sort(key=get_category)

    def sort_items_by_price(self):
        def get_price(item):
            return item.price

        self.items.sort(key=get_price)

    def display_items(self):
        for item in self.items:
            print(item)


def main():
    shopping_list = ShoppingList()

    while True:
        print("\n1. Додати товар")
        print("2. Оновити товар")
        print("3. Видалити товар")
        print("4. Позначити товар як куплений")
        print("5. Фільтрувати за категорією")
        print("6. Сортувати (1 - за назвою, 2 - за категорією, 3 - за ціною)")
        print("7. Показати список")
        print("8. Вийти")
        choice = input("Виберіть опцію: ")

        if choice == "1":
            name = input("Назва товару: ")
            quantity = int(input("Кількість: "))
            category = input("Категорія: ")
            price = float(input("Ціна: "))
            shopping_list.add_item(Item(name, quantity, category, price))
        elif choice == "2":
            old_name = input("Назва товару для оновлення: ")
            new_name = input("Нова назва: ")
            new_quantity = int(input("Нова кількість: "))
            new_category = input("Нова категорія: ")
            new_price = float(input("Нова ціна: "))
            shopping_list.update_item(old_name, new_name, new_quantity, new_category, new_price)
        elif choice == "3":
            name = input("Назва товару для видалення: ")
            shopping_list.remove_item(name)
        elif choice == "4":
            name = input("Назва товару для позначення: ")
            shopping_list.mark_as_purchased(name)
        elif choice == "5":
            category = input("Категорія для фільтрації: ")
            shopping_list.filter_by_category(category)
        elif choice == "6":
            sort_choice = input("Оберіть спосіб сортування: ")
            if sort_choice == "1":
                shopping_list.sort_items_by_name()
            elif sort_choice == "2":
                shopping_list.sort_items_by_category()
            elif sort_choice == "3":
                shopping_list.sort_items_by_price()
        elif choice == "7":
            shopping_list.display_items()
        elif choice == "8":
            print("Вихід...")
            break
        else:
            print("Невідома команда!")


if __name__ == "__main__":
    main()


""" Програма для управління списком покупок. Програма дозволяє користувачам створювати список покупок, редагувати його, групувати товари за категоріями та відзначати придбані товари. Програма повинна реалізовувати наступний функціонал:
Додавання нового товару до списку з вказанням назви, кількості, категорії та орієнтовної ціни;
Оновлення інформації про товар (зміна кількості, назви, категорії тощо).
Видалення товару зі списку;
Позначення товару як купленого;
Фільтрація товарів за категоріями (наприклад: продукти, побутова хімія, електроніка тощо);
Реалізація різних способів сортування (за назвою, категорією, ціною);
"""