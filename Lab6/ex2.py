import os


def rename_files(path):
    try:
        if not os.path.isdir(path):
            raise ValueError("\033[31m Invalid directory path \033[0m")

        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        if len(files) == 0:
            print("No files found")
            return

        for i, old_name in enumerate(files, start=1):
            name, extension = os.path.splitext(old_name)
            new_name = f"file{i}{extension}"
            old_path = os.path.join(path, old_name)
            new_path = os.path.join(path, new_name)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_name} - {new_name}")
            except FileNotFoundError as fnfe:
                print(f"\033[31mFile not found: {str(fnfe)} \033[0m")
            except PermissionError as pe:
                print(f"\033[31mPermission error: {str(pe)} \033[0m")
            except Exception as e:
                print(f"\033[31mError renaming {old_name}: {str(e)} \033[0m")

    except ValueError as ve:
        print("\033[31mError: " + str(ve) + "\033[0m")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    dir_path = "C:/Users/user/Documents/facultate/anul 3/SEM1/PYTHON/exemplu1"
    rename_files(dir_path)
