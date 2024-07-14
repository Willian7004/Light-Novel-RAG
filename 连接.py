import os
import re

def read_and_sort_files(directory):
    files = [f for f in os.listdir(directory) if re.match(r'^\d+\.txt$', f)]
    files.sort(key=lambda x: int(x.split('.')[0]))
    return files

def concatenate_files(directory, sorted_files):
    concatenated_content = ""
    for file_name in sorted_files:
        with open(os.path.join(directory, file_name), 'r', encoding='utf-8') as file:
            content = file.read()
            concatenated_content += f"【{file_name.split('.')[0]}】{content}\n"
    return concatenated_content

def save_concatenated_file(content, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    directory = 'summarize'
    output_file = 'summarize.txt'
    
    sorted_files = read_and_sort_files(directory)
    concatenated_content = concatenate_files(directory, sorted_files)
    save_concatenated_file(concatenated_content, output_file)

if __name__ == "__main__":
    main()