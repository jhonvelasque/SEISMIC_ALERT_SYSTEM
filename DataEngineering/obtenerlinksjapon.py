import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
i
# Configurar el límite de caracteres a mostrar
pd.set_option('display.max_colwidth', None)

# Configurar Selenium
driver = webdriver.Chrome()  # Cambia esto al controlador del navegador que estés utilizando

# Abrir la página
url = 'https://www.data.jma.go.jp/multi/quake/index.html?lang=es'
driver.get(url)

# Encontrar la tabla de resultados
wait = WebDriverWait(driver, 10)
tabla = wait.until(EC.presence_of_element_located((By.ID, 'quakeindex_table')))

# Pausa para permitir que los datos se carguen completamente
time.sleep(2)  # Ajusta el tiempo de pausa según sea necesario

#-------------------------sacamos los links nuevos para la informacion ---------------------
filas = tabla.find_elements(By.XPATH, './/tr')
# Recorrer las filas de la tabla y extraer los enlaces
enlaces = []
for i in range(1, len(filas)):  # Ignorar la primera fila (encabezados de columna)
    fila = filas[i]  # Obtener la fila actual
    
    # Obtener el enlace
    enlace = fila.find_element(By.XPATH, './/td[1]/a').get_attribute('href')
    enlaces.append(enlace)
    

# Guardar los enlaces en un DataFrame
df_enlaces = pd.DataFrame(enlaces, columns=['Enlace'])

# Imprimir el DataFrame
#----------------------------------------creamos la funcion para extraer los datos-------------
def scrape_page(url):
    # Configurar Selenium
    options = Options()
    options.add_argument("--headless")  # Ejecutar en modo headless (sin ventana)
    service = Service('str/chromedriver')  # Reemplaza con la ubicación de tu archivo chromedriver

    # Inicializar el controlador de Selenium
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    
    # Esperar 2 segundos para que se cargue la página
    time.sleep(2)
    
    # Buscar la tabla por su ID
    table = driver.find_element(By.ID, 'quakeindex_table')
    
    # Extraer los datos de la tabla
    data = []
    rows = table.find_elements(By.TAG_NAME, 'tr')
    
    for row in rows[1:]:  # Omitir la primera fila (encabezados)
        columns = row.find_elements(By.TAG_NAME, 'td')
        fecha = columns[0].text
        longitud = columns[1].text
        latitud = columns[2].text
        magnitud = columns[3].text
        profundidad = columns[4].text
        lugar = columns[5].text
        
        data.append({
            'Fecha detectado el terremoto': fecha,
            'longitud': longitud,
            'latitud': latitud,
            'Magnitud': magnitud,
            'profundidad': profundidad,
            'lugar': lugar
        })
    
    # Cerrar el controlador de Selenium
    driver.quit()
    
    return pd.DataFrame(data)

# Crear una lista para almacenar los DataFrames raspados
dfs = []

# Aplicar la función de scraping a cada enlace en el DataFrame
for index, row in df_enlaces.iterrows():
    url = row['Enlace']
    scraped_data = scrape_page(url)
    
    if scraped_data is not None:
        dfs.append(scraped_data)

# Concatenar los DataFrames en uno nuevo
new_df = pd.concat(dfs, ignore_index=True)

# Imprimir el nuevo DataFrame resultante
