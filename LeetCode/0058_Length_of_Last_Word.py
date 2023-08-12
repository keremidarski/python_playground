# Problem description:
# https://leetcode.com/problems/length-of-last-word/


def get_len_of_last_word(string):
  return len(string.strip().split(" ")[-1])

           
# Expected: 6
print(get_len_of_last_word("luffy is still joyboy")
# Expected: 4
print(get_len_of_last_word("   fly me   to   the moon  ")
      
