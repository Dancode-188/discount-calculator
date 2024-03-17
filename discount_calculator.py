import colorama
from colorama import Fore, Style

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price: The original price of the item.
        discount_percent: The discount percentage to be applied.

    Returns:
        The final price after applying the discount.
        If the discount percent is less than 20, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def rainbow_text(text):
    """
    Creates a rainbow-colored text by cycling through different colors for each character.

    Args:
        text: The text to be colored.

    Returns:
        Rainbow-colored text with alternating colors for each character.
    """
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    colored_text = ""
    i = 0
    for char in text:
        colored_text += colors[i % len(colors)] + char
        i += 1
    return colored_text + Style.RESET_ALL

if __name__ == "__main__":
    # Initialize colorama for colored text output
    colorama.init()

    print(rainbow_text("Welcome to the Discount Calculator!"))

    # Main loop for the discount calculator
    while True:
        try:
            price = float(input("Enter the original price of the item: "))
            discount_percent = float(input("Enter the discount percentage: "))

            final_price = calculate_discount(price, discount_percent)

            # Display the final price with or without discount
            if final_price == price:
                print(f"The final price is: {Fore.GREEN}${final_price:.2f}{Style.RESET_ALL} (No discount applied)")
            else:
                print(f"The final price after {Fore.YELLOW}{discount_percent:.2f}%{Style.RESET_ALL} discount is: {Fore.GREEN}${final_price:.2f}{Style.RESET_ALL}")

            # Ask the user if they want to calculate another discount
            another_calculation = input("Do you want to calculate another discount? (y/n): ")
            if another_calculation.lower() != "y":
                break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a valid number." + Style.RESET_ALL)
