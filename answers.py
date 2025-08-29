def transform_text(text: str) -> str:
    # Example transformation: convert to uppercase
    return text.upper()

def read_and_write_modified(input_path: str, output_path: str) -> None:
    with open(input_path, 'r', encoding='utf-8') as infile:
        content = infile.read()
    modified = transform_text(content)
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(modified)

        
# Example usage
input_file = 'input.txt'
output_file = 'output.txt'
read_and_write_modified(input_file, output_file)
print(f"Modified content written to {output_file}")

def remove_blank_lines(text: str) -> str:
    lines = text.splitlines()
    non_blank = [line for line in lines if line.strip() != ""]
    return "\n".join(non_blank)

def read_and_write_filtered(input_path: str, output_path: str) -> None:
    with open(input_path, 'r', encoding='utf-8') as infile:
        content = infile.read()
    modified = remove_blank_lines(content)
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(modified)

#Error handling
def safe_read_file():
    while True:
        filename = input("Enter the filename to read: ").strip()
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = f.read()
            print("File read successfully.")
            print("---- File Preview (first 500 chars) ----")
            print(data[:500])
            return data
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found. Please check the path and try again.")
        except PermissionError:
            print(f"Error: Permission denied reading '{filename}'. Do you have the right permissions?")
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory, not a file.")
        except OSError as e:
            print(f"IO error({e.errno}): {e.strerror}.")
        # Optional: ask to retry or exit
        retry = input("Would you like to try another file? (y/n): ").strip().lower()
        if retry != 'y':
            break
# Run the safe reader        
def safe_write_file(data: str):