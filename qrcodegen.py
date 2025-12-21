import qrcode
url = input("Enter the url :").strip()
file_path="P:\\DSA PYTHON\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img=qr.make_image()
img.save(file_path)

print("QR code generated and saved to", file_path)