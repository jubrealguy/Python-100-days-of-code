from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/news")
web_page = res.text

soup = BeautifulSoup(web_page, "html.parser")
# print(soup.title.string)
n = 1

#Texts
article_tags = soup.find_all(name="span", class_="titleline")
texts = []
links = []
for a in article_tags:
    texts.append(a.find(name='a').string)
    links.append(a.find(name='a').get("href"))

print(texts)
print(links)
upvotes = [int(votes.getText().split()[0]) for votes in soup.find_all(name="span", class_="score")]
print(upvotes)

indexes = []
sorted_votes = sorted(upvotes, reverse=True)
for vote in sorted_votes:
    index = upvotes.index(vote)
    indexes.append(index)

print(indexes)

for index in indexes:
    print(upvotes[index], texts[index])
    # print(f"{n}.", index, upvotes[index], texts[index], links[index])
    n+=1












# import lxml

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "lxml")
# # Gets the content
# # print(soup.title.string)

# # Finding all tags in a website
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)

# # for tag in all_anchor_tags:
# #     print(tag.string)
# #     print(tag.getText())
# # Gets the value of an attribute
# #     print(tag.get("href"))

# findings = soup.find(name="h1", id="name")
# print(findings.getText())