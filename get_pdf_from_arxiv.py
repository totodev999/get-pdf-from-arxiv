import os
import requests
import json

save_directory = "./pdfs"


def retrieve_pdf(url: str, title: str):
    try:
        replaced_url = url.replace("abs", "pdf")
        print("Downloading PDF file...")
        response = requests.get(replaced_url)
        response.raise_for_status()

        pdf_path = os.path.join(save_directory, f"{title}.pdf")
        with open(pdf_path, "wb") as f:
            f.write(response.content)
        print("PDF file downloaded successfully!")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")


def start():
    os.makedirs(save_directory, exist_ok=True)

    with open("all_links.json", "r") as file:
        links = json.load(file)

    for link in links:
        title = link["title"]
        url = link["url"]
        retrieve_pdf(url, title)


start()
print("end")
