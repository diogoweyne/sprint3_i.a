from ultralytics import YOLO
import cv2

class MotoDetector:
    def __init__(self, model_path="yolov8n.pt"):
        # Carrega o modelo YOLO (pré-treinado no COCO)
        self.model = YOLO(model_path)

    def detectar_motos(self, frame):
        # Predição
        results = self.model.predict(frame, conf=0.5, verbose=False)

        # Filtra somente motos (classe 3 = "motorbike" no dataset COCO)
        motos = []
        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                if cls_id == 3:  # 3 = motorbike
                    motos.append(box)

        return motos, results
