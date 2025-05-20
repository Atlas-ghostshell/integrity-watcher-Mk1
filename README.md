# integrity-watcher-Mk1
Initial commit of integrity-watcher Mk1 project which watches over the critical file systems.

# Integrity-Watcher Mk1

**Integrity-Watcher Mk1** is a lightweight Python-based File Integrity Monitoring (FIM) script designed to help detect unauthorized modifications to critical system files in Linux environments. It calculates SHA-256 hash values of trusted system files and continuously verifies their integrity every minute.

## Features

- Monitors the integrity of important system files like `/etc/passwd` and `/etc/shadow`
- Compares real-time file hashes against known-good "true hashes"
- Logs suspicious changes for review
- Clean and minimal logic — no external dependencies
- Perfect for lab environments or as a base for real-world FIM solutions

## How It Works

1. **Initial Setup (Snapshot Phase):**  
   You generate SHA-256 hashes of clean system files and store them in a file (e.g. `fim-based.txt`).

2. **Verification Script:**  
   The script (`verify.py`) recalculates the current hash values every minute and compares them to the stored "true hashes".

3. **Detection and Logging:**  
   If a hash mismatch is found, it is logged as a potential tampering event.

## Example Files

- `fim-based.txt` — Stores original SHA-256 hashes
- `verify.py` — Continuously monitors and checks file integrity

## Optional: Run As a Persistent Background Daemon

To make Integrity-Watcher Mk1 run in the background (and monitor your files 24/7), you can configure it as a **systemd service**. This allows the script to run with root privileges and securely access protected files without changing file permissions.

To use it as a daemon:
1. Create a systemd service file.
2. Point it to your `verify.py` script.
3. Enable and start the service.

## Requirements

- Python 3.x
- Linux system
- Root access for monitoring sensitive files (like `/etc/shadow`)

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

---

## Authors

This project was done by Geoffrey Muriuki (A.K.A Ghost-shell) with the help of my partener Atlas (Open AI Chat GPT)
