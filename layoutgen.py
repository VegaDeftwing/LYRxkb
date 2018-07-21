import os
## enter your keymap choice here, valid options are QWERTY and Dvorak
layout = "QWERTY"
name = "cadet"

mapDict = {
'grave': '<TLDE>',
    '1': '<AE01>',
    '2': '<AE02>',
    '3': '<AE03>',
    '4': '<AE04>',
    '5': '<AE05>',
    '6': '<AE06>',
    '7': '<AE07>',
    '8': '<AE08>',
    '9': '<AE09>',
    '0': '<AE10>',
    '-': '<AE11>',
    '=': '<AE12>',
    'q': '<AD01>',
    'w': '<AD02>',
    'e': '<AD03>',
    'r': '<AD04>',
    't': '<AD05>',
    'y': '<AD06>',
    'u': '<AD07>',
    'i': '<AD08>',
    'o': '<AD09>',
    'p': '<AD10>',
    '[': '<AD11>',
    ']': '<AD12>',
    'a': '<AC01>',
    's': '<AC02>',
    'd': '<AC03>',
    'f': '<AC04>',
    'g': '<AC05>',
    'h': '<AC06>',
    'j': '<AC07>',
    'k': '<AC08>',
    'l': '<AC09>',
    ';': '<AC10>',
    "'": '<AC11>',
    'z': '<AB01>',
    'x': '<AB02>',
    'c': '<AB03>',
    'v': '<AB04>',
    'b': '<AB05>',
    'n': '<AB06>',
    'm': '<AB07>',
    ',': '<AB08>',
    '.': '<AB09>',
    '/': '<AB10>',
    '\\': '<BKSL>',
}

# if using US-Qwerty, then the layout as defined by the mapDict is technically
# correct, however, for code simplicity it is redefined with a redundant
# dictionary below.
# if you are using a key map not provided in this file it may be eaiset to
# simple find how your board maps to qwerty and define it overtop the qwerty
# definition
if layout == "QWERTY":
    layoutDictL = {
        "0": "0",  "1": "1",
        "2": "2",  "3": "3",
        "4": "4",  "5": "5",
        "6": "6",  "7": "7",
        "8": "8",  "9": "9",
        "/": "/", "`": "`",
        "=": "=", "]": "]",
        "[": "[", "p": "p",
        "o": "o", "i": "i",
        "u": "u", "y": "y",
        "t": "t", "r": "r",
        "e": "e", "w": "w",
        "q": "q", "'": "'",
        ";": ";", "l": "l",
        "k": "k", "j": "j",
        "h": "h", "g": "g",
        "f": "f", "d": "d",
        "s": "s", "a": "a",
        "/": "/", ".": ".",
        ",": ",", "m": "m",
        "n": "n", "b": "b",
        "v": "v", "c": "c",
        "x": "x", "z": "z",
    }
    layoutDictU = {
        "0": ")",  "1": "!",
        "2": "@",  "3": "#",
        "4": "$",  "5": "%",
        "6": "^",  "7": "&",
        "8": "*",  "9": "(",
        "/": "?", "`":"~",
        "=": "+", "]": "}",
        "[": "{", "p": "P",
        "o": "O", "i": "I",
        "u": "U", "y": "Y",
        "t": "T", "r": "R",
        "e": "E", "w": "W",
        "q": "Q", "'": '"',
        ";": ":", "l": "L",
        "k": "K", "j": "J",
        "h": "H", "g": "G",
        "f": "F", "d": "D",
        "s": "S", "a": "A",
        "/": "?", ".": ">",
        ",": "<", "m": "M",
        "n": "N", "b": "B",
        "v": "V", "c": "C",
        "x": "X", "z": "Z",
    }
elif layout == "DVORAK":
    layoutDictL = {
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
            ";": ";",  ":": ":",  "λ": "l",  "Λ": "L",
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
def invertdict(toinvert):
    inverted_dict = dict([[v,k] for k,v in toinvert.items()])
    return(inverted_dict)

def makeblock(mapDict, layoutDictL, layoutDictU, layerthreeopt):
    block = ""
    layerthreeopt =  invertdict(layerthreeopt)
    for val, key in mapDict.items():
        layerone = layertwo = layerthree = ""
        for key2, val2 in layoutDictL.items():
            if val == key2:
                layerone = val2
                layertwo = layoutDictU[val2]
                layerthree = layerthreeopt[val2]
        keyfmt = "\tkey " + key + " {"
        block = block + keyfmt + "\t[ " + layerone + ", " + layertwo + ", " + layerthree + " ]" + "};\n"
    return(block)


prefix1 = "xkb_symbols \"basic\""
prefix2 = "\n{\n\tname[Group1] = "
prefix3 = "\"{}\"".format(name)
prefix = prefix1 + prefix2 + prefix3
block = makeblock(mapDict, layoutDictL, layoutDictU, greekDict)
postfix = "};"
print(prefix)
print(block)
print(postfix)
