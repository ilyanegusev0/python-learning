# LESSON #18. Декораторы функций

import webbrowser as wb


def validator(func):
    def wrapper(value):
        if '.' in value:
            func(value)
        else:
            print("Incorrect URL.")

    return wrapper


@validator
def open_url(url):
    wb.open(url)


open_url("https://google.com")
