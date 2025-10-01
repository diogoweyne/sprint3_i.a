import cv2
from detector import MotoDetector

def main():
    detector = MotoDetector("yolov8n.pt")

    cap = cv2.VideoCapture(0)  # 0 = webcam | ou coloque o caminho de um vídeo em /data

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Faz a detecção
        motos, results = detector.detectar_motos(frame)

        # Renderiza frame com bounding boxes
        annotated_frame = results[0].plot()

        # Mostra na tela
        cv2.imshow("Detecção de Motos - Pátio", annotated_frame)

        # Exibe contador
        print(f"Motos detectadas: {len(motos)}")

        # Tecla 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
