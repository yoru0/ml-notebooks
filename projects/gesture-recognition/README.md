# Gesture Recognition

A hand gesture recognizer built with Python, OpenCV and MediaPipe. It reads your webcam, detects media-control gestures, and prints each detection as a JSON event.

## Gestures

- Play/Pause: make a fist, then open your hand within 1 second
- Next: show two fingers (peace sign) and swipe left
- Previous: show two fingers (peace sign) and swipe right
- Detections are filtered by a confidence threshold

## Installation

### Prerequisites

- [uv](https://docs.astral.sh/uv/) (installs Python 3.12)
- Webcam

### Setup

1. Clone the repository and open this project:
   ```bash
   git clone https://github.com/yoru0/ml-notebooks.git
   cd ml-notebooks/projects/gesture-recognition
   ```

2. Install the dependencies:
   ```bash
   uv sync
   ```

3. Run the recognizer:
   ```bash
   uv run python py/recognizer.py
   ```

## Usage

The recognizer opens your camera and starts detecting gestures. Each detection is printed to standard output as one JSON line, for example:

```json
{"gesture": "next", "confidence": 0.91, "hand": "Right", "ts": 1763000000}
```

Logs go to standard error, so another program can read the events from standard output. This project no longer includes a launcher that turns events into media key presses.

Press `q` in the camera window to quit.
