# 🌿 Plant Disease Detection Using CNN

A deep learning web application for detecting **tomato leaf diseases** from images using a custom **Convolutional Neural Network (CNN)** built with **TensorFlow/Keras** and deployed with **Streamlit**.

The application classifies tomato leaf images into three categories:

- 🦠 **Tomato Early Blight**
- 🦠 **Tomato Late Blight**
- ✅ **Tomato Healthy**

> ⚠️ **Disclaimer:** This project is intended for educational and experimental purposes. Predictions should not be treated as a substitute for professional agricultural diagnosis.

---

## 🚀 Live Demo

Try the deployed Streamlit application here:

🔗 **[Plant Disease Detection App](https://plant-disease-detection-cnn-mahadi.streamlit.app/)**

---

## 📌 Project Overview

Plant diseases can significantly reduce crop yield and quality. Early detection is important for timely treatment and better crop management.

This project demonstrates how **Computer Vision** and **Deep Learning** can be used to automatically classify tomato leaf images into healthy or diseased categories. A custom CNN model was trained using selected tomato classes from the **PlantVillage dataset**.

The best-performing model in this experiment was a **CNN with data augmentation**, achieving approximately **92.30% test accuracy** on the project test dataset.

---

## ✨ Features

- Upload tomato leaf images in **JPG, JPEG, or PNG** format
- Classify images into Early Blight, Late Blight, or Healthy
- Display predicted class with confidence score
- Show probability distribution across all classes
- Provide basic disease information and recommendations
- Interactive and user-friendly Streamlit interface
- Trained using a custom CNN architecture
- Evaluation using accuracy, precision, recall, F1-score, and confusion matrix
- Online deployment using Streamlit Community Cloud

---

## 📊 Model Performance

Three model approaches were tested during development:

| Version | Technique | Test Accuracy |
|---|---:|---:|
| V1 | Basic CNN | 91.85% |
| V2 | CNN + Data Augmentation | **92.30%** |
| V3 | MobileNetV2 Transfer Learning | 90.07% |

The **CNN + Data Augmentation** model was selected as the final model because it achieved the highest test accuracy in this experiment.

### Per-Class Performance

| Class | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| Early Blight | 84% | 85% | 84% |
| Late Blight | 95% | 90% | 92% |
| Healthy | 95% | 100% | 97% |

> These results are based on the project's test dataset. Real-world performance may vary due to differences in lighting, background, image quality, disease stage, and camera conditions.

---

## 🗂️ Dataset

This project uses selected tomato classes from the **PlantVillage dataset**.

### Classes Used

| Class | Number of Images |
|---|---:|
| Tomato Early Blight | 1,000 |
| Tomato Late Blight | 1,909 |
| Tomato Healthy | 1,591 |
| **Total** | **4,500** |

### Dataset Split

| Split | Percentage | Images |
|---|---:|---:|
| Training | 70% | 3,150 |
| Validation | 15% | 675 |
| Testing | 15% | 675 |

### Expected Dataset Structure

For local training, organize the dataset as follows:

```text
PlantVillage/
├── Tomato_Early_blight/
├── Tomato_Late_blight/
└── Tomato_healthy/
```

The dataset is required only for training and evaluation. It does **not** need to be included in the deployed Streamlit application.

---

## 🧠 Model Architecture

The final model is a custom Convolutional Neural Network designed for three-class tomato leaf classification.

```text
Input Image: 128 × 128 × 3
        │
        ▼
Conv2D: 32 filters, ReLU
        │
        ▼
MaxPooling2D
        │
        ▼
Conv2D: 64 filters, ReLU
        │
        ▼
MaxPooling2D
        │
        ▼
Conv2D: 128 filters, ReLU
        │
        ▼
MaxPooling2D
        │
        ▼
Flatten
        │
        ▼
Dense: 128 units, ReLU
        │
        ▼
Dropout: 0.5
        │
        ▼
Dense: 3 units, Softmax
        │
        ▼
Prediction
```

### Model Configuration

| Parameter | Value |
|---|---:|
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

Data augmentation was applied to improve model generalization and reduce overfitting.

The training pipeline included:

- Rotation: ±25°
- Width shift: ±10%
- Height shift: ±10%
- Zoom: ±15%
- Horizontal flip

These transformations help the model learn more robust visual patterns instead of memorizing specific image positions or orientations.

---

## 🛠️ Tech Stack

### Programming Language

- Python

### Machine Learning / Deep Learning

- TensorFlow
- Keras
- Scikit-learn

### Data Processing

- NumPy
- Pandas
- Pillow

### Visualization

- Matplotlib
- Seaborn

### Web Application

- Streamlit

---

## 📁 Project Structure

```text
plant-disease-detection-cnn/
│
├── app.py                      # Streamlit web application
├── notebook.ipynb              # Training, experiments, and evaluation
├── plant_disease_final.keras   # Final trained CNN model
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── LICENSE                     # MIT License
├── .gitignore                  # Ignored files and folders
│
└── PlantVillage/               # Local training dataset only
    ├── Tomato_Early_blight/
    ├── Tomato_Late_blight/
    └── Tomato_healthy/
```

> The `PlantVillage/` directory is required only for local training and should not be uploaded to GitHub.

---

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mahadiurrehman-pixel/plant-disease-detection-cnn.git
cd plant-disease-detection-cnn
```

### 2. Create a Virtual Environment

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add the Dataset for Training

Download the PlantVillage dataset from Kaggle and place the required tomato classes in the following structure:

```text
PlantVillage/
├── Tomato_Early_blight/
├── Tomato_Late_blight/
└── Tomato_healthy/
```

---

## 🧪 Training the Model

To train the CNN model from scratch:

1. Open `notebook.ipynb`.
2. Make sure the dataset is available in the correct directory structure.
3. Install all required dependencies.
4. Run the notebook cells sequentially.
5. Train and evaluate the model.
6. Compare experiment results.
7. Save the final model as:

```text
plant_disease_final.keras
```

---

## 💻 Running the Web Application

After installing dependencies and adding the trained model file, run:

```bash
streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

---

## 🖼️ How to Use

1. Open the Streamlit web application.
2. Upload a tomato leaf image in JPG, JPEG, or PNG format.
3. Click the prediction button.
4. View the predicted class and confidence score.
5. Check the probability distribution for all classes.
6. Read the basic disease information and recommendations.

---

## 🔬 Experiments

### V1 — Basic CNN

A custom CNN model was trained without the final augmentation strategy.

**Test Accuracy:** 91.85%

### V2 — CNN with Data Augmentation

Data augmentation was introduced to improve generalization and reduce overfitting.

**Test Accuracy:** 92.30%

This version achieved the highest test accuracy and was selected as the final model.

### V3 — MobileNetV2 Transfer Learning

MobileNetV2 transfer learning was also tested.

**Test Accuracy:** 90.07%

In this experiment, MobileNetV2 performed lower than the custom CNN. One possible reason is the use of 128 × 128 input images, whereas transfer learning models often benefit from higher-resolution inputs and careful fine-tuning.

---

## 🔮 Future Improvements

Possible improvements for future versions include:

- Add more tomato disease classes
- Support additional plant species
- Train on more real-world field images
- Experiment with higher image resolutions
- Add Grad-CAM visual explanations
- Improve the transfer learning pipeline
- Add multilingual support
- Build a mobile application
- Add model monitoring and analytics
- Improve deployment for production use

---

## 📚 What I Learned

This project helped strengthen practical knowledge in:

### Machine Learning

- Dataset preparation
- Train/validation/test splitting
- Classification workflows
- Model evaluation
- Precision, recall, and F1-score
- Confusion matrix analysis

### Deep Learning

- CNN architecture design
- Convolution and pooling layers
- Flatten and dense layers
- Dropout regularization
- Softmax classification
- Categorical crossentropy
- Adam optimization

### Computer Vision

- Image preprocessing
- Image resizing
- Pixel normalization
- Data augmentation
- Image classification

### Deployment

- Saving and loading Keras models
- Building Streamlit applications
- Deploying ML apps online

---

## ⚠️ Limitations

This project was trained using PlantVillage images, which are generally captured in controlled conditions.

Real-world agricultural images may include:

- Uneven or low lighting
- Complex backgrounds
- Different camera qualities
- Multiple leaves in one image
- Different leaf orientations
- Early or advanced disease stages
- Multiple diseases on the same plant

Because of these factors, predictions may be less reliable on real-world field images.

---

## 🤝 Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/your-feature-name
```

3. Make your changes.
4. Commit your changes:

```bash
git add .
git commit -m "Add your feature"
```

5. Push to your branch:

```bash
git push origin feature/your-feature-name
```

6. Open a Pull Request.

---

## 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

## 🙏 Acknowledgments

Special thanks to:

- **PlantVillage** for the plant disease dataset
- **Kaggle** for dataset accessibility
- **TensorFlow/Keras** for the deep learning framework
- **Streamlit** for the web application framework
- **Scikit-learn** for evaluation utilities

---

## 👨‍💻 Author

**Mahadi Ur Rehman**

Aspiring AI/ML Developer interested in Artificial Intelligence, Machine Learning, Computer Vision, NLP, and AI Product Development.

- GitHub: [mahadiurrehman-pixel](https://github.com/mahadiurrehman-pixel)
- Email: [mahadiurrehman@gmail.com](mailto:mahadiurrehman@gmail.com)

---

## ⭐ Support

If you found this project useful, consider giving the repository a star and sharing it with others interested in AI, Machine Learning, and Computer Vision.
