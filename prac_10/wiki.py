"""
CP1404/CP5632 Practical
Wikipedia API
"""
import wikipedia

search = input("Page title or Search Phrase: ")
while search != "":
    result = wikipedia.search(search)
    page = wikipedia.page(result)
    summary = wikipedia.summary(page)
    print("Page Title: ", page.title)
    print("Page Summary: ", summary)
    print("Page Url: ", page.url)
    search = input("Page title or Search Phrase: ")
