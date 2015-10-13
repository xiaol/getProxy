from lxml import etree
from page import get_page
import urllib2
from StringIO import StringIO

of = open('proxy.txt' , 'w')

for page in range(1, 160):
    text = get_page('http://www.xicidaili.com/nn/' + str(page))
    parser = etree.HTMLParser()
    tree = etree.parse(StringIO(text), parser)

    trs = tree.xpath('.//tr')
    for tr in trs[1:]:
        tds = tr.xpath('.//td')
        ip = tds[2].text.strip()
        port = tds[3].text.strip()
        protocol = tds[6].text.strip()
        if protocol == 'HTTP' or protocol == 'HTTPS':
            of.write('%s=%s:%s\n' % (protocol, ip, port) )
            print '%s=%s:%s' % (protocol, ip, port)
    break
of.close()
