# Supermarket Billing System

products = {
    "apple": {"price": 30, "stock": 50},
    "banana": {"price": 10, "stock": 100},
    "milk": {"price": 50, "stock": 20},
    "bread": {"price": 25, "stock": 30}
}

cart = {}

def show_products():
    print("\n📦 Available Products:")
    print("-" * 30)
    for item, info in products.items():
        print(f"{item.title()} - ₹{info['price']} (Stock: {info['stock']})")
    print()

def add_to_cart():
    item = input("Enter product name: ").lower()
    if item in products:
        quantity = int(input("Enter quantity: "))
        if quantity <= products[item]["stock"]:
            cart[item] = cart.get(item, 0) + quantity
            products[item]["stock"] -= quantity
            print(f"✅ Added {quantity} x {item} to cart.")
        else:
            print("❌ Not enough stock.")
    else:
        print("❗ Product not found.")

def view_cart():
    print("\n🛒 Your Cart:")
    print("-" * 30)
    total = 0
    for item, qty in cart.items():
        price = products[item]["price"]
        cost = price * qty
        total += cost
        print(f"{item.title()} x {qty} = ₹{cost}")
    print(f"Total: ₹{total}")
    print()

def checkout():
    view_cart()
    print("✅ Thank you for shopping!")
    # Optional: Save to file
    with open("receipt.txt", "w") as file:
        file.write("🧾 Supermarket Receipt\n")
        file.write("-" * 30 + "\n")
        for item, qty in cart.items():
            cost = products[item]["price"] * qty
            file.write(f"{item.title()} x {qty} = ₹{cost}\n")
        file.write(f"\nTotal: ₹{total}\n")
    print("🧾 Receipt saved to 'receipt.txt'")

def main():
    while True:
        print("\n--- Python Mart Menu ---")
        print("1. Show Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            show_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            checkout()
            break
        elif choice == '5':
            print("👋 Thank you! Visit again.")
            break
        else:
            print("❌ Invalid choice. Try again.")

main()
