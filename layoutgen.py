import os
## enter your keymap choice here, valid options are QWERTY and Dvorak
layout = "QWERTY"
name = "cadet"

mapDict = {
    "<TLDE>":"grave",
    "<AE01>":"1",
    "<AE02>":"2",
    "<AE03>":"3",
    "<AE04>":"4",
    "<AE05>":"5",
    "<AE06>":"6",
    "<AE07>":"7",
    "<AE08>":"8",
    "<AE09>":"9",
    "<AE10>":"0",
    "<AE11>":"-",
    "<AE12>":"=",
    "<AD01>":"q",
    "<AD02>":"w",
    "<AD03>":"e",
    "<AD04>":"r",
    "<AD05>":"t",
    "<AD06>":"y",
    "<AD07>":"u",
    "<AD08>":"i",
    "<AD09>":"o",
    "<AD10>":"p",
    "<AD11>":"[",
    "<AD12>":"]",
    "<AC01>":"a",
    "<AC02>":"s",
    "<AC03>":"d",
    "<AC04>":"f",
    "<AC05>":"g",
    "<AC06>":"h",
    "<AC07>":"j",
    "<AC08>":"k",
    "<AC09>":"l",
    "<AC10>":";",
    "<AC11>":"'",
    "<AB01>":"z",
    "<AB02>":"x",
    "<AB03>":"c",
    "<AB04>":"v",
    "<AB05>":"b",
    "<AB06>":"n",
    "<AB07>":"m",
    "<AB08>":",",
    "<AB09>":".",
    "<AB10>":"/",
    "<BKSL>":"\\",
}

# if using US-Qwerty, then the
# layout as defined by the mapDict is technically correct,
# however, for code simplicity it is redfiend
# with a rudunant dictionary below.
# if you are using a key map not provided in this file it may be
# eaiset to simple find how your board maps to qwerty and define it
# overtop the qwerty definition
if layout == "QWERTY":
    layoutDict = {
        "1":"1",
        "2":"2",
        "3":"3",
        "4":"4",
        "5":"5",
        "6":"6",
        "7":"7",
        "8":"8",
        "9":"9",
        "0":"0",
        "a":"a",
        "b":"b",
        "c":"c",
        "d":"d",
        "e":"e",
        "f":"f",
        "g":"g",
        "h":"h",
        "i":"i",
        "j":"j",
        "k":"k",
        "l":"l",
        "m":"m",
        "n":"n",
        "o":"o",
        "p":"p",
        "q":"q",
        "r":"r",
        "s":"s",
        "t":"t",
        "u":"u",
        "v":"v",
        "w":"w",
        "x":"x",
        "y":"y",
        "z":"z",
    }
elif layout == "DVORAK":
    layoutDict = {
        "a":"a",
        "b":"x",
    }
else:
    print("You need to speciy a valid layout!")
    os.exit(100)



capsDict = {
    "a":"A",
    "b":"B",
    "c":"C",
    "d":"D",
    "e":"E",
    "f":"F",
    "g":"G",
    "h":"H",
    "i":"I",
    "j":"J",
    "k":"K",
    "l":"L",
    "m":"M",
    "n":"N",
    "o":"O",
    "p":"P",
    "q":"Q",
    "r":"R",
    "s":"S",
    "t":"T",
    "u":"U",
    "v":"V",
    "w":"W",
    "x":"X",
    "y":"Y",
    "z":"Z",
}

greekDict = {
    "a":"α"
}

symbolicDict = {
    "a":"α"
}

tinyCapsDict = {
    "a":"α"
}

upsidedownDict = {
    "a":"α"
}

largecharDict = {
    "a":"α"
}

def makeblock(mapDict, layoutDict):
    block = ""
    for key,val in mapDict.items():
        layerone = ""
        keyfmt = "\tkey " + key + " {"
        for key2,val2 in layoutDict.items():
            if val == key2:
                print(val2)
                layerone = val2
            #print(key2 + "," + val2 + "," + val)
        #print("{} = {}".format(key, val))
        block = block + keyfmt + "\t[ " + layerone + " ]" + "};\n"
    return(block)


prefix1 = "xkb_symbols \"basic\""
prefix2 = "\n{\n\tname[Group1] = "
prefix3 = "\"{}\"".format(name)
prefix = prefix1 + prefix2 + prefix3
block = makeblock(mapDict, layoutDict)
postfix = "};"
print(prefix)
print(block)
print(postfix)
