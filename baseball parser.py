from time import sleep
from random import randint
import os

from selenium import webdriver
from bs4 import BeautifulSoup
from openpyxl import Workbook
from user_agent import generate_user_agent


dir = os.path.abspath(os.path.dirname(__file__))
url = "https://www.scoreboard.com/mlb/results/"
out_file_name = 'baseball_2018.xlsx'
out_file_dir = os.path.join(dir, 'data', out_file_name)
wait_time = 5
id_match = []
driver = webdriver.Chrome()
print("Start get match id...")

def random_sleep(start=1, end=3):
    sleep(randint(start, end))

headers = {'User-Agent': generate_user_agent()}
driver.get(url)
driver.minimize_window()

sleep(wait_time)

r = 0
while True:
    try:
        print("Refresh... {}".format(r))
        link = driver.find_element_by_link_text("Show more games")
        link.click()
        r += 1
        sleep(10)
    except:
        break

data = driver.page_source
bsObj = BeautifulSoup(data, "html.parser")

match_cards_odd = bsObj.find_all("tr", class_="odd stage-finished")
match_cards_even = bsObj.find_all("tr", class_="even stage-finished")

# get all match id
for match in match_cards_odd:
    id_match.append(match["id"][4:])

for match in match_cards_even:
    id_match.append(match["id"][4:])

driver.close()

# create out file sheet and headers
wb = Workbook()
ws = wb.create_sheet("baseball_2018")
ws.append([
    "Time",
    "Match",
    "Team_1",
    "Team_2",
    "Team_1_inning_1",
    "Team_1_inning_2",
    "Team_1_inning_3",
    "Team_1_inning_4",
    "Team_1_inning_5",
    "Team_1_inning_6",
    "Team_1_inning_7",
    "Team_1_inning_8",
    "Team_1_inning_9",
    "Team_2_inning_1",
    "Team_2_inning_2",
    "Team_2_inning_3",
    "Team_2_inning_4",
    "Team_2_inning_5",
    "Team_2_inning_6",
    "Team_2_inning_7",
    "Team_2_inning_8",
    "Team_2_inning_9",
    "Team_1_total_score",
    "Team_2_total_score",
])

# scrape data from all match card
print(" Get match card --> {}".format(len(id_match)))
print("Start...")
n = 0
for id in id_match:
    try:
        print("Iteration --> {}".format(n))
        n += 1
        url_card = "https://www.scoreboard.com/game/texas-rangers-new-york-yankees-2018/{}/#game-summary|game-statistics;0|lineups;1".format(id)
        driver = webdriver.Chrome()
        driver.get(url_card)
        sleep(wait_time)
        data = driver.page_source
        bsObj = BeautifulSoup(data, "html.parser")

        # get match time
        match_time = bsObj.find("td", class_="mstat-date").text

        # get teams
        teams = bsObj.find_all("td", class_="fl summary-horizontal")
        team_one_two = []
        for team in teams:
            team_one_two.append(team.find("a").text)

        # get inning team 1
        if bsObj.find("span", class_="p1_home"):
            inning_home_1 = bsObj.find("span", class_="p1_home").text
        else:
            inning_home_1 = 0
        if bsObj.find("span", class_="p2_home"):
            inning_home_2 = bsObj.find("span", class_="p2_home").text
        else:
            inning_home_2 = 0
        if bsObj.find("span", class_="p3_home"):
            inning_home_3 = bsObj.find("span", class_="p3_home").text
        else:
            inning_home_3 = 0
        if bsObj.find("span", class_="p4_home"):
            inning_home_4 = bsObj.find("span", class_="p4_home").text
        else:
            inning_home_4 = 0
        if bsObj.find("span", class_="p5_home"):
            inning_home_5 = bsObj.find("span", class_="p5_home").text
        else:
            inning_home_5 = 0
        if bsObj.find("span", class_="p6_home"):
            inning_home_6 = bsObj.find("span", class_="p6_home").text
        else:
            inning_home_6 = 0
        if bsObj.find("span", class_="p7_home"):
            inning_home_7 = bsObj.find("span", class_="p7_home").text
        else:
            inning_home_7 = 0
        if bsObj.find("span", class_="p8_home"):
            inning_home_8 = bsObj.find("span", class_="p8_home").text
        else:
            inning_home_8 = 0
        if bsObj.find("span", class_="p9_home"):
            inning_home_9 = bsObj.find("span", class_="p9_home").text
        else:
            inning_home_9 = 0
        # get inning team 2
        if bsObj.find("span", class_="p1_away"):
            inning_away_1 = bsObj.find("span", class_="p1_away").text
        else:
            inning_away_1 = 0
        if bsObj.find("span", class_="p2_away"):
            inning_away_2 = bsObj.find("span", class_="p2_away").text
        else:
            inning_away_2 = 0
        if bsObj.find("span", class_="p3_away"):
            inning_away_3 = bsObj.find("span", class_="p3_away").text
        else:
            inning_away_3 = 0
        if bsObj.find("span", class_="p4_away"):
            inning_away_4 = bsObj.find("span", class_="p4_away").text
        else:
            inning_away_4 = 0
        if bsObj.find("span", class_="p5_away"):
            inning_away_5 = bsObj.find("span", class_="p5_away").text
        else:
            inning_away_5 = 0
        if bsObj.find("span", class_="p6_away"):
            inning_away_6 = bsObj.find("span", class_="p6_away").text
        else:
            inning_away_6 = 0
        if bsObj.find("span", class_="p7_away"):
            inning_away_7 = bsObj.find("span", class_="p7_away").text
        else:
            inning_away_7 = 0
        if bsObj.find("span", class_="p8_away"):
            inning_away_8 = bsObj.find("span", class_="p8_away").text
        else:
            inning_away_8 = 0
        if bsObj.find("span", class_="p9_away"):
            inning_away_9 = bsObj.find("span", class_="p9_away").text
        else:
            inning_away_9 = 0

        # get score
        score = bsObj.find_all("td", class_="score")
        score_one_two = []
        for sc in score:
            if sc.find("strong"):
                score_one_two.append(sc.find("strong").text)
        if not score_one_two:
            score_one_two = ["X", "X"]
        if len(score_one_two) == 1:
            score_one_two.append("X")

        driver.close()

        # create line
        data_line = [match_time,
                     "{} vs {}".format(team_one_two[0], team_one_two[1]),
                     team_one_two[0],
                     team_one_two[1],
                     inning_home_1,
                     inning_home_2,
                     inning_home_3,
                     inning_home_4,
                     inning_home_5,
                     inning_home_6,
                     inning_home_7,
                     inning_home_8,
                     inning_home_9,
                     inning_away_1,
                     inning_away_2,
                     inning_away_3,
                     inning_away_4,
                     inning_away_5,
                     inning_away_6,
                     inning_away_7,
                     inning_away_8,
                     inning_away_9,
                     score_one_two[0],
                     score_one_two[1]]
        ws.append(data_line)
        wb.save(out_file_dir)
    except:
        continue

print("Close WebDriver...")
print('Save Data in file {}'.format(out_file_dir))
