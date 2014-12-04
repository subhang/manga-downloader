from bs4 import BeautifulSoup
import urllib2
import os

curr_dir = os.getcwd()
main_soup = BeautifulSoup("<html>Hi</html>")
def get_image(html):
    soup = BeautifulSoup(html)
    images = soup.findAll("img",{"id":"image"})
    link = images[0]["src"]
    return urllib2.urlopen(link)

def download_chapter(manga,v,num):
        os.chdir(curr_dir)
        if(not(os.path.isdir(str(num)))):
            os.mkdir(str(num))
        os.chdir(str(num))
        url = "http://mangafox.me/manga/"
        vol = str(v)
        url = url+manga+"/v"
        temp = v[1:]
        url = url+temp
        url = url+"/c"+str(num)+"/"
        for i in range (1,23):
            link = url+str(i)+".html"
            
            image = get_image(urllib2.urlopen(link))
            output = open(str(i)+".jpg","wb")
            output.write(image.read())
            output.close()
                  
def get_info(link):
    a = link.split("/")
    volume = a[5]
    chapter = a[6]
    return volume,chapter

def get_volume(num):
    temp = str(num)
    for i in mylinks:
        if(i["href"].find(temp) != -1):
            chapter,volume = get_info(i["href"])
            return volume

manga = raw_input("Enter The Manga Name: ")
link = "http://mangafox.me/manga/"
link += manga+"/"
response = urllib2.urlopen(link)
html = response.read()
main_soup = BeautifulSoup(html)
mylinks = main_soup.findAll("a",{"class":"tips"})
max_vol,max_chap = get_info(mylinks[0]["href"])    

temp = max_chap[1:]
num = int(temp)
print "Available Chapters "
print manga+ " Chapters Available From "+temp+" To "+"1"
print "Enter Chapter To Be Downloaded"
temp = raw_input("Enter The Chapter Number : ")
i = int(temp)
volume = get_volume(i)
download_chapter(manga,volume,i)


    


