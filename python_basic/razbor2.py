import os
import hashlib

def getMD5sum(fileName):
    m = hashlib.md5()
    fd = open(fileName, 'rb')
    b = fd.read()
    m.update(b)
    fd.close()
    return m.hexdigest()

output = ''
rootpath = '/run/media/yuri/WORK/'

for dirname, dirnames, filenames in os.walk(rootpath):
    for filename in filenames:
        fname = os.path.join(dirname, filename).replace('\\', '/')
        md5sum = getMD5sum(fname)
        output+='{0}:{1}\n'.format(fname.replace(rootpath, ''), md5sum)

f = open('./checksums.csv', 'w')
f.write(output)
f.close()