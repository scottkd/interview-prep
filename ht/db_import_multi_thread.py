import sys
from multiprocessing import Pool

NUM_POOLS = 4

def db_import_multi_thread(in_col_del='\t', in_row_del='\n', out_col_del=',', out_row_del='\n'):
	pool = Pool(NUM_POOLS)
	chunk = sys.stdin.readline()
	while chunk:
		pool.apply_async(read_chunk, args=(chunk,))
		chunk = sys.stdin.readline()
	pool.close()
	pool.join()

def read_chunk(chunk, in_col_del='\t', in_row_del='\n', out_col_del=',', out_row_del='\n'):
	out_line = chunk.replace(out_row_del, '')								# Remove row delimiters from chunk.
	out_line = out_line.replace(out_col_del, '')							# Remove col delimiters from chunk.
	out_line = out_line.replace(in_col_del, out_col_del) + out_row_del		# Format output line with new delimiters.
	sys.stdout.write(out_line)												# Write line to stdout.

db_import_multi_thread()