import qrcode

# Website URL
website = "https://bandhanbazzar.vercel.app/map.html"

# Create QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(website)
qr.make(fit=True)

# Generate Image
img = qr.make_image(fill_color="black", back_color="white")

# Save Image
img.save("bandhanbazaar_stall_qr.png")

print("✅ QR Code generated successfully!")