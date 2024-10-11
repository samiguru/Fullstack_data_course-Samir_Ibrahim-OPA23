### Lab Overview - The Data Driver YouTuber
___
I denna labb skapas ett dashboard för att analysera och få insikt i statistik och trafik för en YouTube-sida. Koden är organiserad i separata filer för att göra den så tydlig och lätt att följa som möjligt.

Först bearbetas och struktureras CSV-filer med data för att skapa en databas. En EDA (Exploratory Data Analysis) genomförs för att undersöka datan, och sedan används SQL-queries för att extrahera relevant information från tabeller. Detta kommer att förklaras kort nedan:

## .sql files
---
# EDA.sql
- Visa data.
- Förbereda data, ex. ta bort den första raden.
- Förstå data.

# marts_content.sql
- Skapa nya tabeller i (marts) som ska sedan använda för att länka till KPIer och diagram.

# marts_device.sql
skapade nya tabeller som hjälpte till att göra dashboard som förenklade komplexa data. Några av de skapade tabellerna var en tabell som visade förhållandet mellan operativsystemen och antalet visningar.

# marts_statistics.sql
skapade nya tabeller t.ex. en tabell som visade förhållandet mellan den geografiska platsen och antalet visningar.

# view_tables.sql
Denna SQL-fil skapades för att dubbelkolla om de skapade filerna finns.

# delete_tables.sql
Denna SQL-fil skapades för att radera tabeller som har fel på ett snabbt sätt.
___

## .py files
---
# kpi.py
- Skapade klasser och funktioner där kommer att placera KPI:er, vilket gör det enkelt att kalla på dem i dashboard.py.

# graphs.py
- Alla skapade grafer.

# dashboard.py
- Alla KPI:er, grafer, anropas och sätts ihop till en välorganiserad dashboard.
___
