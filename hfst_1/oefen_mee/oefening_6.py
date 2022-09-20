engels_nederlands = { "last":"laatste", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal",
"saw":"zaag", "first":"eerst", "performance":"optreden",
"of":"van", "a":"een", "new":"nieuw", "symphony":"symfonie",
"by":"bij", "one":"een", "world":"wereld", "leading":
"leidend", "modern":"modern", "composer":"componist",
"composers":"componisten", "two":"twee", "shed":"schuur",
"sheds":"schuren" }

zin = input("Geef een zin in het nederlands: ")
lijst_gesplitst = zin.split()
key_list = list(engels_nederlands.keys())
val_list = list(engels_nederlands.values())
for woord in lijst_gesplitst:
    position = val_list.index(woord)
    engels = key_list[position]
    if engels in engels_nederlands:
        locatie = lijst_gesplitst.index(woord)
        lijst_gesplitst.remove(woord)
        lijst_gesplitst.insert(locatie, engels)
zin = " ".join(lijst_gesplitst)
print(zin)


# nederlands naar engels!!!!!!!!!!!!!!!