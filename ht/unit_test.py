import sys

# Read stdin and compare to pre-calculated result of test data.

data = []
chunk = sys.stdin.readline()
while chunk:
	data.append(chunk)
	chunk = sys.stdin.readline()

# Have to sort data for assert because multi-threading doesn't preserve order
sorted_data = ''.join(sorted(data))

# Not the prettiest testing structure, but does the job as described in the problem description. 
# unittest suite would be created for production code.
assert sorted_data == ',\narches,utah\nbadlands,north dakota\ncomma park,oregon\neverglades,miami\ntes\\\\nting,new\\\\nline\ntes\\\\ting,t\\\\tab\nyosemite,california\n', sorted_data
