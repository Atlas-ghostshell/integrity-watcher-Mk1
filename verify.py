#!/usr/bin/env python3

import hashlib
import time
import os

ORIGINAL_HASHES_PATH = "/opt/integrity-watcher/fim-based.txt"
MONITORED_FILES = [
    "/etc/passwd",
    "/etc/shadow",
    "/etc/group",
    "/etc/hosts"
]

def calculate_hash(file_path):
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
            return hashlib.sha256(file_data).hexdigest()
    except FileNotFoundError:
        return "FILE_NOT_FOUND"

def load_true_hashes():
    true_hashes = {}
    with open(ORIGINAL_HASHES_PATH, "r") as f:
        for line in f:
            parts = line.strip().split("  ")
            if len(parts) == 2:
                true_hashes[parts[1]] = parts[0]
    return true_hashes

def check_integrity():
    true_hashes = load_true_hashes()
    for file in MONITORED_FILES:
        current_hash = calculate_hash(file)
        if file not in true_hashes:
            print(f"[ALERT] No baseline hash found for: {file}")
        elif current_hash != true_hashes[file]:
            print(f"[ALERT] Integrity issue detected in: {file}")
        else:
            print(f"[OK] {file} is intact.")

def main():
    while True:
        print("\n[INFO] Starting integrity check...")
        check_integrity()
        print("[INFO] Sleeping for 60 seconds...\n")
        time.sleep(60)

if __name__ == "__main__":
    main()
