import os
import sys


def count(directory_path):
    try:
        if not os.path.isdir(directory_path):
            raise ValueError("\033[31m Invalid directory path \033[0m")
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

        if len(files) == 0:
            raise ValueError("\033[33m No files found \033[0m")
            return
        extensions = {}
        for file in files:
            print("File: " + file)
            _, ext = os.path.splitext(file)
            extensions[ext] = extensions.get(ext, 0) + 1

        for extension, counts in extensions.items():
            print(str(counts)+" files with the extension "+extension)

    except ValueError as ve:
        print("\033[31mError: " + str(ve) + "\033[0m")
    except PermissionError as pe:
        print("\033[31mPermission error: " + str(pe) + "\033[0m")
    except Exception as e:
        print("\033[31m Other error: " + str(e) + "\033[0m")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
    else:
        dir_path = sys.argv[1]
        count(dir_path)


#"C:/Users/user/Documents/facultate/anul 3/SEM1/PYTHON/exemplu2"
#"C:/Users/user/Documents/facultate/anul 3/SEM1/PYTHON/fold"