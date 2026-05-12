# Use the file name mbox-short.txt as the file name
count = 0
tot_spam = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #print(line.rstrip())
    score_index = line.index("0")
    spam = line[score_index:score_index+6]
    #print(spam)
    count+=1
    tot_spam+=float(spam)
#print(count)
#print(tot_spam)
print("Average spam confidence:", tot_spam/count)