# module import
import imgkit
import cv2 as cv
from barcode import Code39
from barcode.writer import ImageWriter

# confrigrations
path_wkthmltoimage = r'C:\\Users\\Studio\\PycharmProjects\\id_card_genreator\\kit\\bin\\wkhtmltoimage.exe'
config = imgkit.config(wkhtmltoimage=path_wkthmltoimage)
options = {'dpi': 365, 'margin-top': '0in', 'margin-bottom': '0in', 'margin-right': '0in', 'margin-left': '0in',
           'page-size': 'A8', "orientation": "Landscape", 'disable-smart-shrinking': ''}

options = {'enable-local-file-access': None,"--quality": 100}
def barcode(name,id):
    my_code = Code39(name, writer=ImageWriter())
    my_code.save("Barcodes/{id}".format(id=id))


def htmler(NAME, ID, BRANCH, DOB, Blood_group, Photo,Bar):
    html = r"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>pccoe_id</title>
    <style>
            html {
    /* off-white, so body edge is visible in browser */
    background: #eee;
    }

    body {
    height: 56mm;
    width: 90mm;

    margin: 0;
    }

    /* fill half the height with each face */
    .face {
    height: 100%;
    width: 100%;
    position: relative;
    }

    /* an image that fills the whole of the front face */
    .face-front img {
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    width: 100%;
    height: 100%;
    z-index:-1;
    }
    #name{
    position: absolute;
    left: 115px;
    top: 56px;
    }

    </style>
    </head>
    <body>
        <div class="face face-front" style="z-index:-1;"><img src="file:///c:\Users\Studio\PycharmProjects\id_card_genreator\front2.png"></div>
    
    <div class="photo"><img src="file:///c:\Users\Studio\PycharmProjects\id_card_genreator\photos\@PHOTO" style="height: 83px;position: absolute;top: 75px;left: 10px;border: 1px solid #000;"></div>
    <div class="barcode"><img src="file:///c:\Users\Studio\PycharmProjects\id_card_genreator\Barcodes\@Bar" style="height: 32px;position: absolute;top: 169px;left: 18px;"></div>
    <p id="name">Name :@NAME<br>
        ID : @ID <br>
        Branch : @BRANCH<br>
        Dob : @DOB<br>
        Blood Group : @Blood_group
    </p>
    </body>
    </html>"""
    html = html.replace("@NAME", NAME)
    html = html.replace("@ID", ID)
    html = html.replace("@BRANCH", BRANCH)
    html = html.replace("@DOB", DOB)
    html = html.replace("@Blood_group", Blood_group)
    html = html.replace("@PHOTO", Photo)
    html = html.replace("@Bar",Bar)
    imgkit.from_string(html, 'out.jpg', config=config, options=options)
    image = cv.imread(r"out.jpg")

    y = 0
    x = 0
    h = 336
    w = 212
    crop_image = image[x:w, y:h]
    cv.imwrite(r"Ids/{id}.jpg".format(id=ID), crop_image)


# barcode("Harsh Baheti","1339769")
# htmler("Harsh Baheti", "1339769", "Computer Science", "22/09/2001", "AB+","photo.jpg","1339769"+".png")

# output


import csv
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        barcode(row["Name"],row["Erp Number"])
        htmler(row["Name"],row["Erp Number"],row["Branch"],row["Date of Birth"],row["BLOOD GROUP"],row['photo for id card'],row["Erp Number"]+".png")
