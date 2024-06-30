from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import pyperclip

def result_get(num, text):
    """type num: if 1 when is binary or if 2 when is text"""
    if num == 1:
        pr = messagebox.askyesno('Successfully!', f'Your binary is {text}\nCopy?')
        print(pr)
        if pr:
            pyperclip.copy(text)
    if num == 2:
        pr = messagebox.askyesno('Successfully!', f'Your text is {text}\nCopy?')
        print(pr)
        if pr:
            pyperclip.copy(text)

def real_text2bin(text):
    """Text string to Binary"""
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

def real_bin2text(binary):
    """Binary string to text"""
    text = ''.join(chr(int(char, 2)) for char in binary.split())
    return text

tk = Tk()
tk.title('Bin2Text & Text2Bin')
tk.resizable(True, True)

bin2str_TE = Entry(tk, justify='left')
def bin2text():
    result = real_bin2text(bin2str_TE.get())
    print(result)
    result_get(1, result)
bin2str_BTN = Button(tk, text='Convert to Text', command=bin2text)
bin2str_TE.grid(row=0, column=2)
bin2str_BTN.grid(row=1, column=2)

str2bin_TE = Entry(tk)
def text2bin():
    result = real_text2bin(str2bin_TE.get())
    print(result)
    result_get(2, result)
str2bin_BTN = Button(tk, text='Convert to Binary', command=text2bin)
str2bin_TE.grid(row=0, column=1)
str2bin_BTN.grid(row=1, column=1)

bin2str_TE.bind('<Control-v>', print)
str2bin_TE.bind('<Control-v>')


tk.mainloop()
