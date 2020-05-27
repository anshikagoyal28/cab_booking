import re


def check_email(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, email):
        return True
    else:
        return False


def check_name(name):
    regex = re.compile(r'^([a-z]+) *( [a-z]+)*$', re.IGNORECASE)
    if regex.search(name):
        return True
    else:
        return False
    # bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', "aastha bhanda"))


def check_id(id):
    if id.isdigit():
        return True
    else:
        return False


