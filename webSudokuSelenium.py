from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sudokuSolver import SudokuSolver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://view.websudoku.com/?level=4")
assert "Web Sudoku" in driver.title
rows = []
for row in range(9):
    columns = []
    for col in range(9):
        idName = "c" + str(col) + str(row)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, idName))
        )
        innerelem = element.find_element_by_css_selector("*")
        inner = innerelem.get_attribute('value')
        if inner:
            columns.append(int(inner))
        else:
            columns.append(0)
    rows.append(columns)

#test = [[4, 7, 0, 9, 0, 0, 0, 8, 0], [0, 0, 2, 0, 0, 0, 0, 0, 9], [8, 5, 0, 0, 2, 3, 0, 0, 0], [9, 4, 0, 0, 3, 0, 0, 0, 0], [0, 2, 0, 0, 7, 0, 0, 5, 0], [0, 0, 0, 0, 8, 0, 0, 6, 3], [0, 0, 0, 4, 5, 0, 0, 9, 6], [2, 0, 0, 0, 0, 0, 4, 0, 0], [0, 8, 0, 0, 0, 7, 0, 2, 5]]
solver = SudokuSolver(rows)
solution = solver.getSolution()
print solution

for row in range(9):
    for col in range(9):
        idName = "c" + str(col) + str(row)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, idName))
        )
        innerelem = element.find_element_by_css_selector("*")
        inner = innerelem.get_attribute('value')
        if not inner:
            innerelem.send_keys(str(solution[row][col]))

#square = driver.find_element_by_xpath("//td[@id='c00']")
#rint element
#innerelem = element.find_element_by_css_selector("*")
#print innerelem
#inner = innerelem.get_attribute('value')
#print "inner: ", inner
#elem = driver.find_element_by_name("q")

#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#driver.close()