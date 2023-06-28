import random
 
def word_generator(str_len):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    word = ""
    while len(word) < str_len:
        word += alphabet[random.randrange(27)]
    return word


def scores(goal, test_str):
    num_score = 0
    for i in range(len(goal)):
        if goal[i] == test_str[i]:
            num_score += 1
    return (num_score / len(goal)) * 100

def main():
    goal_str = "methinks it is like a weasel"
    new_str = word_generator(28)
    best = 0
    count = 0
    result = []
    new_score = scores(goal_str, new_str)
    while new_score < 100 and count < 100000:
        if new_score > best:
            print(new_score, new_str)
            best = new_score
            result.append(best)
        new_str = word_generator(28)
        new_score = scores(goal_str, new_str)
        count += 1
    print(max(result), count)
    return max(result)

  
main()