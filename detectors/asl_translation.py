classes = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'Next', 27: 'Space'}

class ASLTranslation:
    def __init__(self, model):
        self.model = model

    async def translate(self, input):
        results = list(self.model.predict(input)) # Convert the tuple to a list
        output = ""
        max_conf = 0
        for i in enumerate(results):
            class_id = results[i].boxes.cls.cpu().numpy().astype(int)
            curr_conf = results[i].boxes.conf.cpu().numpy().astype(float)

            if output == "" and curr_conf > 0.8:
                output += classes[class_id[0]]
                max_conf = curr_conf

            if class_id != 26 :
                if output[-1] == classes[class_id[0]] and curr_conf > max_conf:
                    max_conf = curr_conf
                elif output[-1] != classes[class_id[0]]:
                    output += classes[class_id[0]]
                    max_conf = curr_conf
            
            elif class_id == 26:
                output += classes[class_id[0]]
                max_conf = 0

        output = output.replace(classes[26], '')
        return output
