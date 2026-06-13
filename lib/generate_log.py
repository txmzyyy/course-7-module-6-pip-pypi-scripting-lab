from datetime import datetime
import os
from urllib import response
import requests

def generate_log(data):
    # TODO: Implement log generation logic

    def fetch_data():
    #fetching data from an API
     response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    if response.status_code == 200:
        return response.json()

    print("Failed to fetch data.")
    return {}


def write_log(post):
    #Writeing log data to a file containing a timestamp
    filename = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w") as file:
        file.write("=== Automation Log ===\n")
        file.write(
            f"Generated: {datetime.now()}\n\n"
        )

        file.write(
            f"Post ID: {post.get('id', 'N/A')}\n"
        )
        file.write(
            f"Title: {post.get('title', 'No title')}\n"
        )
        file.write(
            f"Body: {post.get('body', 'No content')}\n"
        )

    print(f"Log written to {filename}")


if __name__ == "__main__":
    print("Fetching data from API...")

    post = fetch_data()

    if post:
        print(
            "Fetched Post Title:",
            post.get("title")
        )
        write_log(post)

    print("Script completed successfully.")
