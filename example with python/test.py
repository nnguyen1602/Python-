# uppercase all letters
name = 'hieu'
#print(name.upper())

## split splitted_txt
txt = "hieu is handsome"
print(txt)
splitted_txt = txt.split(None,1)
print(splitted_txt)
word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
print(word)
print(txt)
