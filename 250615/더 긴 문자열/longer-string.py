text, text2 = input().split()

if len(text)>len(text2):
    print(text, len(text))
elif len(text)<len(text2):
    print(text2,len(text2))
elif len(text)==len(text2):
    print("same")