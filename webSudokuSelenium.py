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
            #sleep(1.5)
            innerelem.send_keys(str(solution[row][col]))