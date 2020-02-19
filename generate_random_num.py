import random
def generate_random_nums(randomlength):
    random_str = ''
    base_str = '0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str
