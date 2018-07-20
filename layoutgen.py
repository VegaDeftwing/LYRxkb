import os
## enter your keymap choice here, valid options are QWERTY and Dvorak
layout = "QWERTY"
name = "cadet"

mapDict = {
    "<TLDE>": "grave",
    "<AE01>": "1", "<AE02>": "2",
    "<AE03>": "3", "<AE04>": "4",
    "<AE05>": "5", "<AE06>": "6",
    "<AE07>": "7", "<AE08>": "8",
    "<AE09>": "9", "<AE10>": "0",
    "<AE11>": "-", "<AE12>": "=",
    "<AD01>": "q", "<AD02>": "w",
    "<AD03>": "e", "<AD04>": "r",
    "<AD05>": "t", "<AD06>": "y",
    "<AD07>": "u", "<AD08>": "i",
    "<AD09>": "o", "<AD10>": "p",
    "<AD11>": "[", "<AD12>": "]",
    "<AC01>": "a", "<AC02>": "s",
    "<AC03>": "d", "<AC04>": "f",
    "<AC05>": "g", "<AC06>": "h",
    "<AC07>": "j", "<AC08>": "k",
    "<AC09>": "l", "<AC10>": ";",
    "<AC11>": "'", "<AB01>": "z",
    "<AB02>": "x", "<AB03>": "c",
    "<AB04>": "v", "<AB05>": "b",
    "<AB06>": "n", "<AB07>": "m",
    "<AB08>": ",", "<AB09>": ".",
    "<AB10>": "/", "<BKSL>": "\\",
}

# if using US-Qwerty, then the layout as defined by the mapDict is technically
# correct, however, for code simplicity it is redefined with a redundant
# dictionary below.
# if you are using a key map not provided in this file it may be eaiset to
# simple find how your board maps to qwerty and define it overtop the qwerty
# definition
if layout == "QWERTY":
    layoutDict = {
        "0": "0",  "1": "1",  "2": "2",  "3": "3",
        "4": "4",  "5": "5",  "6": "6",  "7": "7",
        "8": "8",  "9": "9",  "/": "/",  "+": "+",
        "=": "=",  "?": "?",  "]": "]",  "}": "}",
        "[": "[",  "{": "{",  "p": "p",  "P": "P",
        "o": "o",  "O": "O",  "i": "i",  "I": "I",
        "u": "u",  "U": "U",  "y": "y",  "Y": "Y",
        "t": "t",  "T": "T",  "r": "r",  "R": "R",
        "e": "e",  "E": "E",  "w": "w",  "W": "W",
        "q": "q",  "Q": "Q",  "'": "'",  '"': '"',
        ";": ";",  ":": ":",  "l": "l",  "L": "L",
        "k": "k",  "K": "K",  "j": "j",  "J": "J",
        "h": "h",  "H": "H",  "g": "g",  "G": "G",
        "f": "f",  "F": "F",  "d": "d",  "D": "D",
        "s": "s",  "S": "S",  "a": "a",  "A": "A",
        "/": "/",  "?": "?",  ".": ".",  ">": ">",
        ",": ",",  "<": "<",  "m": "m",  "M": "M",
        "n": "n",  "N": "N",  "b": "b",  "B": "B",
        "v": "v",  "V": "V",  "c": "c",  "C": "C",
        "x": "x",  "X": "X",  "z": "z",  "Z": "Z",
    }
elif layout == "DVORAK":
    layoutDict = {
        "0": "0",  "1": "1",  "2": "2",  "3": "3",
        "4": "4",  "5": "5",  "6": "6",  "7": "7",
        "8": "8",  "9": "9",  "]": "/",  "}": "+",
        "[": "=",  "{": "?",  "=": "]",  "+": "}",
        "/": "[",  "?": "{",  "l": "p",  "L": "P",
        "r": "o",  "R": "O",  "c": "i",  "C": "I",
        "g": "u",  "G": "U",  "f": "y",  "F": "Y",
        "y": "t",  "Y": "T",  "p": "r",  "P": "R",
        ".": "e",  ">": "E",  ",": "w",  "<": "W",
        "'": "q",  '"': "Q",  "-": "'",  "_": '"',
        "s": ";",  "S": ":",  "n": "l",  "N": "L",
        "t": "k",  "T": "K",  "h": "j",  "H": "J",
        "d": "h",  "D": "H",  "i": "g",  "I": "G",
        "u": "f",  "U": "F",  "e": "d",  "E": "D",
        "o": "s",  "O": "S",  "a": "a",  "A": "A",
        "z": "/",  "Z": "?",  "v": ".",  "V": ">",
        "w": ",",  "W": "<",  "m": "m",  "M": "M",
        "b": "n",  "B": "N",  "x": "b",  "X": "B",
        "k": "v",  "K": "V",  "j": "c",  "J": "C",
        "q": "x",  "Q": "X",  ";": "z",  ":": "Z",
    }
else:
    print("You need to speciy a valid layout!")
    os.exit(100)


# Yes, we could use toCaps or whatever, but this should make all of the code a bit more consistant.
# Whatever works, right?
capsDict = {"a":"A","b":"B","c":"C","d":"D","e":"E","f":"F","g":"G","h":"H","i":"I","j":"J","k":"K","l":"L","m":"M","n":"N","o":"O","p":"P","q":"Q","r":"R","s":"S","t":"T","u":"U","v":"V","w":"W","x":"X","y":"Y","z":"Z",
}
# http://stevelosh.com/blog/2012/10/a-modern-space-cadet/
greekDict = {
            "0": "0",  "1": "1",  "2": "2",  "3": "3",
            "4": "4",  "5": "5",  "6": "6",  "7": "7",
            "8": "8",  "9": "9",  "/": "/",  "+": "+",
            "=": "=",  "?": "?",  "]": "]",  "}": "}",
            "[": "[",  "{": "{",  "π": "p",  "Π": "P",
            "ο": "o",  "Ο": "O",  "ι": "i",  "Ι": "I",
            "υ": "u",  "Υ": "U",  "ψ": "y",  "Ψ": "Y",
            "τ": "t",  "Τ": "T",  "ρ": "r",  "Ρ": "R",
            "ε": "e",  "Ε": "E",  "ω": "w",  "Ω": "W",
            "θ": "q",  "Θ": "Q",  "'": "'",  '"': '"',
            ";": ";",  ":": ":",  "λ": "Λ",  "L": "L",
            "κ": "k",  "Κ": "K",  "ϑ": "j",  "J": "J",
            "η": "h",  "Η": "H",  "γ": "g",  "Γ": "G",
            "φ": "f",  "Φ": "F",  "δ": "d",  "Δ": "D",
            "σ": "s",  "Σ": "S",  "α": "a",  "Α": "A",
            "/": "/",  "?": "?",  ".": ".",  ">": ">",
            ",": ",",  "<": "<",  "μ": "m",  "Μ": "M",
            "ν": "n",  "Ν": "N",  "β": "b",  "Β": "B",
            "ς": "v",  "V": "V",  "χ": "c",  "Χ": "C",
            "ξ": "x",  "Ξ": "X",  "ζ": "z",  "Ζ": "Z",
}
# http://stevelosh.com/blog/2012/10/a-modern-space-cadet/
symbolicDict = {
    "a":"α"
}

# ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ
tinyCapsDict = {
    "a":"α"
}
# ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎzƖᄅƐㄣϛ9ㄥ86¡⅋({
upsidedownDict = {
    "a":"α"
}
# https://en.wikipedia.org/wiki/Blackboard_bold
largecharDict = {
    "a":"α"
}

# https://en.wikipedia.org/wiki/Tengwar http://freetengwar.sourceforge.net/mapping.html


def makeblock(mapDict, layoutDict):
    block = ""
    for key, val in mapDict.items():
        layerone = layertwo = ""
        keyfmt = "\tkey " + key + " {"
        for key2, val2 in layoutDict.items():
            if val == key2:
                layerone = val2
                layertwo = layoutDict[val2.capitalize()]
        for key2, val2 in layoutDict.items():
            if val == key2:
                layerone = val2
            #print(key2 + "," + val2 + "," + val)
        #print("{} = {}".format(key, val))
        block = block + keyfmt + "\t[ " + layerone + ", " + layertwo + " ]" + "};\n"
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
