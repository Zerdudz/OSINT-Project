import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from time import sleep
from bs4 import BeautifulSoup


class Scrapper_Paruvendu:

    def __init__(self):
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        self.DRIVER_PARU = uc.Chrome(options=options)

        self.DRIVER_PARU.maximize_window()
        pass

    def get_annonces(self, marque, num_results = 20):
        list_annonces=[]

        marque_cod_dict = {
            "Abarth": "VVOAB000",
            "Aiways": "VVOAW000",
            "Aleko": "VVOAK000",
            "Alfa Romeo": "VVOAL000",
            "Alpina": "VVOAP000",
            "Alpine": "VVOAI000",
            "Aro": "VVOAO000",
            "Aston Martin": "VVOAM000",
            "Audi": "VVOAU000",
            "Austin": "VVOAN000",
            "Autres": "VVOZZ000",
            "Auverland": "VVOAD000",
            "BMW": "VVOBM000",
            "BYD": "VVOBY000",
            "Bentley": "VVOBT000",
            "Bertone": "VVOBE000",
            "Buggy": "VVOBG000",
            "Buick": "VVOBU000",
            "Cadillac": "VVOCC000",
            "Caterham": "VVOCM000",
            "Chevrolet": "VVOCV000",
            "Chrysler": "VVOCH000",
            "Citroën": "VVOCI000",
            "Corvette": "VVOCO000",
            "Cupra": "VVOCU000",
            "Dacia": "VVODC000",
            "Daewoo": "VVODA000",
            "Daihatsu": "VVODH000",
            "Daimler": "VVODL000",
            "Dangel": "VVODG000",
            "De la Chapelle": "VVODE000",
            "Dodge": "VVODO000",
            "Donkervoort": "VVODK000",
            "DS": "VVODS000",
            "Ferrari": "VVOFE000",
            "Fiat": "VVOFI000",
            "Fisker": "VVOFK000",
            "Ford": "VVOFO000",
            "GMC": "VVOGM000",
            "Gac Gonow": "VVOGG000",
            "Honda": "VVOHO000",
            "Hummer": "VVOHU000",
            "Hyundai": "VVOHY000",
            "Infiniti": "VVOIN000",
            "Isuzu": "VVOIS000",
            "Jaguar": "VVOJA000",
            "Jeep": "VVOJE000",
            "Kia": "VVOKI000",
            "LEVC": "VVOLV000",
            "Lada": "VVOLD000",
            "Lamborghini": "VVOLA000",
            "Lancia": "VVOLC000",
            "Land-Rover": "VVOLR000",
            "Landwin": "VVOLW000",
            "Lexus": "VVOLX000",
            "Lotus": "VVOLO000",
            "Lynk & CO": "VVOLY000",
            "MG": "VVOMG000",
            "MPM Motos": "VVOMP000",
            "Mahindra": "VVOMH000",
            "Maruti": "VVOMR000",
            "Maserati": "VVOMZ000",
            "Maybach": "VVOMY000",
            "Mazda": "VVOMA000",
            "McLaren": "VVOML000",
            "Mercedes": "VVOME000",
            "Mercedes-AMG": "VVOMG001",
            "Mercedes-Maybach": "VVOMM000",
            "Mercury": "VVOMU000",
            "Microcar": "VVOMI000",
            "Mini": "VVOMN000",
            "Mitsubishi": "VVOMT000",
            "Morgan": "VVOMO000",
            "Nissan": "VVONI000",
            "Opel": "VVOOP000",
            "PGO": "VVOPO000",
            "Peugeot": "VVOPG000",
            "Plymouth": "VVOPM000",
            "Pontiac": "VVOPO001",
            "Porsche": "VVOPS000",
            "Renault": "VVORE000",
            "Rivian": "VVORV000",
            "Rolls-Royce": "VVORO000",
            "Rover": "VVORV001",
            "SEAT": "VVOSE000",
            "Saab": "VVOSB000",
            "Santana": "VVOSA000",
            "Saturn": "VVOST000",
            "Scion": "VVOSC000",
            "Skoda": "VVOSK000",
            "Smart": "VVOSM000",
            "Ssangyong": "VVOSY000",
            "Subaru": "VVOSU000",
            "Suzuki": "VVOSZ000",
            "Tesla": "VVOTE000",
            "Toyota": "VVOTO000",
            "Triumph": "VVOTR000",
            "Volkswagen": "VVOVO000",
            "Volvo": "VVOVL000",
            "Wartburg": "VVOWA000",
            "Zastava": "VVOZT000",
            "Zotye": "VVOZO000",
            "e.GO": "VVOEG000"
        }

        code_marque=marque_cod_dict[marque]

        self.DRIVER_PARU.get(f"https://www.paruvendu.fr/auto-moto/listefo/default/default?r={code_marque}&r1=&trub=&pa=FR&lo=&codeINSEE=#")

        # Wait until cookies
        element = WebDriverWait(self.DRIVER_PARU, 100).until(
            EC.presence_of_element_located((By.XPATH, '//button[text()="Accepter et Fermer"]')))
        element.click()
        self.DRIVER_PARU.execute_script("document.body.style.zoom='8%'")

        soup = BeautifulSoup(self.DRIVER_PARU.page_source, 'html.parser')

        list_div = soup.find(id="listevignette")

        for annonce in list_div.find_all("div", class_="lazyload_bloc"):
            titre = annonce.find("h3").text.strip()
            url = annonce.find("a")['href'].strip()
            img = annonce.find("img")['original'].strip()

            h3 = annonce.find("h3")
            location = h3.find_next_sibling().text.strip()

            new_annonce={
                "titre": titre,
                "image_url": img,
                "url": url,
                "location": location
            }
            list_annonces.append(new_annonce)

            if len(list_annonces) == num_results:
                break


        annonces = {
            "items": list_annonces

        }
        self.DRIVER_PARU.close()

        return annonces
