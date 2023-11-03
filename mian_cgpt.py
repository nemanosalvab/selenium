from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options

def select_option_by_index(select_element, index):
    select = Select(select_element)
    select.select_by_index(index)

def wait_for_element(browser, by, value, timeout=5):
    return WebDriverWait(browser, timeout).until(EC.presence_of_element_located((by, value)))

def table_rec():
    try:
        return wait_for_element(browser, By.XPATH, '//table[@id="ctl00_ctl00_cph_contents_cph_contents_GridViewHistorico"]')
    except Exception:
        print("!Table not loaded¡")
        return None

try:
    opts = Options()
    opts.headless = True  # Set to True for headless mode
    browser = webdriver.Firefox(options=opts)
    browser.get('https://sicodis.dnp.gov.co/ReportesSGP/FichaSGP_Entidad.aspx')

    # Selectors for dropdowns
    departamento_selector = lambda : wait_for_element(browser, By.XPATH, '//select[@id="ctl00_ctl00_cph_contents_cph_contents_List_CriterioBusquedaDepartamento"]')
    criterio_busqueda_selector = lambda : wait_for_element(browser, By.XPATH, '//select[@id="ctl00_ctl00_cph_contents_cph_contents_List_CriterioBusqueda"]')
    vigencia_selector = lambda : wait_for_element(browser, By.XPATH, '//select[@id="ctl00_ctl00_cph_contents_cph_contents_Drp_PresupuestoVigencia"]')

    # Your loop for selecting options and clicking the button
    for i, depto in enumerate(Select((departamento_selector())).options):
        select_option_by_index(departamento_selector(), i)
        for j, mun in enumerate(Select(criterio_busqueda_selector()).options):
            select_option_by_index(criterio_busqueda_selector(), j)
            for k, vig in enumerate(Select(vigencia_selector()).options):
                select_option_by_index(vigencia_selector(), k)
                try:
                    wait_for_element(browser, By.XPATH, '//input[@id="ctl00_ctl00_cph_contents_cph_contents_Btn_Consultar"]').click()
                    result = table_rec()
                    # Process the result here
                except Exception:
                    print("!Error while clicking the button¡")
except Exception:
    print("!Error in the main process¡")
finally:
    browser.quit()
