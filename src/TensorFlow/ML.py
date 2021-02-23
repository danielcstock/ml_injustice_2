import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

class ML():
    def __init__(self):
        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)
        # Load the model
        self.model = tensorflow.keras.models.load_model('keras_model.h5')
        self.model.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

        # Create the array of labels
        self.labels = ['ENTER_MULTIVERSE', 'ENTER_IN_BATTLE', 'ROSTER_BATMAN', 'PAUSE', 'REPEAT']
        # Create the array of the right shape to feed into the keras model
        # The 'length' or number of images you can put into the array is
        # determined by the first position in the shape tuple, in this case 1.
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    
    def predict(self):
        # Replace this with the path to your image
        image = Image.open('img.jpg')

        #resize the image to a 224x224 with the same strategy as in TM2:
        #resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        #turn the image into a numpy array
        image_array = np.asarray(image)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        # Load the image into the array
        self.data[0] = normalized_image_array

        # run the inference
        prediction = self.model.predict(self.data)
        return self.labels[prediction.argmax()]

#ml = ML()
#print(ml.predict())