dl_string = "wget \"http://www.uvm.edu/storylab/share/papers/dodds2014a/data/$@\""

print("default:")
print("\techo \"Try another rule\"")
print("")

all_langs = []

for lang in ["english", "chinese", "arabic", "french", "german", "indonesian", "korean", "portuguese", "russian", "spanish"]:
    scores_csv = "labMTscores-%s.csv" % lang
    words_csv = "labMTwords-%s.csv" % lang
    print(scores_csv+":")
    print("\t"+dl_string)
    print("")

    print(words_csv+":")
    print("\t"+dl_string)
    print("")

    print("%s.tsv: %s %s" % (lang, words_csv, scores_csv))
    print("\tpython combine.py $+ > $@")
    print("")

    all_langs.append("%s.tsv" % (lang))

print("all: "+' '.join(all_langs))
print("")
