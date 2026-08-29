st = input("Enter string: ")

words = st.split()
coding = False

nwords = []

if coding:
    for word in words:
        if len(word) >= 3:
            stnew = "sdf" + word[1:] + word[0] + "gfd"
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])

else:
    for word in words:
        if len(word) >= 3:
            stnew = word[3:-3]      
            stnew = stnew[-1] + stnew[:-1]   
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])

print(" ".join(nwords))