from AESCipher import AESCipher
from QRGenerator import create_qr
from PIL import Image
from pyzbar.pyzbar import decode


class QRTest:

    def __init__(self, key, file_name):
        self.key = key
        self.file_name = file_name
        self.cipher = AESCipher(bytes(self.key, encoding='utf8'))

    def set_key(self, key):
        self.key = key
        self.cipher = AESCipher(bytes(self.key, encoding='utf8'))

    @staticmethod
    def decode_qr(image_name):
        data = decode(Image.open(image_name))
        text = data[0].data
        # print(str(text, "utf8"))
        return text

    def encrypt(self, plain_text):
        encrypted = self.cipher.encrypt(plain_text)
        create_qr(encrypted, 'encrypted_'+self.file_name+'.png')
        return encrypted

    def decrypt(self, encrypted_text):
        decrypted = self.cipher.decrypt(encrypted_text)
        create_qr(decrypted, 'decrypted_'+self.file_name+'.png')
        return decrypted







