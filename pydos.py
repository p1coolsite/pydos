import subprocess
pydos = True
def userinputget():
    if i == "run":
        exe_path = input("path to exe: (a to abort):")
        result = subprocess.run(exe_path, capture_output=True, text=True)
        print("Output:", result.stdout)
        print("Error:", result.stderr)
    elif i == "cls":
        subprocess.call('cls', shell=True)
    elif i == "help":
        print("""run- run an app
cls- clear screen
help- to get help(what you're seeing right now)
pymake- open pymake""")
    elif i == "pymake":
        with open('pymake.py') as file:
            exec(file.read())
    else:
        print("command not recognised")
#banner 3d 
print(
"""
'########::'##:::'##:'########:::'#######:::'######::
 ##.... ##:. ##:'##:: ##.... ##:'##.... ##:'##... ##:
 ##:::: ##::. ####::: ##:::: ##: ##:::: ##: ##:::..::
 ########::::. ##:::: ##:::: ##: ##:::: ##:. ######::
 ##.....:::::: ##:::: ##:::: ##: ##:::: ##::..... ##:
 ##::::::::::: ##:::: ##:::: ##: ##:::: ##:'##::: ##:
 ##::::::::::: ##:::: ########::. #######::. ######::
..::::::::::::..:::::........::::.......::::......:::
:::'##::::::::::'#####:::'####:                      
:'####:::::::::'##.. ##:: ####:                      
:.. ##::::::::'##:::: ##: ####:                      
::: ##:::::::: ##:::: ##:: ##::                      
::: ##:::::::: ##:::: ##::..:::                      
::: ##:::'###:. ##:: ##::'####:                      
:'######: ###::. #####::: ####:                      
:......::...::::.....::::....::                      
"""
)
#main loop
print("version: alpha 1.0")
print("welcome to pydos!")
print("press 'help' for help and info.")
while True:
    i = input("pydos terminal>")
    userinputget()

