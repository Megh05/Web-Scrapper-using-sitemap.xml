# Website Sitemap Scraper

This script scrapes website content based on a given sitemap, allowing the user to:
- Fetch and parse a sitemap from a URL.
- Choose how many pages to scrape.
- Optionally skip URLs with certain extensions (e.g., `.pdf`, `.jpg`).
- Save the scraped content into JSON and TXT formats.
- Display a progress bar while scraping.

## Features
- **Automatic Sitemap Detection**: If the input URL is not an XML file, `/sitemap.xml` is appended automatically.
- **User Control**: Select the number of pages to scrape.
- **Filter Out Unwanted Files**: Skip URLs with extensions like `.pdf`, `.jpg`, `.png`, etc.
- **Data Storage**: Saves extracted content in both JSON and TXT formats.
- **Progress Tracking**: Uses a progress bar to show scraping progress.

## Prerequisites
Make sure you have Python installed, along with the required dependencies:

```sh
pip install requests beautifulsoup4 tqdm
```

## How to Use

1. **Run the Script**:
   ```sh
   python scraper.py
   ```  

2. **Enter the Website URL** (e.g., `https://example.com` or `https://example.com/sitemap.xml`).  

3. **Choose the Number of Pages** to scrape from the sitemap.  

4. **Decide Whether to Skip Certain File Types** (e.g., PDFs, images).  

5. **Scraping Progress** will be displayed via a progress bar.  

6. **Check the Output Folder** (`output/{domain_name}`) for the saved JSON and TXT files.  

## Output Files

- `output/{domain}.json`: Contains structured scraped data.  
- `output/{domain}.txt`: Stores the scraped content in a readable format.  

## Example Output Directory
```
output/
│── example_com/
│   ├── example_com.json
│   ├── example_com.txt
```

## Notes
- The script only scrapes pages listed in the sitemap.  
- Avoid overloading a website with too many requests.