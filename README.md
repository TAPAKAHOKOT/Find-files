# Find-files
Using it you can find files on your pc


Add folder "run file" in path to use program
open cmd and write command "whereis"

next you can add flags -f -t 
-t : write running time
-f : script will skip some folders ("Windows", "FileHistory", "Program Files", "Program Files (x86)", "AppData",".gradle", ".atom", "sdk")

you need to add a files, that you would like to find "text.txt"

or you can write some masks:
  special symbols:
    ? at this position can be located any one letter 
    * here can be located any number of any letters
    
mask examples: t??t.py test. m*n.py* ect...

program running example: whereis -f -t main.py *.txt program.ex?
