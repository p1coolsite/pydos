import subprocess
pydos = True
def userinputget():
    if i == "pydos":
        with open('pydos.py') as file:
            exec(file.read())
    elif i == "cls":
        subprocess.call('cls', shell=True)
    elif i == "pymake":
        filename = input("file name (and file name extension)")
            f = open(filename, "w")
            inputtext = input("write the text here:")
            f.write(inputtext)
            f.close()
    elif i == "read":
        try:
            filename = input("file:")
            f = open(filename, "r")
            print(f.read())
            f.close()
        except:
            print("no such file exists")
    elif i == "help":
        print("""pydos- goes back to the pydos shell
cls- clears the screen (same as in pydos)
pymake- for makeing files
read- for reading files
help- to get help (what you're seeing right now, same as in pydos)""")
    else:
        print("command not recognised")
#banner 3d 
print(
    """
     _        _        _        _        _        _    
   _( )__   _( )__   _( )__   _( )__   _( )__   _( )__ 
 _|     _|_|     _|_|     _|_|     _|_|     _|_|     _|
(_ P _ (_(_ Y _ (_(_ M _ (_(_ A _ (_(_ K _ (_(_ E _ (_ 
  |_( )__| |_( )__| |_( )__| |_( )__| |_( )__| |_( )__|
     _        _        _                               
   _( )__   _( )__   _( )__                            
 _|     _|_|     _|_|     _|                           
(_ F _ (_(_ O _ (_(_ R _ (_                            
  |_( )__| |_( )__| |_( )__|                           
     _        _        _        _        _             
   _( )__   _( )__   _( )__   _( )__   _( )__          
 _|     _|_|     _|_|     _|_|     _|_|     _|         
(_ P _ (_(_ Y _ (_(_ D _ (_(_ O _ (_(_ S _ (_          
  |_( )__| |_( )__| |_( )__| |_( )__| |_( )__|         
"""
)
#main loop
print("version: pymake (same as pydos)")
print("welcome to pymake for pymake!")
print("press 'help' for help and info. (same as in pydos)")
while True:
    i = input("pymake terminal>")
    userinputget()
