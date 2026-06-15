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


def write_to_file(post):
    
    #writing the results to a file with a timestamp in the filename

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"post_log_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write("API DATA REPORT\n")
        file.write("=" * 40 + "\n")
        file.write(f"Post ID: {post['id']}\n")
        file.write(f"Title: {post['title']}\n")
        file.write(f"Body: {post['body']}\n")

    print(f"Results saved to {filename}")


def main():
    print("Retrieving data from API...")

    post = fetch_post()

    if post:
        print("Post retrieved successfully.")
        print("Title:", post["title"])
        write_to_file(post)
    else:
        print("No data retrieved.")


if __name__ == "__main__":
    main()