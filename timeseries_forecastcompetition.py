import pandas as pd
import numpy as np
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
from tqdm import tqdm
import pmdarima as pm
import sys
import smtplib
from socket import gaierror
if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")

final=pd.DataFrame()

def calculomape(sreal,spred):
        try:
                mape = (abs(sreal-spred)/sreal)*100
                return(mape)
        except Exception as e:
                mape = 2000
                return(mape) 

def readData(i):
        df = pd.read_csv('C:/Users/mauxy/Documents/MatrizPronosticoLunes9.csv')
        df = df.iloc[[i],:]
        df = (np.transpose(df))
        df = df.fillna(0)
        df.columns = df.iloc[0]
        df = df.tail(len(df)-1)
        return(df)

def mapear(i):
        df = i
        train = df.iloc[:(round(len(df)*.85)),0]
        hell = df.iloc[(round(len(df)*.85)):,0]
        model = pm.auto_arima(train, start_p=0, start_q=0,
                        test='adf',       # use adftest to find optimal 'd'
                        max_p=3, max_q=3, # maximum p and q
                        m=1,              # frequency of series
                        d=None,           # let model determine 'd'
                        seasonal=False,   # No Seasonality
                        start_P=0, 
                        D=0,
                        trace=True,
                        error_action='ignore',  
                        suppress_warnings=True, 
                        stepwise=True)
        longitr = round(len(df)*.90)
        longitp = len(df)
        n_periods = len(hell)
        fc, confint = model.predict(n_periods=n_periods, return_conf_int=True)
        sreal = (sum(hell))
        spred = (sum(fc))
        mape = calculomape(sreal,spred)
        return(mape) 

def mapesar(i):
        df = i 
        train = df.iloc[:(round(len(df)*.85)),0]
        hell = df.iloc[(round(len(df)*.85)):,0]
        model = pm.auto_arima(train, start_p=0, start_q=0,
                        test='adf',       # use adftest to find optimal 'd'
                        max_p=3, max_q=3, # maximum p and q
                        m=1,              # frequency of series
                        d=None,           # let model determine 'd'
                        seasonal=True,   # No Seasonality
                        start_P=0, 
                        D=1, 
                        trace=True,
                        error_action='ignore',  
                        suppress_warnings=True, 
                        stepwise=True)
        longitr = round(len(df)*.90)
        longitp = len(df)
        n_periods = len(hell)
        fc, confint = model.predict(n_periods=n_periods, return_conf_int=True)
        sreal = (sum(hell))
        spred = (sum(fc))
        mape = calculomape(sreal,spred)
        return(mape)
        
def holttm(i):
        df = i
        train = np.asarray(df.iloc[:(round(len(df)*.85)),0])
        hell = df.iloc[(round(len(df)*.85)):,0]
        fit1p = Holt(train).fit(smoothing_level=0.3, smoothing_slope=0.13, optimized= False)
        fcastp = fit1p.forecast(len(hell))
        sreal = (sum(hell))
        spred = (sum(fcastp))
        mape = calculomape(sreal,spred)
        return(mape)  

def sesm(i):
        df = i
        train = np.asarray(df.iloc[:(round(len(df)*.85)),0])
        hell = df.iloc[(round(len(df)*.85)):,0]
        fit1 = SimpleExpSmoothing(train).fit(smoothing_level=0.2,optimized=True)
        suav = fit1.fittedvalues
        fcast1 = fit1.forecast(len(hell))
        sreal = (sum(hell))
        spred = (sum(fcast1))
        mape = calculomape(sreal,spred)
        return(mape)        
######
def autosar(i,fc_periods,df):
        df = df     
        hell=df.iloc[0:,0]
        model = pm.auto_arima(hell, start_p=0, start_q=0,
                        test='adf',       # use adftest to find optimal 'd'
                        max_p=3, max_q=3, # maximum p and q
                        m=1,              # frequency of series
                        d=None,           # let model determine 'd'
                        seasonal=True,   # No Seasonality
                        start_P=0, 
                        D=1, 
                        trace=True,
                        error_action='ignore',  
                        suppress_warnings=True, 
                        stepwise=True)       
        n_periods = fc_periods
        fc, confint = model.predict(n_periods=n_periods, return_conf_int=True)
        return(fc)

def autoar(i,fc_periods,df):
        df = df
        hell=df.iloc[:394,0]
        hell=df.iloc[0:,0]
        model = pm.auto_arima(hell, start_p=0, start_q=0,
                        test='adf',       # use adftest to find optimal 'd'
                        max_p=3, max_q=3, # maximum p and q
                        m=1,              # frequency of series
                        d=None,           # let model determine 'd'
                        seasonal=False,   # No Seasonality
                        start_P=0, 
                        D=0, 
                        trace=True,
                        error_action='ignore',  
                        suppress_warnings=True, 
                        stepwise=True)       
        n_periods = fc_periods
        fc, confint = model.predict(n_periods=n_periods, return_conf_int=True)
        return(fc)

def holtt(i,fc_periods,df):
        df = df
        hell=np.asarray(df.iloc[0:,0])
        train=df.iloc[394:,0]
        modelo=SimpleExpSmoothing(hell).fit(smoothing_level=.2,optimized=False)
        resultado=modelo.fittedvalues
        df['pronostico']=resultado
        nombre=list(df.columns.values.tolist())
        fit1 = Holt(hell).fit(smoothing_level=0.35, smoothing_slope=0.1, optimized= True)
        print(fit1.summary())
        fcast1 = fit1.forecast(fc_periods)
        return(fcast1)
        
def sess(i,fc_periods,df):
        df = df
        saledata=np.asarray(df.iloc[0:,0])
        fit1 = SimpleExpSmoothing(saledata).fit(smoothing_level=0.2,optimized=True)
        suav=fit1.fittedvalues
        df['pronostico']=suav
        nombre=list(df.columns.values.tolist())
        fcast1 = fit1.forecast(fc_periods)
        return(fcast1)

def pronosticar(i,fc_periods,data):
        
        df = data
        df = df.iloc[[i],:]
        df = (np.transpose(df))
        df.columns = df.iloc[0]
        df = df.tail(len(df)-1)
        nombre = list(df.columns.values.tolist())
        
        df = df.fillna(0)
        sarim = mapesar(df)
        holtw = holttm(df)
        arima = mapear(df)
        ssuav = sesm(df)
        print("DATSET")
        print(df)
        if sarim<holtw and sarim<arima and sarim<ssuav:          
                print("sarima mejor opcion "+ str(sarim))
                final[nombre[0]]=autosar(i,fc_periods,df)

        elif arima<sarim and arima<holtw and arima<ssuav:
                print("arima mejor opcion "+ str(arima))
                final[nombre[0]]=autoar(i,fc_periods,df)

        elif ssuav<sarim and ssuav<holtw and ssuav<arima:
                print("suavizacion ex mejor opcion "+ str(ssuav))
                final[nombre[0]]=sess(i,fc_periods,df)

        elif holtw<sarim and holtw<arima and holtw<ssuav:
                print("holt wintes mejor opcion "+ str(holtw))            
                final[nombre[0]]=holtt(i,fc_periods,df)

        else :
                final[nombre[0]]=sess(i,fc_periods,df)

# def enviarMail():
#         from_addr = 'sender@gmail.com'
#         to = 'reciever@gmail.com'
#         message = 'Reporte de pronostico'

#         # Reemplaza estos valores con tus credenciales de Google Mail
#         username = 'user@gmail.com'
#         password = 'password'

#         server = smtplib.SMTP('smtp.gmail.com:587')
#         server.starttls()
#         server.login(username, password)
#         server.sendmail(from_addr, to, message)

#         server.quit()                                                       

def _main_():
        df = pd.read_csv('C:/Users/mauxy/Documents/MatrizPronosticoLunes10.csv')
        data = df
        nombre = list(df.iloc[:,0])
        pbar = tqdm(total=5500)
        for i in range(5500):
                try:
                        pronosticar(i,30,data)
                        pbar.update(1)          
                except Exception as e:
                        print("Datos Insuficientes"*5)
                        final[nombre[i]]=(0)
                        pbar.update(1)       
        pbar.close()
        final2 = final.sum(axis=0)
        final2 = pd.DataFrame(final2)
        final2.columns = ['Fcs_15dias']
        final2['FCS30'] = (final2['Fcs_15dias']) + final2['Fcs_15dias']         
        final2['FCS60'] = (final2['Fcs_15dias']*2) + final2['Fcs_15dias']
        final2['Fcs_15dias'] = abs(round(final2['Fcs_15dias']))
        final2['FCS30'] = abs(round(final2['FCS60']))
        final2['FCS60'] =  abs(round(final2['FCS90']))
        print(final2)
        final2.to_csv('pronosticoLunes10.csv')
        final2.to_json('pronos.json')
        # enviarMail()
_main_()