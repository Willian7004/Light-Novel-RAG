import os

def split_and_save_chapters(file_path, delimiter, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    chapters = content.split(delimiter)

    for index, chapter in enumerate(chapters):
        if chapter.strip():  # Skip empty chapters
            output_file_path = os.path.join(output_folder, f"{index + 1}.txt")
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(chapter.strip())

# Define the file path, delimiter, and output folder
file_path = 'book.txt'
delimiter = '------------'
output_folder = 'chapter'

# Call the function to split and save chapters
split_and_save_chapters(file_path, delimiter, output_folder)