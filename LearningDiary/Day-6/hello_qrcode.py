import qrcode
from qrcode.image.pure import PymagingImage

img = qrcode.make('Hello Python', image_factory=PymagingImage)

fout = open('test.png','wb')
img.save(fout)
fout.close()