import re

for x in [x for x in iter(input, 'end')]:
    res = re.sub(r"<a\s?href=\"(.*?)\">(.*?)</a>", r"[URL href=\"\1\">\2[/URL]", x)
    res = res.replace('\\','')
    res = res.replace('">', '"]')
    print(res)

'''
input:
<ul>
  <li>
    <a href="http://softuni.bg">SoftUni</a>
 </li>
</ul>
end

output:
<ul>
  <li>
    [URL href="http://softuni.bg"]SoftUni[/URL]
  </li>
</ul>
'''
