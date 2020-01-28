""" 
Kode ini akan mengubah nama file INPUT.txt menjadi hash dari Nama pada INPUT.txt
hash yang digunakan adalah fungsi hash() yang built-in dari python
"""
import os
from rename_file import read_file

if __name__ == "__main__":

	lst = read_file("INPUT.txt")
	name = lst[0].split('-')[1].strip();
	hashfunc = hash(name)
	os.rename("INPUT.txt", str(hashfunc)+".txt")

