from selenium import webdriver
import os
import json
import time
directory = os.getcwd()
element_list = []
driver = webdriver.Chrome(os.path.join(
    directory, 'driver', 'chromedriver.exe'))
pages = list(range(1, 73))


page_url = 'https://store.steampowered.com/search/?sort_by=Price_ASC&specials=1'

driver.get(page_url)

titles = driver.find_element_by_xpath(
    '//*[@id="search_results_filtered_warning_persistent"]/div[1]')
match = int(titles.get_attribute('innerHTML').split(' ')[0].replace(',', ''))
excluded = int(titles.get_attribute(
    'innerHTML').split(' ')[5].replace(',', ''))
info = json.dumps({"Match": match, "Excluded": excluded})
with open('Games.txt', 'w') as f:
    f.write(info)
    f.write('\n')

print(f"Match:{match} Excluded: {excluded}")

scrolling = True
SCROLL_PAUSE_TIME = 0.5
new_init = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while scrolling:

    print('WORKING...')
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)

    # print("INTERMEDIATE RUN")
    games = driver.find_element_by_xpath('//*[@id="search_resultsRows"]')
    iteration_len = len(games.find_elements_by_xpath('./*'))
    print(f"\nStart: {new_init} | End: {iteration_len}\n")
    # try:
    for x in range(new_init, iteration_len):
        try:
            Title = driver.find_element_by_xpath(
                f'//*[@id="search_resultsRows"]/a[{x}]/div[2]/div[1]/span').text
        except:
            Title = None
        try:
            Date = driver.find_element_by_xpath(
                f'//*[@id = "search_resultsRows"]/a[{x}]/div[2]/div[2]').text
        except:
            Date = None
        try:
            old_price = driver.find_element_by_xpath(
                f'//*[@id="search_resultsRows"]/a[{x}]/div[2]/div[4]/div[2]/span/strike').text
        except:
            old_price = None
        try:
            new_price = driver.find_element_by_xpath(
                f'//*[@id = "search_resultsRows"]/a[{x}]/div[2]/div[4]/div[2]').text.split('\n')[1]
        except:
            new_price = None

        Game_details = json.dumps({"Item": x, "Title": Title, "Date": Date,
                                   "Old Price": old_price, "New Price": new_price})
        with open('Games.txt', 'a') as f:
            f.write(Game_details)
            f.write('\n')
    new_init = iteration_len
    print(f"\nNew Starting item: {new_init}\n")
    new_height = driver.execute_script("return document.body.scrollHeight")
    print('SCROLLING...')
    if new_height == last_height:
        print('SCROLL HEIGHT UNCHANGED !')
    last_height = new_height
    if x >= match:
        print('Exit CONDITION !')
        scrolling = False
