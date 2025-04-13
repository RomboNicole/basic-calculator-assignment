def calculate_discount(price, discount_percent):
    print(f"Original price: {price}")
    print(f"Discount percentage: {discount_percent}%")
    
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after discount
        final_price = price - discount_amount
        print(f"Discount applied: {discount_amount:.2f}")
        return final_price
    else:
        # Return the original price if discount is less than 20%
        print("No discount applied, returning original price.")
        return price

# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and store the result
final_price = calculate_discount(price, discount_percent)

# Print the final price after applying the discount or the original price
print(f"The final price is: {final_price:.2f}")

