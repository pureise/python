import os
fld = '/home/natt/Pulpit/pajton/Python1'
print("Zamiana formatow plików w folderze: ", fld, "\n\nPodaj stare rozszerzenie, a potem nowe (w argumentach funkcji)")
def change_file_ext(old_ext, new_ext):
    files = os.listdir(fld)
    for filename in files:
        file_ext = os.path.splitext(filename)[1]
        if old_ext == file_ext:
            newfile = filename.replace(old_ext, new_ext)
            os.rename(filename, newfile)

        
    
