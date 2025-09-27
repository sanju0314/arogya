import tensorflow.lite as tflite
import joblib
import numpy as np
interpreter = tflite.Interpreter(model_path="weights/arrhythmia.tflite")
interpreter.allocate_tensors()
hypo_model = joblib.load("weights/hypoxia.pkl")

def predict_arrhythmia(ecg: list[float]) -> bool:
    x = np.array(ecg, dtype=np.float32).reshape(1, 20, 1)
    interpreter.set_tensor(interpreter.get_input_details()[0]['index'], x)
    interpreter.invoke()
    prob = interpreter.get_tensor(interpreter.get_output_details()[0]['index'])[0][1]
    return prob > 0.5

def predict_hypoxia(spo2: int, hr: int) -> bool:
    return bool(hypo_model.predict([[spo2, hr]])[0])
