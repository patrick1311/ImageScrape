import csv
import urllib
import urllib.parse
import urllib.request
import time
import sys

def ReadCSV(filePath, desiredCol):
    try:
        with open(filePath, "r") as csvfile:
            column = []
            reader = csv.reader(csvfile)
            list_data = list(reader)
            for x in range(1, len(list_data)):
                column.append(list_data[x][desiredCol])
            return column
    except Exception as e:
        print(str(type(e)) + ": " + str(e))
        pass


def ScrapeImage():
    #read specific column in csv
    count = 0
    csvfile = ReadCSV("Creators.csv", 2)
    #print(csvfile)
    for row in csvfile:
        count = count + 1
        if row != '292_20051003024042_creator.jpg':
            url = "http://www.comicbookdb.com/graphics/comic_graphics/" + row
            print(count)
            print(row)
            filename = url[url.rfind('/') + 1:-4]
            print(filename)
            urllib.request.urlretrieve("http://www.comicbookdb.com/graphics/comic_graphics/"+row, "CreatorsImages/"+filename+".jpg")
            time.sleep(0.3)


ScrapeImage()

#http://www.comicbookdb.com/graphics/comic_graphics/292_20051003024042_creator.jpg
