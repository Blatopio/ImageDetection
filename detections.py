from ultralytics import YOLO
import easyocr
import matplotlib.pyplot as plt
from collections import Counter
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np

MODEL_GLASS = YOLO("C:\\Alghi\\Boothcamp\\Purwadhika\\Materi\\Modul 4\\Session 6\\glass-defect\\bestglass.pt")
MODEL_PLATE = YOLO("C:\\Alghi\\Boothcamp\\Purwadhika\\Materi\\Modul 4\\Session 6\\glass-defect\\bestplate.pt")

CLASS_NAMES_GLASS = ['defect', 'glass']
CLASS_NAMES_PLATE = ['plate']

def detect_defectGlass(image):
    results = MODEL_GLASS.predict(source=image, save=False, conf=0.3)[0]
    image_np = np.array(image)
    annotated_img = image_np.copy()

    class_counter = Counter()
    defect_found = False

    for box in results.boxes:  # type: ignore
        cls_id = int(box.cls)
        label = CLASS_NAMES_GLASS[cls_id]
        conf = float(box.conf)
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        class_counter[label] += 1

        if label == "defect":
            defect_found = True

        color = (0, 255, 0) if label == "glass" else (255, 0, 0)
        cv2.rectangle(annotated_img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(annotated_img, f"{label} [{conf:.2f}]", (x1, y1-8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
        
    summary = "\n".join([f"{label}: {count}" for label, count in class_counter.items()])

    if defect_found:
        status_html = (
            "<div style='padding:10px; background-color:#ffe5e5; color:#a30000;"
            "border-left: 6px solid #0f0; font-weight:bold;'>DEFECT DETECTED! PLEASE INSPECT!.</div>"
        )
    else:
       status_html = (
            "<div style='padding:10px; background-color:#e6ffe6; color:#006600;"
            "border-left: 6px solid #0f0; font-weight:bold;'>GAK ADA DEFECT! YEAY!.</div>"
        )

    return Image.fromarray(annotated_img), summary or "NO OBJECT DETECTED!", status_html

def detect_plateNumber(image):
    results = MODEL_PLATE.predict(source=image, save=False, conf=0.3)[0]
    image_np = np.array(image)
    annotated_img = image_np.copy()

    class_counter = Counter()

    for box in results.boxes:  # type: ignore  
        cls_id = int(box.cls)
        label = CLASS_NAMES_PLATE[cls_id]
        conf = float(box.conf)
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        class_counter[label] += 1

        color = (0, 255, 0) if label == "plate" else (255, 0, 0)
        cv2.rectangle(annotated_img, (x1, y1), (x2, y2), color, 2)
        cv2.putText(annotated_img, f"{label} [{conf:.2f}]", (x1, y1-8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
    
    cropped_img = image_np[y1:y2, x1:x2] # type: ignore

    reader = easyocr.Reader(['en'])
    plate_number = reader.readtext(np.array(cropped_img))


    summary = "\n".join([f"{label}: {count}" for label, count in class_counter.items()])
    return Image.fromarray(annotated_img), Image.fromarray(cropped_img), summary + str(plate_number) or "NO PLATE NUMBER DETECTED!"
