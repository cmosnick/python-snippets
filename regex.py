import re


badstring = '<div class="classname"><p class="classname" style="stylestuffhere">helloworld</p></div>'
print(badstring)


goodstring = re.sub(r"(?<=(\<[a-zA-Z]{1}))+ [^\>]*(?=\>)|(?<=(\<[a-zA-Z]{2}))+ [^\>]*(?=\>)|(?<=(\<[a-zA-Z]{3}))+ [^\>]*(?=\>)|(?<=(\<[a-zA-Z]{4}))+ [^\>]*(?=\>)|(?<=(\<[a-zA-Z]{5}))+ [^\>]*(?=\>)|(?<=(\<[a-zA-Z]{6}))+ [^\>]*(?=\>)", "", badstring)
print(goodstring)