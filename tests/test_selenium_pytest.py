from selenium import webdriver
import pytest


@pytest.fixture
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://8000-cs-453440873740-default.cs-europe-west1-akef.cloudshell.dev/index.html")
    yield 
    driver.close()
    driver.quit()
    print("fin des tests")

class TestSample(self, test_setup):

    def test_home_page_title(self):
        x = self.driver.title
        assert x == "Projet Teoschool Brahami Rabah"

    def test_git_page_acces(self):
        self.driver.find_element_by_id("github-image").click()
        githubTitle = self.driver.title
        assert "brahamirabah94" in githubTitle

    def test_dockercoin_page_acces(self):
        self.driver.find_element_by_id("dockercoin-image").click()
        CoinTitle = self.driver.title
        assert "Dockercoin" in CoinTitle 

    def test_teolia_page_acces(self):
        self.driver.find_element_by_id("teo-image").click()
        TeoliaTitle = self.driver.title
        assert "Teolia" in TeoliaTitle 


    def test_linkedin_page_acces(self):
        self.driver.find_element_by_id("linkedin-image").click()
        LinkedinTitle = self.driver.title
        assert "Rabah" in linkedinTitle 
