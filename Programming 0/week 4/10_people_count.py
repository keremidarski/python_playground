def get_people_count(activity):
    people_count = []

    for person in activity:
        if person not in people_count:
            people_count.append(person)

    return len(people_count)

print(get_people_count(["Rado", "Ivo", "Maria", "Anneta", "Rado", "Rado", "Anneta", "Ivo", "Maria", "Rado"]))