from barcode.writer import ImageWriter
from io import BytesIO
from PIL import Image
# from django.core.files.base import ContentFile

def generate_barcode(user_id):
    # generating the barcode 
    EAN = utils.get_barcode_class('ean13')
    ean = EAN(str(user_id).zfill(12), writer=ImageWriter())
    
    # saving barcode as png 
    buffer = BytesIO()
    ean.write(buffer, format = 'PNG')
    
    # return the buffer content as raw bytes
    return buffer.getvalue()

    # return content as special object for the ImageField 
    # return buffer.getvalue(), name=f'barcode_{user_id}.png')