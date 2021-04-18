from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import matplotlib.pyplot as plt
import csv
import time
import pandas as pd
from datetime import datetime
#from lxml import html
#import lxml
#from bs4 import BeautifulSoup

s = datetime.now().strftime('%m%d%y_%I%M%p')
filer_query = datetime.now().strftime('%d/%m/%Y') 

url = 'C:\\Users\\aronv\\Documents\\Github\\4s-scrap\\ssrc_exp_' + s + '.csv'
#url = 'C:\\Users\\aronv\\Documents\\Github\\4s-scrap\\ssrc_exp_032521_1118PM.csv'

driver = webdriver.Chrome(executable_path="C:\\Users\\aronv\\Documents\\Github\\4s-scrap\\chromedriver.exe")
driver.get('http://ahvaldes:p4$Sw0rd_7811@abclscl134.anglo.local/ssrc/ASPX/Index.aspx')
driver.get('http://abclscl134.anglo.local/ssrc/ASPX/solicitudes/consultar/resultado.aspx?as_id_estado=&as_buscar_por=1&as_buscar_por_dato=&as_buscar_estado=[TODOS]&as_fecha_inicio=24/11/2020&as_fecha_termino='+filer_query+'&as_orden=9')
webtable_df = pd.read_html(driver.find_element_by_xpath("//html/body/form/table").get_attribute('outerHTML'))[0] 

webtable_df.to_csv(url)
df = pd.read_csv(url, skiprows=2)
df4s = pd.DataFrame({
        'Creador'   : ['Camilo salvador valencia Perez', 'Miguel Antonio Alarcon Medina'],
        'Status'    : ['Active', 'Inactive'] })


inner_merged_total = pd.merge(df4s, df, on=["Creador", "Creador"])
#print(inner_merged_total)
new_df = inner_merged_total[['Solicitante','Creador','Recurso','Supervisor','Creacion','Estado','Ejecución','Apr. Supervisor','Apr. Dueño', 'Rechazo']]
new_df['Solicitante'] = new_df['Solicitante'].astype(str)
new_df['Creador'] = new_df['Creador'].astype(str)
new_df['Recurso'] = new_df['Recurso'].astype(str)
new_df['Supervisor'] = new_df['Supervisor'].astype(str)
new_df['Estado'] = new_df['Estado'].astype(str)
new_df['Ejecución'] = pd.to_datetime(new_df['Ejecución'])
new_df['Apr. Supervisor'] = pd.to_datetime(new_df['Apr. Supervisor'])
new_df['Apr. Dueño'] = pd.to_datetime(new_df['Apr. Dueño']) 
new_df['Creacion'] = pd.to_datetime(new_df['Creacion']) 
new_df['Rechazo'] = new_df['Rechazo'].astype(str)

new_df.to_csv('C:\\Users\\aronv\\Documents\\Github\\4s-scrap\\aaaaa.csv')

plt.bar(inner_merged_total[['Supervisor']], inner_merged_total[['Supervisor']], tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])

plt.hist(inner_merged_total[['Supervisor']], 
inner_merged_total, 
inner_merged_total, color = 'green',
        histtype = 'bar', rwidth = 0.8)

inner_merged_total.plot(kind='scatter',x='Creacion',y='Recurso')
plt.show()

new_df['cre_to_now'] = abs((datetime.now() - new_df['Creacion']))
new_df['cre_date'] = datetime.strptime(str(new_df['Creacion'],'%d-%m-%Y').date()
#new_df.info()