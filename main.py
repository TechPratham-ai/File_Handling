import os
import subprocess
Path="/storage/emulated/0/qpython/"

def change_Path(Path1):
    Path=Path1
    
def open_file(file_name,extension):
    n="{}{}"
    try:
        file1=open(n.format(file_name,extension),"r")
        for x in file1:
            print(x)
    except:
        print("Enable to open the File ")

        
def write_file(file_name,extension):
    n="{}{}"
    try:
        file1=open(n.format(file_name,extension),"a")
        file_r=file_name+extension
        edit_file=str(input("Enter The Content "))
        file1.write(edit_file)
        printf("File Edited Succsfully")
    except:
        print("Enable to open the File")
        
def creat_file(file_name,extension):
    n="{}{}"
    try:
        file1=open(n.format(file_name,extension),"a")
        file_r=file_name+extension
        with open(os.path.join(Path,file_name),"w") as fp:
            pass
        print("File Created Succsfully")
    except:
        print("Enable to open the File")

def Delet_file(file_name,extension):
    n="{}{}"
    try:
        file1=open(n.format(file_name,extension),"a")
        file_r=file_name+extension
        os.remove(file_r)
        print("File Deleted Succsfully")
    except:
        print("Enable to open the File")
    
print("Enter 1 to Display Record")
print("Enter 2 to Add Record")
print("Enter 3 to creat Record")
print("Enter 4 to Delet Record")
ch=str(input(" "))
if ch=='1':
    subprocess.run("clear")
    file_name=str(input("Enter The File Name :: "))
    extension=str(input("Enter Extension of file :: "))
    open_file(file_name,extension)
elif ch=='2':
    subprocess.run("clear")
    file_name=str(input("Enter The File Name :: "))
    extension=str(input("Enter Extension of file :: "))
    write_file(file_name,extension)
elif ch=='3':
    subprocess.run("clear")
    file_name=str(input("Enter The File Name :: "))
    extension=str(input("Enter Extension of file :: "))
    creat_file(file_name,extension)
elif ch=='4':
    subprocess.run("clear")
    file_name=str(input("Enter The File Name :: "))
    extension=str(input("Enter Extension of file :: "))
    Delet_file(file_name,extension)
elif ch=='*#':
    #subprocess("clear")
    Path=str(input("Enter the Path :: "))
    change_Path(Path)
else:
    print("Invalid Input")
