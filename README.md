# Rodriguez

A PyQt5 and Python program to make diode and transistor IV plots using an Arduino as the electrical interface.

Rodriguez makes current and voltage traces of various semiconductors.  

In its current form, it can trace diodes (including LEDs) and bipolar junction transistors (NPN and PNP.)

Rodriguez makes use of an Arduino and some very simple hardware.  The simple hardware sets limits on the range (and hence the usefulness) of the system, but makes it possible for any beginning hobbyist to build it.  Rodriguez gets by using the analog to digital converters of the Arduino and the PWM outputs.

![Rodriguez's hardware](/Schematic/Rodriguez-Schematic.png)

