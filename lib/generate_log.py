from datetime import datetime
import os
import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    if response.status_code == 200:
        return response.json()

    return {}


def generate_log(log_data):
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    post = fetch_data()

    filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as file:
        file.write("=== LOCAL LOG DATA ===\n")
        for item in log_data:
            file.write(f"{item}\n")

        file.write("\n=== EXTERNAL API DATA ===\n")
        file.write(f"Title: {post.get('title', 'No title')}\n")
        file.write(f"Body: {post.get('body', 'No body')}\n")

    print(f"Log written to {filename}")

    return filename


if __name__ == "__main__":
    sample_logs = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    generate_log(sample_logs)