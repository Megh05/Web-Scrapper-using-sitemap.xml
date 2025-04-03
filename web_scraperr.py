import xml.etree.ElementTree as ET
import json
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def fetch_sitemap(website):
    """Fetch the sitemap.xml from the given website."""
    parsed_url = urlparse(website)
    if not parsed_url.path.endswith(".xml"):
        website = urljoin(website, "/sitemap.xml")

    try:
        response = requests.get(website, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching sitemap: {e}")
        return None

def parse_sitemap(sitemap_content):
    """Parse the sitemap.xml and extract all links."""
    try:
        root = ET.fromstring(sitemap_content)
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [url.text for url in root.findall("ns:url/ns:loc", namespace)]
        return urls
    except ET.ParseError:
        print("Error parsing the sitemap XML.")
        return []

def scrape_page(url):
    """Scrape the given URL and extract all textual content."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No Title"
        meta_desc = "No Meta Description"
        meta_tag = soup.find("meta", attrs={"name": "description"})
        if meta_tag and meta_tag.get("content"):
            meta_desc = meta_tag["content"]

        text_content = " ".join([p.get_text(strip=True) for p in soup.find_all("p")])

        return {
            "url": url,
            "title": title,
            "meta_description": meta_desc,
            "content": text_content,
        }
    except requests.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return None

def save_to_json(data, output_folder, domain):
    """Save extracted data to a JSON file under the output folder."""
    os.makedirs(output_folder, exist_ok=True)
    filename = os.path.join(output_folder, f"{domain}.json")
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"Saved data to {filename}")
    except OSError as e:
        print(f"Error saving JSON file: {e}")

def save_to_txt(data, output_folder, domain):
    """Save extracted data to a TXT file under the output folder."""
    os.makedirs(output_folder, exist_ok=True)
    filename = os.path.join(output_folder, f"{domain}.txt")
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for page in data:
                f.write(f"URL: {page['url']}\n")
                f.write(f"Title: {page['title']}\n")
                f.write(f"Meta Description: {page['meta_description']}\n")
                f.write(f"Content:\n{page['content']}\n")
                f.write("-" * 80 + "\n")
        print(f"Saved data to {filename}")
    except OSError as e:
        print(f"Error saving TXT file: {e}")

def main():
    """Main function to process the sitemap and scrape content."""
    website = input("Enter the website URL (e.g., https://example.com or https://example.com/sitemap.xml): ").strip()
    parsed_url = urlparse(website)
    domain = parsed_url.netloc.replace('.', '_')
    output_folder = os.path.join("output", domain)

    sitemap_content = fetch_sitemap(website)
    if not sitemap_content:
        return

    urls = parse_sitemap(sitemap_content)
    if not urls:
        print("No URLs found in the sitemap.")
        return

    scraped_data = []
    for url in urls:
        page_data = scrape_page(url)
        if page_data:
            scraped_data.append(page_data)

    save_to_json(scraped_data, output_folder, domain)
    save_to_txt(scraped_data, output_folder, domain)

if __name__ == "__main__":
    main()
