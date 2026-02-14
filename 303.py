# Dictionary: word -> digit
w2d = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}

# Reverse dictionary: digit -> word
d2w = {v: k for k, v in w2d.items()}

# Function: convert арыптерды сандарга
def words_to_num(s):
    num = ""
    i = 0
    while i < len(s):
        for w in w2d:
            if s.startswith(w, i):   # check if substring starts with a word
                num += w2d[w]        # add digit to number string
                i += len(w)          # move index forward
                break
    return int(num)

# Function: сандарды арыптерге
def num_to_words(n):
    return "".join(d2w[d] for d in str(n))


expr = input().strip()   # read input string

# Find operator and split into left/right parts
if "+" in expr:
    left, right = expr.split("+")
    res = words_to_num(left) + words_to_num(right)
elif "-" in expr:
    left, right = expr.split("-")
    res = words_to_num(left) - words_to_num(right)
elif "*" in expr:
    left, right = expr.split("*")
    res = words_to_num(left) * words_to_num(right)

# Print result in word form
print(num_to_words(res))