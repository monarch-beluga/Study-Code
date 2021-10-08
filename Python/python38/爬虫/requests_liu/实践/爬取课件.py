import requests

url = 'https://s3.ananas.chaoxing.com/doc/00/63/5b/2b4b9585cd1062027224be134c8623f2/thumb/{0}.png'
path = r'E:/temp/'

for i in range(1, 2):
    src_url = url.format(i)
    img = requests.get(url=src_url).content
    with open(path + '{0}.png'.format(i), 'wb') as fp:
        fp.write(img)
    print(i)


