from ultralytics import YOLO

class YOLOModel:
    def __init__(self):
        self.model = YOLO("C:\\Users\\LENOVO\\Sign_language_translation\\detectors\\weights\\best(1).pt")

    def predict(self, input):
        return self.model.predict(input)

