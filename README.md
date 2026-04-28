# 🚀 Jamming Detection and Forecasting Model Using Transport & Application Layer Parameters in Wi-Fi Based IoT Systems

## 📖 Table of Contents
- Introduction
- Problem Statement
- Objectives
- Features
- System Architecture
- Technologies Used
- Project Structure
- Dataset Description
- Installation
- Usage
- Model Workflow
- Results
- Screenshots
- Future Scope
- Team Details
- License
- Acknowledgement

---

# 📌 Introduction

The rapid growth of IoT (Internet of Things) devices has increased the dependency on wireless communication systems such as Wi-Fi. However, these networks are highly vulnerable to **Jamming Attacks**, where malicious interference blocks legitimate communication between devices.

This project presents an intelligent deep learning-based system for detecting and forecasting jamming attacks using **Transport Layer** and **Application Layer** network parameters instead of relying only on physical layer metrics.

The proposed hybrid model combines:

- CNN (Convolutional Neural Network)
- GRU (Gated Recurrent Unit)
- Attention Mechanism

This improves detection accuracy, efficiency, and adaptability in Wi-Fi-based IoT environments. :contentReference[oaicite:0]{index=0}

---

# ❗ Problem Statement

Traditional jamming detection systems mainly use physical layer indicators such as:

- Signal Strength
- Noise Level
- Packet Delivery Ratio

These methods often fail in dynamic environments and cannot effectively identify intelligent or adaptive jamming attacks.

Therefore, an advanced solution is required that uses higher-layer parameters and deep learning techniques for accurate and faster detection. :contentReference[oaicite:1]{index=1}

---

# 🎯 Objectives

- Detect Wi-Fi jamming attacks in IoT systems.
- Forecast possible future communication disruptions.
- Improve accuracy using transport/application layer features.
- Compare proposed hybrid model with SVM and LSTM.
- Build an interactive web-based detection system.
- Provide real-time monitoring and prediction results. :contentReference[oaicite:2]{index=2}

---

# ✨ Key Features

✅ Intelligent attack detection  
✅ Forecasting future network issues  
✅ Uses real network performance metrics  
✅ Deep Learning based prediction  
✅ Interactive Flask Web Interface  
✅ Multiple model comparison  
✅ Result visualization dashboard  
✅ Fast and efficient hybrid model  

---

# 🧠 System Architecture

## Proposed Hybrid Model
Input Dataset
     ↓
Preprocessing
     ↓
CNN Layer
     ↓
GRU Layer
     ↓
Attention Layer
     ↓
Dense Output Layer
     ↓
Prediction Result
Module Explanation
🔹 CNN Layer

Extracts short-term traffic patterns and local anomalies.

🔹 GRU Layer

Captures sequential dependencies in time-series data.

🔹 Attention Layer

Focuses on the most important traffic intervals.

🔹 Output Layer

Classifies:

Normal Communication
Jamming Attack
🛠️ Technologies Used
💻 Programming Language
Python
📚 Libraries
NumPy
Pandas
Matplotlib
Scikit-learn
TensorFlow
Keras
🌐 Web Technologies
Flask
HTML
CSS
JavaScript
Bootstrap
🗄️ Database
SQLite3
📂 Project Structure
Jamming-Detection-Project/
│── app.py
│── train_model.py
│── predict.py
│── dataset.csv
│── requirements.txt
│── static/
│   ├── css/
│   ├── js/
│   └── images/
│
│── templates/
│   ├── index.html
│   ├── login.html
│   ├── predict.html
│   └── result.html
│
│── models/
│   ├── svm.pkl
│   ├── lstm.h5
│   └── cnn_gru_attention.h5
│
└── README.md
📊 Dataset Description

The dataset contains traffic records collected from Wi-Fi IoT environments under:

Normal Communication
Jamming Attack Conditions
Features Used
Packet Delay
Retransmission Rate
Throughput
Signal-to-Noise Ratio (SNR)
Response Time
Preprocessing Steps
Remove missing values
Normalize data
Shuffle dataset
Split into train/test (80:20)

⚙️ Installation Guide
Step 1: Clone Repository
git clone https://github.com/your-username/jamming-detection.git
cd jamming-detection
Step 2: Create Virtual Environment
python -m venv venv
Step 3: Activate Environment
Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate
Step 4: Install Dependencies
pip install -r requirements.txt
Step 5: Run Project
python app.py
🚀 Usage
Open Browser:
http://127.0.0.1:5000/
Login to system
Upload dataset file
Select model:
SVM
LSTM
CNN2D
CNN-GRU-Attention
Click Predict
View output:
Attack / Normal
Accuracy
Precision
Recall
F1 Score
🔄 Model Workflow
Collect Dataset
   ↓
Preprocess Data
   ↓
Train Models
   ↓
Evaluate Models
   ↓
Select Best Model
   ↓
Deploy with Flask
   ↓
Predict New Data
📈 Results
Evaluation Metrics Used
Accuracy
Precision
Recall
F1 Score
Confusion Matrix
Outcome

The proposed CNN-GRU-Attention model outperformed traditional SVM and LSTM models in:

✅ Detection Accuracy
✅ Faster Training
✅ Better Generalization
✅ Efficient Forecasting

📸 Screenshots
🏠 Home Screen

(Add Image)

🔐 Login Screen

(Add Image)

📂 Prediction Screen

(Add Image)

📊 Result Dashboard

(Add Image)

🔮 Future Scope
Real-time packet sniffing integration
Live network dashboard
Cloud deployment
Edge AI for IoT devices
Multi-class attack detection
Mobile app monitoring system
Automatic alert notifications
👨‍💻 Team Members
T. Neeraja – 22551A42B2
M. L. M. Bapiraju – 22551A4293
G. Vamsi – 22551A4280
👩‍🏫 Project Guide

Dr. R. Tamilkodi
Professor, Dept. of CSE (AIML & CS)

🏫 Institution

Godavari Institute of Engineering & Technology (Autonomous)
Rajamahendravaram, Andhra Pradesh, India

🤝 Contribution

Contributions, ideas, and suggestions are welcome.

Fork → Clone → Modify → Pull Request
📜 License

This project is developed for academic and research purposes only.

🙏 Acknowledgement

We sincerely thank our guide, faculty members, and Godavari Institute of Engineering & Technology for their valuable support and infrastructure to complete this project successfully.
