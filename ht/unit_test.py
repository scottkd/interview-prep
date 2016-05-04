import sys

# Read stdin and compare to pre-calculated result of test data.

data = ''
chunk = sys.stdin.readline()
while chunk:
	data += chunk
	chunk = sys.stdin.readline()

# Not the prettiest testing structure, but does the job as described in the problem description. 
# unittest suite would be created for production code.
assert data == """yosemite,california
arches,utah
badlands,north dakota
everglades,miami
testing,newline
,
testing,ttab
comma park,oregon
testing\\,back\\slash\\
""", data
