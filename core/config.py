# input used to test for injection
# TODO: add more eventHandlers
# TODO: add more specialTagAttr
TEST_INJCT = "6ix8uzz"

eventHandlers = ["onload", "onclick",  "onmouseover"]
specialTagAttrs = ["src", "href"]
tags = ["div"]

# inputs that may be filtered
filtered_inputs = ["<", ">", "script", "\'", "\""]

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip',
    'Connection': 'close',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
}
