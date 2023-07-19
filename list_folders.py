import os

def list_folders():
    folders = [folder for folder in os.listdir() if os.path.isdir(folder)]
    with open('folder.txt', 'w') as file:
        for folder in folders:
            file.write(folder + '\n')

if __name__ == "__main__":
    list_folders()
