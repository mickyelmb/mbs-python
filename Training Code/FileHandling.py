file = open("sample", 'r')
content = file.readlines()
print(content)
contentList =[i.rstrip("\n") for i in content]
print(contentList)
file.close()