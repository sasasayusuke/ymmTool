import pathlib
import json
import shutil
import datetime

formatPath = "format"
jsn = {}
targets = ["いっち", "スレ民A", "スレ民B", "スレ民C", "スレ民D", "スレ民E", "スレ民F"]
idLine = {
            "Start": 0,
            "Length": 0,
            "IsBold": True,
            "IsItalic": False,
            "Scale": 0.75,
            "Font": "Yu Gothic UI Semibold",
            "Foreground": "#FF1AFF76",
            "IsLineBreak": False,
            "HasDecoration": True
}

newPath = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
shutil.copytree('format', newPath)


path = pathlib.Path('./' + newPath).glob('*.ymmp')
for p in path:
    with open(p.absolute(), "r", encoding="utf_8_sig") as infile:
        jsn = json.load(infile)

    for item in jsn["Timeline"]["Items"]:
        if "CharacterName" in item.keys() and item["CharacterName"] in targets:
            idLine["Length"] = len(item["Serif"].split("\r\n")[0])
            item["Decorations"].append(idLine)

            h = item["Hatsuon"].split("\r\n")
            h[0] = ""
            item["Hatsuon"] = "\r\n".join(h)

    with open(p.absolute(), 'w') as outfile:
        json.dump(jsn, outfile, indent=4)
