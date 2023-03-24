"""
A sample Hello World server.
"""
import os

from flask import Flask, render_template, request, render_template_string
from PIL import Image
from PIL.ExifTags import TAGS
from google.cloud import storage
import datetime
import google.auth
import os
from google.cloud import datastore
from markupsafe import Markup


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/phaneendraganji3/credentials.json'

storage_client = storage.Client()
source_bucket_name = 'proj2_phani'     
source_bucket = storage_client.bucket(source_bucket_name)

# Create a client object
datastore_client = datastore.Client()
# Define the entity kind
kind = 'image_logs'
# Create a key object for the new entity
key = datastore_client.key(kind)


# pylint: disable=C0103
app = Flask(__name__)

@app.route('/')
def index():
        # storage_client = storage.Client.from_service_account_json('/home/phaneendraganji3/credentials.json')
    blobs = storage_client.list_blobs('proj2_phani')
    bucket = storage_client.bucket('proj2_phani')
    url_lst=[]
    name_lst=[]    
    for blb in blobs:
        image_blob = bucket.blob(blb.name)        
        url = image_blob.generate_signed_url(datetime.timedelta(minutes=15))
        url_lst.append(url)
        name_lst.append(blb.name)
        zp = zip(url_lst,name_lst)
    # table_html = create_image_table(url_lst)
    return render_template('index.html' , image_urls=zp)

# def create_image_table(image_list):
    # # Determine the number of rows needed based on the length of the image list
    # num_rows = len(image_list) // 3 + (1 if len(image_list) % 3 != 0 else 0)

    # # Create an HTML table element with the appropriate number of rows and columns
    # table_html = '<table>'
    # for i in range(num_rows):
    #     table_html += '<tr>'
    #     for j in range(3):
    #         index = i * 3 + j
    #         if index < len(image_list):
    #             table_html += f'<td> <img src="{image_list[index]}" alt="Image {index}"> </td>'
    #         else:
    #             table_html += '<td> </td>'
    #     table_html += '</tr>'
    # table_html += '</table>'

    # # Return the HTML code for the table
    # return table_html


@app.route('/', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        # Get the file from the request
        file = request.files['image']
        name = file.filename.split('.')[0]

        # Initialize the Cloud Storage client
        storage_client = storage.Client()

        # Get the source and destination buckets
        source_bucket_name = 'proj2_phani'
        # destination_bucket_name = 'my-transformed-bucket'        

        source_bucket = storage_client.bucket(source_bucket_name)

        # Upload the file to the source bucket
        blob = source_bucket.blob(name+'.jpeg')
        blob.upload_from_file(file)
    return "uploaded sucessfully"


@app.route('/<path:file_name>')
def get_image_info(file_name):
    blob = source_bucket.blob(file_name)
    blob.download_to_filename('/home/phaneendraganji3/gallery_app/pictures/'+file_name)
    
    # image_html="<h2>"+file_name+"</h2>"+ \
    #     '<image src="/pictures/1.jpeg" width="500" height="300">' 

    image = Image.open(os.path.join("/home/phaneendraganji3/gallery_app/pictures/",file_name))
    # image_blob = source_bucket.blob(file_name)
    # url = image_blob.generate_signed_url(datetime.timedelta(minutes=15))
    # url_lst.append(url)
    # img = Image.open(url)

    image_blob = source_bucket.blob(file_name)        
    url = image_blob.generate_signed_url(datetime.timedelta(minutes=15))
    
    exifdata = image.getexif()

    # image_html = '<p>'+str(exifdata)+'</p>'
    image_html ='<table border = 1 width = "500">'
    image_html += '<th>Tag</th><th>Value</th>'

    for tag_id in exifdata:
        tag_name = TAGS.get(tag_id,tag_id)
        value = exifdata.get(tag_id)
        image_html +="<tr><td>"+str(tag_name)+"</td><td>"+str(value)+"</td></tr>"
    image_html+="</table>"

    image_html+='<br><a href="/">Back</a>'

    page = '''<!DOCTYPE html>
    <h2>{{file_name}}</h2>
    <img src="{{ url }}" alt="image" width="300">
    {{table}}
      
    '''
    # return image_html
    return render_template_string(page, file_name=file_name, url = url, table = Markup(image_html))



    


# @app.route('/files')
# def files():    
    # storage_client = storage.Client.from_service_account_json('/home/phaneendraganji3/credentials.json')
    # blobs = storage_client.list_blobs('proj2_phani')
    # bucket = storage_client.bucket('proj2_phani')
    # lst=[]
    # for blb in blobs:
    #     image_blob = bucket.blob(blb.name)
    #     url = image_blob.generate_signed_url(datetime.timedelta(minutes=15))
    #     lst.append(url)
    # return render_template("view.html", image_urls=lst)

# @app.route('/', methods=['GET','POST'])
# def meta():
#     if request.method == 'POST':
#         file = request.files['image']
#         img = Image.open(file)
#         width, height = img.size
#         format = img.format
#         mode = img.mode
#         info = img.info
#     return 'Image properties: width={}, height={}, format={}, mode={}, info={}'.format(width, height, format, mode, info)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
