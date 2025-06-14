text, text2 = input().split()

if len(text)>len(text2):
    print(text, len(text2)+1)
elif len(text)<len(text2):
    print(text2,len(text)+1)
elif len(text)==len(text2):
    print("same")