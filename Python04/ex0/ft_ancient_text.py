#!/usr/bin/env python3

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

try:
    archive = open("ancient_fragment.txt", 'r')
    print("\nAccessing Storage Vault: ancient_fragment.txt")
    print("Connection stablished...")

    print("\nRECOVERED DATA:")
    print(archive.read())

    archive.close()
    print("\nData recovery complete. Storage unit disconnected.")
except FileNotFoundError:
    print("\nERROR: Storage vault not found. Run data generator first.")
