import glob

files = glob.glob("*.html")
for file in files:
    with open(file, "rb") as f:
        data = f.read()
    data = data.replace(b'<meta name="robots" content="noindex">', b"")
    with open(file, "wb") as f:
        data = f.write(data)