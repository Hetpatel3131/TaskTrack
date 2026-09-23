# ICA04 Reflection

## 1. Local and Remote Repositories
The local TaskTrack repository lives entirely on your personal computer's hard drive and tracks changes locally. The remote repository hosted on GitHub acts as a centralized, cloud-based backup and collaboration point that you must actively sync your local changes to.

## 2. Connecting and Pushing
Adding `origin` only created a local shortcut or address book entry pointing to the GitHub URL; it did not transfer any data. To actually upload the project files and commit history to GitHub, a `git push` command is required.

## 3. Cloning
Downloading a ZIP archive only gives you a snapshot of the project files at a specific moment in time without any version control tracking. Cloning a repository downloads the files along with the entire hidden `.git` folder, preserving the full commit history and automatically linking the new folder to the remote repository.

## 4. Fetching and Pulling
The `git fetch` command downloaded updated tracking data and commit history from GitHub without modifying your local working files. The `git pull` command goes a step further by actually downloading those remote changes and immediately merging them into your current local files.

## 5. Focused Commits
Committing code, data, and documentation separately creates a clean, readable project history. If a bug is introduced, isolated commits make it much easier to pinpoint exactly which change caused the error and revert it without undoing unrelated work.