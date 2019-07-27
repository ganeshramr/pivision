
import os
from google.cloud import storage
from google.cloud import vision
import smtplib
import ssl


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/ganeshram/projects/blockchain/GCP-PI/pivision/raspberrypi.json'


def upload_file_to_bucket(bucket_name, object_name, file_path):
    # Imports the Google Cloud client library
    # Instantiates a client
    storage_client = storage.Client()
    # Creates the new bucket
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(file_path)


def call_gcp_vision_api(storage_url):
    vision_client = vision.ImageAnnotatorClient()
    return vision_client.annotate_image({
                'image': {'source': {'image_uri': storage_url}},
                'features': [{'type': vision.enums.Feature.Type.OBJECT_LOCALIZATION}],
                 })


def send_email(message):
    # Create a secure SSL context

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login("", "")
        server.sendmail("unmama@4725.com", "7703650103@txt.att.net", message)


upload_file_to_bucket('picturefrompi',
                      'image2.jpg',
                      '/Users/ganeshram/projects/blockchain/GCP-PI/image2.jpg')

response = call_gcp_vision_api('gs://picturefrompi/image2.jpg')
print(response.localized_object_annotations[0].name)

print("Attempting to send email")
send_email(response.localized_object_annotations[0].name)
print("Done!!")







