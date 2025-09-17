import pyqrcode

url = "Welcome to LBRCE"
k = pyqrcode.create(url)
k.svg("LBRCE.svg", scale=20)
