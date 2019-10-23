import pyqrcode


def create_qr(text, qr_name):
    text_qr = pyqrcode.create(text)
    # text_qr.svg('uca-url.svg', scale=8)
    # text_qr.eps('uca-url.eps', scale=2)
    text_qr.png(qr_name, scale=6)
    # print(text_qr.terminal(quiet_zone=1))
