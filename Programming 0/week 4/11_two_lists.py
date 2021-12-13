def combine_lists(list_a, list_b):
    for name in list_a:
        for technology in list_b:
            print(name, technology)

combine_lists(['Ivan', 'Maria'], ['Python', 'Django'])