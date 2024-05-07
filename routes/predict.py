from fastapi import APIRouter, UploadFile
from schemas.transtext import TranslatedTextResponse
import cv2
from detectors.asl_translation import ASLTranslation
from detectors.yolov8 import YOLOModel

router = APIRouter()

@router.post("/trans")
async def yolo_video_upload(file: UploadFile):
    contents = await file.read()
    
    # Tạo một file tạm thời từ dữ liệSSSu được tải lên
    with open("temp.mp4", "wb") as temp_file:
        temp_file.write(contents)
    
    # Tạo một đối tượng VideoCapture từ file tạm thời
    cap = cv2.VideoCapture("temp.mp4")
    
    frames = []
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            # Thêm khung hình vào danh sách
            frames.append(frame)
        else:
            break
    model = YOLOModel()
    asl_translator = ASLTranslation(model)
    output = None
    # Xử lý khung hình tại đây
    output = await asl_translator.translate(frames)

    return TranslatedTextResponse(text=output)
