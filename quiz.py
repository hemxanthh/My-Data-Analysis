import requests
from datetime import datetime

def fetch_conversion(from_currency, to_currency, amount):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("result", None)
    except Exception as e:
        print("❌ Error fetching data:", e)
        return None

def save_history(from_currency, to_currency, amount, result):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("conversion_history.txt", "a") as file:
        file.write(f"[{now}] {amount} {from_currency} → {result:.2f} {to_currency}\n")

def currency_converter():
    print("💱 Welcome to Python Currency Converter!")
    print("-" * 40)

    while True:
        from_currency = input("From Currency (e.g., USD): ").upper()
        to_currency = input("To Currency (e.g., INR): ").upper()

        if not from_currency.isalpha() or not to_currency.isalpha():
            print("❗ Please enter valid 3-letter currency codes.")
            continue

        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("❗ Invalid amount. Please enter a number.")
            continue

        result = fetch_conversion(from_currency, to_currency, amount)

        if result is not None:
            print(f"✅ {amount} {from_currency} = {result:.2f} {to_currency}")
            save_history(from_currency, to_currency, amount, result)
        else:
            print("❌ Conversion failed. Please try again.")

        # Ask user if they want to convert again
        again = input("Convert again? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Thanks for using the Currency Converter!")
            break

# Run the converter
currency_converter()
