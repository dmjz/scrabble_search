import os
import logging
logging.basicConfig(level=logging.DEBUG)


logging.debug('Loading dictionary (word_list_2015.txt)...')
with open(os.path.join(os.getcwd(), 'word_search', 'word_list_2015.txt')) as f:
    wordList = [line.rstrip() for line in f]
    

def removeNonAlpha(word):
    """Remove non-alphabetical characters from string"""
    letters = [l for l in word if l.isalpha()]
    return ''.join(letters)
            
def letterCounts(word):
    """Get dict of letter counts for a word"""
    letters = [l for l in word]
    counts = {}
    for l in letters:
        if l in counts:
            counts[l] += 1
        else:
            counts[l] = 1
    return counts
    
def isLetterSubset(sub, sup):
    """Check if sub letter counts contained in sup letter counts
    i.e. you can form the word rep. by sub out of letters from sup"""
    for letter, count in sub.items():
        if not letter in sup:
            return False
        if sup[letter] < count:
            return False
    return True
    
def basicSearch(word):
    """Search for word in dictionary
    
    Input: str
    Return: list of str (either empty, or contains single word)
    """
    word = word.upper()
    try:
        idx = wordList.index(word)
        return [word]
    except ValueError:
        return []
            
def startSearch(prefix):
    """Search for words starting with prefix
    
    Input: str
    Return: list of str
    """
    prefix = prefix.upper()
    N = len(prefix)
    words = []
    for word in wordList:
        if len(word) >= N and word[:N] == prefix:
            words.append(word)
    return words
    
def endSearch(postfix):
    """Search for words ending in postfix
    
    Input: str
    Return: list of str
    """
    postfix = postfix.upper()
    N = len(postfix)
    words = []
    for word in wordList:
        if len(word) >= N and word[-N:] == postfix:
            words.append(word)
    return words
                
def containSearch(token):
    """Search for words made from string of letters
    
    Input: str
    Return: list of str
    """
    token = token.upper()
    N = len(token)
    words = []
    for word in wordList:
        if len(word) >= N and token in word:
            words.append(word)
    return words
    
def usingLettersSearch(letters):
    """Search for words made from string of letters
    
    Input: str
    Return: list of str
    """
    letters = letters.upper()
    letters = removeNonAlpha(letters)
    counts = letterCounts(letters)
    words = []
    for word in wordList:
        if isLetterSubset(sub=letterCounts(word), sup=counts):
            words.append(word)
    return words
        
