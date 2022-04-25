#todo: Задан словарь, его значения необходимо внести по соответствующим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">
 
  <p>?</p>

 </body>
</html>
"""

index_html = open('index.html', 'w')
index_html.write(template)
index_html.close()
index_html = open('index.html', 'r')
index_html_list = list(index_html.readlines())
for key in page.keys():
        for phrase in index_html_list:
                if key in phrase:
                        index_html_list[index_html_list.index(phrase)] = phrase.replace('?', page.get(key))
index_html.close()
index_html = open('index.html', 'w')
index_html.writelines(index_html_list)
index_html.close()