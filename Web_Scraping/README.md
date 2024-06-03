# Web Scraping W3Schools Python Tutorials

## Project Overview
This project involves web scraping the W3Schools Python tutorial pages to extract the page titles, subtitles, and headlines from each tutorial page. The extracted data is saved into a CSV file for further analysis or use.

## Project Structure
- `Web_scraping.py`: Main script to perform web scraping and save the data into a CSV file.
- `headlines.csv`: Output file containing the scraped data (generated after running the script).

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pandas` library

## Usage
1. Ensure that you have an active internet connection.
2. Run the script using Python:
3. The script will scrape the tutorial pages and save the extracted data into `headlines.csv`.

## Script Details

### Main URL
The script starts by accessing the main URL of the W3Schools Python tutorials:

### Extracting Tutorial Links
The script extracts all the tutorial links from the left menu of the main page

### Extracting Data from Tutorial Pages
For each tutorial URL, the script extracts the page title, subtitle (if available), and headlines

### Splitting Page Titles
The script splits the page titles into Title and Sub title columns, handling cases where there is no hyphen

### Reordering Columns and Saving to CSV
The script reorders the columns so that the Headline column appears after Title and Sub title, then saves the DataFrame to a CSV file

### Output
The output of the script is a CSV file named headlines.csv, which contains the following columns  
•	URL: The URL of the tutorial page.  
•	Title: The main title of the tutorial page.  
•	Sub title: The subtitle of the tutorial page (if available).  
•	Headline: The headlines found on the tutorial page.  


