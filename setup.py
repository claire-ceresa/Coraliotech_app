import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("main.py", base=base, targetName="Coraliotech.exe", icon="icone.ico")]

packages = ["os", "sqlite3", "Bio", "xlsxwriter", "urllib"]
excludes = ['tkinter']

include_files = ["database",
                 "graphic",
                 "objects",
                 "logo.png",
                 "useful_functions.py"]

options =  {
    "build_exe":
                {"packages": packages ,
                "excludes": excludes,
                 "include_files":include_files,
                "include_msvcr": True}}

setup(
    name = "Coraliotech",
    options = options,
    version = "1.0",
    description = 'Cree par Claire Ceresa',
    executables = executables
)