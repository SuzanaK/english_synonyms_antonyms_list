import codecs
from bs4 import BeautifulSoup

# html file downloaded at http://www.gutenberg.org/files/28900/28900-h/28900-h.htm
# (website does not allow online crawling)

fh = codecs.open('syns.htm', 'r', 'iso-8859-1')
html = fh.read()
soup = BeautifulSoup(html)

keywords = soup.select('h3')
print keywords[:10]

out = codecs.open('syns.csv', 'w', 'utf-8')
for k in keywords:

    keyword = k.text.lower().replace('.', '')
    if len(keyword.split(',')) > 1:
        keyword = keyword.split(',')[0]

    h4 = k.find_next_sibling('h4')
    syns = ""
    if 'Synonyms' in h4.text:

        table = h4.find_next()
        if table and table.name == 'table':
            syns_tds = table.find_all('td')
            syns = [s.text.replace(',', '') for s in syns_tds]
            syns = [s.replace('.', '') for s in syns]
            syns = ", ".join(syns)

    h4 = h4.find_next_sibling('h4')
    ants = ""
    if 'Antonyms' in h4.text:

        table = h4.find_next()
        if table and table.name == 'table':
            ant_tds = table.find_all('td')
            ants = [s.text.replace(',', '') for s in ant_tds]
            ants = [s.replace('.', '') for s in ants]
            ants = ", ".join(ants)

    out.write(keyword + "\t" + syns + "\t" + ants + "\n")
    if 'youthful' in keyword:
      break

out.close()



       




