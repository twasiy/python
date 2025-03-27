import  qrcode 
import qrcode.constants
qr = qrcode.QRCode( version = 1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,border=2)

qr.add_data(input('Enter your adress:'))
qr.make(fit =True)
img = qr.make_image()
img.save('xyz.png')