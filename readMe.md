# Screen Monitoring and Auto Clicker

## Overview

This Python script monitors specified areas on the screen and automatically clicks on predefined positions if any changes are detected. It is useful for automating tasks that require monitoring visual changes on the screen.

## Features

Allows users to specify screen regions to monitor.

Captures and compares images of the selected regions to detect changes.

Automatically clicks on predefined positions when changes are detected.

Supports refreshing the screen before monitoring changes.

## Prerequisites

Ensure you have the following dependencies installed before running the script:

```bash

pip install -r requirements.txt
```

## Usage

### 1. Define Monitoring Areas

Run the script and follow the instructions to specify the screen areas to monitor:

Move your mouse to the top-left corner of the area and wait for 5 seconds.

Move your mouse to the bottom-right corner and wait for 5 seconds.

Confirm the selected area.

Repeat if necessary.

### 2. Define Click Positions

For each monitoring area, specify a click position:

Move your mouse to the position where a click should occur when a change is detected.

The script will record the position.

### 3. Start Monitoring

Once the monitoring areas and click positions are set, the script will:

Periodically refresh the screen.

Capture and compare images of the monitoring areas.

Click at the predefined positions when changes are detected.

Stop monitoring a region once a click is performed.

## Configuration

The script refreshes the screen using Command + R (Mac) or F5 (Windows). Uncomment the appropriate command in refresh_screen().

The monitoring interval is randomized between 0.5 to 1.5 seconds to avoid detection.

The image difference threshold is set to 10. Modify this in images_different() if needed.

## Notes

The script requires screen access permissions on macOS. Enable screen recording in System Preferences > Security & Privacy > Privacy.

Run the script in an environment where UI automation is allowed.
