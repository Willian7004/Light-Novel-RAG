import os
import re

def read_and_sort_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    files.sort(key=lambda x: int(re.search(r'\d+', x).group()))
    contents = []
    for file in files:
        with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
            content = f.read()
            contents.append((file, content))
    return contents

def concatenate_files(contents, batch_size):
    concatenated_contents = []
    for i in range(0, len(contents), batch_size):
        batch = contents[i:i + batch_size]
        concatenated_content = ""
        for file, content in batch:
            number = re.search(r'\d+', file).group()
            concatenated_content += f"【{number}】{content}\n"
        concatenated_contents.append(concatenated_content)
    return concatenated_contents

def save_concatenated_files(concatenated_contents, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for i, content in enumerate(concatenated_contents):
        with open(os.path.join(output_directory, f"{i+1}.txt"), 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    input_directory = 'summarize'
    output_directory = 'chapter2'
    batch_size = 20

    contents = read_and_sort_files(input_directory)
    concatenated_contents = concatenate_files(contents, batch_size)
    save_concatenated_files(concatenated_contents, output_directory)

if __name__ == "__main__":
    main()