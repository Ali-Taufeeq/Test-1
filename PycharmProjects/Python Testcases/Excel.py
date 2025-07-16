import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By

driver =  webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
#header content:
driver.find_elements(By.CSS_SELECTOR,"rdt_TableHeadRow")
header_cell = driver.find_elements(By.CSS_SELECTOR,".rdt_TableCol")
header_text = [head.text for head in header_cell]

#for whole table data:
data=[]
rows=driver.find_elements(By.CSS_SELECTOR,".rdt_TableRow")
for row in rows:
    row_cell=row.find_elements(By.CSS_SELECTOR,".rdt_TableCell")
    cell_text= [cell.text for cell in row_cell]
    data.append(cell_text)

#excel:
book=openpyxl.load_workbook("D:\\python_demo.xlsx")
sheet = book.active

sheet.append(header_text) #header

for cell in data: # table data:
    sheet.append(cell)

book.save("D:\\python_demo.xlsx")
book.close()

