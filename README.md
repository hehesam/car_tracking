# Car Tracking Project

This repository contains a collection of Python scripts for car detection and tracking using computer vision techniques with OpenCV. The project explores different approaches to vehicle detection and tracking in video streams.

## Project Structure

```
car_tracking/
├── src/                    # Main application scripts
│   ├── background_subtraction_tracking.py  # Tracking using background subtraction and Euclidean distance
│   ├── haar_cascade_detection.py           # Car detection using Haar cascades
│   ├── pretrained_model_detection.py       # Alternative detection method (Haar cascades)
│   ├── video_comparison.py                 # Compare multiple video feeds
│   ├── line_drawer.py                      # Interactive line drawing on video
│   └── square_cropper.py                   # Interactive region cropping
├── utils/                  # Utility modules
│   ├── stacker.py          # Image stacking utility
│   ├── tracker.py          # Euclidean distance tracker class
│   └── BGS_methods.py      # Background subtraction methods demo
├── data/                   # Data files
│   ├── cars.xml            # Haar cascade classifier for cars
│   └── threshold.txt       # Threshold values
└── README.md               # This file
```

## Features

- **Background Subtraction Tracking**: Uses MOG2 background subtractor combined with contour detection and Euclidean distance tracking to track vehicles.
- **Haar Cascade Detection**: Employs pre-trained Haar cascades for car detection.
- **Video Comparison**: Displays multiple video streams simultaneously for comparison.
- **Interactive Tools**: Line drawing and region cropping utilities for video analysis.
- **Utility Functions**: Image stacking for better visualization of processing steps.

## Dependencies

- Python 3.x
- OpenCV (cv2)

Install dependencies:
```
pip install opencv-python
```

## Usage

1. Ensure video files are placed in the appropriate directory (scripts expect videos at `C:/GIT/car_tracking_videos/` by default).

2. Run any of the main scripts:
   ```
   python src/background_subtraction_tracking.py
   python src/haar_cascade_detection.py
   python src/video_comparison.py
   ```

3. Press 't' to exit any running script.

## Notes

- Video paths are hardcoded in the scripts. Update them to match your video locations.
- The Haar cascade method may be slower and less accurate compared to background subtraction.
- Background subtraction works best with stable camera positions.

## Contributing

Feel free to improve the code, add new detection methods, or optimize existing algorithms.
