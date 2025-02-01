import glob
from tqdm import *

files = glob.glob("*.html")
for file in tqdm(files):
    with open(file, "rb") as f:
        data = f.read()
    data = data.replace(b'<meta name="robots" content="noindex">', b"")
    data = data.replace(b'<head>', b'''<head> 
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-HEFX4ERE73"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-HEFX4ERE73');
</script>
''')
    with open(file, "wb") as f:
        data = f.write(data)