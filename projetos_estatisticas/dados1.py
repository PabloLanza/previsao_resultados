import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import numpy as np

#CONSIDERAÇÃO IMPORTANTE: DURANTE O DESENVOLVIMENTO DO CÓDIGO EU TIVE ALGUNS PROBLEMAS
#DE MEMÓRIA E ALGUNS BUGS DO SITE. A IDEIA INICIAL ERA UM PROGRAMA TOTALMENTE AUTOMÁTICO
# PORÉM DEVIDO AOS PROBLEMAS, A CADA RODADA FOI NECESSÁRIO ALTERAR ALGUMAS COISAS NO CÓDIGO
#SÃO ELAS: PLANILHA A SER CARREGADA, PLANILHA A SER SALVA E O NMERO DE REPETIÇÕES DO LAÇO.

#Carregando a base de dados
base = pd.read_excel("estisticas.xlsx") #O nome da planilha a ser carregada deve ser alterado a cada rodada
print(len(base))

#Entrando no site
driver = webdriver.Chrome(r'chromedriver.exe')
driver.get("https://www.sofascore.com/tournament/football/spain/laliga/8")
driver.execute_script("window.scroll(0, 1300)")
sleep(2)
botao_rodada = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div[5]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/button")
jogos = driver.find_elements(by=By.CLASS_NAME, value="sc-29ae2005-0")
indice = 0
while indice < len(jogos):
    sleep(3)
    driver.execute_script("window.scroll(1300, 1350)")
    driver.execute_script("window.scroll(1350, 1300)")
    botao_rodada = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div[5]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/button")
    sleep(1)
    for c in range(0, 0): #Nesse laço o valor deve ser aumentado em 1 a cada rodada 
        botao_rodada.click()
        sleep(1)
    jogos = driver.find_elements(by=By.CLASS_NAME, value="sc-29ae2005-0")
    jogos[indice].click()
    driver.execute_script("window.scroll(1300, 1250)")
    sleep(4)
    try:
        condicao_estatisticas = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div[5]/div/div[2]/div/div/div[2]/div/div/div/div/div[3]/div/div[1]/div/div[3]").text
        if condicao_estatisticas == "STATISTICS":
            try:
                estatisticas = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[1]/div[2]/div[1]/div[5]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[1]/ul/li[3]/a/span").click()
                sleep(2)
                #Identificar mando de campo
                time_casa = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span").text
                time_fora = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span").text
                gols_casa =  driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[1]/span").text
                gols_fora = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div[3]/span").text
                if gols_casa > gols_fora:
                    resultado = "VITORIA"
                elif gols_casa == gols_fora:
                    resultado = "EMPATE"
                else:
                    resultado = "DERROTA"
                driver.execute_script("window.scroll(0, 2200)")
                sleep(2)
                #Coleta dos dados
                posse_casa = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div[2]/div/div[1]/span").text
                posse_fora = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div[2]/div/div[3]/span").text
                chutes_casa = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div[3]/div[1]/div[1]/span").text
                chutes_fora = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div[3]/div[1]/div[3]/span").text
                chutes_gol_casa = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div[3]/div[2]/div[1]/span").text
                chutes_gol_fora = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div[3]/div[2]/div[3]/span").text
                escanteios_casa = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div[4]/div[1]/div[1]/span").text
                escanteios_fora = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div[4]/div[1]/div[3]/span").text
                driver.execute_script("window.scroll(2200, 2400)")
                faltas_casa = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div[4]/div[2]/div[1]/span").text
                faltas_fora = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div[4]/div[2]/div[3]/span").text
                driver.execute_script("window.scroll(2400, 2700)")
                passes_casa = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div[6]/div[1]/div[1]/span").text
                passes_fora = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div[6]/div[1]/div[3]/span").text
                passes_certos_casa = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div[6]/div[2]/div[1]/span").text
                passes_certos_fora = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div[6]/div[2]/div[3]/span").text
                print(posse_casa, posse_fora, chutes_casa, chutes_fora, chutes_gol_casa, chutes_gol_fora, escanteios_casa, escanteios_fora, faltas_casa, faltas_fora, passes_casa, passes_fora, passes_certos_casa, passes_certos_fora, resultado)
                driver.execute_script("window.scroll(2700, 0)")
                driver.back()

                #Criando estrutura de decisão para adicionar os dados corretamente na tabela
                i = len(base)
                base.loc[i] = [time_casa, time_fora, posse_casa, posse_fora, chutes_casa, chutes_fora, chutes_gol_casa, chutes_gol_fora, escanteios_casa, escanteios_fora, faltas_casa, faltas_fora, passes_casa, passes_fora, passes_certos_casa, passes_certos_fora, resultado]
                indice += 1
                sleep(2)
                driver.execute_script("window.scroll(0, 1300)")
                sleep(1)
            except:
                indice += 1
                driver.refresh()
        else:
            indice += 1
            driver.refresh()
    except:
        indice += 1
        driver.refresh()
driver.quit()
base.to_excel("stats1.xlsx") #O nome da planilha salva deve ser alterado a cada rodada