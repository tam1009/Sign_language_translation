from ultralytics import YOLO

class YOLOModel:
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = YOLO("C:\\Users\\LENOVO\\Sign_language_translation\\detectors\\weights\\best(3).pt")

    def predict(self, input):
        return self.model.predict(input)

