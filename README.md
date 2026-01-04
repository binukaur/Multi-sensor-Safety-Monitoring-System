# Wearable Multisensor Safety Monitoring System

A wearable, on-device safety system that detects abnormal struggle-like motion using multimodal sensing and triggers evidence capture autonomously.

## Problem Statement

Unsafe situations such as harassment or physical assault often occur suddenly, leaving victims unable to manually trigger safety mechanisms. Most existing solutions rely on smartphones or SOS buttons, which may not be accessible during panic or physical restraint. There is a need for an autonomous wearable system that can detect distress situations automatically and respond in real time.

## Goal of the Project

The goal of this project is to design a **wearable safety system** that:
- Automatically detects abnormal, struggle-like motion
- Uses multimodal sensing (motion and audio) to reduce false alarms
- Operates fully on-device without cloud dependency
- Triggers evidence capture only during high-confidence unsafe situations
- Preserves privacy by avoiding continuous recording

## Dataset Description

This project uses **real-time sensor data** collected directly from hardware.

### Motion Data
- Source: IMU (accelerometer) on Nicla Vision
- Data: 3-axis acceleration values (ax, ay, az)
- Activities:
  - Normal activities (walking, jogging, dancing)
  - Abnormal activities (simulated struggle-like motion)

### Audio Data (Planned)
- Source: Onboard microphone
- Target sounds: screaming, shouting, distress vocalizations

No pre-recorded or public datasets are used.

## Model Pipeline and Workflow

1. **Sensor Data Acquisition**
   - Continuous IMU and audio sampling

2. **Feature Extraction**
   - Acceleration magnitude
   - Sliding window variance
   - Directional inconsistency
   - Audio energy

3. **Decision Logic**
   - Motion alert triggered when variance and directional inconsistency exceed thresholds
   - Audio alert triggered by high-energy distress sounds
   - Final alert:
     ```
     Motion Alert AND Audio Alert
     ```

4. **System Response**
   - On-device LED alert
   - Camera activation
   - Image capture and local storage

## Deployment Details

### Wearable Device
- Platform: Arduino Nicla Vision
- Firmware: OpenMV (MicroPython)
- Mode: Standalone wearable
- Power: Power bank

### External System
- Platform: Laptop / Desktop
- Function:
  - Receives alert signal
  - Activates camera
  - Saves images locally

The system operates offline and does not require internet connectivity.

## Instructions to Run the Code

### Running on Nicla Vision
1. Install **OpenMV IDE**
2. Connect Nicla Vision via USB
3. Open `main.py`
4. Click **Run**
5. Save script to device:


### Wearable Mode
1. Disconnect USB
2. Power device using a power bank
3. Wear the device on the wrist
4. LED behavior:
- OFF → Normal activity
- ON → Abnormal motion detected

## Team Members

- **Binwant Kaur** – Motion Detection 
- **Anushka Nehra** – Audio Detection & Model Training 
- **Bhagyalakshmi Murlidharan** – Workflow and Integration  
- **Manya S** – Documentation & System Integration


## License

This project is licensed under the MIT License.
