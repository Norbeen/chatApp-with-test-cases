from rfc3987 import parse


def validateUrl(string):
    url_message = ""
    nonurl_message = ""
    try:
        parsed_message = parse(string, rule='URI')
        url_message = string
    except:
        nonurl_message = string
    return url_message, nonurl_message
