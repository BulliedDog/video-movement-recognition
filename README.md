# Video Movement Recognition and Prediction
### Abstract  
This code analyses frames in videos to detect any moving object and will predict it's position with various techniques.

### Table of contents
1. [Abstract](#abstract)
2. [TODOS](#todos)
3. [Plan](#plan)

### Plan
- [ ] Phase 1: Frame Extraction & Preprocessing
    - [ ] Extract frames from video input using OpenCV (cv2.VideoCapture)
    - [ ] Store frames in memory or as temporary files
    - [ ] Normalize frame dimensions for consistent processing
- [ ] Phase 2: Motion Detection via Frame Differencing
    - [ ] Implement frame-to-frame subtraction using OpenCV
    - [ ] Convert frames to grayscale for efficient comparison
    - [ ] Apply Gaussian blur to reduce noise
    - [ ] Use binary thresholding to isolate moving regions
    - [ ] Dilate/erode morphological operations to clean up the binary masks
- [ ] Phase 3: Contour Detection & Analysis
    - [ ] Extract contours from the binary masks using cv2.findContours
    - [ ] Filter contours by area (remove noise and very large objects)
    - [ ] Calculate contour properties: aspect ratio, area, perimeter, circularity
    - [ ] Store bounding boxes for each detected object
- [ ] Phase 4: Object Classification (Rule-Based)
    - [ ] Develop heuristic rules to distinguish mosquitoes from humans based on:
        - [ ] Contour size (mosquitoes are small, humans are large)
        - [ ] Aspect ratio (mosquitoes are elongated, humans vary)
        - [ ] Movement speed and patterns
    - [ ] Classify each detected object into categories
- [ ] Phase 5: Performance Metrics
    - [ ] Track detection accuracy, processing time per frame
    - [ ] Log false positives/negatives
    - [ ] Prepare data for later AI model comparison