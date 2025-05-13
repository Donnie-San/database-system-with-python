from inventory import InventoryManager

def main():
    ims = InventoryManager()

    while (True):
        print("INVENTORY MANAGEMENT SYSTEM")
        print("1. Display tables")
        print("2. Add product")
        print("3. Update stock")
        print("4. Show product with low stock")
        print("5. Exit")
        choice = int(input("Choice (1/2/3/4/5): "))
        match (choice):
            case 1:
                table = input("Enter a table (products/transactions): ")
                print(ims.display_table(table))

            case 2:
                product_name = input("Enter product name    :")
                category = input("Enter category:    :")
                stock_quantity = int(input("Enter stock quantity    :"))
                price = float(input("Enter price    :"))
                ims.add_product(product_name, category, stock_quantity, price)

            case 3:
                product_id = int(input("Enter product id    :"))
                quantity = int(input("Enter quantity    :"))
                transaction_type = input("Enter transaction type ('in'/'out'):")
                ims.update_stock(product_id, quantity, transaction_type)

            case 4:
                threshold = int(input("Enter threshold: "))
                print(ims.get_low_stock_items(threshold))

            case 5:
                break

    ims.close_connection()

if __name__ == '__main__':
    main()