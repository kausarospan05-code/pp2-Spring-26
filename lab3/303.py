# Dictionary: word to digit
w2d = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}

# Reverse dictionary: digit to  word
d2w = {v: k for k, v in w2d.items()}

# Function: convert арыптерды сандарга
def words_to_num(s):
    num = ""
    i = 0
    while i < len(s):
        for w in w2d:
            if s.startswith(w, i):   # check if substring starts with a word
                num += w2d[w]        # сол создын цифрын косамыз 
                i += len(w)          # move index алдыға
                break
    return int(num) #уанфор-14

# Function: сандарды арыптерге
def num_to_words(n):
    return "".join(d2w[d] for d in str(n)) #14 bolsa -onefou


expr = input().strip()   # reads :one+two

# Find operator and split into left/right parts
if "+" in expr:
    left, right = expr.split("+")
    res = words_to_num(left) + words_to_num(right)#ornekte+ bolsa
elif "-" in expr:
    left, right = expr.split("-")
    res = words_to_num(left) - words_to_num(right)
elif "*" in expr:
    left, right = expr.split("*")
    res = words_to_num(left) * words_to_num(right)

# Print result in word form
print(num_to_words(res))
#input one+two
#process:1 +2=3
#out thr