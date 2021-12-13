def winter_is_coming(seasons):
    is_coming = False
    counter = 0

    for season in seasons:
        if season != 'winter':
            counter += 1
        else:
            counter = 0
    
    if counter >= 5:
        is_coming = True

    return is_coming

print(winter_is_coming(["spring", "summer", "summer", "spring", "srping"]))