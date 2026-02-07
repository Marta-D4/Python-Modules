#!/usr/bin/env python3

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

archive = "new_discovery.txt"
archive_data = "{[}ENTRY 001{]} New quantum algorithm discovered\n" \
"{[}ENTRY 002{]} Efficiency increased by 347 %\n" \
"{[}ENTRY 003{]} Archived by Data Archivist trainee"

print(f"\nInitializing new storage unit: {archive}")

fd = open(archive, 'w')
print("Storage unit created succesfully...")

print("\nInscribing preservation data...")
fd.write(archive_data)
print(archive_data)

fd.close()
print("\nData inscription complete. Storage unit sealed.")
print(f"Archive '{archive}' ready for long-term preservation.")
