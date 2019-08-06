

Needed custom packages (all python3):

opencv
numpy
pyttsx3


for pyttsx3 you need Espeak:
linux: sudo apt-get install espeak
windows: http://espeak.sourceforge.net/

-----------------
Opening file in linux:

open the terminal (in windows cmd)
type cd "/path/to/directory/"
type python3 Randomdetect.py

opening file in windows:
windows key + R
type CMD
type cd "/path/to/file/"
drag python file to cmd window
--------------------------
make custom word list:
make sure the file is a txt and it's called words
line break every word
----------------------------

This was tested as of August 6 2019 on Ubuntu linux and windows 10.
distro: Ubuntu MATE 19.04 with python 3.73
windows: python 3.74
