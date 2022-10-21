flag = []
with open('flag.txt','r') as f:
    text = f.read()
    result = list(text.split(" \n"))
    for key in result:
        flag.append(chr(int(key)))
flag.pop()
print(''.join(flag))
