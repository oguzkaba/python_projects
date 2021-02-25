#Generate QR

# import pyqrcode

# qr=pyqrcode.create('oguzkaba')
# qr.png('deneme_qr.jpg',8)


#Read QR

from pyzbar.pyzbar import decode
from PIL import Image
import time

zaman=time.time()
d=decode(Image.open('imag/output1.jpg'))
print(str(time.time()-zaman))
print(d[0].data.decode('ascii'))