Using a switch
==============
W. H. Bell

Overview
--------

Connect a wire between one of the ground (GND) connections on the GPIO connector and a one 
of the input connections on a switch.  Connect the other side of the switch back to one of
the GPIO pins.  Then use the same GPIO pin number in the switch.py program.

switch
------

Type

sudo ./switch.py

to run the example.  The program uses an interrup to check if the switch is closed.  This 
means the CPU is idle until the switch has been closed.
