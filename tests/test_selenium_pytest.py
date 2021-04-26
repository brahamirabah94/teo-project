from selenium import webdriver
import pytest

class TestSample():
    @pytest.fixture
    def test_setup():
        global driver
        driver = webdriver.Chrom(executable_path="le liens vers l'executable de chrome")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("liens a definir apres la mis en place de l'ingress")
        yield 
        driver.close()
        driver.quit()
        print("fin des tests")

    def test_home_page_title():
        x = driver.title
        assert x == "Projet Teoschool Brahami Rabah"

    def test_git_page_acces():
        driver.find_element_by_id("github-image").click()
        driver.get("https://github.com/brahamirabah94/teo-project-rabah")
        githubTitle = driver.title
        resultGit= driver.find_element_by_link_text("teo-project-rabah")
        assert resultGit != None

    def test_dockercoin_page_acces():
        driver.find_element_by_id("dockercoin-image").click()
        driver.get("le liens de la page de dockercoin")
        github-title = driver.title
        result-git= driver.find_element_by_link_text("teo-project-rabah")

    def test_teolia_page_acces():
        driver.find_element_by_id("teo-image").click()
        driver.get("https://www.teolia.fr/")
        result-git= driver.find_element_by_link_text("teo-project-rabah")


    def test_linkedin_page_acces():
        driver.find_element_by_id("linkedin-image").click()
        driver.get("https://www.linkedin.com/in/rabah-brahami-780898128/")
        result-git= driver.find_element_by_link_text("teo-project-rabah")    
