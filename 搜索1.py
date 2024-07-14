import re
import os
import sys
import api

def main():
    # 1. 程序运行时在命令行输入内容
    text = input("请输入内容: ")

    # 2. 导入“api”包，把输入的内容保存为text字符串并传入"api.search1()"函数
    search1_output = api.search1(text)

    # 3. 在第2步调用"api.search1()"函数的输出内容中匹配连续的两个双引号
    pattern = r'"([^"]*)"'
    matches = re.findall(pattern, search1_output)

    if matches:
        # 获取双引号中用空格分割的数字
        numbers = []
        for match in matches:
            numbers.extend(match.split())
        print(f"传入的原文分段：{', '.join(numbers)}")
    else:
        print(search1_output)
        return

    # 4. 根据第3步获取的数字，在当前目录的chapter文件夹中获取文件名为对应数字的txt文件
    chapter_folder = 'chapter'
    files_to_read = []
    for number in numbers:
        file_path = os.path.join(chapter_folder, f'{number}.txt')
        if os.path.exists(file_path):
            files_to_read.append(file_path)

    # 5. 用utf-8编码依次打开第4步获取的txt文件，连接为content字符串
    content = ""
    for file_path in files_to_read:
        with open(file_path, 'r', encoding='utf-8') as file:
            content += file.read()

    # 把content字符串和text字符串依次传入“api.search11()”函数
    search11_output = api.search11(content, text)

    # 6. 打印第5步调用api.search11()”函数的输出内容，结束程序
    print(search11_output)

main()