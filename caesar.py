import string

alphabet = string.ascii_lowercase

def decode(ciphertext, key=3):
	''' Return decoded string or dict using the specified key
		:brute: - use all possible rotations
    '''
	plaintext = ''

	if key == 'brute':
		print('Try to find the suitable rotation below: ')

		# Create dict {key:decode(key) x 25}
		brute = {key:decode(ciphertext, key=key) for key in range(1, 26)}

		# Print the dict if we are in main
		# [print(k, v) for k, v in brute.items()]
		return brute

	for letter in ciphertext:
		if letter in alphabet:
			plaintext += alphabet[(alphabet.find(letter) - key) % 26]
		elif letter.swapcase() in alphabet:
			plaintext += alphabet[(alphabet.find(letter.swapcase()) - key) % 26].swapcase()
		else:
			plaintext += letter
	return plaintext

def encode(plaintext, key=3):
	''' Return encoded string using the specified key '''
	ciphertext = ''
	for letter in plaintext:
		if letter in alphabet:
			ciphertext += alphabet[(alphabet.find(letter) + key) % 26]
		elif letter.swapcase() in alphabet:
			ciphertext += alphabet[(alphabet.find(letter.swapcase()) + key) % 26].swapcase()
		else:
			ciphertext += letter
	return ciphertext

