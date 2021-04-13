import pandas as pd
import numpy as np
import datetime as dt
from tqdm import tqdm
import sys
if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")
def rencodigIaacute(archivo):
	# df =pd.read_csv("C:/Users/mauxy/Documents/prono_30.csv",engine='python')
	fileName_ = archivo
	print('>>>>>CARGAGO ARCHIVO')
	df=pd.read_csv(fileName_,low_memory=True , encoding='utf-8')
	print(">>>>>ARCHIVO CARGAGO")
	pbar = tqdm(total=14)
	df = df.replace("&aacute;","á", regex=True)
	pbar.update(1)
	df = df.replace("&eacute;","é", regex=True)
	pbar.update(1)
	df = df.replace("&iacute;","í", regex=True)
	pbar.update(1)
	df = df.replace("&oacute;","ó", regex=True)
	pbar.update(1)
	df = df.replace("&uacute;","ú", regex=True)
	pbar.update(1)

	df = df.replace("&Aacute;","Á", regex=True)
	pbar.update(1)
	df = df.replace("&Eacute;","É", regex=True)
	pbar.update(1)
	df = df.replace("&Iacute;","Í", regex=True)
	pbar.update(1)
	df = df.replace("&Oacute;","Ó", regex=True)
	pbar.update(1)
	df = df.replace("&Uacute;","Ú", regex=True)
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

	print("Finalizado")
	df.to_csv(archivo+"output.csv",encoding='utf-8-sig',index=False)


def rencodingAfa(fileName_ = "C:/Users/mauxy/Documents/sumarizadoSANBORNS_.csv"):
	
	df=pd.read_csv(fileName_,low_memory=True , encoding='utf-8')
	print("Trabajando")
	df = df.replace("ÃƒÂ¡","á", regex=True)
	df = df.replace("ÃƒÂ©","é", regex=True)
	df = df.replace("ÃƒÂ­-","í", regex=True)
	df = df.replace("ÃƒÂ³","ó", regex=True)
	df = df.replace("ÃƒÂº","ú", regex=True)

	# df = df.replace("&Aacute;","Á", regex=True)
	# df = df.replace("","É", regex=True)
	# df = df.replace("ÃƒÂ-","Í", regex=True)
	# df = df.replace("&Oacute;","Ó", regex=True)
	# df = df.replace("&Uacute;","Ú", regex=True)

	# df = df.replace("&deg;","°", regex=True)
	# df = df.replace("&quot;","", regex=True)
	# df = df.replace("&#039;","'", regex=True)
	df = df.replace("ÃƒÂ±","ñ", regex=True)

	print("Finalizado")
	df.to_csv(fileName_ +'_output.csv',encoding ='utf-8-sig',index=False)
# rencodingAfa()

# rencodigIaacute("C:/Users/mauxy/Downloads/Concilia CS 19102020.csv")
# rencodigIaacute("C:/Users/mauxy/Documents/BUENFIN_FCST_.csv")
rencodigIaacute("C:/Users/mauxy/Documents/resumenBasePronosticoLunes.csv")