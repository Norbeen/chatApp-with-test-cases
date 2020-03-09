from rfc3987 import parse


def validateUrl(string):
    url_message = ""
    nonurl_message = ""
    try:
        parsed_message = parse(string, rule='URI')
        url_message = string
        print("Got an URL:", url_message)
    except:
        nonurl_message = string
        print("Not an URL: ", nonurl_message)
    return url_message, nonurl_message
