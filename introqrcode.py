import qrcode

data = """ Name : Himani Dhakal
 Email : himanidhakal16@gmail.com
 Phone : 9769002556
 Address : Kathmandu, Nepal
 Github : himanidhakal16"""

img = qrcode.make(data)
type(img)  # qrcode.image.pil.PilImage
img.save("himani.png")