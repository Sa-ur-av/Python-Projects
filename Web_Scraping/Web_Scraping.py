from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL of the main page to scrape tutorial links
main_url = 'https://www.w3schools.com/python/default.asp'

# List to store URLs
urls = []

# Request the main page source
main_page = requests.get(main_url)

# Check if the request was successful
if main_page.status_code == 200:
    # Parse the main page content
    main_soup = BeautifulSoup(main_page.content, 'html.parser')
    
    # Find all links under the div with id 'leftmenuinnerinner'
    left_menu = main_soup.find('div', {'id': 'leftmenuinnerinner'})
    
    # Find all <a> tags within the left menu
    links = left_menu.find_all('a', href=True)
        
    # Extract URLs from <a> tags
    urls = ['https://www.w3schools.com/python/' + link['href'] for link in links]

else:
    print(f"Failed to retrieve the main page: {main_url}. Status code: {main_page.status_code}")

# List to store data
data = []

# Iterate over each tutorial URL
for url in urls:
    # Request page source from URL
    page = requests.get(url)
    
    # Check if the request was successful
    if page.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(page.content, 'html.parser')
        
        page_title = soup.title.text.strip()

        # Find the specific div with class 'w3-col l10 m12' and id 'main'
        main_content = soup.find('div', {'class': 'w3-col l10 m12', 'id': 'main'})

        # Find all the <h2> tags within this specific div
        headlines = main_content.find_all('h2')
            
        # Store the URL and the text of each headline
        for headline in headlines:
            # Exclude headlines within the div with class 'w3-panel' and id 'getdiploma'
            parent_div = headline.find_parent('div', {'class': 'w3-panel', 'id': 'getdiploma'})
                
            if parent_div is None:
                data.append({
                    'URL': url,
                    'Page Title': page_title,
                    'Headline': headline.get_text().strip()
                })
    else:
        print(f"Failed to retrieve the webpage: {url}. Status code: {page.status_code}")

# Create a DataFrame from the data
df = pd.DataFrame(data)

split_columns = df['Page Title'].str.split('-', n=1, expand=True)

# Rename the columns after splitting
split_columns.columns = ['Title', 'Sub title']

# Handle rows where there was no hyphen
split_columns['Sub title'].fillna('', inplace=True)

# Merge the split columns back into the original dataframe
df[['Title', 'Sub title']] = split_columns[['Title', 'Sub title']]
df = df[['URL', 'Title', 'Sub title', 'Headline']]
# Save the DataFrame to a CSV file
df.to_csv('headlines.csv', index=False)

print("Data has been saved to headlines.csv")
