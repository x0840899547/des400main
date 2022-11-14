#import the API dependencies
from fastapi import File, FastAPI, UploadFile,Form
from typing import List
import aiofiles
#import the model
from modelmain import *


app = FastAPI()

@app.post("/uploadsingle")
async def singlefile_upload(username:str = Form(),password:str = Form(),file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    prediction = prediction_model(image)

    return prediction



    
@app.post("/uploadmultifile")
async def mulitplefile_upload(username:str = Form(),password:str = Form(),files: List[UploadFile] = File(...)):
    for file in files:
        destination_file_path = file.filename 
        async with aiofiles.open(destination_file_path, 'wb') as out_file:
            while content := await file.read(): 
                await out_file.write(content)
    return {"Result": "Uploaded", "filenames": [file.filename for file in files]}