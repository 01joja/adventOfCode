import os
import shutil
from datetime import datetime

currentYear = datetime.now().year
currentMonth = datetime.now().month
currentDay = datetime.now().day
currentHour = datetime.now().hour

if currentMonth == 12:
    endDay = currentDay
else:
    currentYear -=1
    endDay = 99

years = []
for y in range(2015,currentYear+1):
    years.append(str(y))

daysBefore2025 = []
for d in range(1,25+1):
    daysBefore2025.append(str(d))

daysAfter2025 = []
for d in range(1,12+1):
    daysAfter2025.append(str(d))

currentPath = os.getcwd()
onlyFolders = [f for f in os.listdir(currentPath) if os.path.isdir(os.path.join(currentPath, f))]
templatePath = os.path.join(currentPath, "template.py")

for y in years:
    yPath = os.path.join(currentPath,y)
    if y not in onlyFolders:
        os.makedirs(yPath)

    filesInFolder = os.listdir(yPath)
    if int(y) < 2025:
        days = daysBefore2025
    else:
        days = daysAfter2025

    for d in days:
        if endDay < int(d):
            break
        if len(d) == 1:
            d = "0"+d
        dPath = os.path.join(yPath,d)
        dPathData = dPath + ".data"
        dPathProblem = dPath + "problem.md"
        dPathSolution = dPath + "Solution.py"
        if not os.path.exists(dPathData):
            open(dPathData, "a").close
        if not os.path.exists(dPathProblem):
            open(dPathProblem, "a").close
        if not os.path.exists(dPathSolution):
            shutil.copyfile(templatePath,dPathSolution)

