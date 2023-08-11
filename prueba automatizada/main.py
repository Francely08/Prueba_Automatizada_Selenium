
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

driver=webdriver.Firefox()
driver.get("https://orbi.edu.do/orbi/")

def olvidar_usuaraio():
    olviade_user=driver.find_element(By.LINK_TEXT,'Olvidaste tu clave?')
    olviade_user.click()
    driver.save_screenshot('results/ovidar_usuario.png')
    recupera_user=driver.find_element(By.NAME,'txtUsuario')
    recupera_user.send_keys("santosfrali3@gmail.com")
    boton_submit=driver.find_element(By.CLASS_NAME,'espacio-d20')
    boton_submit.click()
    driver.save_screenshot('results/boton_submit.png')
    

def registro_tecnologo():
    rgtecnologo=driver.find_element(By.LINK_TEXT,'Registro Tecnólogo')
    rgtecnologo.click()
    driver.save_screenshot('results/tecnologo.png')
    email_tecnologo=driver.find_element(By.ID,'email')
    password_tecnologo=driver.find_element(By.ID,'password')
    boton_iniciar=driver.find_element(By.ID,'btnLogin')
    email_tecnologo.send_keys("")
    password_tecnologo.send_keys("")
    boton_iniciar.click()
    driver.save_screenshot('results/tecnolo_vacio.png')




def iniciarSesion():
    usuario_input=driver.find_element(By.NAME,'txtNombreUsuario')
    driver.save_screenshot('results/input_ingresar_usuario.png')
    passwor_input=driver.find_element(By.NAME,'txtContrasena')
    driver.save_screenshot('results/input_ingresar_contraseñá.png')
    boton_ingresar=driver.find_element(By.NAME,'submit')
    usuario_input.send_keys("santosfran3@gmail.com")
    driver.save_screenshot('results/Usuario.png')
    passwor_input.send_keys("franc17")
    driver.save_screenshot('results/Contraseña.png')
    boton_ingresar.click()
    driver.save_screenshot('results/inicioSesion.png')
    


def calendario_Academico():
    aceptar=driver.find_element(By.ID, 'bajar')
    driver.save_screenshot('results/formulario.png')
    aceptar.click()
    boton_aceptar=driver.find_element(By.LINK_TEXT,'Aceptar')
    driver.save_screenshot('results/boton_aceptar.png')
    boton_aceptar.click()
    inicio=driver.find_element(By.ID,'cerrar-sesion')
    time.sleep(10)
    inicio.click()
    driver.save_screenshot('results/cerrar.png')
    boton_Si=driver.find_element(By.CLASS_NAME,'fast_confirm_proceed')
    time.sleep(5)
    boton_Si.click()
    driver.save_screenshot('results/Si.png')


   




    

# olvidar_usuaraio()
registro_tecnologo()
# iniciarSesion()
# calendario_Academico()


