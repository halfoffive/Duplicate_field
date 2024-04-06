import time
# pip install python-docx
from docx import Document

# 创建一个新的docx文档
doc = Document()

r_time = input("输入次数：")
text = input("输入重复的内容：")

start_time = time.time()
# 循环写入
for i in range(int(r_time)):
    print("正在写入...", i + 1, "/", r_time)
    doc.add_paragraph(text)
end_time = time.time()
# 保存文档
save_name = text + ".docx"
doc.save(save_name)
print("已保存至“" + save_name + "”")
print("开始于", start_time, ",结束于", end_time, "。")
print("共耗时", str(end_time - start_time), "s")

# 退出
print(input("按回车键退出"))
