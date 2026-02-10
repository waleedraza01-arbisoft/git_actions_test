# git_actions_test
This repository demonstrates how to automate computer vision tasks using **GitHub Actions**. 

## How it Works
1. **Trigger**: Any push to the `main` branch.
2. **Environment**: GitHub-hosted Ubuntu runner.
3. **Execution**: The workflow installs `opencv-python-headless` and runs `inference.py`.
4. **Task**: Detects faces in `input.jpg` using a Haar Cascade classifier.

## Files
* `inference.py`: Python script for face detection.
* `.github/workflows/main.yml`: The automation configuration.
* `input.jpg`: The sample image to process.
