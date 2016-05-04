Coding Challenge - Data Engineering
===================================

DELIVERABLES
------------
1. The python, ruby, perl, or node.js script

	+ db_import_single_thread.py

2. The shell command line to execute it, assuming the existence of the dbexport
program

	<code>dbexport ­t mytable | python db_import_single_thread.py > output.txt</code>

3. The delimiter you are going to choose in the UI above when importing the file

	*Comma*

4. A test dataset representing example output from dbexport that will be piped into your
script. Be sure to include any unusual field data that could potentially cause import
errors if not handled correctly. You should able to run your script with this command:

	<code>cat test_dataset.txt | python db_import_single_thread.py > output.txt</code>

5. A unit test that can be used to verify that your script does “the right thing”. You should
be able to run your unit test with this command:

	<code>cat test_dataset.txt | python db_import_single_thread.py | python unit_test.py</code>

6. Written description of edge cases considered and trade­offs made

	Edge cases:
	+ Empty fields
	+ Input column and row delimiters removed from output (and backslashes removed)
	+ Output column and row delimiter removed from output
	+ Double backslash characters in input -> single backslash character in output
	+ If there are two consecutive backslashes, the next char doesn't think it is 'escaped' 
		- Protects against '\' being the last char of field value.
		- Properly handles multiple backslashes in a row.
