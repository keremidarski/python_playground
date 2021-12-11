# Problem description:
# https://leetcode.com/problems/truncate-sentence/

def truncate_sentence(s, k):
    truncated = []
    counter = 0
    
    for char in s:
        if char == ' ':
            counter += 1
            if counter < k:
                truncated.append(char)
            else:
                break
        else:
            truncated.append(char)

    s = ''.join(truncated)
    
    return s

# Expected: 'Hello how are you'
print(truncate_sentence('Hello how are you Contestant', 4))
