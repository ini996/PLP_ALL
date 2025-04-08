#To create a function name calculate_discount(price) that calculates the final
#price after applying a discount

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
#Divide the percentage discount by 100
        discount = float ((discount_percent)/100)
#Calculate the final price by substarcting the disounted amount from the original price
        sales = price -  (discount * price)
        return sales
    else:
        return price

# Promt the user for the original price and discount percentage
price = float (input ('Enter the original price: '))
discount_percent = float(input('Enter the discount percentage: '))

#To calculate the final price using the function
sales = calculate_discount(price, discount_percent)

#Print the final price
print(f'Final price after calculating discount is: {sales}')
