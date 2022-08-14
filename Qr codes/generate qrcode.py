import qrcode
link=input("Enter your link : ")
img = qrcode.make(link)

name=input("Name of qr code  : ")
img.save(name+".png",'PNG')
