import requests

from bs4 import BeautifulSoup



def simple_web_crawler(start_url, max_depth=3):

    visited = set([start_url])

    current_url = start_url

    for depth in range(max_depth):

        try:

            response = requests.get(current_url)

            soup = BeautifulSoup(response.text, 'html.parser')



            # Print the current URL and the title of the page

            print(f"Depth {depth}: {current_url}")

            print(f"Title: {soup.title.string if soup.title else 'No title'}\n")



            # Find all links on the page

            links = soup.find_all('a', href=True)

            for link in links:

                href = link['href']

                if href not in visited:

                    visited.add(href)

                    current_url = href

                    break

            else:

                print("No new links found, stopping.")

                break

        except Exception as e:

            print(f"Failed to fetch {current_url} due to {e}. Skipping.")

            break



# Example usage

start_url = 'http://google.com'

simple_web_crawler(start_url, max_depth=3)

