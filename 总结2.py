import os
import glob

def process_files(chapter_folder, summarize_folder):
    # 确保summarize2文件夹存在
    if not os.path.exists(summarize_folder):
        os.makedirs(summarize_folder)

    # 获取chapter2文件夹中所有的txt文件
    txt_files = glob.glob(os.path.join(chapter_folder, '*.txt'))

    for txt_file in txt_files:
        try:
            # 读取txt文件内容
            with open(txt_file, 'r', encoding='utf-8') as file:
                content = file.read()

            # 使用api.summarize2()函数处理内容
            from api import summarize2
            summarized_content = summarize2(content)

            # 获取文件名
            file_name = os.path.basename(txt_file)

            # 保存处理后的内容到summarize2文件夹
            output_file_path = os.path.join(summarize_folder, file_name)
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(summarized_content)

        except Exception as e:
            print(f"Error processing file {txt_file}: {e}")

# 定义文件夹路径
chapter2_folder = 'chapter2'
summarize2_folder = 'summarize2'

# 处理文件
process_files(chapter2_folder, summarize2_folder)
