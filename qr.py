import qrcode
import json
import time

# function to add to JSON
def write_json(new_data, filename='data.json'):
    with open("static/log.json",'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["qrs"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

def make_qr(image):
    newdata = {"text":image,"time":time.ctime(time.time()),"unix":time.time(),"placeholder":"test"}
    write_json(newdata)

    img = qrcode.make(image)
    img.save("static/QR.jpg")
