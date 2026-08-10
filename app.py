import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# Page config
st.set_page_config(page_title="Plant Disease Detector", page_icon="🌿", layout="centered")

# Load model (cached - sirf ek baar load hoga)
@st.cache_resource
def load_my_model():
    return load_model("plant_disease_final.keras")

model = load_my_model()

# Class names
class_names = ['Early Blight', 'Late Blight', 'Healthy']

# Class descriptions
class_info = {
    'Early Blight': "🦠 Fungal disease. Dark spots on older leaves. Treat with fungicide.",
    'Late Blight': "🦠 Serious fungal disease. Brown patches, spreads fast. Immediate action needed.",
    'Healthy': "✅ Leaf is healthy. No disease detected."
}

# ---------- UI ----------
st.title("🌿 Plant Disease Detector")
st.write("Upload a **tomato leaf image** to detect disease.")
st.markdown("---")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Show image
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Leaf", use_container_width=True)
    
    # Preprocess
    img_resized = img.resize((128, 128))
    img_array = image.img_to_array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Predict button
    if st.button("🔍 Predict Disease"):
        with st.spinner("Analyzing..."):
            prediction = model.predict(img_array, verbose=0)
            pred_class = class_names[np.argmax(prediction)]
            confidence = np.max(prediction) * 100
        
        st.markdown("---")
        st.subheader("Prediction Result")
        
        # Result display
        if pred_class == "Healthy":
            st.success(f"### ✅ {pred_class}")
        else:
            st.error(f"### ⚠️ {pred_class}")
        
        st.write(f"**Confidence:** {confidence:.2f}%")
        st.progress(float(confidence / 100))
        
        st.info(class_info[pred_class])
        
        # Show all probabilities
        st.markdown("### 📊 All Class Probabilities")
        for i, cls in enumerate(class_names):
            prob = prediction[0][i] * 100
            st.write(f"**{cls}**: {prob:.2f}%")
            st.progress(float(prob / 100))

else:
    st.info("👆 Please upload a tomato leaf image to get started.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using TensorFlow & Streamlit")