import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from time import sleep
import requests

class Scrapper_Finishers:

    def __init__(self):
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        self.DRIVER = uc.Chrome(options=options)

        self.DRIVER.maximize_window()
        pass

    def get_courses(self, pays, num_results = 20):
        list_courses=[]

        country_links_dict = {
            "Afrique du Sud": "/ou-courir/afrique/afrique-du-sud",
            "Algérie": "/courses?location_t=country&location_l=Alg%C3%A9rie&location_v=Afrique%20%3E%20Alg%C3%A9rie",
            "Allemagne": "/ou-courir/europe/allemagne",
            "Andorre": "/ou-courir/europe/andorre",
            "Argentine": "/ou-courir/amerique-du-sud/argentine",
            "Autriche": "/ou-courir/europe/autriche",
            "Belgique": "/ou-courir/europe/belgique",
            "Bhoutan": "/courses?location_t=country&location_l=Bhoutan&location_v=Asie%20%3E%20Bhoutan",
            "Bolivie": "/courses?location_t=country&location_l=Bolivie&location_v=Am%C3%A9rique%20du%20Sud%20%3E%20Bolivie",
            "Bosnie-Herzégovine": "/courses?location_t=country&location_l=Bosnie-Herz%C3%A9govine&location_v=Europe%20%3E%20Bosnie-Herz%C3%A9govine",
            "Brésil": "/ou-courir/amerique-du-sud/bresil",
            "Bulgarie": "/ou-courir/europe/bulgarie",
            "Cambodge": "/courses?location_t=country&location_l=Cambodge&location_v=Asie%20%3E%20Cambodge",
            "Canada": "/ou-courir/amerique-du-nord/canada",
            "Cap-Vert": "/courses?location_t=country&location_l=Cap-Vert&location_v=Afrique%20%3E%20Cap-Vert",
            "Chili": "/courses?location_t=country&location_l=Chili&location_v=Am%C3%A9rique%20du%20Sud%20%3E%20Chili",
            "Chine": "/ou-courir/asie/chine",
            "Chypre": "/courses?location_t=country&location_l=Chypre&location_v=Europe%20%3E%20Chypre",
            "Colombie": "/ou-courir/amerique-du-sud/colombie",
            "Corée du Sud": "/courses?location_t=country&location_l=Cor%C3%A9e%20du%20Sud&location_v=Asie%20%3E%20Cor%C3%A9e%20du%20Sud",
            "Costa Rica": "/courses?location_t=country&location_l=Costa%20Rica&location_v=Am%C3%A9rique%20Centrale%20%3E%20Costa%20Rica",
            "Croatie": "/ou-courir/europe/croatie",
            "Danemark": "/ou-courir/europe/danemark",
            "El Salvador": "/courses?location_t=country&location_l=El%20Salvador&location_v=Am%C3%A9rique%20Centrale%20%3E%20El%20Salvador",
            "Espagne": "/ou-courir/europe/espagne",
            "Estonie": "/ou-courir/europe/estonie",
            "États-Unis": "/ou-courir/amerique-du-nord/etats-unis",
            "Finlande": "/ou-courir/europe/finlande",
            "France": "/ou-courir/europe/france",
            "Grèce": "/ou-courir/europe/grece",
            "Guatemala": "/courses?location_t=country&location_l=Guatemala&location_v=Am%C3%A9rique%20Centrale%20%3E%20Guatemala",
            "Hong Kong": "/ou-courir/asie/hong-kong",
            "Hongrie": "/ou-courir/europe/hongrie",
            "Inde": "/ou-courir/asie/inde",
            "Indonésie": "/ou-courir/asie/indonesie",
            "Irlande": "/ou-courir/europe/irlande",
            "Islande": "/ou-courir/europe/islande",
            "Israël": "/ou-courir/asie/israel",
            "Italie": "/ou-courir/europe/italie",
            "Japon": "/ou-courir/asie/japon",
            "Lettonie": "/ou-courir/europe/lettonie",
            "Liechtenstein": "/courses?location_t=country&location_l=Liechtenstein&location_v=Europe%20%3E%20Liechtenstein",
            "Lituanie": "/ou-courir/europe/lituanie",
            "Luxembourg": "/ou-courir/europe/luxembourg",
            "Malaisie": "/ou-courir/asie/malaisie",
            "Malte": "/courses?location_t=country&location_l=Malte&location_v=Europe%20%3E%20Malte",
            "Maroc": "/ou-courir/afrique/maroc",
            "Mexique": "/ou-courir/amerique-du-nord/mexique",
            "Monaco": "/courses?location_t=country&location_l=Monaco&location_v=Europe%20%3E%20Monaco",
            "Népal": "/ou-courir/asie/nepal",
            "Norvège": "/ou-courir/europe/norvege",
            "Nouvelle-Zélande": "/ou-courir/oceanie/nouvelle-zelande",
            "Pays-Bas": "/ou-courir/europe/pays-bas",
            "Pérou": "/ou-courir/amerique-du-sud/perou",
            "Philippines": "/ou-courir/asie/philippines",
            "Pologne": "/ou-courir/europe/pologne",
            "Portugal": "/ou-courir/europe/portugal",
            "Royaume-Uni": "/ou-courir/europe/royaume-uni",
            "Russie": "/ou-courir/europe/russie",
            "Singapour": "/ou-courir/asie/singapour",
            "Slovaquie": "/ou-courir/europe/slovaquie",
            "Slovénie": "/ou-courir/europe/slovenie",
            "Suède": "/ou-courir/europe/suede",
            "Suisse": "/ou-courir/europe/suisse",
            "Taïwan": "/ou-courir/asie/taiwan",
            "Thaïlande": "/ou-courir/asie/thailande",
            "Turquie": "/ou-courir/europe/turquie",
            "Ukraine": "/ou-courir/europe/ukraine",
            "Vietnam": "/ou-courir/asie/vietnam"
        }
        link = country_links_dict[pays]

        self.DRIVER.get(f"https://www.finishers.com{link}")

        element = WebDriverWait(self.DRIVER, 10).until(
            EC.visibility_of_element_located(
                (By.ID, 'c-p-bn'))
        )
        element.click()

        self.DRIVER.get(self.DRIVER.find_element(By.XPATH, '//a[contains(@class, "button button-secondary") and text()="Voir toutes les courses"]').get_attribute("href"))

        element = WebDriverWait(self.DRIVER, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'a[class^="style_EventPreview__"][class*="no-link-underline"]'))
        )

        for course in self.DRIVER.find_elements(By.CSS_SELECTOR,'a[class^="style_EventPreview__"][class*="no-link-underline"]'):
            new_course = {
                "nom": course.find_element(By.CLASS_NAME,'typo-h4').get_attribute("innerText"),
                "date":course.find_element(By.CSS_SELECTOR,'div[class^="style_Date__"]').get_attribute("innerText"),
                "image_url": course.find_element(By.TAG_NAME,"img").get_attribute("src"),
                "url": course.get_attribute("href"),
                "location": course.find_element(By.CSS_SELECTOR,'div[class^="style_City__"]').get_attribute("innerText"),
            }

            list_courses.append(new_course)

            if len(list_courses) == num_results:
                break


        courses = {
            "items": list_courses

        }
        self.DRIVER.close()

        return courses
