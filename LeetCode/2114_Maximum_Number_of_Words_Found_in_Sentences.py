# Problem description:
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

def most_words_found(sentences):
    result = 0
        
    for sentence in sentences:
        if len(sentence.split(' ')) > result:
            result = len(sentence.split(' '))
                
    return result

# Expected: 6
print(most_words_found(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
