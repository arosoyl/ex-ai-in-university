from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

methodProsal = ['Name', 'Abstract']
# methodProsal = ['Name','Abstract','LinkPdf']
df = pd.DataFrame(columns=methodProsal)

# driver = webdriver.PhantomJS()
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = driver = webdriver.Chrome(executable_path=r'E:/setup/chrome/chromedriver.exe')
url = ['https://proceedings.neurips.cc/paper/2016']
fileName = ['TestResult.csv']  # ,'nips2012.csv']


def crawlPaperFromNIPS(url):
    driver.get(url)
    eleList = driver.find_elements_by_tag_name("li")
    listOfPaper = []

    index = 0
    i = 1
    try:
        #     for i in range(1,len(ele)):
        while eleList:
            ele = eleList.pop()
            #         name = ele.text
            urlPdf = "/html/body/div[2]/div/ul/li[" + str(i) + "]/a[1]"
            #         driverAbstract = webdriver.PhantomJS() # webdriver.Chrome()
            urlAbstract = ele.find_element(By.XPATH, urlPdf).get_attribute('href')
            print(i, '. ', urlAbstract)
            listOfPaper.append(urlAbstract)
            i = i + 1
            if (i > 100):
                break;
    except:
        pass
    # finally:
    #     df.to_csv("ListOfPaper.csv")

    #     driver.close()
    #     driver.quit()
    j = 1
    while listOfPaper:
        ele = listOfPaper.pop()
        driver.get(ele)
        #         abstract = driver.find_element(By.CLASS_NAME, "abstract").text
        abstract = driver.find_element_by_xpath('/html/body/div[2]/div/p[3]').text
        name = driver.find_element_by_xpath('/html/body/div[2]/div/h4[1]').text
        #         name = driver.find_element(By.CLASS_NAME,"subtitle").text
        #         linkpdf = ele + ".pdf"
        df.set_value(index, "Name", name)
        #         df.set_value(index,"LinkPdf",linkpdf)
        df.set_value(index, "Abstract", abstract)
        try:
            print('%d. Name: %s' % (j, name))
            j = j + 1
        except:
            pass
        index = index + 1
        if (index > 100):
            break;
    return df


try:
    for i in range(0, len(url)):
        crawlPaperFromNIPS(url[i]).to_csv(fileName[i])
except:
    pass
finally:
    driver.close()
    driver.quit()