from Crypto.Cipher import AES
import encrypt
import base64
import os
def decryption(encryptedString):
	PADDING = '{'
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	#Key is FROM the printout of 'secret' in encryption
	#below is the encryption.
	encryption = encryptedString
	key = secret
	cipher = AES.new(key)
	decoded = DecodeAES(cipher, encryption)
	print decoded


decryption("Gs70aei1FgM9xVmE/Re2j1lhnGe3OI8duIphphX/NIQ=")
