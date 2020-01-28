""" 
Kode ini akan parsing data INPUT.txt sesuai permintaan OUTPUT.txt
nama file yang dibuat adalah RESULT.txt
"""
import os
from rename_file import read_file

if __name__ == "__main__":

	lst = read_file("INPUT.txt")

	first, last= 0, 0

	# mencari baris pertama yang berisi "tahun ajaran" sebagai pertanda mulai parsing
	while "Tahun Ajaran" not in lst[first]:
		first+=1

	# mencari baris terakhir yang ada mata kuliah sebagai pertanda selesai parsing
	while "detail" not in lst[last-1]:
		last-=1

	lst = lst[first:last]

	writer = open("result.txt", "w")

	# bagian parsing
	result = []
	current_year = 0
	current_term = 0
	current_tahun_ajaran = "-"
	accumulated_credits = 0
	

	for line in lst:

		# update tahun ajaran
		if "Tahun Ajaran" in line:

			tahun_ajaran = line.split(' ')[2]
			
			if tahun_ajaran != current_tahun_ajaran:

				current_year += 1
				current_term = 1
				accumulated_credits = 0
				current_tahun_ajaran = tahun_ajaran

			else:

				current_term += 1
				accumulated_credits = 0

		# dapat data
		else :

			# membuat list matkul data dengan setiap elemen dihapus leading & trailing whitespacenya
			matkul_data = [elemen.strip() for elemen in line.split('\t')]
			
			accumulated_credits+=int(matkul_data[5])
			
			# karena format last aneh, buat manual
			# intinya panjang totalnya 5
			last_entry = matkul_data[8]
			while len(last_entry) + len(str(accumulated_credits)) < 5:
				last_entry += ' '
			last_entry += str(accumulated_credits)

			
			writer.write(str(current_year)+str(current_term)+' '+matkul_data[1]+' '+
						 matkul_data[5]+' '+last_entry+'\n')

	writer.close()
	

