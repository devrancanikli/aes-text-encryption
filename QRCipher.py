from AESCipher import AESCipher
from PIL import Image
from pyzbar.pyzbar import decode
import pyqrcode


class QRCipher:

    def __init__(self, key, file_name):
        self.key = key
        self.file_name = file_name
        self.cipher = AESCipher(bytes(self.key, encoding='utf8'))

    def set_key(self, key):
        self.key = key
        self.cipher = AESCipher(bytes(self.key, encoding='utf8'))

    @staticmethod
    def create_qr(text, qr_name):
        qr_code = pyqrcode.create(text)
        qr_code.png(qr_name, scale=6)
        # text_qr.svg('uca-url.svg', scale=8)
        # text_qr.eps('uca-url.eps', scale=2)
        # print(text_qr.terminal(quiet_zone=1))
        return qr_code
    
    @staticmethod
    def decode_qr_image(image_name):
        data = decode(Image.open(image_name))
        text = data[0].data
        return text

    def encrypt(self, plain_text):
        encrypted_text = self.cipher.encrypt(plain_text)
        return self.create_qr(encrypted_text, 'encrypted_'+self.file_name+'.png')

    def decrypt(self, encrypted_text):
        decrypted_text = self.cipher.decrypt(encrypted_text)
        return self.create_qr(decrypted_text, 'decrypted_'+self.file_name+'.png')
