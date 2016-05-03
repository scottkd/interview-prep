Coding Challenge - Data Engineering
===================================

DELIVERABLES
------------
1. The python, ruby, perl, or node.js script

	+ db_import_single_thread.py
	+ db_import_multi_thread.py

2. The shell command line to execute it, assuming the existence of the dbexport
program

	<code>dbexport ­t mytable | python db_import_multi_thread.py > output.txt</code>

3. The delimiter you are going to choose in the UI above when importing the file

	*Comma*

4. A test dataset representing example output from dbexport that will be piped into your
script. Be sure to include any unusual field data that could potentially cause import
errors if not handled correctly. You should able to run your script with this command:

	<code>cat test_dataset.txt | python db_import_multi_thread.py > output.txt</code>

5. A unit test that can be used to verify that your script does “the right thing”. You should
be able to run your unit test with this command:

	<code>cat test_dataset.txt | python db_import_multi_thread.py | python unit_test.py</code>

6. Written description of edge cases considered and trade­offs made

	Started with single-threaded answer, went to multi-threaded. This assumes that the order of the output doesn't matter, which I thought was a safe assumption for a full table import.

	Note: In multi-threaded solution I made assumptions that I didn't in single-threaded. I relied on fact that output of dbexport will have \n as row delimiter, allowing me to process a row at a time in parallel. Single-threaded answer will look at a CHUNK_SIZE chunks at a time and explicitly find the end of a row before processing output.

	Note on edge cases: I don't test for improperly formatted output of dbexport. If the output on dbexport doesn't meet the specifications, then the function will fail. Protection can be added, but wasn't for the sake of time.

	Edge cases:
	+ Empty fields
	+ Output column and row delimiter escaped 
	+ Output column delimiter removed if it can't be escaped (i.e. \n can be escaped, comma cannot)

	Note: Didn't bother dealing with the compressed option, but that functionality can be added to the python script to allow compressing the output text file.
