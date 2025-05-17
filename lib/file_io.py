def write_file(file_name, file_content):
    file_path = f"{file_name}.txt"
    with open(file_path, mode='w', encoding='utf-8') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_path = f"{file_name}.txt"
    with open(file_path, mode='a', encoding='utf-8') as file:
        file.write(append_content)

def read_file(file_name):
    file_path = f"{file_name}.txt"
    with open(file_path, mode='r', encoding='utf-8') as file:
        return file.read()
