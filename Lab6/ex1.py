import os
import sys


def read_dir(dir_path, file_extension):
    try:
        if not os.path.isdir(dir_path):
            raise ValueError("\033[31m Invalid directory path \033[0m")
        files = [f for f in os.listdir(dir_path) if f.endswith(file_extension)]
        if not files:
            print("No files found with this extension")
            return
        for f in files:
            file_path = os.path.join(dir_path, f)
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    print("\033[34m Contents of "+ str(f)+"\033[0m")
                    print(content)
                    print("-----------------------------------------------------------------")
            except Exception as e:
                print("Error while reading: " + str(e))
                
    except ValueError as ve:
        print("\033[31mError: " + str(ve)+"\033[0m")
    except Exception as e:
        print("Error: " + str(e))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid number of arguments")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]
        read_dir(directory_path, file_extension)


#"C:\Users\user\Documents\facultate\anul 3\SEM1\Programare-in-Python\Lab4"