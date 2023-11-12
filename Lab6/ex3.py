import os
import sys


def calculate(path):
    try:
        if not os.path.isdir(path):
            raise ValueError("\033[31m Invalid directory path \033[0m")
        size = 0
        for dir, subdir, files in os.walk(path):
            print("Current directory: " + dir)
            print("   The subdirectories from the directory: " + str(subdir))
            print("   The files from the directory: " + str(files))
            for file in files:
                file_path = os.path.join(dir, file)
                try:
                    size += os.path.getsize(file_path)
                except FileNotFoundError as fnfe:
                    print("\033[31mFile not found: " + str(fnfe) + "\033[0m")
                except PermissionError as pe:
                    print("\033[31mPermission error: " + str(pe) + "\033[0m")
                except Exception as e:
                    print("Error while reading: " + str(e))

        print("Total size: " + str(size) + " bytes")

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
        directory_path = sys.argv[1]
        calculate(directory_path)

# "C:\Users\user\Documents\facultate\anul 3\SEM1\PYTHON"
