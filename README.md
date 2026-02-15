# AI-Enabled Public Safety System

**Author:** Samarth Khandelwal  
**Course:** Project-Based Learning (PBL)

---

## Abstract

This project presents a modular AI-enabled public safety surveillance framework designed to enhance traditional monitoring systems through automated anomaly detection. The system integrates video motion analysis and audio signal processing to generate real-time risk scores and alert mechanisms.

The prototype demonstrates how multimodal sensing (video and audio) can improve detection accuracy, reduce response latency, and minimize dependence on manual surveillance. The architecture is intentionally designed for scalability, allowing future integration of deep learning models such as convolutional neural networks (CNNs) and sequence-based models.

---

## 1. Introduction

Conventional surveillance systems rely heavily on continuous human monitoring of multiple camera feeds. This approach suffers from:

- Operator fatigue  
- Delayed incident detection  
- Limited ability to detect subtle abnormal patterns  
- Scalability constraints in large surveillance networks  

This project proposes an intelligent augmentation layer that introduces automated anomaly scoring and alert generation without restructuring existing infrastructure.

---

## 2. System Design and Architecture

The system follows a layered architecture:

### 2.1 Input Layer
- Real-time camera feed  
- Live microphone audio stream  

### 2.2 Processing Layer
- Frame differencing for motion intensity extraction  
- Root Mean Square (RMS) calculation for audio intensity measurement  

### 2.3 Decision Layer
- Rule-based anomaly scoring  
- Weighted risk evaluation mechanism  

### 2.4 Output Layer
- Risk score generation  
- Automated alert trigger when threshold is exceeded  

The modular structure enables replacement of rule-based components with machine learning models in future iterations.

---

## 3. Methodology

### 3.1 Video Anomaly Estimation

Motion intensity is computed using frame differencing between consecutive frames. Pixel intensity variation is aggregated to generate a motion score.

### 3.2 Audio Intensity Estimation

Audio streams are processed using RMS energy calculations to determine high-intensity acoustic events.

### 3.3 Risk Scoring Model

Risk is calculated using a weighted combination of motion and audio features:

Risk = w1(MotionScore) + w2(AudioLevel)

If the computed risk exceeds a predefined threshold, an alert is generated.

---

## 4. Prototype Implementation

Programming Language:
- Python  

Libraries Used:
- OpenCV  
- NumPy  
- SoundDevice  
- Basic signal processing utilities  

The implementation follows a modular file structure to support scalability and future machine learning integration.

---

## 5. Identified Datasets for Future Model Training

To transition from rule-based detection to machine learning-based anomaly detection, the following datasets are identified:

- UCSD Anomaly Detection Dataset  
- UCF Crime Dataset  
- UrbanSound8K Dataset  
- ESC-50 Dataset  

These datasets support video anomaly detection, aggression detection, and environmental sound classification tasks.

---

## 6. Future Work

- CNN-based object detection (e.g., YOLO architecture)  
- LSTM-based temporal sequence modeling  
- Spectrogram-based audio classification  
- Database logging and event history analysis  
- Deployment-ready monitoring dashboard  

---

## 7. Ethical and Privacy Considerations

The system focuses on behavioral anomaly detection rather than identity recognition. No facial recognition or biometric identification mechanisms are included in the prototype to ensure privacy-aware and responsible AI development.

---

## 8. Conclusion

The AI-Enabled Public Safety System demonstrates a scalable and modular approach to intelligent surveillance augmentation. While the current implementation employs rule-based anomaly scoring, the architecture supports seamless transition to advanced machine learning frameworks.

This project establishes a foundation for further research in multimodal threat detection, proactive monitoring, and AI-assisted public safety systems.
