classes = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: '~', 27: ' '}

class ASLTranslation:
    def __init__(self, model):
        self.model = model

    async def translate(self, input):
        results = list(self.model.predict(input)) # Convert the tuple to a list
        output = ""
        max_conf = 0
        for result in results:
            class_id = result.boxes.cls.cpu().numpy().astype(int)
            curr_conf = result.boxes.conf.cpu().numpy().astype(float)

            if class_id.size == 0:
                continue
            else:
                if class_id[0] != 26 :
                    if output == "" and curr_conf[0] > 0.8:
                        output += classes[class_id[0]]
                        max_conf = curr_conf[0]
                    elif output != "":
                        if output[-1] == classes[class_id[0]] and curr_conf[0] > max_conf:
                            max_conf = curr_conf[0]
                        elif output[-1] != classes[class_id[0]]:
                            output += classes[class_id[0]]
                            max_conf = curr_conf[0]
                
                else:
                    output += classes[class_id[0]]
                    max_conf = 0

        output = output.replace(classes[26], '')
        return output
