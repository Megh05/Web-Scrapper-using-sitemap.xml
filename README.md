# Sitemap Scraper

## Overview
This Python script fetches the `sitemap.xml` file from a given website, extracts all the links, scrapes the content of each page, and saves the data in JSON and XML formats. The extracted data is stored in an organized folder structure.

## Features
- Fetches and parses the `sitemap.xml` of a given website
- Scrapes the full textual content of each page, including:
  - URL
  - Title
  - Meta description
  - Paragraph text
- Saves the extracted data in both JSON and XML formats
- Automatically organizes the data into an `output` folder, with subfolders named after the website domain

## Requirements
- Python 3.x
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `xml.etree.ElementTree`
  - `json`
  - `os`
  - `sys`
  - `urllib.parse`

You can install the required dependencies using:
```bash
pip install requests beautifulsoup4
```

## Usage
1. Run the script:
```bash
python sitemap_scraper.py
```
2. Enter the website URL when prompted (e.g., `https://example.com`). The script will automatically append `/sitemap.xml`.
3. The extracted data will be saved in:
   - `output/<domain>/data.json`
   - `output/<domain>/data.xml`

## Output Format
### JSON Format (`data.json`)
```json
[
    {
        "url": "https://example.com/page1",
        "title": "Page Title",
        "meta_description": "Short description of the page",
        "content": "Full textual content from the page"
    }
]
```
### XML Format (`data.xml`)
```xml
<pages>
    <page>
        <url>https://example.com/page1</url>
        <title>Page Title</title>
        <meta_description>Short description of the page</meta_description>
        <content>Full textual content from the page</content>
    </page>
</pages>
```

## Notes
- If the sitemap does not exist or cannot be fetched, the script will exit with an error message.
- The script handles request exceptions and parsing errors gracefully.

## License
This project is licensed under the MIT License.

