from datetime import datetime
import os

def generate_log(log_data):
    # Validate input
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    # Createing filename.
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Writing the file
    with open(filename, "w") as file:
        for item in log_data:
            file.write(f"{item}\n")

    # Confirmation message
    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    sample_logs = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_logs)