# Use a regex to strip all html tag attributes, up to 6 instances of tags
# Input: <div class="classname"><p class="classname" style="stylestuffhere">helloworld</p></div>
# Output: <div><p>helloworld</p></div>

import re

badstring = '<div class="classname"><p class="classname" style="stylestuffhere">helloworld</p></div>'
print(badstring)


goodstring = re.sub(r"(?<=(\<[a-zA-Z]{1}))+ [^\>]*(?=\>)|(?<=(\<[a-zA-Z]{2}))+ [^\>]*(?=\>)|(?<=(\<[a-zA-Z]{3}))+ [^\>]*(?=\>)|(?<=(\<[a-zA-Z]{4}))+ [^\>]*(?=\>)|(?<=(\<[a-zA-Z]{5}))+ [^\>]*(?=\>)|(?<=(\<[a-zA-Z]{6}))+ [^\>]*(?=\>)", "", badstring)
print(goodstring)