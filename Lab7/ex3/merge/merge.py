
def merge_files(files, output_file, separators=None):
    with open(output_file, 'w') as output:
        for idx, file_path in enumerate(files):
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    separator = separators[idx] if separators and idx < len(separators) else '\n'
                    output.write(content)
                    output.write(separator)
            except FileNotFoundError:
                print(f"File {file_path} not found")
                continue

