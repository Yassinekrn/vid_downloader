# just for tests, nth special

def non_spc_carc(string):
    res = string
    for i in range(0, len(string)-1):
        if string[i] in ["\\", "/", ":", "*", "?", "<", ">", "|"]:
            res = res[0: i] + res[i+1: len(res)]
    return res


res = non_spc_carc("What | Yasuo")
print(res)
