import barcode
from barcode.writer import ImageWriter

msg = input("Enter the data to encode in the barcode: ").strip()

file_path = "P:\\DSA PYTHON\\barcode.png"

# Select the barcode format (Code128 supports alphanumeric data)
bar = barcode.get('code128', msg, writer=ImageWriter())

# Save the barcode as a PNG image
bar.save(file_path)

print("Barcode generated and saved to", file_path + ".png")
