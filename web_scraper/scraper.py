"""
fill this later
"""
import requests
from bs4 import BeautifulSoup

mexico_wiki_url = "https://en.wikipedia.org/wiki/History_of_Mexico"





def get_citations_needed_count(url: str):
    """
    fill this later
    """
    count = 0
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    result = soup.find("div",id="mw-content-text") # makes search faster.
    citations_needed = result.find_all('sup',class_="noprint Inline-Template Template-Fact")
    for i in citations_needed:
        count += 1
    return count
    



def get_citations_needed_report(url: str):
    """
    fill this later
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    result = soup.find("div",id="mw-content-text") # makes search faster.
    citations_needed = result.find_all('sup',class_="noprint Inline-Template Template-Fact")
    final_string = ""
    for i in citations_needed:
        text = i.previous_element.text.replace(")","").strip()
        string = f'Citation needed for "{text}"'
        final_string += f"\n{string}"

    return final_string


if __name__ == '__main__':
    print(get_citations_needed_report(mexico_wiki_url))