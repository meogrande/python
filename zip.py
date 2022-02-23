#unzip file and extract to a folder
def unzip(file, folder):
    import zipfile
    import os
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(folder)
    return

for i in range(100,3000):
    # unzip('test'+str(i)+'.zip', 'test'+str(i))
    unzip('zip/flag'+str(3000-i)+'.zip', 'zip/')
