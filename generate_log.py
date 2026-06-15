from datetime import datetime
import os
import requests

def fetch_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def generate_log(log_data):
    """
    Creates a timestamped log file from a list of entries.
    """

    if not isinstance(log_data, list):
        raise ValueError("Input must be a list.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")

    return filename

def main():
    print("Retrieving data from API...")

    post = fetch_post()

    if post:
        print("Post retrieved successfully.")
        print("Title:", post["title"])
        log_data = [
            f"Post ID: {post['id']}",
            f"Title: {post['title']}",
            f"Body: {post['body']}"
        ]
        generate_log(log_data)
    else:
        print("No data retrieved.")


if __name__ == "__main__":
    main()