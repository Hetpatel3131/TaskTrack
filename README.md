# TaskTrack

TaskTrack is a command-line task manager built in Python. It allows users to quickly view, add, and manage their daily tasks directly from the terminal, saving all progress automatically so no tasks are lost between sessions.

## Current Features

- View a numbered list of all current tasks.
- Add new tasks to the list.
- Reject empty or blank task entries.
- Automatically save and load tasks to a persistent text file.

## Requirements

- Python 3

## Project Files

- `tasktrack.py` — The main Python script containing the program logic and menu loop.
- `tasks.txt` — A plain text data file where the user's tasks are stored.
- `.gitignore` — Specifies intentionally untracked files that Git should ignore.

## Running the Program

Open a terminal in the project folder and run the following command:

```text
python tasktrack.py