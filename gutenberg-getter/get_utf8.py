import fileinput
import os, sys
import zipfile

numToPath = {}

for line in fileinput.input():
    path = line.strip()
    base = os.path.basename(path)
    (root, ext) = os.path.splitext(base)
    if ext != '.zip':
        continue
    num = root
    if '-' in root:
        num = root.split('-')[0]
    if num not in numToPath:
        numToPath[num] = []
    numToPath[num].append((root, path))

print(len(numToPath))

nums = sorted(numToPath.keys(), key=lambda x: int(x))

with zipfile.ZipFile('gutenberg.utf8.zip', 'w', allowZip64=True) as fp:
    for num in nums:
        opts = numToPath[num]
        (root, path) = opts[0]
        # prefer utf-8 if available:
        if len(opts) > 1:
            for (proot, popt) in opts:
                if '-8' in proot:
                    root = proot
                    path = popt
                    break
        # open path as zipfile:
        zpath = root+'.txt'
        print(num, zpath, path)
        text = ""
        with zipfile.ZipFile(path, 'r') as zf:
            for nm in zf.infolist():
                if nm.filename.endswith(zpath):
                    text = zf.read(nm.filename)
                    break
        if text:
            fp.writestr(num, text, zipfile.ZIP_DEFLATED)

