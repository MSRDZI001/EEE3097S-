import filecmp

#comparing the csv file before compression witht the file after compression

#original_data = open('IMUdata.csv', 'rb').read()
#final_data = open('Datadecompressed.csv', 'rb').read()

#using the cmp function to compare the two files before and after compression
if filecmp.cmp (Datadecompressed.csv,Datadecompressed.csv): #(original_data, final_data):

	print( "Both files are the same before and after compression and decompression respectively.")

else:
	print( "Both files are different before and after compression and decompression respectively.")

