# INVALID SOLUTION DOESN'T PROPERLY ANSWER QUESTION

"""
import re
import sys
from multiprocessing import Pool

CHUNK_SIZE = 500
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
	out_line = re.sub('[{0}{1}]'.format(out_row_del, out_col_del), '', chunk)	# Remove row, col delimiters from chunk with regex, one pass through data instead of instead of two.
	out_line = out_line.replace(in_col_del, out_col_del) + out_row_del			# Format output line with new delimiters.
	sys.stdout.write(out_line)													# Write line to stdout.

db_import_multi_thread()
"""