import zlib

original_data = open('IMUdata.csv', 'rb').read()
compressed_data = zlib.compress(original_data, zlib.Z_BEST_COMPRESSION)

#the constant Z_BEST_COMPRESSION gives the best compression level this algorithm has to offer

compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))
#calculates the level of compression based on the ratio of length of compressed data over length of original data.

print('Compressed: %d%%' % (100.0 * compress_ratio))
#prints the % of compression.

f=open('outputfile.csv', 'wb')
f.write(compressed_data)
f.close()
