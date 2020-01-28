""" 
Kode ini akan mengubah nama file INPUT.txt menjadi Nama pada INPUT.txt
"""
import os

# membaca file dan return list yang sudah dirapikan
def read_file(path):

	lst = []

	with open(path, "r") as file:

		# filer line hanya whitespice
		for line in file:
			line = line.strip()
			if line != '':
				lst.append(line)
				
	return lst

if __name__ == "__main__":

	lst = read_file("INPUT.txt")
	name = lst[0].split('-')[1].strip();
	os.rename("INPUT.txt", name+".txt")

