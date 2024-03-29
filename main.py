from QRCipher import QRCipher

if __name__ == '__main__': 

    user1 = QRCipher('`?.F(fHbN6XK|j!t', 'user1')

    encrypted1 = user1.encrypt("I <3 Computer Science")
    print("Encrypted: " + encrypted1.data.decode())
    decoded_qr = user1.decode_qr_image("encrypted_user1.png")

    print("Decoded QR_1: " + str(decoded_qr, 'utf8'))
    decrypted1 = user1.decrypt(encrypted1.data.decode())
    print("Decrypted_1: " + decrypted1.data.decode())

    user2 = QRCipher('denemeHbN6XK|i!t', 'user2')
    user2.set_key('`?.F(fHbN6XK|j!t')

    decoded_qr2 = user2.decode_qr_image("encrypted_user1.png")
    print("Decoded QR_2: " + str(decoded_qr2, 'utf8'))
    decrypted2 = user2.decrypt(encrypted1.data.decode())
    print("Decrypted_2: " + decrypted2.data.decode())

