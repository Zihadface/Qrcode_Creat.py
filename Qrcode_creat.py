import qrcode as qr
data = input("Enter your qrcode data.(link,password,number):")
img = qr.make(data)
img.save('data.png')
