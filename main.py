import caesar
from tkinter import *
from tkinter import messagebox as mb 
from tkinter import filedialog as fd

def encode_wrapper():
	''' Wrapper for the encode function '''
	ciphertextText.delete(1.0, END)
	text = plaintextText.get(1.0, END)
	key = int(keyEntry.get())
	ciphertextText.insert(1.0, caesar.encode(text, key))

def decode_wrapper():
	''' Wrapper for the decode function '''
	plaintextText.delete(1.0, END)
	text = ciphertextText.get(1.0, END)
	key = int(keyEntry.get())
	if check_brute_var.get():
		for k,v in caesar.decode(text, 'brute').items():
			plaintextText.insert(END, f'### Key: {k} ###\n')
			plaintextText.insert(END, v)
	else:
		plaintextText.insert(1.0, caesar.decode(text, key))

def insert_text():
	''' Open plaintext or ciphertext from file '''
	filename = fd.askopenfilename()
	with open(filename) as f:
		# If want to decode - insert to ciphertext else to plaintext
		if mb.askyesno('Encoding or Decoding?', 'Do you want to decode file?'):
			ciphertextText.delete(1.0, END)
			ciphertextText.insert(1.0, f.read())
		else:
			plaintextText.delete(1.0, END)
			plaintextText.insert(1.0, f.read())

def save_text():
	''' Save plaintext or ciphertext to file '''
	filename = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                        	   ("HTML files", "*.html;*.htm"),
                                               ("All files", "*.*")))
	with open(filename, 'w') as f:
		if mb.askyesno('Save Encoded or Decoded Text', 'Do you want to save decoded text?'):
			f.write(plaintextText.get(1.0, END))
		else:
			f.write(ciphertextText.get(1.0, END))


root = Tk()
root.title('Caesar Cipher Decoder and Encoder')
root.resizable(False, False)

lFrame = LabelFrame(root, text='Plaintext', padx=5, pady=5)
rFrame = LabelFrame(root, text='Ciphertext', padx=5, pady=5)

# Var for the checkbox
check_brute_var = BooleanVar()
check_brute_var.set(0)

lFrame.pack(side=LEFT)
plaintextText = Text(lFrame, width=50, height=20, font='Arial 12')
plaintextText.pack()


encodeButton = Button(lFrame, text='Encode', command=encode_wrapper)
encodeButton.pack(pady=5, padx=5, side=LEFT, fill=X, expand=1)
openButton = Button(lFrame, text='Open...', command=insert_text)
openButton.pack(pady=5, padx=5, side=LEFT, fill=X, expand=1)
saveButton = Button(lFrame, text='Save...', command=save_text)
saveButton.pack(pady=5, padx=5, side=LEFT, fill=X, expand=1)

rFrame.pack()
ciphertextText = Text(rFrame, width=50, height=20, font='Arial 12')
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