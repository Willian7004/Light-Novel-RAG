import os
import re

def read_and_sort_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    files.sort(key=lambda x: int(re.search(r'\d+', x).group()))
    contents = []
    for file in files:
        with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
            content = f.read()
            number = re.search(r'\d+', file).group()
            contents.append(f"【{number}】{content}\n")
    return ''.join(contents)

def save_combined_file(content, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    directory = 'summarize2'
    output_file = 'summarize2.txt'
    combined_content = read_and_sort_files(directory)
    save_combined_file(combined_content, output_file)

main()