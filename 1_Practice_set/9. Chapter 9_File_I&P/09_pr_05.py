# Repeat question no. 4 for a list of words to be censored.

ls = ['donkey','bitch','doggy','fuck']

with open("sample.txt") as f:
    _txt = f.read()

for word in ls:
    _txt = _txt.replace(word,"######")
    with open("sample.txt",'w') as f:
        f.write(_txt)