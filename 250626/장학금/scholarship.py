mid,fin=map(int, input().split())
wgr=0
if mid>=90 and fin>=95:
    wgr=100000
elif mid>=90 and fin>=90:
    wgr=50000
print(wgr)