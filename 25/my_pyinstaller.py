import PyInstaller.__main__

PyInstaller.__main__.run([
    'mainclass.py',
    '--onefile',
    '--windowed',
    '--noconsole'
    
])

# "--add-data=todolist.db;."