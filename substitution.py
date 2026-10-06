#lesson 4/ week 1

from collections import Counter
import string

ciphertext = """
ZOZM NZGSRHLM GFIRMT DZH Z YIRGRHS NZGSVNZGRXRZM, OLTRXRZM, XIBKGZMZOBHG, ZMW XLNKFGVI HXRVMGRHG. SV DZH SRTSOB RMUOFVMGRZO RM GSV WVEVOLKNVMG LU XLNKFGVI HXRVMXV, KILERWRMT Z ULINZORHZGRLM LU GSV XLMXVKGH LU "ZOTLIRGSN" ZMW "XLNKFGZGRLM" DRGS GSV GFIRMT NZXSRMV. GFIRMT RH DRWVOB XLMHRWVIVW GL YV GSV UZGSVI LU XLNKFGVI HXRVMXV ZMW ZIGRURXRZO RMGVOORTVMXV.

WFIRMT DLIOW DZI RR, GFIRMT DLIPVW ULI GSV TLEVIMNVMG XLWV ZMW XBKSVI HXSLLO (TXXH) ZG YOVGXSOVB KZIP, YIRGZRM'H XLWVYIVZPRMT XVMGIV.

ULI Z GRNV SV DZH SVZW LU SFG 8, GSV HVXGRLM IVHKLMHRYOV ULI TVINZM MZEZO XIBKGZMZOBHRH. SV WVERHVW Z MFNYVI LU GVXSMRJFVH ULI YIVZPRMT TVINZM XRKSVIH, RMXOFWRMT GSV NVGSLW LU GSV YLNYV, ZM VOVXGILNVXSZMRXZO NZXSRMV GSZG XLFOW URMW HVGGRMTH ULI GSV VMRTNZ NZXSRMV.

ZUGVI GSV DZI SV DLIPVW ZG GSV MZGRLMZO KSBHRXZO OZYLIZGLIB, DSVIV SV XIVZGVW LMV LU GSV URIHG WVHRTMH ULI Z HGLIVW-KILTIZN XLNKFGVI, GSV ZXV.

RM 1948 GFIRMT QLRMVW NZC MVDNZM'H XLNKFGRMT OZYLIZGLIB ZG NZMXSVHGVI FMREVIHRGB, DSVIV SV ZHHRHGVW RM GSV WVEVOLKNVMG LU GSV NZMXSVHGVI XLNKFGVIH ZMW YVXZNV RMGVIVHGVW RM NZGSVNZGRXZO YRLOLTB.

SV DILGV Z KZKVI LM GSV XSVNRXZO YZHRH LU NLIKSLTVMVHRH, ZMW KIVWRXGVW LHXROOZGRMT XSVNRXZO IVZXGRLMH HFXS ZH GSV YVOLFHLE-ASZYLGRMHPB IVZXGRLM, DSRXS DVIV URIHG LYHVIEVW RM GSV 1960H.

GFIRMT'H SLNLHVCFZORGB IVHFOGVW RM Z XIRNRMZO KILHVXFGRLM RM 1952, DSVM SLNLHVCFZO ZXGH DVIV HGROO ROOVTZO RM GSV FMRGVW PRMTWLN. SV ZXXVKGVW GIVZGNVMG DRGS UVNZOV SLINLMVH (XSVNRXZO XZHGIZGRLM) ZH ZM ZOGVIMZGREV GL KIRHLM.

GFIRMT WRVW RM 1954, QFHG LEVI GDL DVVPH YVULIV SRH 42MW YRIGSWZB, UILN XBZMRWV KLRHLMRMT. ZM RMJFVHG WVGVINRMVW GSZG SRH WVZGS DZH HFRXRWV; SRH NLGSVI ZMW HLNV LGSVIH YVORVEVW SRH WVZGS DZH ZXXRWVMGZO.

LM 10 HVKGVNYVI 2009, ULOOLDRMT ZM RMGVIMVG XZNKZRTM, YIRGRHS KIRNV NRMRHGVI TLIWLM YILDM NZWV ZM LUURXRZO KFYORX ZKLOLTB LM YVSZOU LU GSV YIRGRHS TLEVIMNVMG ULI "GSV ZKKZOORMT DZB SV DZH GIVZGVW."

ZH LU NZB 2012 Z KIREZGV NVNYVI'H YROO DZH YVULIV GSV SLFHV LU OLIWH DSRXS DLFOW TIZMG GFIRMT Z HGZGFGLIB KZIWLM RU VMZXGVW.
"""

# Standard English letter frequency, highest to lowest
english_frequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

# Remove spaces, punctuation and numbers
letters_only = [
    ch for ch in ciphertext.upper()
    if ch in string.ascii_uppercase
]

# Count frequency of each cipher letter
counts = Counter(letters_only)

# Sort cipher letters from most common to least common
cipher_frequency = "".join(
    letter for letter, count in counts.most_common()
)

print("Letter frequencies:")
for letter, count in counts.most_common():
    percentage = (count / len(letters_only)) * 100
    print(f"{letter}: {count:4} ({percentage:.2f}%)")

print("\nCipher frequency order:")
print(cipher_frequency)

print("\nExpected English frequency:")
print(english_frequency)

# Create an initial substitution key using frequency analysis
mapping = {}

for cipher_letter, english_letter in zip(
    cipher_frequency, english_frequency
):
    mapping[cipher_letter] = english_letter

print("\nInitial frequency mapping:")
for cipher_letter, plain_letter in mapping.items():
    print(f"{cipher_letter} -> {plain_letter}")

# Produce initial guessed plaintext
guessed_text = ""

for ch in ciphertext.upper():
    if ch in mapping:
        guessed_text += mapping[ch]
    else:
        guessed_text += ch

print("\nInitial frequency-analysis guess:")
print(guessed_text)


# --------------------------------------------------------
# After examining the frequencies and word patterns,
# this ciphertext can be identified as an Atbash cipher.
# In Atbash:
#
# A <-> Z
# B <-> Y
# C <-> X
# ...
# --------------------------------------------------------

alphabet = string.ascii_uppercase
reverse_alphabet = alphabet[::-1]

atbash_key = dict(zip(alphabet, reverse_alphabet))

plaintext = ""

for ch in ciphertext.upper():
    if ch in atbash_key:
        plaintext += atbash_key[ch]
    else:
        plaintext += ch

print("\nFinal decrypted plaintext:")
print(plaintext)
