# Use a regex to extract html values from inside the tags
# Input: <div class="classname"><p class="classname" style="stylestuffhere">helloworld</p></div><div lwqkdnwlqe>hello again</div>
# Output: helloworld   hello again

import re


badstring = '<div class="classname"><p class="classname" style="stylestuffhere">helloworld</p></div><div lwqkdnwlqe>hello again</div>'
print(badstring)

regexpattern = r"(\<[^\>]*\>)"
goodstring = re.sub(regexpattern, " ", badstring)
print(goodstring)