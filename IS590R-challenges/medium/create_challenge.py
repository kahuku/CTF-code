import random

pages = 50
links_per_page = 200

f = open("challenge/start.html", 'w')
words = open("words.txt","r").read().splitlines()

for i in range(pages):
    html_template = """
    <html>
    <head>
    <title>Challenge</title>
    </head>
    <body>
    <h2>Are you still clicking?</h2>
    """

    cut = random.randint(0, links_per_page)
    true_link = random.choice(words)

    for j in range(cut):
        word = random.choice(words)
        html_template += f"<a>{word}</a><br>"

    html_template += f"<a href='./{true_link}.html' style='text-decoration: none; color: black;'>{true_link}</a><br>"

    for j in range(cut + 1, links_per_page):
        word = random.choice(words)
        html_template += f"<a>{word}</a><br>"
    
    html_template += "</body></html>"
  
    f.write(html_template)
    f.close()

    print(cut, true_link)

    f = open("challenge/" + true_link + ".html", 'w')

f.close()