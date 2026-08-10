chai_type = "Ginger Tea"
customer_name = "Priya"

print(f"Order for {customer_name}: {chai_type} please!")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"reverse string: {chai_description[::-1]}")

label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")