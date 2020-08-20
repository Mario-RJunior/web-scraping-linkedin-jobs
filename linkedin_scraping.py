# Finalizado!
from selenium import webdriver
from time import sleep

URL = 'https://br.linkedin.com/jobs/cientista-de-dados-vagas?position=1&pageNum=0'

class ChromeAuto:
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.lista_descricao = []
    
    def access_page(self, url):
        return self.driver.get(url)
    
    def colect_data(self):
        resultados = self.driver.find_elements_by_class_name('result-card')
        
        while True:    
            for r in resultados[len(self.lista_descricao):]:
                r.click()
                sleep(1)
                
                try:
                    descricao = self.driver.find_element_by_class_name('description')
                    self.lista_descricao.append(descricao.text)
                except:
                    print('Erro')
                    pass
                    
                resultados = self.driver.find_elements_by_class_name('result-card')       
        
            if len(self.lista_descricao) == len(resultados):
                break
        
        return self.lista_descricao
    
    def save_text(self):
        descricao_salvar = '\n'.join(self.lista_descricao)
        
        with open('descricoes_vagas.txt', 'w', encoding='utf-8') as f:
            f.write(descricao_salvar)
        
    def close_page(self):
        return self.driver.close()

if __name__ == '__main__':
    drivers = ChromeAuto()
    drivers.access_page(URL)
    drivers.colect_data()
    drivers.save_text()
    sleep(5)
    drivers.close_page()
