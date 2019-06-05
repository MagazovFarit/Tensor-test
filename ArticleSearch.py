import sys
import urllib.request

# gets url
script, url = sys.argv

# gets index.html
with urllib.request.urlopen(url) as response:
   html = response.read().decode('utf-8')

class Article:

    def __init__(self):
        self.title = ''
        self.paragraphs = []

    def AddTitle(self,title):
        self.title = title

    def AddParagraph(self, paragraph):
        self.paragraphs.append(paragraph)

    def FindUrl(self, paragraph):
        newparagraph = ''
        i = 0
        while paragraph.find('<a ', i) > 0:
            newparagraph += paragraph[i:paragraph.find('<a ', i)]
            urlstart = paragraph.find('"', i)
            urlend = paragraph.find('"',urlstart+1)
            newparagraph += '[' + paragraph[urlstart:urlend] + '] '
            urltextstart = paragraph.find('>', i) + 1
            urltextend = paragraph.find('</a', i)
            newparagraph += paragraph[urltextstart:urltextend]
            i = paragraph.find('>', urltextend) + 1
        newparagraph += paragraph[i:len(paragraph)]
        return newparagraph
    
    def ParseArticle(self, html):
        i = 0
        while html.find('<p', i) > 0:
            paragraph = ''
            k = html.find('<p', i)
            i = html.find('>', k)
            if i - k < 140:
                paragraph += html[i+1:html.find('</p', i)]
                paragraph = self.FindUrl(paragraph)
                if paragraph != '':
                    self.AddParagraph(paragraph+'\r\n\r\n')

    def WriteArticle(self, html):
        self.ParseArticle(html)
        output = open('index.txt', 'wb')
        for paragraph in article.paragraphs:
            strstart = 0
            i = paragraph.find(' ', 0)
            while i > 0:
                if paragraph.find(' ', i) - strstart > 80:
                    stringtowrite = paragraph[strstart:i]+'\r\n'
                    output.write(stringtowrite.encode('utf-8'))
                    strstart = i + 1
                i = paragraph.find(' ', i+1)
            output.write(paragraph[strstart:len(paragraph)].encode('utf-8'))
        output.close()

article = Article()
article.WriteArticle(html)




