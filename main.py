print ("Currency Converter")

EXCHANGE_RATES ={
    "USD": 1.0,
   "EUR": 0.92,
    "GBP": 0.79,
    "INR": 83.50,
    "JPY": 155.00,
    "CAD": 1.36,
    "AUD": 1.52,
    "CHF": 0.91,
    "CNY": 7.24,
    "SGD": 1.35
}


transaction_history = []


def display_supported_currencies():
    """Outputs all currently supported currency codes."""
    print("\n=== Supported Currencies ===")
    for code in EXCHANGE_RATES:
        print(f"- {code}");


def convert_currency(amount: float, source: str, target: str) -> float:
    
    amount_in_usd = amount / EXCHANGE_RATES[source]
    return amount_in_usd * EXCHANGE_RATES[target]


def process_conversion():
    """Handles user input, validates edge cases, computes output, and logs history."""
    print("\n--- Currency Conversion ---")
    display_supported_currencies()

    
    source = input("\nEnter source currency code (e.g., USD): ").strip().upper()
    if source not in EXCHANGE_RATES:
        print("[ERROR] Unsupported source currency code. Please choose from the list.")
        return

    
    target = input("Enter target currency code (e.g., INR): ").strip().upper()
    if target not in EXCHANGE_RATES:
        print("[ERROR] Unsupported target currency code. Please choose from the list.")
        return


    try:
        amount = float(input("Enter amount to convert: "))
        if amount <= 0:
            print("[ERROR] Conversion amount must be greater than zero.")
            return
    except ValueError:
        print("[ERROR] Invalid numerical input. Please enter a valid number.")
        return

    result = convert_currency(amount, source, target)
    record = f"{amount:.2f} {source} -> {result:.2f} {target}"

    print(f"\n[SUCCESS] Conversion Result: {record}")
    
    
    transaction_history.append(record)






def main():
    """Main execution loop controlling application workflow and loop termination."""
    while True:
        print("\n=======================================")
        print("  COMMAND-LINE CURRENCY EXCHANGE SYSTEM ")
        print("=======================================")
        print("1. Convert Currency")
        print("2. Display Supported Currencies")
        print("3. View Session History")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            process_conversion()
        elif choice == "2":
            display_supported_currencies()
        elif choice == "3":
            view_history()
        elif choice == "4":
            print("\nExiting system. Thank you for using Currency Exchange CLI!")
            sys.exit(0)
        else:
            print("[ERROR] Invalid choice. Please select an option between 1 and 4.")


if __name__ == "__main__":
    main()
