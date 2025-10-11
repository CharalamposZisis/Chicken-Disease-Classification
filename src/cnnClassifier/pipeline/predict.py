import numpy as np
import tensorflow.keras.models as load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        
        
    def predict(self):
        model = load_model.load_model(os.path.join("artifacts","training","model.h5"))
        
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)
        print(result)
        
        if result[0] == 1:
            prediction = 'Healthy'
            return [{'image': prediction}]
        else:
            prediction = 'Coccidiosis'
            return [{'image': prediction}]
        
    