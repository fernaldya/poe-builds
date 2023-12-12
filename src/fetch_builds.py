from src.build import Build

def fetch_builds(table_rows):
    """
    This function fetches all the elements we want to grab by parsing through each row
    and fetching all the information we want from the relevant table cells <td>.
    The parameters:
    1. table_rows -> All the table rows obtained from the function scrape
    
    The function returns a list containing all the objects (builds).
    """
    builds = [] # List to store all the build informations
    
    for row in table_rows:
        cells = row.find_all('td') # Fetch all cells from the row
        life = cells[2].getText() # Life
        es = cells[3].getText() # Energy shield
        dps = cells[4].getText() # DPS
        
        # Lvl / Asc
        level = cells[1].find('div', class_='grid gap-2 items-center grid-flow-col').getText() # Level
        asc = cells[1].find('img')['alt'] # Ascendancy
        
        # Skills
        all_skills = cells[5].find('div', class_='grid grid-flow-col auto-cols-max gap-1').find_all('img')
        skills = [skill_alt['alt'] for skill_alt in all_skills]
        
        # Keystones
        try:
            all_keystones = cells[5].find('div', class_='grid grid-flow-col auto-cols-max gap-1 justify-end').find_all('img')
            keystones = [keystone_alt['alt'] for keystone_alt in all_keystones]
        except AttributeError:
            keystones = []
            
        # print(level, asc, life, es, dps, skills, keystones)
        build = Build(level, asc, dps, skills, keystones, life, es)
        builds.append(build)
        
    return builds