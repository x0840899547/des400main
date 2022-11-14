from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np
from io import BytesIO
from PIL import Image

model = MobileNetV2(weights='imagenet')

def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

def prediction_model(image: Image.Image):
    
    image = np.asarray(image.resize((224, 224)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0


    result = decode_predictions(model.predict(image), 1)[0]
    response = []
    for i, res in enumerate(result):
        resp = {}
        resp["class"] = res[1]
        resp["confidence"] = f"{res[2]*100:0.2f} %"

        response.append(resp)

    return response    
