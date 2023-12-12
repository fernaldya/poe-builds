# Affliction League Starter Builds

It's always interesting to see how new leagues start in Path of Exile. As with most leagues, mines or traps are usually the most played builds at the start of the league. So, I've taken this opportunity to see how this new league fares in terms of builds at league start. Massive thanks for poe.ninja for providing the entire data, it's always fun to see how league starters compete at the start of each league.

> NOTE: I haven't actively played PoE since Harvest League (June 2020 until September 2020), I dabbled a bit in Heist but didn't really get into it much. So my knowledge on current PoE is very outdated.

## Background Information
With the new Affliction league in PoE being released, it will be interesting to see what the current meta is by looking at (scraping) the top dps builds at the moment. To do that, we can browse [poe.ninja](https://poe.ninja/builds/affliction?sort=dps) sorted by DPS to see how much DPS each build is doing. Furthermore, since this web scraping is done at a specific time, the data will most likely not fully represent current data. A script will be provided that will scrape data and save it as csv with appropriate time markings.

The `robots.txt` 
```
user-agent: *
disallow: */builds/char/*

sitemap: https://poe.ninja/sitemap.xml
```
disallows crawlers from accessing each individual character. This project will respect the exclusion protocol and only browse the endpoint `/builds/affliction` and not go into each character's page.

## Conclusion
As with most leagues, mines or traps are usually the most played builds at the start of the league due to its safety and possibly off-screen potential. At the time of scraping, 

Most played ascendancies:
1. Occultist
2. Assassin
3. Saboteur

Most played builds:
1. Hexblast
2. Ice Trap

## Recommendation
There aren't any build recommendations here because this is more of a personal interest project. Play whatever build you want! Re-roll or make a new character if it sucks. 

## Flicker Strike best build.

## Serious Note
If poe.ninja doesn't change any of their site format / structure, you can definitely re-run this entire project given that you have the pre-requisites installed. Some crucial thing to note, by default the url used is strictly for this current league https://poe.ninja/builds/affliction. Once we enter the next league(s), you might want to adjust the url in `main.py`.

## How to replicate this project
### 1. Setup webdriver
You can use any webdrivers, but I used chromedriver. Please refer to [this documentation](https://sites.google.com/chromium.org/driver/getting-started?authuser=0) if you want to use chromedriver.

### 2. Create a new virtual environment with conda (Optional)
```bash
conda create --name <env_name> python=3.11.5
conda activate <env_name>
```
Python version is up to you, but make sure there are no version clashes.

### 3. Clone this repo
```bash
git clone git@github.com:fernaldya/poe-builds.git
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```
If you want to run the notebook `poeninja.ipynb`, you'll also need to install other libraries by running this
```bash
pip install requests matplotlib seaborn
```

### 5. Usage
You can get the csv file by running the application
```bash
python main.py
```