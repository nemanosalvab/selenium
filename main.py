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

        elements = WebDriverWait(browser, 5).until(
            EC.presence_of_all_elements_located((By.XPATH,'//select[@id="ctl00_ctl00_cph_contents_cph_contents_List_CriterioBusquedaDepartamento"]')))
        departamentos = Select(elements[0])

        for i, depto in enumerate(departamentos.options):
            departamentos.select_by_index(i)

            elements = WebDriverWait(browser, 5).until(
                EC.presence_of_all_elements_located((By.XPATH,'//select[@id="ctl00_ctl00_cph_contents_cph_contents_List_CriterioBusqueda"]')))
            
            municipios = Select(elements[0])
            
            for j, mun in enumerate(municipios.options):
                municipios.select_by_index(j)

                elements = WebDriverWait(browser, 5).until(
                    EC.presence_of_all_elements_located((By.XPATH,'//select[@id="ctl00_ctl00_cph_contents_cph_contents_Drp_PresupuestoVigencia"]')))

                vigencias = Select(elements[0])
                for k , anno in enumerate(vigencias.options):
                    vigencias.select_by_index(k)

                    try:
                        WebDriverWait(browser, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//input[@id="ctl00_ctl00_cph_contents_cph_contents_Btn_Consultar"]')),
                        ).click()
                    except Exception:
                        print("!More btn not loaded¡")
                    

                    result = table_rec()


except Exception:
    print("!Table not loaded¡")

for key , element in enumerate(select.options):
    print(key , element)

#depto = select.select_by_visible_text(select.options[0].accessible_name)

