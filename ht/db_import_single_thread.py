import sys

CHUNK_SIZE = 500	# Number of bytes of stdin to process at a time.

def db_import_single_thread(in_col_del='\t', in_row_del='\n', out_col_del=',', out_row_del='\n'):
	chunk = sys.stdin.read(CHUNK_SIZE)
	prev_slash = False
	to_write = ''
	backslash = '\\'
	while chunk:
	# While there is input to process:
		for i in range(len(chunk)):
			char = chunk[i]
			if prev_slash:
			# Two cases if we see a backslash: either we will see a 2nd backslash for the literal character,
			# or we will see an input delimiter. 
				if char in (in_row_del, in_col_del):
					pass								# Backslash and escaped delimiter NOT written to output 

				elif char == backslash:
					to_write += backslash				# Single backslash written to output

			else:
				if char == in_col_del:
					to_write += out_col_del				# Replace input col delim with output col delim
				
				elif char == in_row_del:
					to_write += out_row_del				# Replace input col delim with output col delim
					sys.stdout.write(to_write)			# Write row of data
					to_write = ''

				elif char != backslash and char not in (out_row_del, out_col_del):
					to_write += char					# Non-backslash, Non-delim added to output

			if char != backslash:
				prev_slash = False

			else:
				prev_slash = True if not prev_slash else False	# next iter of prev_slash set to True ONLY IF we don't have a pair of slashes 

		chunk = sys.stdin.read(CHUNK_SIZE)
			
db_import_single_thread()
