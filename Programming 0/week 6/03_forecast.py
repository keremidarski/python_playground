# Problem description:
# https://github.com/HackBulgaria/Programming0-1/tree/master/week6/3-Forecast

def forecast(days):
    sunny_days = 0
    rainy_days = 0
    snowy_days = 0

    for day in days:
        if day == 'sunshine':
            sunny_days += 1
        elif day == 'rain':
            rainy_days += 1
        elif day == 'snow':
            snowy_days += 1
    
    if sunny_days > rainy_days and sunny_days > snowy_days:
        return 'sunshine'
    elif rainy_days > sunny_days and rainy_days > snowy_days:
        return 'rain'
    elif snowy_days > rainy_days and snowy_days > sunny_days:
        return 'snow'
    elif snowy_days == rainy_days and snowy_days > sunny_days:
        return 'sunshine'
    elif sunny_days == snowy_days and sunny_days > rainy_days:
        return 'rain'
    elif rainy_days == sunny_days and rainy_days > snowy_days:
        return 'snow'
    elif sunny_days == rainy_days and sunny_days == snowy_days:
        return days[-1]

days = ["snow", "snow", "rain", "sunshine"]
print(forecast(days))
