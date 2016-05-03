import sys

CHUNK_SIZE = 500	# Number of bytes of stdin to process at a time.

def db_import_single_thread(in_col_del='\t', in_row_del='\n', out_col_del=',', out_row_del='\n'):
	chunk = sys.stdin.read(CHUNK_SIZE)
	while chunk:
	# While there is input to process:
		try:
			index = chunk.index(in_row_del)											# Find row delimter.
			out_line = chunk[:index].replace(out_row_del, '')						# Remove row delimiters from chunk.
			out_line = out_line.replace(out_col_del, '')							# Remove col delimiters from chunk.
			out_line = out_line.replace(in_col_del, out_col_del) + out_row_del		# Format output line with new delimiters.
			sys.stdout.write(out_line)												# Write line to stdout.
			chunk = chunk[index+1:]													# Move forward in chunk.
		except ValueError:
		# If in_row_del not in chunk, add next chunk.
			chunk += sys.stdin.read(CHUNK_SIZE)
			
db_import()
