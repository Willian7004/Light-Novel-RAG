#本程序包含用于各项任务的提示词，由项目内其它程序调用，使用前需要在send函数填写自己使用的模型的api地址和api key。
# python3
# Please install OpenAI SDK first：`pip3 install openai`
from openai import OpenAI

def send(system,user):
    client = OpenAI(api_key=" ", base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-coder",
        messages=[
            {"role": "system", "content":system},
            {"role": "user", "content":user},
        ],
        stream=False
    )

    return(response.choices[0].message.content)

def summarize(text):
    output=send("用一段话总结以下文章：",text)
    return(output)

def summarize2(text):
    output=send("以下是对一部小说的一部分的分段总结，用一段话概括这段文字并提取时间、地点和主要人物等方面的关键词，按{关键词：  概括：  }格式回答：",text)
    return(output)

def search11(content,text):
    string1="以下是一部小说的部分片段，根据这部分分段的内容回答后面的问题："
    string2=string1+content    
    output=send(string2,text)
    return(output)

def search1(text):
    string1="以下是对一部小说的分段总结，每个分段前的中括号内的数字为分段序号，根据这部分内容回答后面的问题。如果本次提供的内容足够回答问题或问题涉及的内容超过20个分段，请直接回答问题。如果需要获取不超过20个分段的原文来回答问题，请在两个双引号中依次回复对应分段的序号并用空格分隔开（例如需要2、3、6、8分段应回复""2 3 6 8""）："
    with open("summarize.txt", 'r', encoding='utf-8') as f:
        content = f.read()
    string2=string1+content    
    output=send(string2,text)
    return(output)

def search22(content,text):
    string1="以下是对一部小说部分分段的总结，每个分段前的中括号内的数字为分段序号，根据这部分分段的内容回答后面的问题。如果本次提供的内容足够回答问题或问题涉及的内容超过20个分段，请直接回答问题。如果需要获取不超过20个分段的原文来回答问题，请在两个双引号中依次回复对应分段的序号并用空格分隔开（例如需要2、3、6、8分段应回复""2 3 6 8""）："
    string2=string1+content    
    output=send(string2,text)
    return(output)

def search2(text):
    string1="以下是对一部小说的分段总结，每个分段前的中括号内的数字为分段序号，每个分段包含关键词和概括，根据这部分内容回答后面的问题。如果本次提供的内容足够回答问题或问题涉及的内容超过10个分段，请直接回答问题。如果需要获取不超过10个分段的原文来回答问题，请在两个双引号中依次回复对应分段的序号并用空格分隔开（例如需要2、3、6、8分段应回复""2 3 6 8""）："
    with open("summarize2.txt", 'r', encoding='utf-8') as f:
        content = f.read()
    string2=string1+content    
    output=send(string2,text)
    return(output)