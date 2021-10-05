import gzip
import shutil
with gzip.open('IMUdata.csv.gz', 'rb') as f_in:
	with open('imudata_1.csv', 'wb') as f_out:
		shutil.copyfileobj(f_in,f_out)
