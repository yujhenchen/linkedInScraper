from pages.components.search_bar import searchBar


def test_get_keyword_input():
    keyword_input = searchBar.keyword_input()
    print(keyword_input.text)
