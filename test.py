from QRTest import QRTest

user1 = QRTest('`?.F(fHbN6XK|j!t', 'user1')

encrypted1 = user1.encrypt("anahtarlar nerde")
print("Encrypted: " + encrypted1)
decoded_qr = user1.decode_qr("encrypted_user1.png")

print("Decoded QR_1: " + str(decoded_qr, 'utf8'))
decrypted1 = user1.decrypt(encrypted1)
print("Decrypted_1: " + decrypted1)

print()

user2 = QRTest('denemeHbN6XK|i!t', 'user2')
user2.set_key('`?.F(fHbN6XK|j!t')

decoded_qr2 = user2.decode_qr("encrypted_user1.png")
print("Decoded QR_2: " + str(decoded_qr2, 'utf8'))
decrypted2 = user2.decrypt(encrypted1)
print("Decrypted_2: " + decrypted2)


