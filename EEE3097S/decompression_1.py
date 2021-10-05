import zlib
import csv

compressed_data = open('outputfile.csv','rb').read()
decompressed_data = zlib.decompress(compressed_data)

f=open('Datadecompressed.csv', 'wb')
f.write(decompressed_data)
f.close()

