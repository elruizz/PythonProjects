from Crypto.Cipher import AES

import base64

import os

def encryptpass(privateInfo):
	#32 bytes = 256 bits
	#16 = 128 bits
	# the block size for cipher obj, can be 16 24 or 32. 16 matches 128 bit.
	BLOCK_SIZE = 16
	# the character used for padding
	# used to ensure that your value is always a multiple of BLOCK_SIZE
	PADDING = '{'
	# function to pad the functions. Lambda
	# is used for abstraction of functions.
	# basically, its a function, and you define it, followed by the param
	# followed by a colon,
	# ex = lambda x: x+5
	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	# encrypt with AES, encode with base64
	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
	# generate a randomized secret key with urandom
	secret = os.urandom(BLOCK_SIZE)
	print 'Encryption key:',secret
	# creates the cipher obj using the key
	cipher = AES.new(secret)
	# encodes you private info!
	encoded = EncodeAES(cipher, privateInfo)
	print 'Encrypted string:', encoded


encryptpass("@blee@blaahh@secret@message@")
