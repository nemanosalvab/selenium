from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

opts = Options()
opts.headless = False

browser = webdriver.Firefox(options = opts)
browser.get('https://sicodis.dnp.gov.co/ReportesSGP/FichaSGP_Entidad.aspx')



#Table by id=ctl00_ctl00_cph_contents_cph_contents_GridViewHistorico

#Click by id="ctl00_ctl00_cph_contents_cph_contents_Btn_Consultar"



def table_rec():
    #select table by id
    try:
        elements = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//table[@id="ctl00_ctl00_cph_contents_cph_contents_GridViewHistorico"]')))
    except Exception:
        print("!Table not loaded¡")
    
    return elements




try:

        departamentos = Select(WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,'//select[@id="ctl00_ctl00_cph_contents_cph_contents_List_CriterioBusquedaDepartamento"]'))))

        for i, depto in enumerate(departamentos.options):

            if i == 0:
                departamentos.select_by_index(i)
            else:
                
                departamentos = Select(WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,'//select[@id="ctl00_ctl00_cph_contents_cph_contents_List_CriterioBusquedaDepartamento"]'))))
                departamentos.select_by_index(i)

            municipios = Select(WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,'//select[@id="ctl00_ctl00_cph_contents_cph_contents_List_CriterioBusqueda"]'))))
            
            for j, mun in enumerate(municipios.options):

                if j == 0:
                    municipios.select_by_index(j)
                else:
                    municipios = Select(WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,'//select[@id="ctl00_ctl00_cph_contents_cph_contents_List_CriterioBusqueda"]'))))
                    municipios.select_by_index(j)
                
                vigencia = Select(WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,'//select[@id="ctl00_ctl00_cph_contents_cph_contents_Drp_PresupuestoVigencia"]'))))
                
                for k, vig in enumerate(vigencia.options):
                    if k == 0:
                        vigencia.select_by_index(k)
                    else:
                        vigencia = Select(WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,'//select[@id="ctl00_ctl00_cph_contents_cph_contents_Drp_PresupuestoVigencia"]'))))
                        vigencia.select_by_index(k)

                    try:
                        WebDriverWait(browser, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//input[@id="ctl00_ctl00_cph_contents_cph_contents_Btn_Consultar"]')),
                        ).click()
                    except Exception:
                        print("!More btn not loaded¡")
                    

                    result = table_rec()


except Exception:
    print("!Table not loaded¡")


