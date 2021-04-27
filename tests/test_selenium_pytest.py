from selenium import webdriver
import pytest

class TestSample():
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

    def test_home_page_title(test_setup):
        x = driver.title
        assert x == "Projet Teoschool Brahami Rabah"

    def test_git_page_acces():
        driver.find_element_by_id("github-image").click()
        githubTitle = driver.title
        assert "brahamirabah94" in githubTitle

    def test_dockercoin_page_acces():
        driver.find_element_by_id("dockercoin-image").click()
        CoinTitle = driver.title
        assert "Dockercoin" in CoinTitle 

    def test_teolia_page_acces():
        driver.find_element_by_id("teo-image").click()
        TeoliaTitle = driver.title
        assert "Teolia" in TeoliaTitle 


    def test_linkedin_page_acces():
        driver.find_element_by_id("linkedin-image").click()
        LinkedinTitle = driver.title
        assert "Rabah" in linkedinTitle 
