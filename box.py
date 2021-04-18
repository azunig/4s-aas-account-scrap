from boxsdk import OAuth2, Client 
import pandas as pd
import openpyxl

oauth = OAuth2(
    client_id='46lbyt5j6n1xse3wzq3yzim8cacyvqnm',
    client_secret='XkYcpvjaMpDF7GUCg0vUq9znYb2N0qxU',
    access_token='zYK26jAwFJRhab2x9rEktU2L5y9e8FyP',
)

df = pd.read_excel('LContratos.xlsx', header=5, usecols='C:G')
df.rename(columns = {'|':'name', 'ADMINISTRACIÓN Y PLANIFICACIÓN':'adm', 'M. T':'MT','EM':'EM','PIPELINE':'PI' }, inplace = True)
#df['folderid'] = ''

root_mt = df.dropna(subset=['MT'])
root_em = df.dropna(subset=['EM'])
root_pi = df.dropna(subset=['PI'])
print(root_mt.count())
print(root_em.count())
print(root_pi.count())
#root_dowload = pd.DataFrame(columns = ['Archivo_planilla','Archivo_box','Carpeta'])
root_box = pd.DataFrame(columns = ['Archivo_box','Nombre', 'Id', 'Carpeta'])

client = Client(oauth)
#root_folder = client.folder(folder_id='0')
items = client.folder(folder_id='134563649698').get_items()

#for archivo in root_mt["name"]:
#    largo = len(archivo)

for item in items:
    #print('{0} {1} FOLDER "{2}"'.format(item.type.capitalize(), item.id, item))
    sub_items = client.folder(folder_id=item.id).get_items()
    for sub_item in sub_items:
        print('{0} {1} SUB "{2}"'.format(sub_item.type.capitalize(), sub_item.id, sub_item.name))
        new_row_box = {'Archivo_box':sub_item.name, 'Nombre':sub_item.name[0:25], 'Id': sub_item.id, 'Carpeta':item.name}
        root_box = root_box.append(new_row_box, ignore_index=True)

#for box, d in root_box["Nombre", "Id"]:
#    if archivo.strip() == box.strip() :
#        file_content = client.file(file_id).content()
#        print(archivo)
#        print(Id)
#
#
#  Lo primero es buscar las credenciales de BOX 
#  Credenciales :
#  https://app.box.com/developers/console/app/1500088/configuration
#  Reference : 
#  https://developer.box.com/reference/
#  Guide :
#  https://developer.box.com/guides/downloads/get-url/
#   
#  La otra wea que hace, es leer el EXCEL 
#        
#  Después lee las weas de items que se conecta con el cliente
#  
#  Después compara las dos cagas.
#  
#   Falta agregar los datos que no estan en box y si estan en el excel .
#             
ruta_em = 'C:\\Users\\aronv\\Documents\\Cloud\\4S\\4Solutions\\4S-Proyectos - Documents\\21AAS_PRY001\\Archivo\\EM\\' 
for index_box, row_box in root_box.iterrows():
    for index_em, row_em in root_em.iterrows():
        if row_em['name'].strip() == row_box['Nombre'].strip() :
            npath = ruta_em + row_box['Archivo_box']
            with open(npath, 'wb') as f:
                client.file(row_box['Id']).download_to(f)

ruta_pi = 'C:\\Users\\aronv\\Documents\\Cloud\\4S\\4Solutions\\4S-Proyectos - Documents\\21AAS_PRY001\\Archivo\\PI\\' 
for index_box, row_box in root_box.iterrows():
    for index_pi, row_pi in root_pi.iterrows():
        if row_pi['name'].strip() == row_box['Nombre'].strip() :
            npath = ruta_pi + row_box['Archivo_box']
            with open(npath, 'wb') as f:
                client.file(row_box['Id']).download_to(f)

ruta_mt = 'C:\\Users\\aronv\\Documents\\Cloud\\4S\\4Solutions\\4S-Proyectos - Documents\\21AAS_PRY001\\Archivo\\MT\\' 
for index_box, row_box in root_box.iterrows():
    for index_mt, row_mt in root_mt.iterrows():
        if row_mt['name'].strip() == row_box['Nombre'].strip() :
            npath = ruta_mt + row_box['Archivo_box']
            with open(npath, 'wb') as f:
                client.file(row_box['Id']).download_to(f)


""" 

for archivo in root_mt["name"]:
    for box in root_box["Nombre"]:
        if archivo.strip() == box.strip() :

    for index, row in root_box.iterrows():
        print(row['Id'])
        #print(index)
        #file_content = client.file(row['Id']).content()
        path = 'C:\\Users\\aronv\\Documents\\Cloud\\4S\\4Solutions\\4S-Proyectos - Documents\\21AAS_PRY001\\Archivo\\EM\\' + row['Archivo_box']
        with open(path, 'wb') as f:
            client.file(row['Id']).download_to(f)
        print(file_content)

    for index, row in root_box.iterrows():
        print(row)
        print(index)

        if archivo.strip() == box.strip() :
            #file_content = client.file(file_id).content()
            print(archivo)
            print(Id)

for archivo in root_mt["name"]:
    for box in root_box["Nombre"]:
        if archivo.strip() == box.strip() :
            #file_content = client.file(file_id).content()

            print(archivo)
            print(Id)
            
for archivo in root_em["name"]:
    for box in root_box["Nombre"]:
        if archivo.strip() == box.strip() :
            print(archivo)

for archivo in root_pi["name"]:
    for box in root_box["Nombre"]:
        if archivo.strip() == box.strip() :
            print(archivo)

new_df.to_csv('C:\\Users\\aronv\\Documents\\Cloud\\4S\\4Solutions\\4S-Proyectos - Documents\\21AAS_PRY001\\Archivo\\EM\\')
new_df.to_csv('C:\\Users\\aronv\\Documents\\Cloud\\4S\\4Solutions\\4S-Proyectos - Documents\\21AAS_PRY001\\Archivo\\PI\\')
new_df.to_csv('C:\\Users\\aronv\\Documents\\Cloud\\4S\\4Solutions\\4S-Proyectos - Documents\\21AAS_PRY001\\Archivo\\MT\\')

    file.content()  # returns the file contents as `bytes`
    file.download_to(writeable_stream)  # write the file contents to a stream

file_id = '11111'
file_content = client.file(file_id).content()

#new_row_box = {'Archivo_planilla':archivo, 'Archivo_box':sub_item.name, 'Carpeta':'mt'}
           #if(str(archivo) in str(sub_item.name))
           #if(my_str.find(archivo))
                #print('archivo : ')
                #print('box : ' + str(sub_item.name))

            #new_row = {'Archivo_planilla':archivo, 'Archivo_box':sub_item.name, 'Carpeta':'mt'}
            #root_folder = root_folder.append(new_row, ignore_index=True)
     """