import w3lib.html
doc = '<div><p><b>This is a link </b><a href="www.example.com"> example</a>></a><<p></div>'
result =w3lib.html.remove_tags_with_content(doc, which_ones=('b',))
print(result)