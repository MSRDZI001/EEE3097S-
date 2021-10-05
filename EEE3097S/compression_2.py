import gzip
import shutil

with open('IMUdata.csv', 'rb') as f_in:
	with open('IMUdata.csv.gz', 'wb') as f_out:
		with gzip.GzipFile('IMUdata.csv', 'wb', fileobj=f_out) as f_out:
			shutil.copyfileobj(f_in,f_out)
