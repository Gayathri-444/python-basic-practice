#problem : write a python program to calculate the CGST and SGST for a product CGST=9% and SGST = 9% and print the total.

def calculate_gst(price):
    cgst_rate = 9 / 100  
    sgst_rate = 9 / 100  
    
    cgst = price * cgst_rate
    sgst = price * sgst_rate
    total_price = price + cgst + sgst
    
    return cgst, sgst, total_price

price = float(input("Enter the product price: "))
cgst, sgst, total_price = calculate_gst(price)


print("CGST: ₹", round(cgst, 2))
print("SGST: ₹", round(sgst, 2))
print("Total Price: ₹", round(total_price, 2))
