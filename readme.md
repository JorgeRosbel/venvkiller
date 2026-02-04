# EnvKiller

EnvKiller is a command-line tool designed to help you reclaim disk space by finding and removing unnecessary Python virtual environments. It provides a simple Text User Interface (TUI) to list, search, and delete virtual environments recursively from your current directory.

## Features

- **Auto-Discovery**: Recursively scans the current directory for common virtual environment folders (`.venv`, `venv`, `env`).
- **Disk Usage Stats**: Displays the size of each environment and calculates total potential space generated.
- **Interactive Interface**: Use arrow keys to navigate and Space/Enter to delete environments.
- **Visual Feedback**: Color-coded status (Available vs Deleted) to track your cleanup.

## Requirements

- Python 3.x
- `colorama` library
- `curses` (Standard in Python on Linux/macOS. For Windows, you may need `windows-curses`).

## Installation

1. Clone this repository or download the script.
2. Install the required dependencies:

   ```bash
   pip install colorama
   ```

## Usage

1. Navigate to the directory where you want to search for virtual environments.
2. Run the script:

   ```bash
   python3 envkiller.py
   ```

3. **Controls**:
   - **Arrow Up/Down**: Navigate the list.
   - **Space** or **Enter**: Delete the selected virtual environment.
   - **q**: Quit the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 Jorge

----
----
