import os
import re
import sys
import api

def main():
    # 1. 程序运行时在命令行输入内容
    text = input("请输入内容: ")
    
    # 2. 导入“api”包，把输入的内容保存为text字符串并传入"api.search2()"函数
    output_search2 = api.search2(text)
    
    # 3. 在第2步调用"api.search2()"函数的输出内容中匹配连续的两个双引号
    match = re.search(r'"([^"]+)"', output_search2)
    if match:
        numbers = match.group(1).split()
        print(f"传入的概括分段：{numbers}")
    else:
        print(output_search2)
        return
    
    # 4. 根据第3步获取的数字，在当前目录的chapter2文件夹中获取文件名为对应数字的txt文件
    content = ""
    for number in numbers:
        file_path = os.path.join("chapter2", f"{number}.txt")
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content += file.read()
    
    # 5. 把content字符串和text字符串依次传入“api.search22()”函数
    output_search22 = api.search22(content, text)
    
    # 6. 在第5步调用“api.search22()”函数的输出内容中匹配连续的两个双引号
    match = re.search(r'"([^"]+)"', output_search22)
    if match:
        numbers = match.group(1).split()
        print(f"传入的原文分段：{numbers}")
    else:
        print(output_search22)
        return
    
    # 7. 根据第6步获取的数字，在当前目录的chapter文件夹中获取文件名为对应数字的txt文件
    content = ""
    for number in numbers:
        file_path = os.path.join("chapter", f"{number}.txt")
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                content += file.read()
    
    # 8. 把content字符串和text字符串依次传入“api.search11()”函数
    output_search11 = api.search11(content, text)
    
    # 9. 打印第8步调用api.search11()”函数的输出内容，结束程序
    print(output_search11)

main()