# Problem description:
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

def most_words_found(list):
    result = 0
        
    for sentence in list:
        if len(sentence.split(' ')) > result:
            result = len(sentence.split(' '))
                
    return result
  
