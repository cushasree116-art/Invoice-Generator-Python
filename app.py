from fpdf import FPDF

print("===== INVOICE GENERATOR =====")

customer_name = input("Enter Customer Name: ")
customer_phone = input("Enter Phone Number: ")

product_name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Item: "))

total = quantity * price

pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "INVOICE", ln=True, align="C")

pdf.ln(10)

pdf.set_font("Arial", size=12)

pdf.cell(200, 10, f"Customer Name: {customer_name}", ln=True)
pdf.cell(200, 10, f"Phone Number: {customer_phone}", ln=True)

pdf.ln(5)

pdf.cell(200, 10, f"Product Name: {product_name}", ln=True)
pdf.cell(200, 10, f"Quantity: {quantity}", ln=True)
pdf.cell(200, 10, f"Price Per Item: Rs.{price}", ln=True)

pdf.ln(5)

pdf.cell(200, 10, f"Total Amount: Rs.{total}", ln=True)

pdf.ln(10)

pdf.cell(200, 10, "Thank You For Your Purchase!", ln=True)

pdf.output("invoice.pdf")

print("\nInvoice Generated Successfully!")
print("Customer Name :", customer_name)
print("Product Name  :", product_name)
print("Quantity      :", quantity)
print("Price         :", price)
print("Total Amount  :", total)
print("PDF saved as invoice.pdf")