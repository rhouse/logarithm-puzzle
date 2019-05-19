logarithm-puzzle
================
                             A logarithm puzzle

In today's world of computers, calculators, cellphones, etc., nobody uses
logarithm tables for doing arithmetic.  However, not so long ago logarithm
tables were indispensible.  They allowed multiplication to be done by
addition, and division to be done by subtractionn.  Even exponentiation was
tractable; it could be done by multiplying.  
<a href="https://en.wikipedia.org/wiki/Common_logarithm">Here</a> are some 
examples.

Although logarithm tables have, by and large, been replaced by calculators,
they can still be found here and there.  The file prop-logs-with-example.pdf
contains a logarithm table from 
<a href="https://smile.amazon.com/Raphaels-Ephemeris-2020-Edwin-Raphael/dp/0572047800/ref=sr_1_fkmrnull_1?keywords=raphaels+ephemeris+2020&qid=1558292779&s=gateway&sr=8-1-fkmrnull">
Raphaels 2020 Ephemeris</a>.  (At this 
<a href="http://www.rosicrucian.com/images/ssaen018.gif">link</a> is a part
of the same table from a different source.)

Note that an entry in these tables is accessed by selecting a column using
either hours of time or degrees of arc, and selecting a row using minutes
(of time or arc).  The selected table entry is a logarithm.  But, a
logarithm of what exactly?

This is the puzzle to be solved.  The file make_log_table.py is a Python
program which computes and prints the heart of the log table seen in
prop-logs-with-example.pdf.  But the return statement in the mylog function
must be replaced with a return statement which calls a Python standard
library math function.  Change the return statement and run the program and
you will get the same table as in prop-logs-with-example.pdf.

Have fun.
