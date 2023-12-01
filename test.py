#pip install googlesearch-python

# from googlesearch import search

# api_key = "AIzaSyCGvOZdAY03ePGTsNzCfz1YSsODqnnJM2k"  # Replace with your actual API key
# query = "Amazfit Pop2 Ultra"

# results = search(query, num=10, stop=10, pause=2, api_key=api_key)

# for result in results:
#     print(result)



# from googlesearch import search

# query = "AMAZFIT Pop"
# num_results = 2

# for i, result in enumerate(search(query, num_results=num_results), start=1):
#     print(f"{i}. {result}")

# import urllib.parse
# from bs4 import BeautifulSoup

# import requests

# def google_search_url(query):
#     base_url = "https://www.google.com/search"
#     query_params = {'q': query}
#     search_url = base_url + '?' + urllib.parse.urlencode(query_params)
#     return search_url

# Example usage:
# query = "Amazfit Pop2 Ultra"
# search_url = google_search_url(query)
# # print("Google Search URL:", search_url)

# def get_links_from_google_search(search_url):
#     # search_url = f"https://www.google.com/search?q={query}"
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
#     response = requests.get(search_url, headers=headers)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         cite_tags = soup.find_all('cite')
#         links = [cite.text for cite in cite_tags]
#         return links
#     else:
#         print(f"Failed to fetch {search_url}. Status code: {response.status_code}")
#         return []

# links = get_links_from_google_search(search_url)

# for link in links:
#     print(link)

# import requests
# from bs4 import BeautifulSoup

# def fetch_google_search_results(query):
#     base_url = "https://www.google.com/search"
#     params = {'q': query}
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

#     response = requests.get(base_url, params=params, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     results = []
#     for link in soup.find_all('a'):
#         href = link.get('href')
#         if href and '/url?q=' in href:
#             url = href.split('/url?q=')[1].split('&')[0]
#             results.append(url)

#     return results

# # Example usage:
# query = "Amazfit Pop2 Ultra"
# search_results = fetch_google_search_results(query)

# if search_results:
#     for i, result in enumerate(search_results, start=1):
#         print(f"{i}. {result}")
# else:
#     print("No results found.")

# import requests
# from bs4 import BeautifulSoup

# def get_google_search_links(query):
#     url = f"https://www.google.com/search?q={query}"
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         cite_tags = soup.find_all('a')
#         links = [cite.get('href') for cite in cite_tags]
#         return links
#     else:
#         print(f"Failed to fetch {url}. Status code: {response.status_code}")
#         return []

# query = "AMAZFIT Pop 2 with Ultra-"
# links = get_google_search_links(query)

# for link in links[:2]:
#     print(link)

import requests
from bs4 import BeautifulSoup

def get_google_search_links(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        result_divs = soup.find_all('div', class_='tF2Cxc')  # Adjust the class based on the current structure

        links = []
        for result_div in result_divs:
            link_tag = result_div.find('a')
            if link_tag:
                href_value = link_tag.get('href')
                clean_url = href_value.split('&')[0]
                links.append(clean_url)

        return links
    else:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")
        return []

query = "ujjain temple"
links = get_google_search_links(query)

for link in links[:2]:
    print(link)




