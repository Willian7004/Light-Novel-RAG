import os
import glob

# 假设api包已经安装并且包含summarize函数
import api

def process_files(chapter_folder, summarize_folder):
    # 确保summarize文件夹存在
    if not os.path.exists(summarize_folder):
        os.makedirs(summarize_folder)

    # 获取chapter文件夹中所有的txt文件
    txt_files = glob.glob(os.path.join(chapter_folder, '*.txt'))

    for txt_file in txt_files:
        try:
            # 读取文件内容
            with open(txt_file, 'r', encoding='utf-8') as file:
                content = file.read()

            # 使用api.summarize()函数处理内容
            summary = api.summarize(content)

            # 获取文件名（不包括路径）
            file_name = os.path.basename(txt_file)

            # 保存摘要到summarize文件夹
            summary_file_path = os.path.join(summarize_folder, file_name)
            with open(summary_file_path, 'w', encoding='utf-8') as summary_file:
                summary_file.write(summary)

        except Exception as e:
            print(f"Error processing file {txt_file}: {e}")

# 使用当前目录下的chapter文件夹和summarize文件夹
process_files('chapter', 'summarize')