import pandas as pd
import numpy as np
import pdfkit
import matplotlib as plt
# from matplotlib.backends.backend_pdf import PdfPages

def topProducts(filename, top = 10):
	df = pd.read_csv(filename, low_memory=True, encoding='utf-8')
	datos = filtroConcilia(df)
	datos = (datos.groupby(['Id_Producto','Nombre_Producto']).agg({'Indice':'count', 'Precio_Venta_Producto': 'sum'}).reset_index().rename(columns={'Piezas_Vendidas':'Total de Venta'}))
	datos = pd.DataFrame(datos.sort_values(by=['Precio_Venta_Producto','Indice'],ascending=False))
	data = pd.DataFrame(datos.head(top)) 
	x = range(0,top)
	data.to_csv((filename.replace('.csv','_output_Top')+((str) (top))+'.csv'), index=False,encoding='utf-8-sig')

def topAllCategories(filename, top = 10):
	df = pd.read_csv(filename, low_memory = True, encoding = 'utf-8')
	datos = filtroConcilia(df)
	categories = datos['Categoria'].unique()
	D = {}
	i = 0
	for category in categories:
		topCat = datos[datos['Categoria'] == category]
		topCat = (topCat.groupby(['Id_Producto','Nombre_Producto','Categoria']).agg({'Indice':'count', 'Precio_Venta_Producto': 'sum'}).reset_index().rename(columns={'Piezas_Vendidas':'Total de Venta'}))
		topCat = pd.DataFrame(topCat.sort_values(by=['Precio_Venta_Producto','Indice'],ascending=False))
		topCat = pd.DataFrame(topCat)
		topCat['Piezas_Vendidas'] =  topCat['Indice']
		topCat['Precio_Venta_Producto'] = topCat['Precio_Venta_Producto'].apply(format)
		topCat['Venta_Producto'] = topCat['Precio_Venta_Producto']
		topCat = topCat.drop(columns = ['Precio_Venta_Producto','Indice'])
		topCat = pd.DataFrame(topCat.head(top)).reset_index(drop = True)
		D[i] = pd.DataFrame(topCat.head(top))
		i += 1
	
	# for x in range(len(categories)):
	# 	try:
	# 		print(categories[x])
	# 		# print(D[x])
	# 		f = open(categories[x]+'.html','w')
	# 		table = pd.DataFrame(D[x])
	# 		# # styles = [{'props':[("font-family", "Calibri")]},
	# 		# # {
	# 		# # 	'selector': 'th',
	# 		# # 	'props': [
	# 		# # 		('background-color', 'yellow')]
	# 		# # 		}
	# 		# # ]
	# 		# table.style.set_properties(**{"font-family":"Calibri",
	# 		# 	"font-size":"30px"

	# 		# })
	# 		a = table.to_html()
	# 		f.write(a)
	# 		f.close()
	# 		path_wkhtmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
	# 		config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
	# 		pdfkit.from_file(categories[x]+'.html',('TOP'+ (str (top)) + categories[x] + '.pdf') ,configuration=config)
	# 		print(x)

	# 	except:
	# 		continue
	table = pd.DataFrame(D[0])
	print('pruebaas')
	write_to_html_file(table, title='Prueba' , filename="prueba.html")
# print(D[1])# data.to_csv((filename.replace('.csv','_output_Top')+((str) (top))+'.csv'), index=False,encoding='utf-8-sig')

def filtroConcilia(data):
	datos = data  
	print(datos['Estatus_Reza'].unique())
	print(len(datos))
	df2 = datos[datos['Estatus_Reza'] == 'Autorizado']
	print('autorizados')
	print(len(df2))
	
	estatus_p = ['Cancelado','En disputa','Cancelado por Validación Telefónica','Dictaminado Fraude Telmex','Intento','Pendiente por Validación Telefónica','Rechazo validación manual','Reembolso realizado','Rechazado','Reembolso autorizado','TDC rechazada']
	for x in range(len(estatus_p)):
		df2=df2[df2['Estatus_Pedido_Desc']!=estatus_p[x]]
		print(estatus_p[x])
		print(len(df2))

	estatus_pr = ['Cancelado','Solicita Cancelacion','En disputa','Cancelado','Cancelado por Validación Telefónica','Dictaminado Fraude Telmex','Intento','Pendiente por Validación Telefónica','Rechazo validación manual','Reembolso realizado','Rechazado','Reembolso autorizado','Solicita rembolso','TDC rechazada']
	for x in range(len(estatus_pr)):
		df2 = df2[df2['EstatusProducto']!=estatus_pr[x]]
		print(estatus_pr[x])
		print(len(df2))
	
	# df2['MotivoCancela'] = df2['MotivoCancela'].fillna(0)
	# df2 = df2[df2['MotivoCancela']==0]
	print('MotivoCancela')
	print(len(df2))
	return df2

def format(x):
		return '${0:,.2f}'.format(x)

def write_to_html_file(df, title='', filename='out.html'):
	print('llego')
	result = '''
		<html>
		<head>
		<style>

			h2 {
				text-align: center;
				font-family: Helvetica, Arial, sans-serif;
			}
			table { 
				margin-left: auto;
				margin-right: auto;
			}
			table, th, td {
				border: 1px solid black;
				border-collapse: collapse;
			}
			th, td {
				padding: 5px;
				text-align: center;
				font-family: Helvetica, Arial, sans-serif;
				font-size: 90%;
			}
			table tbody tr:hover {
				background-color: #dddddd;
			}
			.wide {
				width: 90%; 
			}

		</style>
		</head>
		<body>
		'''
	result += '<h2> %s </h2>\n' % title
	if type(df) == pd.io.formats.style.Styler:
		result += df.render()
	else:
		result += df.to_html(classes='wide', escape=False)
		result += '''
		</body>
	</html>
	'''
	with open(filename, 'w') as f:
		f.write(result)

