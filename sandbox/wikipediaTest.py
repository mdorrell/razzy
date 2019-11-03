import wikipedia

search = "tell me about Barak Obama"

keywords = []
keywords.append(["tell", "me", "about"])
keywords.append(["explain"])
keywords.append(["who", "is"])
keywords.append(["what", "is"])

print(keywords)

# remove workds in keywords from search
wordList = search.split()
for row in keywords:
    for word in row:
        if word in wordList:
            wordList.remove(word)

search = ' '.join(wordList)
print(search)
response = wikipedia.summary("Barak Obama", sentences=2)
#$response = wikipedia.page("explain Barak Obama")
print(response)
