# 🌿 Plant Disease Detection using CNN

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange.svg)](https://www.tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A deep learning web application that detects **tomato leaf diseases** using a Convolutional Neural Network (CNN) built with TensorFlow/Keras and deployed through Streamlit.

The application classifies uploaded tomato leaf images into three categories:

- 🦠 **Early Blight**
- 🦠 **Late Blight**
- ✅ **Healthy**

---

## 📑 Table of Contents

- [🚀 Demo](#-demo)
- [📌 Project Overview](#-project-overview)
- [✨ Features](#-features)
- [📊 Model Performance](#-model-performance)
- [🗂️ Dataset](#️-dataset)
- [🧠 Model Architecture](#-model-architecture)
- [🔄 Data Augmentation](#-data-augmentation)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🚀 Installation & Setup](#-installation--setup)
- [🧪 Training the Model](#-training-the-model)
- [💻 Running the Web Application](#-running-the-web-application)
- [🖼️ How to Use](#️-how-to-use)
- [📈 Training Configuration](#-training-configuration)
- [🔬 Experiments](#-experiments)
- [🔮 Future Improvements](#-future-improvements)
- [📚 What I Learned](#-what-i-learned)
- [⚠️ Limitations](#️-limitations)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🙏 Acknowledgments](#-acknowledgments)
- [👨‍💻 Author](#-author)

---

## 🚀 Demo

The application provides an interactive interface where users can:

1. Upload a tomato leaf image
2. Run the trained CNN model
3. View the predicted disease
4. See the model's confidence score
5. View probability distribution across all three classes
6. Get basic disease information and recommendations

---

## 📌 Project Overview

Plant diseases can significantly affect crop production and agricultural productivity. This project explores how **Computer Vision and Deep Learning** can be used to automatically identify diseases from plant leaf images.

A CNN was trained on the **PlantVillage dataset** to classify tomato leaves into three categories.

The final CNN model achieved approximately **92.30% test accuracy** after applying data augmentation.

---

## ✨ Features

- 🌿 Tomato leaf image classification
- 🧠 CNN-based deep learning model
- 📊 Confidence score for predictions
- 📈 Class-wise probability visualization
- 🖼️ JPG/PNG image upload support
- 💻 Interactive Streamlit interface
- 🔬 Model evaluation using precision, recall, and F1-score
- 📚 Disease information and recommendations

---

## 📊 Model Performance

Three different approaches were experimented with during development.

| Model Version | Technique | Test Accuracy |
|---------------|-----------|---------------|
| V1 | Basic CNN | 91.85% |
| V2 | CNN + Data Augmentation | **92.30%** ⭐ |
| V3 | Transfer Learning — MobileNetV2 | 90.07% |

The **CNN + Data Augmentation** model was selected as the final model because it achieved the highest test accuracy.

### Per-Class Performance

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| Early Blight | 84% | 85% | 84% |
| Late Blight | 95% | 90% | 92% |
| Healthy | 95% | 100% | 97% |

> **Note:** Performance depends on the dataset and testing conditions. Predictions on real-world photographs may differ from results obtained on the PlantVillage dataset.

---

## 🗂️ Dataset

This project uses the **PlantVillage dataset**.

- **Dataset:** PlantVillage — Tomato Leaf Disease Images
- **Source:** Kaggle

The project uses three tomato-related classes:

| Class | Images |
|-------|--------|
| Tomato Early Blight | 1,000 |
| Tomato Late Blight | 1,909 |
| Tomato Healthy | 1,591 |
| **Total** | **4,500** |

### Dataset Split

The dataset was divided into:

- **Training:** 70% — 3,150 images
- **Validation:** 15% — 675 images
- **Testing:** 15% — 675 images

---

## 🧠 Model Architecture

The final model is a custom Convolutional Neural Network.

```text
Input Image
128 × 128 × 3
    │
    ▼
┌─────────────────────────┐
│ Conv2D (32 filters)     │
│ + MaxPooling2D          │
└─────────────────────────┘
    │
    ▼
┌─────────────────────────┐
│ Conv2D (64 filters)     │
│ + MaxPooling2D          │
└─────────────────────────┘
    │
    ▼
┌─────────────────────────┐
│ Conv2D (128 filters)    │
│ + MaxPooling2D          │
└─────────────────────────┘
    │
    ▼
┌─────────────────────────┐
│ Flatten                 │
└─────────────────────────┘
    │
    ▼
┌─────────────────────────┐
│ Dense (128)             │
│ Dropout (0.5)           │
└─────────────────────────┘
    │
    ▼
┌─────────────────────────┐
│ Dense (3) + Softmax     │
└─────────────────────────┘
    │
    ▼
Prediction
```

### Model Configuration

| Parameter | Value |
|-----------|-------|
| Input Size | 128 × 128 × 3 |
| Output Classes | 3 |
| Optimizer | Adam |
| Loss Function | Categorical Crossentropy |
| Batch Size | 32 |
| Epochs | 15 |
| Dropout | 0.5 |
| Total Parameters | 3,305,027 |

---

## 🔄 Data Augmentation

To improve generalization and reduce overfitting, the final CNN model uses data augmentation techniques.

The following transformations were applied:

- 🔄 Rotation — ±25°
- ↔️ Width shift — ±10%
- ↕️ Height shift — ±10%
- 🔍 Zoom — ±15%
- 🔃 Horizontal flipping

---

## 🛠️ Tech Stack

### Programming Language

- **Python 3.10+**

### Machine Learning / Deep Learning

- **TensorFlow**
- **Keras**
- **Scikit-learn**

### Data Processing

- **NumPy**
- **Pandas**
- **Pillow**

### Visualization

- **Matplotlib**
- **Seaborn**

### Web Application

- **Streamlit**

---

## 📁 Project Structure

```text
plant-disease-detection/
│
├── PlantVillage/
│   ├── Tomato_Early_blight/
│   ├── Tomato_Late_blight/
│   └── Tomato_healthy/
│
├── notebook.ipynb
├── app.py
├── plant_disease_final.keras
├── requirements.txt
├── README.md
└── LICENSE
```

### File Description

| File / Folder | Description |
|---------------|-------------|
| `PlantVillage/` | Dataset directory |
| `notebook.ipynb` | Model training and experimentation |
| `app.py` | Streamlit web application |
| `plant_disease_final.keras` | Trained CNN model |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |
| `LICENSE` | MIT License |

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mahadiurrehman-pixel/plant-disease-detection.git
cd plant-disease-detection
```

### 2. Create a Virtual Environment

Creating a virtual environment is recommended to keep project dependencies isolated.

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the Dataset

Download the PlantVillage dataset from Kaggle and extract the required tomato classes into the project directory.

The expected structure is:

```text
PlantVillage/
├── Tomato_Early_blight/
├── Tomato_Late_blight/
└── Tomato_healthy/
```

---

## 🧪 Training the Model

If you want to train the model from scratch:

1. Open `notebook.ipynb`
2. Make sure the dataset is available
3. Install all dependencies
4. Run the notebook cells sequentially
5. Evaluate the trained model
6. Save the final model as `plant_disease_final.keras`

---

## 💻 Running the Web Application

After installing the dependencies and making sure the trained model exists, run:

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

---

## 🖼️ How to Use

### Step 1 — Upload an Image

Upload a tomato leaf image in JPG or PNG format.

### Step 2 — Run Prediction

Click the **Predict Disease** button.

### Step 3 — View Results

The application displays:

- Predicted disease
- Confidence score
- Probability of each class
- Disease information
- Basic recommendations

---

## 📈 Training Configuration

The final model was trained using the following configuration:

```text
Optimizer:   Adam
Loss:        Categorical Crossentropy
Batch Size:  32
Epochs:      15
Image Size:  128 × 128 × 3
```

---

## 🔬 Experiments

During development, multiple approaches were tested.

### V1 — Basic CNN

A simple CNN architecture was trained without extensive augmentation.

**Test Accuracy:** 91.85%

### V2 — CNN + Data Augmentation

Data augmentation was introduced to improve generalization.

**Test Accuracy:** **92.30%**

This version achieved the best performance and was selected as the final model.

### V3 — MobileNetV2 Transfer Learning

Transfer learning using MobileNetV2 was also experimented with.

**Test Accuracy:** 90.07%

Although transfer learning can be highly effective, this implementation performed worse than the custom CNN for this particular experiment. The lower performance is likely due to using 128 × 128 input size instead of MobileNetV2's optimal 224 × 224.

---

## 🔮 Future Improvements

The project can be extended in several ways:

- 🌱 Add more plant species such as potato and pepper
- 🦠 Add more disease classes
- 🧠 Experiment with stronger CNN architectures
- 📐 Increase input resolution to 224 × 224
- 🔬 Add Grad-CAM visualizations
- ☁️ Deploy the application online
- 📱 Build a mobile application
- 🌐 Add Urdu, Hindi, and English language support
- 📊 Add model monitoring and analytics
- 🔍 Improve performance on real-world field images

---

## 📚 What I Learned

Through this project, I practiced and learned:

- Building CNNs from scratch
- Image preprocessing
- Image classification
- Data augmentation
- Dataset splitting
- Handling class imbalance
- Model training and validation
- Transfer learning with MobileNetV2
- Confusion matrices
- Precision, recall, and F1-score
- Model evaluation
- Saving and loading Keras models
- Building ML applications with Streamlit
- Deploying machine learning models as interactive applications

---

## ⚠️ Limitations

This project is primarily an educational and experimental machine learning project.

The model was trained using the PlantVillage dataset, which consists of controlled leaf images. Real-world agricultural images may contain different lighting conditions, backgrounds, camera qualities, leaf orientations, and disease stages.

Therefore, the model's prediction should **not be treated as a professional agricultural diagnosis**.

---

## 🤝 Contributing

Contributions are welcome!

If you would like to improve the project:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/your-feature
```

3. Make your changes
4. Commit your changes

```bash
git commit -m "Add your feature"
```

5. Push the branch

```bash
git push origin feature/your-feature
```

6. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

## 🙏 Acknowledgments

Special thanks to:

- **PlantVillage** for the plant disease dataset
- **Kaggle** for making the dataset accessible
- **TensorFlow/Keras** for the deep learning framework
- **Streamlit** for providing an easy way to build the web application
- **Scikit-learn** for model evaluation tools

---

## 👨‍💻 Author

**Mahadi Ur Rehman**

- **GitHub:** [@mahadiurrehman-pixel](https://github.com/mahadiurrehman-pixel)
- **Email:** [mahadiurrehman@gmail.com](mailto:mahadiurrehman@gmail.com)
