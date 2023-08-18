from collections import deque

def palindrome(word):
    word_deq = deque()
    for char in word:
        word_deq.append(char)
    
    while len(word_deq) > 1:
        rear_char = word_deq.popleft()
        front_char = word_deq.pop()
        if rear_char != front_char:
            return False
    return True

print(palindrome("rear"))