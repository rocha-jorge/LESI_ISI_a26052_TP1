import qrcode

# Link a ser convertido em QR Code
link = "https://github.com/rocha-jorge/LESI_ISI_a26052_TP1.git"

# Gerar o QR Code
qr = qrcode.make(link)

# Guardar o QR Code em PNG
qr.save("qrcode_26052_videos.png")
