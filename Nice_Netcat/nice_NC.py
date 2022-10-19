result = []
with open('flag.txt','r') as f:
    b = bytes.fromhex(f.read()).decode('utf-8')
    a = list(b.split(" \n"))
    a.pop()
    for i in a:
        c = chr(int(i))
        result.append(c)
print(''.join(result))
