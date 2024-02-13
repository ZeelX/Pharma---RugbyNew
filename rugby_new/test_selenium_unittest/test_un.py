import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def count_nb_line():
    driver = webdriver.Chrome("")
    driver.get("http://localhost:8000/")

    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h4")
    time.sleep(10)
    element = element.text

    return element

# def count_nb_column():
#     driver = webdriver.Chrome("")
#     driver.get("http://localhost:8000/")
#
#     list_road = driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li[2]/a")
#     list_road.click()
#     time.sleep(5)
    entete = driver.find_element(By.XPATH, "/html/body/div/table/thead/tr")




def fifth_element_from_last_line():
    driver = webdriver.Chrome("")
    driver.get("http://localhost:8000/")

    list_road = driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li[2]/a")
    list_road.click()
    time.sleep(2)
    last_page = driver.find_element(By.XPATH, "/html/body/div/div/a[2]")
    last_page.click()
    time.sleep(2)

    td = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[5]")
    return td.text


class TestClub(unittest.TestCase):
    """_summary_

    Args:
        TestCase (_type_): _description_
    """

    def setUp(self) -> None:
        """Définie mes paramètres d'initialisation
        """

    def test_count(self):
        count = count_nb_line()
                                      # 117389
        self.assertEqual(count, "Nombre de lignes de ODS : 117389")

    # def test_nb_columns(self):
    #     count = count_nb_column()
    #     self.assertIsNotNone(count)

    def test_element_line(self):

        element = "nan NR NR - Non réparti FF du Sport Universitaire"
        self.assertEqual(element, fifth_element_from_last_line())



if __name__ == "__main__":
    unittest.main()