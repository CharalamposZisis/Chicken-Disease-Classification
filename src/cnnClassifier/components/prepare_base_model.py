import os
import urllib.request as request
import zipfile as ZipFile
import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config
        
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16( # VGG16 is a pretrained model ready to use for deep learning tasks.
            input_shape=self.config.params_image_size,
            include_top=self.config.params_include_top,
            weights=self.config.params_weights
        )
        self.save_model(path = self.config.base_model_path, model = self.model)


    @staticmethod #Static method because it does not use the class or instance. 
                  #As you can see it only uses the parameters passed to it and not self or cls.
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False # This freezes all the layers of the model.
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False # This freezes the layers except the last 'freeze_till' layers (the last 50 layers).
        
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(units=classes, activation='softmax')(flatten_in)
        
        full_model = tf.keras.models.Model(inputs=model.input, outputs=prediction)
        full_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                           loss=tf.keras.losses.CategoricalCrossentropy(), # because we have two categories (Healthy and Coccidiosis)
                           metrics=['accuracy'])
        full_model.summary()
        return full_model
    
    
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None, # freeze_till is used to freeze the layers except the last 6 layers.
            learning_rate=self.config.params_learning_rate
        )
        self.save_model(path = self.config.updated_base_model_path, model = self.full_model)
        
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
        print(f"Model saved at : {path}")