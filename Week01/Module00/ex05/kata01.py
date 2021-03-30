languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
}

for language, author in languages.items():
    print("%(language)s was created by %(author)s" % {"language":language, "author":author})
