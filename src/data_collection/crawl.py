import wptools
import requests

class Crawler:
    def __init__(self, category, limit=100):
        self.category = category.lower()
        self.limit = limit
        self.pages = []

        assert self.category == "nba players" or self.category == "computer scientists",\
              "Category must be either 'nba players' or 'computer scientists'"

    def get_category_page(self):
        if self.category == "nba players":
            url = "https://en.wikipedia.org/wiki/Lists_of_NBA_players"
        else:
            url = "https://en.wikipedia.org/wiki/List_of_computer_scientists"

        page = wptools.page(url)
            
        return page
    

cralwer = Crawler("nba players")
page = cralwer.get_category_page()
print(page)
