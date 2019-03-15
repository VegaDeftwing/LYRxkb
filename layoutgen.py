import os, sys
import hashlib

# OPTIONS NOT EXPOSED TO CLI
name = "lyrxkb"
layerthreedependent = False #Does layer3 depend on the layout (dvorak/qwerty)

def showhelp():
    print("""
    -nu              --- disable unicode conversion
    QWERTY or DVORAK --- set keymap base
    -nr              --- disable root check
    -h or --help     --- show this help
    -dry             --- dry run, don't do install
    """)
    sys.exit()

if "-h" in sys.argv:
    showhelp()
if "--help" in sys.argv:
    showhelp()

if "-nu" in sys.argv: #no unicode printing
    unicodeOut = False
else:
    unicodeOut = True

if "QWERTY" in sys.argv:
    print("using QWERTY mode")
    layout = "QWERTY" #TODO fix QWERTY mode
elif "DVORAK" in sys.argv:
    print("using DVORAK mode")
    layout = "DVORAK"
elif "-q" in sys.argv:
    layout = "QWERTY" #doesn't matter
else:
    print("Please speciy a keymap - either DVORAK or QWERTY (in all caps)")
    sys.exit()
# This script must be run as root to copy files to the install dir
if "-nr" not in sys.argv:
    if not os.geteuid()==0:
        print("This script must be run as root \nin order to install the files")
        sys.exit('use -nr to disable root check')

qmkLOne = ["ESC", "1", "2", "3", "4", "5", "`", "TT(15)", "6", "7", "8", "9", "0", "BSPC", "TAB", "'", ",", ".", "P", "Y", '\\', "PGUP", "F", "G", "C", "R", "L", "=", "/", "A", "O", "E", "U", "I", "D", "H", "T", "N", "S", "-", "LSPO", ";", "Q", "J", "K", "X", "/", "PGDN", "B", "M", "W", "V", "Z", "RSPC", "LEAD", "TT(1)", "TT(2)", "INS", "DEL", "RCTL", "RALT", "APP", "TT(3)", "TT(4)", "[", "HOME", "END", "]", "UP", "LEFT", "SPC", "LGUI", "DOWN", "RGHT", "ENT", "SPC"]
    

mapDict = { # Dict for actually making the xkb file
    "`": '<TLDE>',
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
    '\\': '<BKSL>', #TODO add backspace, spacebar, modifier keys etc.
}

# if using US-Qwerty, then the layout as defined by the mapDict is technically
# correct, however, for code simplicity it is redefined with a redundant
# dictionary below.
# if you are using a key map not provided in this file it may be eaiset to
# simple find how your board maps to qwerty and define it overtop the qwerty
# definition

# TODO redefnie qwerty map to include all necssary chars for valid
# keymay according to dvo layout
qwertyDict = {
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
        "`":"`",
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
        "-":"&",
        "=":"=",
        "q":"'",
        "w":",",
        "e":".",
        "r":"p",
        "t":"y",
        "y":"f",
        "u":"g",
        "i":"c",
        "o":"r",
        "p":"l",
        "[":"/",
        "]":"+",
        '\\':'\\',
        "a":"a",
        "s":"o",
        "d":"e",
        "f":"u",
        "g":"i",
        "h":"d",
        "j":"h",
        "k":"t",
        "l":"n",
        ";":"s",
        "'":"-",
        "z":";",
        "x":"q",
        "c":"j",
        "v":"k",
        "b":"x",
        "n":"b",
        "m":"m",
        ",":"w",
        ".":"v",
        "/":"z",
    }
    layoutDictU = {
        "1": "!",
        "2": "@",  "3": "#",
        "4": "№",  "5": "%",
        "6": "$",  "7": "¢",
        "8": "©",  "9": "™", "0": "●",
        "/": "?", "`":"~", "-":"_", '\\':'|',
        "=": "^", "]": "}",
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
        ".": "𐄂",
        ",": "✓", "m": "M",
        "n": "N", "b": "B",
        "v": "V", "c": "C",
        "x": "X", "z": "Z",
        "&": "§", "?": "!",
        "+": "*",
    }
else:
    print("You need to speciy a valid layout!")
    os.exit(100)


# Yes, we could use toCaps or whatever, but this should make all of the code a bit more consistant.
# Whatever works, right?
capsDict = {"a":"A","b":"B","c":"C","d":"D","e":"E","f":"F","g":"G","h":"H","i":"I","j":"J","k":"K","l":"L","m":"M","n":"N","o":"O","p":"P","q":"Q","r":"R","s":"S","t":"T","u":"U","v":"V","w":"W","x":"X","y":"Y","z":"Z",
}
# http://stevelosh.com/blog/2012/10/a-modern-space-cadet/
greekDictL = {
"/": "/",
"`": "`",
"=": "=",
"]": "]",
"[": "[",
"'": "'",
";": ";",
"/": "/",
".": ".",
",": ",",
"1":"Ⅰ",
"2":"Ⅱ",
"3":"Ⅲ",
"4":"Ⅳ",
"5":"Ⅴ",
"6":"Ⅵ",
"7":"Ⅶ",
"8":"Ⅷ",
"9":"Ⅸ",
"0":"Ⅹ",
"q":"θ",
"w":"ω",
"e":"ε",
"r":"ρ",
"t":"τ",
"y":"ψ",
"u":"υ",
"i":"ι",
"o":"ο",
"p":"π",
"a":"α",
"s":"σ",
"d":"δ",
"f":"φ",
"g":"γ",
"h":"η",
"j":"ϑ",
"k":"κ",
"l":"λ",
"z":"ζ",
"x":"ξ",
"c":"χ",
"v":"ς",
"b":"β",
"n":"ν",
"m":"μ",
}
greekDictU = {
"/": "/",
"`": "`",
"=": "=",
"]": "]",
"[": "[",
"'": "'",
";": ";",
"/": "/",
".": ".",
",": ",",
"1":"Ⅰ",
"2":"Ⅱ",
"3":"Ⅲ",
"4":"Ⅳ",
"5":"Ⅴ",
"6":"Ⅵ",
"7":"Ⅶ",
"8":"Ⅷ",
"9":"Ⅸ",
"0":"Ⅹ",
"Q":"Θ",
"W":"Ω",
"E":"Ε",
"R":"Ρ",
"T":"Τ",
"Y":"Ψ",
"U":"Υ",
"I":"Ι",
"O":"Ο",
"P":"Π",
"A":"Α",
"S":"Σ",
"D":"Δ",
"F":"Φ",
"G":"Γ",
"H":"Η",
"J":"J",
"K":"Κ",
"L":"Λ",
"Z":"Ζ",
"X":"Ξ",
"C":"Χ",
"V":"V",
"B":"Β",
"N":"Ν",
"M":"Μ",
}
# http://stevelosh.com/blog/2012/10/a-modern-space-cadet/
#
# The following symbolic dict should use a 'qwerty' layout in both Dvorak
# and qwerty mode as the keymay is 'absolute'
symbolicDict = {
"`":"¡",
"0": "ⅹ",
"1": "ⅰ",
"2": "ⅱ",
"3": "ⅲ",
"4": "ⅳ",
"5": "ⅴ",
"6": "ⅵ",
"7": "ⅶ",
"8": "ⅷ",
"9": "ⅸ",
"-":"⎡",
"=":"⎤",
"q":"☐",
"w":"☑",
"e":"☒",
"r":"⎨",
"t":"⎬",
"y":"⎪",
"u":"⎧",
"i":"⎩",
"o":"⎫",
"p":"⎭",
"[":"⎣",
"]":"⎦",
'\\':'\\',
"a":"~",
"s":"(",
"d":")",
"f":"`",
"g":"<",
"h":">",
"j":"[",
"k":"]",
"l":"{",
";":"}",
"'":"⎥",
"z":"U0303",
"x":"U0308",
"c":"U0301",
"v":"U030b",
"b":"≤",
"n":"≥",
"m":"U0306",
",":"︸",
".":"︷",
"/":"⎢",
"&": "&",
"?": "?",
"+": "+",
}

tinyCapsDict = {
"/": "/",
"`": "`",
"=": "=",
"]": "]",
"[": "[",
"'": "'",
";": ";",
"/": "/",
".": ".",
",": ",",
"1":"Ⅰ",
"2":"Ⅱ",
"3":"Ⅲ",
"4":"Ⅳ",
"5":"Ⅴ",
"6":"Ⅵ",
"7":"Ⅶ",
"8":"Ⅷ",
"9":"Ⅸ",
"0":"Ⅹ",
"a":"ᴀ",
"b":"ʙ",
"c":"ᴄ",
"d":"ᴅ",
"e":"ᴇ",
"f":"ғ",
"g":"ɢ",
"h":"ʜ",
"i":"ɪ",
"j":"ᴊ",
"k":"ᴋ",
"l":"ʟ",
"m":"ᴍ",
"n":"ɴ",
"o":"ᴏ",
"p":"ᴘ",
"q":"ǫ",
"r":"ʀ",
"s":"s",
"t":"ᴛ",
"u":"ᴜ",
"v":"ᴠ",
"w":"ᴡ",
"x":"x",
"y":"ʏ",
"z":"ᴢ",
}

upsidedownDict = {
"&": "&",
"+": "+",
"-": "-",
"\\":"\\",
"/": "¡",
"`": "`",
"=": "⅋",
"]": "]",
"[": "[",
"'": "'",
";": ";",
".": ".",
",": ",",
"1":"Ɩ",
"2":"ᄅ",
"3":"Ɛ",
"4":"ㄣ",
"5":"ϛ",
"6":"9",
"7":"ㄥ",
"8":"8",
"9":"6",
"0":"Ⅹ",
"a":"ɐ",
"b":"q",
"c":"ɔ",
"d":"p",
"e":"ǝ",
"f":"ɟ",
"g":"ƃ",
"h":"ɥ",
"i":"ᴉ",
"j":"ɾ",
"k":"ʞ",
"l":"l",
"m":"ɯ",
"n":"u",
"o":"o",
"p":"d",
"q":"b",
"r":"ɹ",
"s":"s",
"t":"ʇ",
"u":"n",
"v":"ʌ",
"w":"ʍ",
"x":"x",
"y":"ʎ",
"z":"z",
}
# https://en.wikipedia.org/wiki/Blackboard_bold #TODO
largecharDict = {
    "a":"α"
}

mathDict = {
"`":"`",
"0": "0",
"1": "1",
"2": "2",
"3": "3",
"4": "4",
"5": "5",
"6": "6",
"7": "7",
"8": "8",
"9": "9",
"-":"≠",
"=":"=",
"q":"∫",
"w":"∠",
"e":"⇒",
"r":"⇔",
"t":"∝",
"y":"∃",
"u":"∄",
"i":"∀",
"o":"∧",
"p":"∨",
"[":"⊕",
"]":"≅",
'\\':'\\',
"a":"√",
"s":"¬",
"d":"∑",
"f":"±",
"g":"∞",
"h":"∅",
"j":"ℕ",
"k":"ℤ",
"l":"ℚ",
";":"ℝ",
"'":"ℂ",
"z":"∈",
"x":"∋",
"c":"∉",
"v":"∌",
"b":"⊂",
"n":"⊃",
"m":"∩",
",":"∪",
".":"←",
"/":"→",
"&": "←",
"?": "→",
"+": "+",
}



# https://en.wikipedia.org/wiki/Tengwar http://freetengwar.sourceforge.net/mapping.html #TODO

def tounicode(key):
    if key == "":
        return("NoSymbol")
    if len(key) >= 2:
        return(key.upper())
    key = "U"+hex(ord(key))[2:].zfill(4)
    return(key.upper())

def invertdict(toinvert):
    inverted_dict = dict([[v,k] for k,v in toinvert.items()])
    return(inverted_dict)

def makeblock(qwertyDict, layerthreedependent, unicodeOut, mapDict, layoutDictL, layoutDictU, layerthreeopt, layerfouropt, layerfiveopt):
    block = ""
    for val, key in mapDict.items():
        layerone = layertwo = layerthree = layerfour = layerfive = ""
        for qw, lo in layoutDictL.items(): # qw stands for qwerty, lo for layout
            if val == qw:
                layerone = lo
                layertwo = layoutDictU[lo]
                if layerthreedependent == True:
                    layerthree = layerthreeopt[lo]
                else:
                    layerthree = layerthreeopt[qw]
                layerfour = layerfouropt[lo]
                layerfive = layerfiveopt[lo]
            keyfmt = "\tkey " + key + " {"
        if unicodeOut == True:
            layerone = tounicode(layerone)
            layertwo = tounicode(layertwo)
            layerthree = tounicode(layerthree)
            layerfour = tounicode(layerfour)
            layerfive = tounicode(layerfive)
        block = block + keyfmt + " [ " + layerone + ", " + layertwo + ", " + layerthree + ", " + layerfour + " ]\t" + "};\n"
    return(block)

def makeQNames(dictA, dictB):
    for A, B in dictB.items():
        h = hashlib.sha1(B.encode("UTF-8"))
        d = h.digest()
        s = ""
        for i in range(0,8): 
            x = d[i] % 52
            if x >= 26:
                s += chr(ord('A') + x - 26)
            else:
                s += chr(ord('a') + x)
        print("\t" + s, end ="")
        print(",  // " + A + ":: " + B)

def makeQmap(dictA, dictB):
    for A, B in dictB.items():
        h = hashlib.sha1(B.encode("UTF-8"))
        d = h.digest()
        s = ""
        for i in range(0,8): 
            x = d[i] % 52
            if x >= 26:
                s += chr(ord('A') + x - 26)
            else:
                s += chr(ord('a') + x)
        print("\t[" + s, end ="]")
        print(" = 0x" + tounicode(B)[1:] + ",  // " + A + ":: " + B)

def getQhash(dictA, dictB, key):
    s = ""
    for A, B in dictB.items():
        if A == key:
            h = hashlib.sha1(B.encode("UTF-8"))
            d = h.digest()
            for i in range(0,8): 
                x = d[i] % 52
                if x >= 26:
                    s += chr(ord('A') + x - 26)
                else:
                    s += chr(ord('a') + x)
    return(s)

def makeqmkline(qwertyDict, qmkLOne, uniDicta, uniDictb, uniDictc, uniDictd):
    print("enum unicode_names {")

    # Generate a hash of the unicode character to be used as a name. This is bad. I don't care.
    makeQNames(qwertyDict, uniDicta)
    makeQNames(qwertyDict, uniDictb)
    makeQNames(qwertyDict, uniDictc)
    makeQNames(qwertyDict, uniDictd)
    print("};")

    print("\nconst uint32_t PROGMEM unicode_map[] = {")
    makeQmap(qwertyDict, uniDicta)
    makeQmap(qwertyDict, uniDictb)
    makeQmap(qwertyDict, uniDictc)
    makeQmap(qwertyDict, uniDictd)
    print("};\n")

    qmkLa = []
    qmkLb = []
    qmkLc = []
    qmkLd = []

    print("[1] = LAYOUT_ergodox_pretty(")
    for key in qmkLOne:
        print("\t", end ="")
        keyHash = getQhash(qwertyDict, uniDicta, key.lower())
        if keyHash != "":
            print("X(" + keyHash + "), //" + key.lower())
        else:
            if key[:-3] == "TT":
                print("TT(" + str(0) + "),")
            else:
                print("KC_" + key + ",")
    print(")")

    print("[2] = LAYOUT_ergodox_pretty(")
    for key in qmkLOne:
        print("\t", end ="")
        keyHash = getQhash(qwertyDict, uniDictb, key.lower())
        if keyHash != "":
            print("X(" + keyHash + "), //" + key.lower())
        else:
            if key[:-3] == "TT":
                print("TT(" + str(0) + "),")
            else:
                print("KC_" + key + ",")
    print(")")

    print("[3] = LAYOUT_ergodox_pretty(")
    for key in qmkLOne:
        print("\t", end ="")
        keyHash = getQhash(qwertyDict, uniDictc, key.lower())
        if keyHash != "":
            print("X(" + keyHash + "), //" + key.lower())
        else:
            if key[:-3] == "TT":
                print("TT(" + str(0) + "),")
            else:
                print("KC_" + key + ",")
    print(")")

    print("[4] = LAYOUT_ergodox_pretty(")
    for key in qmkLOne:
        print("\t", end ="")
        keyHash = getQhash(qwertyDict, uniDictd, key) #greekDictU needs uppercase
        if keyHash != "":
            print("X(" + keyHash + "), //" + key.lower())
        else:
            if key[:-3] == "TT":
                print("TT(" + str(0) + "),")
            else:
                print("KC_" + key + ",")
    print(")")


def doinstall(qwertyDict, layerthreedependent, mapDict, layoutDictL, layoutDictU, symbolicDict, mathDict, upsidedownDict):
    print("----------------Installing-------------------")
    if os.path.isdir("/usr/share/X11/xkb/symbols/"):
        print("Found Directory /usr/share/X11/xkb/symbols/")
    else:
        sys.exit(1)
    if os.path.exists("/usr/share/X11/xkb/rules/evdev.xml"):
        print("Found File /usr/share/X11/xkb/rules/evdev.xml")
    else:
        sys.exit(1)
    # make the file to be installed
    unicodeOut = True #force unicode mode on for actuall file gen
    prefix1 = "xkb_symbols \"basic\""
    prefix2 = "\n{\n\tname[Group1] = "
    prefix3 = "\"{}\"".format(name)
    block = prefix1 + prefix2 + prefix3 + ";"
    print("Generating file...\t", end='')
    block = block + makeblock(qwertyDict, layerthreedependent, unicodeOut, mapDict, layoutDictL, layoutDictU, symbolicDict, mathDict, upsidedownDict)
    block = block + "};"
    print("✓")
    # Write file
    print("Writing file...\t\t", end='')
    layoutfile = open("lyrxkb", "w")
    layoutfile.write(block)
    layoutfile.close()
    print("✓")
    # Copy the file
    print("Copying File...\t\t", end='')
    print("✓")
    # Create backup of rules file
    print("Backing up rules file...\t\t", end='')
    print("✓")
    # Add layout
    print("----------------Completed--------------------")
    print("Use setxkbmap lyrxkb to use the layout")
    print("""
    It may be a good idea to have setxkbmap US
    (or whatever you normally use) in your history so
    you can easily switch back if something went wrong
    """)


if "-v" in sys.argv:
    includes = "include \"level3(caps_switch)\""
    prefix1 = "xkb_symbols \"basic\""
    prefix2 = "\n{\n\tname[Group1] = "
    prefix3 = "\"{}\"".format(name)
    block = includes + prefix1 + prefix2 + prefix3 + ";"
    block = block + makeblock(qwertyDict, layerthreedependent, unicodeOut, mapDict, layoutDictL, layoutDictU, symbolicDict, mathDict, upsidedownDict)
    block = block + "};"
    print(block)
if "-dry" not in sys.argv:
    doinstall(qwertyDict, layerthreedependent, mapDict, layoutDictL, layoutDictU, symbolicDict, mathDict, upsidedownDict)

if "-q" in sys.argv:
    makeqmkline(qwertyDict, qmkLOne, mathDict, symbolicDict, greekDictL, greekDictU )
