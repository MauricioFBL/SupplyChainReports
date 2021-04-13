import pandas as pd
import numpy as np
import pdfkit
from tqdm import tqdm
import pandas.io.formats.style

def topProducts(filename, top = 10):
	df = pd.read_csv(filename, low_memory=True, encoding='utf-8')
	datos = filtroConcilia(df)
	datos = (datos.groupby(['Id_Producto','Nombre_Producto']).agg({'Id_RelacionPed':'count', 'Precio_Venta_Producto': 'sum'}).reset_index().rename(columns={'Piezas_Vendidas':'Total de Venta'}))
	datos = pd.DataFrame(datos.sort_values(by=['Precio_Venta_Producto','Id_RelacionPed'],ascending=False))
	data = pd.DataFrame(datos.head(top)) 
	x = range(0,top)
	data.to_csv((filename.replace('.csv','_output_Top')+((str) (top))+'.csv'), index=False,encoding='utf-8-sig')

def topAllCategories(filename, top = 10):
	df = pd.read_csv(filename, encoding = 'utf-8')
	print('>>>>> ARCHIVO CARGAGO')
	datos = filtroConcilia(df)
	datos = rencodigIaacute(datos)
	categories = datos['Categoria'].unique()
	D = {}
	i = 0
	for category in categories:
		topCat = datos[datos['Categoria'] == category]
		topCat = (topCat.groupby(['Id_Producto','Nombre_Producto','Categoria']).agg({'Id_RelacionPed':'count', 'Precio_Venta_Producto': 'sum'}).reset_index().rename(columns={'Piezas_Vendidas':'Total de Venta'}))
		topCat = pd.DataFrame(topCat.sort_values(by=['Precio_Venta_Producto','Id_RelacionPed'],ascending=False))
		topCat = pd.DataFrame(topCat)
		topCat['Piezas_Vendidas'] =  topCat['Id_RelacionPed']
		topCat['Precio_Venta_Producto'] = pd.to_numeric(topCat['Precio_Venta_Producto']).apply(format)
		topCat['Venta_Producto'] = topCat['Precio_Venta_Producto']
		topCat = topCat.drop(columns = ['Precio_Venta_Producto','Id_RelacionPed'])
		topCat = pd.DataFrame(topCat.head(top)).reset_index(drop = True)
		D[i] = pd.DataFrame(topCat.head(top))
		i += 1
	
	for x in range(len(categories)):
		try:
			print(categories[x])
			table = pd.DataFrame(D[x]).style.hide_index()
			writeHtml(table, title = categories[x], filename = 'reporte.html')
			# writeHtml(table, title = categories[x], filename = categories[x]+'.html')
			path_wkhtmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
			config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
			pdfkit.from_file('reporte.html',('TOP'+ (str (top)) + categories[x] + '.pdf') ,configuration=config)
		except:
			continue

def filtroConcilia(data):
	datos = data  
	print('>>>>> FILTRANDO ARCHIVO')
	df2 = datos[datos['Estatus_Reza'] == 'Autorizado']
	print('autorizados')
	print(len(df2))
	
	# estatus_p = ['Cancelado','En disputa','Cancelado por Validación Telefónica','Dictaminado Fraude Telmex','Intento','Pendiente por Validación Telefónica','Rechazo validación manual','Reembolso realizado','Rechazado','Reembolso autorizado','TDC rechazada']
	# for x in range(len(estatus_p)):
	# 	df2=df2[df2['Estatus_Pedido_Desc']!=estatus_p[x]]
	# 	print(estatus_p[x])
	# 	print(len(df2))

	# estatus_pr = ['Cancelado','Solicita Cancelacion','En disputa','Cancelado','Cancelado por Validación Telefónica','Dictaminado Fraude Telmex','Intento','Pendiente por Validación Telefónica','Rechazo validación manual','Reembolso realizado','Rechazado','Reembolso autorizado','Solicita rembolso','TDC rechazada']
	# for x in range(len(estatus_pr)):
	# 	df2 = df2[df2['EstatusProducto']!=estatus_pr[x]]
	# 	print(estatus_pr[x])
	# 	print(len(df2))
	
	# df2['MotivoCancela'] = df2['MotivoCancela'].fillna(0)
	# df2 = df2[df2['MotivoCancela']==0]
	# print('MotivoCancela')
	# print(len(df2))
	return df2

def format(x):
		return '${0:,.2f}'.format(x)

def writeHtml(df, title='', filename='out.html'):
	result = '''
		<html>
		<head>
		<meta charset="utf-8">
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
				text-align: justify;
				font-family: Helvetica, Arial, sans-serif;
				font-size: 85%;
				height: 25px;
			}
            th {
                background-color : #FF0000;
                color: #FFFFFF
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

def rencodigIaacute(data):
	df = data
	print(">>>>> CORRECCION DE CARACTERES")
	pbar = tqdm(total=14)
	df = df.replace("&aacute;","a", regex=True)
	pbar.update(1)
	df = df.replace("&eacute;","e", regex=True)
	pbar.update(1)
	df = df.replace("&iacute;","i", regex=True)
	pbar.update(1)
	df = df.replace("&oacute;","o", regex=True)
	pbar.update(1)
	df = df.replace("&uacute;","i", regex=True)
	pbar.update(1)
	df = df.replace("&Aacute;","A", regex=True)
	pbar.update(1)
	df = df.replace("&Eacute;","E", regex=True)
	pbar.update(1)
	df = df.replace("&Iacute;","I", regex=True)
	pbar.update(1)
	df = df.replace("&Oacute;","O", regex=True)
	pbar.update(1)
	df = df.replace("&Uacute;","U", regex=True)
	pbar.update(1)
	df = df.replace("&deg;","°", regex=True)
	pbar.update(1)
	df = df.replace("&quot;","", regex=True)
	pbar.update(1)
	df = df.replace("&#039;","'", regex=True)
	pbar.update(1)
	df = df.replace("&ntilde;","ñ", regex=True)
	pbar.update(1)
	pbar.close()
	return df

topAllCategories('Concilia-Oct.csv')
