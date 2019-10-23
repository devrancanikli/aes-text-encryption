from AESCipher import AESCipher
from PIL import Image
from pyzbar.pyzbar import decode
import pyqrcode


class QRTest:

    def __init__(self, key, file_name):
        self.key = key
        self.file_name = file_name
        self.cipher = AESCipher(bytes(self.key, encoding='utf8'))

    def set_key(self, key):
        self.key = key
        self.cipher = AESCipher(bytes(self.key, encoding='utf8'))

    @staticmethod
    def create_qr(text, qr_name):
        text_qr = pyqrcode.create(text)
        text_qr.png(qr_name, scale=6)
        # text_qr.svg('uca-url.svg', scale=8)
        # text_qr.eps('uca-url.eps', scale=2)
        # print(text_qr.terminal(quiet_zone=1))
    
    @staticmethod
    def decode_qr(image_name):
        data = decode(Image.open(image_name))
        text = data[0].data
        # print(str(text, "utf8"))
        return text

    def encrypt(self, plain_text):
        encrypted = self.cipher.encrypt(plain_text)
        self.create_qr(encrypted, 'encrypted_'+self.file_name+'.png')
        return encrypted

    def decrypt(self, encrypted_text):
        decrypted = self.cipher.decrypt(encrypted_text)
        self.create_qr(decrypted, 'decrypted_'+self.file_name+'.png')
        return decrypted

