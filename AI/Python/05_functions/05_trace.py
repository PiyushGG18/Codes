def calculate_vat (price, vat_rate):
    return price * (100 + vat_rate)/100

orders = [100, 150, 200]

for order in orders:
    final_amount = calculate_vat(order, 10)
    print(f"Original: {order}, Final with VAT: {final_amount}")