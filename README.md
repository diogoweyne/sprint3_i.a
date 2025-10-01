# 🚀 Sprint 3 - Protótipo de Visão Computacional (Pátio de Motos)

Este projeto é um protótipo desenvolvido na Sprint 3 com foco em **Visão Computacional**, para realizar a **detecção de motocicletas em pátios** usando **YOLOv8** e **OpenCV**.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.9+**
- **Ultralytics YOLOv8** → modelo de detecção pré-treinado em COCO
- **OpenCV** → captura de vídeo e exibição dos resultados
- **Matplotlib** → visualização de métricas e gráficos
- **Git/GitHub** → versionamento e controle do código

---

## 🚀 Instruções de Uso

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/diogoweyne/sprint3_i.a.git
cd sprint3_i.a
```

### 2️⃣ Criar ambiente virtual (recomendado)
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Baixar modelo YOLOv8 pré-treinado
```bash
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

### 5️⃣ Executar o código
- **Com webcam**:
```bash
python src/main.py
```

- **Com vídeo (coloque um vídeo em /data e edite `main.py`)**:
```python
cap = cv2.VideoCapture("data/motos.mp4")
```

- **Com imagem estática** (modo teste):
```python
img = cv2.imread("data/moto.jpg")
```

---

## 📊 Resultados Parciais

- O modelo **YOLOv8n** detecta motos em tempo real com **boa precisão**.  
- Testes em CPU mostraram desempenho médio de **10 a 15 FPS**.  
- O sistema exibe **caixas delimitadoras** ao redor das motos e imprime a **quantidade detectada por frame**.  
- Pode ser expandido para:
  - Contagem de veículos no pátio
  - Registro de histórico em banco de dados
  - Criação de dashboards de monitoramento
  - Alertas automáticos em casos de irregularidades  

Exemplo ilustrativo de saída YOLO:  
![Exemplo de detecção](https://github.com/ultralytics/assets/raw/main/im/detect.jpg)

---

## ✨ Próximos Passos

- Salvar as detecções em **CSV/JSON/BD**  
- Criar **interface web/dashboard** para visualização  
- Implementar **rastreamento de múltiplas motos** em tempo real  

## 👨‍💻 Autores
- Diogo Paquete Weyne - RM558380
- Gustavo Tonato Maia - RM555393
- João Victor de Souza - RM555290

