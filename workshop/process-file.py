from BeautifulSoup import BeautifulSoup
import urllib2
page = urllib2.urlopen('http://www.wunderground.com/history/airport/KTYS/2011/10/20/DailyHistory.html')
# optional -------- page = open("DailyHistory.html", "r").read() ----------
page_contents = BeautifulSoup(page)
candidates = page_contents.findAll(attrs={"class":"nobr"})
value = candidates[4].span.string
print value