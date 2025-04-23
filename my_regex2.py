import re

def logs():
    with open("../talktoweb/assets/logdata.txt", "r") as file:
        logdata = file.read()

    # YOUR CODE HERE
    pattern = """
    (?P<host>.*)         # Host IP
    (\ -\ )              # Separator 1
    (?P<user_name>\w*|-)   # The User name doesn't have a space
    (\s\[)               # space and brackets for the time delimitation
    (?P<time>.*)         # time of requisition
    (\]\ ")              # separatior of Requisition
    (?P<request>\w*\ .*)  # Request Specs only grab POST
    ("\w*\n)                   # end of line
    """
    result = []
    for item in re.finditer(pattern, logdata, re.VERBOSE):
        result.append(item.groupdict())
    return result
assert len(logs()) == 979
print(logs())
results = logs()
one_item = {
    "host": "146.204.224.152",
    "user_name": "feest6811",
    "time": "21/Jun/2019:15:45:24 -0700",
    "request": "POST /incentivize HTTP/1.1",
}
assert one_item in results