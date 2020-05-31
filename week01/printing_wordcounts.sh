
for i in $(find * -type f,d); do 
	echo -n "$i has ";
	echo -n $i | wc -c; 
done