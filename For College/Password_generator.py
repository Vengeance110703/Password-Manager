import random

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lowercase = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
uppercase = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
symbols = [
    "@",
    "#",
    "$",
    "%",
    "=",
    ":",
    "?",
    ".",
    "/",
    "|",
    "~",
    ">",
    "*",
    "(",
    ")",
    "<",
]

rand_digit = random.choice(digits)
rand_upper = random.choice(uppercase)
rand_lower = random.choice(lowercase)
rand_symbol = random.choice(symbols)

randomlst = [
    "rand_digit",
    "rand_lower",
    "rand_upper",
    "rand_symbol",
]
lists = ["digits", "lowercase", "uppercase", "symbols"]


def generator(max_len, choice):
    combined = []
    temp_pass_list = []
    temp_pass = ""
    cnt = 0

    for x in range(0, 4):
        if choice[x]:
            temp_pass = temp_pass + eval(randomlst[x])
            combined = combined + eval(lists[x])
            cnt = cnt + 1

    for x in range(max_len - cnt):
        temp_pass = temp_pass + random.choice(combined)
        temp_pass_list = list(filter(lambda i: (i in temp_pass), temp_pass))
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x

    return password
