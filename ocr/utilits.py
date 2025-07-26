import cv2
import numpy as np
from paddleocr import PaddleOCR
import re
def process_image(image_file):
    # DRF'dan kelgan rasmni to'g'ridan-to'g'ri numpy arrayga o‘tkazish
    file_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)

    # OpenCV bilan rasmni dekodlash (BGR formatda)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Agar rasm noto‘g‘ri bo‘lsa
    if img is None:
        print("Rasmni o'qishda xatolik yuz berdi.")
        return None

    # Grayscale formatga o‘tkazish
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Shovqinni kamaytirish
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Threshold orqali binarizatsiya
    _, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 3-kanalli formatga o‘tkazish (PaddleOCR uchun)
    thresholded_bgr = cv2.cvtColor(thresholded, cv2.COLOR_GRAY2BGR)

    return thresholded_bgr


def clean_string(input_str):
    # Faqat raqamlar qoladi, bo'shliqlar va boshqa barcha belgilar olib tashlanadi
    cleaned_str = re.sub(r'[^0-9]', '', input_str)  # faqat raqamlar qoladi
    return cleaned_str



def  captcha_text(img):
     ocr = PaddleOCR(
    use_doc_orientation_classify=False, 
    use_doc_unwarping=False, 
    use_textline_orientation=False
)  
     result=ocr.predict(process_image(img))
     return clean_string(' '.join([res['rec_texts'][0] for res in result]) )
