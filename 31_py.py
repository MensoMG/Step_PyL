words = input().lower().split(' ')
wordDict = {}
for word in words:

    if wordDict.get(word) != None:
        wordDict[word] += 1
    else:
        wordDict.setdefault(word,1)

for key, value in wordDict.items():
    print(key, value) 
