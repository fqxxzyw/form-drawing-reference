"""Restore bundled Three.js and model assets, without network access."""
from pathlib import Path
import base64
import hashlib
import io
import json
import zipfile

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'resources/manifest.json').read_text())
archive = b''.join(base64.b64decode((root / name).read_text().strip(), validate=True)
                   for name in manifest['parts'])
if hashlib.sha256(archive).hexdigest() != manifest['sha256']:
    raise SystemExit('资源校验失败，请重新下载仓库。')
with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
    for entry in bundle.infolist():
        target = (root / entry.filename).resolve()
        if root not in target.parents:
            raise SystemExit('资源包路径无效。')
    bundle.extractall(root)
print('资源已还原。运行 python -m http.server 8000 --directory dist')
