# Glen Paul Florendo
# COMPTNG16
# October 11, 2017

loremIpsumText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

loremIpsumList = loremIpsumText.split()

# Task 1
loremIpsumDict = {w: loremIpsumList.count(w) for w in loremIpsumList}

# Task 2
loremIpsumUniqCount = len(loremIpsumDict)

# Task 3
def uniq(text=""):
    if not text: # if empty string
        return None

    uniqDict = {}

    for word in text:
        if word not in uniqDict:
            uniqDict[word] = 1
        else: # word is in uniqDict
            uniqDict[word] = uniqDict.get(word) + 1
    return uniqDict


