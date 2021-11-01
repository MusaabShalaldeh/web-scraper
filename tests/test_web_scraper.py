from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report, mexico_wiki_url

def test_version():
    assert __version__ == '0.1.0'





def test_citation_needed():
    # Arange
    expected = 5

    # Actual
    actual = get_citations_needed_count(mexico_wiki_url)

    # Assert
    assert actual == expected


# not really sure how to make a test for the required report....