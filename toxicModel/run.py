import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense
from .process import Text
import pickle
import os 

class Model:
    
    def __init__(self, device = "auto"):
        
        if device=="cpu":
            os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
        elif device=="auto":
            self.find_id()
        else:
            self.device = device
            
        self.load_model()
        
        with open('weights/tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)
            
    def find_id(self):
        visible_devices = tf.config.experimental.get_visible_devices()
        gpu_id = None
        
        for device in visible_devices:
            if 'GPU' in device.device_type:
                gpu_id = int(device.name.split(':')[-1])
                break
        if gpu_id>=0:
            self.device = "gpu:" + str(gpu_id)
            print(f"GPU ID FOUND BY AUTO DETECT>> {gpu_id}")
        else:
            print("NO GPU ID FOUND BY AUTO DETECT LOADING MODEL ON CPU. IF YOU THINK THIS IS A MISTAKE PASS DEIVCE eg:'gpu:0'")
            os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
            
    def load_model(self):
        
        with tf.device(self.device):
            self.model = tf.keras.Sequential([
                Embedding(25000, 200, input_length=300),
                LSTM(16, activation="tanh"),
                Dense(6, activation="sigmoid"), 
            ])
            
            self.model.load_weights('weights/weights.h5')
            # self.model = self.model.to("gpu:0")
        
    def predict(self, text):
        text = Text.preprocess(text)
        
        text_tokenized = self.tokenizer.texts_to_sequences([text])
        text_sequence = pad_sequences(text_tokenized, maxlen=300,
                                padding="post", truncating="post")
        with tf.device(self.device):
            tensor = tf.convert_to_tensor(text_sequence, dtype=tf.float32)
            out = self.model.predict(tensor)[0]
        return out
        
    