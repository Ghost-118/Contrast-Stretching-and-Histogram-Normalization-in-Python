# 📈 Estiramiento de Contraste y Normalización de Histograma en Python

Este repositorio contiene una implementación en Python para realizar el **estiramiento de contraste (Contrast Stretching / Normalización Min-Max)** sobre imágenes en escala de grises. 

El algoritmo toma una imagen de bajo contraste (`img2_bajo_contraste.jpg`), expande linealmente su rango dinámico de intensidades al rango completo $[0, 255]$, guarda la imagen mejorada (`img2_E12.jpg`) y visualiza la nueva distribución de frecuencias mediante un histograma (*stem plot*) guardado como `img2_histograma_E12.jpg`.

---

## 📐 Fundamento Matemático

El estiramiento de contraste ajusta las intensidades de los píxeles utilizando la siguiente fórmula de normalización Min-Max:

$$I_{\text{out}} = \left( \frac{I_{\text{in}} - I_{\text{min}}}{I_{\text{max}} - I_{\text{min}}} \right) \times 255$$

Donde:
* $I_{\text{in}}$ es el valor de intensidad del píxel original.
* $I_{\text{min}}$ e $I_{\text{max}}$ representan los valores mínimo y máximo de intensidad presentes en la imagen.
* $I_{\text{out}}$ es la intensidad resultante reescalada al rango $[0, 255]$.

---

## 🚀 Características

* **Normalización Automática:** Obtiene los valores extremos $I_{\text{min}}$ e $I_{\text{max}}$ de la imagen mediante NumPy para maximizar el rango dinámico.
* **Procesamiento de Imagen:** Guarda el resultado transformado de la imagen con contraste mejorado.
* **Histograma Estilizado:** Genera una gráfica de tallos (*stem plot*) con tamaño $16 \times 9$ aplicando el estilo gráfico de **Seaborn**.

---

## 🛠️ Requisitos e Instalación

### Requisitos previos
* Python 3.x
* OpenCV (`opencv-python` o `opencv-python-headless`)
* NumPy
* Matplotlib
* Seaborn

### Instalación

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/Ghost-118/Contrast-Stretching-and-Histogram-Normalization-in-Python.git](https://github.com/Ghost-118/Contrast-Stretching-and-Histogram-Normalization-in-Python.git)
   cd Contrast-Stretching-and-Histogram-Normalization-in-Python
