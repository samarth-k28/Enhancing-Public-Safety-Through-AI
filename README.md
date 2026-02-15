📌 AI-Enabled Public Safety System
👤 Author
Samarth Khandelwal
Reg No: 2427030343
🚀 Project Overview
The AI-Enabled Public Safety System is a modular surveillance prototype designed to transform traditional passive CCTV monitoring into a proactive AI-driven safety solution.
The system integrates:
🎥 Video motion analysis
🎤 Audio intensity monitoring
🧠 Risk scoring engine
🚨 Real-time alert generation
This project demonstrates how multimodal analysis can improve public safety across campuses, transport hubs, workplaces, and community spaces.
🏗 System Architecture
Input Layer
   ├── Camera Feed
   └── Microphone Input

Processing Layer
   ├── Frame Differencing (Motion Detection)
   └── Audio RMS Calculation

Decision Engine
   ├── Rule-Based Risk Scoring
   └── Threshold Evaluation

Output Layer
   ├── Risk Score
   └── Alert Notification
The architecture is modular and designed for future integration of machine learning models such as:
CNN-based object detection
LSTM-based behavior sequence modeling
Audio spectrogram classification models
🧠 Current Prototype Features
Real-time motion intensity detection
Real-time audio intensity detection
Multi-factor risk scoring
Alert triggering when risk threshold is exceeded
Scalable modular design
📦 Technologies Used
Python
OpenCV
NumPy
SoundDevice
Basic Signal Processing
🔮 Future Enhancements
YOLO-based object detection
Pose estimation for behavior analysis
CNN audio classification using spectrograms
Web-based dashboard
Cloud-based alert system
Database logging of incidents
📊 Datasets for Future Model Training
UCSD Anomaly Detection Dataset
UCF Crime Dataset
UrbanSound8K Dataset
ESC-50 Dataset
🎯 Project Objective
To develop a scalable AI-driven surveillance framework capable of detecting abnormal activities in real-time and reducing reliance on manual monitoring.
⚠ Disclaimer
This prototype focuses on behavioral pattern analysis rather than identity recognition to ensure ethical AI usage and privacy compliance.
