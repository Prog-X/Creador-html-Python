import ctypes

print "Bienvenido Al Creador De Archivos HTML Python\n"
nombre_py = raw_input("Escriba el nombre del archivo\n")
titulo_py = raw_input("Escriba el titulo\n")
contenido_py = raw_input("Escriba el Contenido\n")
NombreHtml = nombre_py+".html"
html_py=open(NombreHtml,'w')
html_py=open(NombreHtml,'a')

html_py.write("<html>"+"<title>"+titulo_py+"</title>"+"<body>"+contenido_py+"</body>"+"</html>")
html_py.close()


ctypes.windll.user32.MessageBoxA(0, "Se ha creado con exito!!", "Python Creador Html", 0)
