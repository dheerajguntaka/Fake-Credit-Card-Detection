""# Fake Credit Card Detection System Using Luhn Algorithm

from datetime import datetime

def luhn_algorithm(card_number: str) -> bool:
    """Validates credit card number using Luhn's Algorithm."""
    card_number = card_number.replace(' ', '')
    if not card_number.isdigit():
        return False

    total = 0
    reverse_digits = card_number[::-1]

    for idx, digit in enumerate(reverse_digits):
        n = int(digit)
        if idx % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return total % 10 == 0


def get_card_type(card_number: str) -> str:
    """Identifies the credit card type based on its number."""
    if card_number.startswith('4'):
        return 'Visa'
    elif card_number.startswith(('34', '37')):
        return 'American Express'
    elif card_number.startswith(('51', '52', '53', '54', '55')):
        return 'MasterCard'
    elif card_number.startswith('6011') or card_number.startswith(('65',)):
        return 'Discover'
    else:
        return 'Unknown'


def main():
    print("== Credit Card Validator ==")
    
    # User Inputs
    card_number = input("Enter the credit card number: ")
    amount = input("Enter the transaction amount: ")
    timestamp = input("Enter the transaction timestamp (YYYY-MM-DD HH:MM:SS): ")

    # Validation
    if luhn_algorithm(card_number):
        card_type = get_card_type(card_number)
        print("=== Transaction Details ===")
        print(f"Card Number: {card_number}")
        print(f"Card Type: {card_type}")
        print(f"Amount: ${amount}")
        print(f"Timestamp: {timestamp}")
        print("Status: Valid Card ✅")
    else:
        print("Invalid credit card number ❌")


if __name__ == "__main__":
    main()
""
