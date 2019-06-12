from tkinter import *
import caesar

'''
	TODO: Open and Save buttons
	TODO: Hints that left textbox is plaintext and right text is ciphertext
'''

def encode_wrapper():
	ciphertextText.delete(1.0, END)
	text = plaintextText.get(1.0, END)
	key = int(keyEntry.get())
	ciphertextText.insert(1.0, caesar.encode(text, key))

def decode_wrapper():
	plaintextText.delete(1.0, END)
	text = ciphertextText.get(1.0, END)
	key = int(keyEntry.get())
	if check_brute_var.get():
		for k,v in caesar.decode(text, 'brute').items():
			plaintextText.insert(END, f'### Key: {k} ###\n')
			plaintextText.insert(END, v)
	else:
		plaintextText.insert(1.0, caesar.decode(text, key))

root = Tk()
root.title('Caesar Cipher Decoder and Encoder')
root.resizable(False, False)

lFrame = Frame(root, width=50, height=20)
rFrame = Frame(root, width=50, height=20)

# Vars for radioboxes declaration
check_brute_var = BooleanVar()
check_brute_var.set(0)

lFrame.pack(side=LEFT)
plaintextText = Text(lFrame, width=50, height=20, font='Arial 16')
plaintextText.pack()


encodeButton = Button(lFrame, text='Encode', command=encode_wrapper)
encodeButton.pack(pady=5, padx=5, side=LEFT, fill=X, expand=1)
openButton = Button(lFrame, text='Open...', command=lambda: print('open'))
openButton.pack(pady=5, padx=5, side=LEFT, fill=X, expand=1)
saveButton = Button(lFrame, text='Save...', command=lambda: print('save'))
saveButton.pack(pady=5, padx=5, side=LEFT, fill=X, expand=1)

rFrame.pack()
ciphertextText = Text(rFrame, width=50, height=20, font='Arial 16')
ciphertextText.pack()

decodeButton = Button(rFrame, text='Decode', command=decode_wrapper)
decodeButton.pack(pady=5, padx=5, side=LEFT, fill=X, expand=1)
Label(rFrame, text='Key:', width=5).pack(pady=5, padx=5, side=LEFT)
keyEntry = Entry(rFrame, width=5)
keyEntry.insert(1, 3) # Default Key: 3
keyEntry.pack(pady=5, padx=5, side=LEFT)
dec_key_check = Checkbutton(rFrame, text='Bruteforce', variable=check_brute_var, offvalue=0, onvalue=1)
dec_key_check.pack(pady=5, padx=5, side=LEFT)

root.mainloop()