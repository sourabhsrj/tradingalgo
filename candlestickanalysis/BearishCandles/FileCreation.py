# Read file names from the text file
text_file_path = 'bearishcandles.txt'

try:
    with open(text_file_path, 'r') as file:
        file_names = file.read().splitlines()
except FileNotFoundError:
    print(f"Error: File '{text_file_path}' not found.")
    exit()

# Create files with the specified names
for file_name in file_names:
    try:
        with open(file_name+".py", 'w') as new_file:
            # You can add content to the files if needed
            new_file.write("This is a sample content.")
        print(f"File '{file_name}' created successfully.")
    except IOError:
        print(f"Error: Unable to create file '{file_name}'.")

