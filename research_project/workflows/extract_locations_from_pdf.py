"""
Scan full PDF text (body + figure captions) for real geographic locations
for papers that currently have no curated location or show a study-type label.
Updates memory/paper_locations.json in-place.
"""

import json
import re
import sys
from pathlib import Path

import pymupdf  # noqa: PyMuPDF

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = PROJECT_ROOT / "memory" / "papers"
LOC_FILE = PROJECT_ROOT / "memory" / "paper_locations.json"

# ---------------------------------------------------------------------------
# Location patterns — ordered specific → generic.
# Each tuple: (compiled_regex, canonical_label)
# ---------------------------------------------------------------------------
_PLACE_PATTERNS = [
    # US cities/counties — frequently cited in EV papers
    (r"\bSan\s+Francisco\b", "San Francisco, CA, USA"),
    (r"\bLos\s+Angeles\b", "Los Angeles, CA, USA"),
    (r"\bNew\s+York\b(?:\s+City)?", "New York City, NY, USA"),
    (r"\bChicago\b", "Chicago, IL, USA"),
    (r"\bHouston\b", "Houston, TX, USA"),
    (r"\bPhoenix\b(?:,\s*AZ)?", "Phoenix, AZ, USA"),
    (r"\bPhiladelphia\b", "Philadelphia, PA, USA"),
    (r"\bSan\s+Antonio\b", "San Antonio, TX, USA"),
    (r"\bSan\s+Diego\b", "San Diego, CA, USA"),
    (r"\bDallas\b", "Dallas, TX, USA"),
    (r"\bAustin\b(?:,\s*TX)?", "Austin, TX, USA"),
    (r"\bJacksonville\b", "Jacksonville, FL, USA"),
    (r"\bSeattle\b", "Seattle, WA, USA"),
    (r"\bDenver\b", "Denver, CO, USA"),
    (r"\bBoston\b", "Boston, MA, USA"),
    (r"\bNashville\b", "Nashville, TN, USA"),
    (r"\bPortland\b(?:,\s*OR)?", "Portland, OR, USA"),
    (r"\bLas\s+Vegas\b", "Las Vegas, NV, USA"),
    (r"\bMemphis\b", "Memphis, TN, USA"),
    (r"\bAtlanta\b", "Atlanta, GA, USA"),
    (r"\bBaltimore\b", "Baltimore, MD, USA"),
    (r"\bMilwaukee\b", "Milwaukee, WI, USA"),
    (r"\bAlbuquerque\b", "Albuquerque, NM, USA"),
    (r"\bTucson\b", "Tucson, AZ, USA"),
    (r"\bFresno\b", "Fresno, CA, USA"),
    (r"\bSacramento\b", "Sacramento, CA, USA"),
    (r"\bKansas\s+City\b", "Kansas City, MO, USA"),
    (r"\bOmaha\b", "Omaha, NE, USA"),
    (r"\bRaleigh\b", "Raleigh, NC, USA"),
    (r"\bColorado\s+Springs\b", "Colorado Springs, CO, USA"),
    (r"\bMinneapolis\b", "Minneapolis, MN, USA"),
    (r"\bCleveland\b", "Cleveland, OH, USA"),
    (r"\bPittsburgh\b", "Pittsburgh, PA, USA"),
    (r"\bSt\.\s*Louis\b", "St. Louis, MO, USA"),
    (r"\bCincinnati\b", "Cincinnati, OH, USA"),
    (r"\bOrlando\b", "Orlando, FL, USA"),
    (r"\bMiami\b", "Miami, FL, USA"),
    (r"\bTampa\b", "Tampa, FL, USA"),
    (r"\bDetroit\b", "Detroit, MI, USA"),
    (r"\bIndianapolis\b", "Indianapolis, IN, USA"),
    (r"\bColumbus\b(?:,\s*OH)?", "Columbus, OH, USA"),
    (r"\bCharlotte\b(?:,\s*NC)?", "Charlotte, NC, USA"),
    (r"\bFort\s+Worth\b", "Fort Worth, TX, USA"),
    (r"\bEl\s+Paso\b", "El Paso, TX, USA"),
    (r"\bOklahoma\s+City\b", "Oklahoma City, OK, USA"),
    (r"\bLong\s+Beach\b", "Long Beach, CA, USA"),
    (r"\bVirginia\s+Beach\b", "Virginia Beach, VA, USA"),
    (r"\bArlington\b(?:,\s*(?:TX|VA))?", "Arlington, TX, USA"),
    (r"\bNew\s+Orleans\b", "New Orleans, LA, USA"),
    (r"\bBaker[s]?field\b", "Bakersfield, CA, USA"),
    (r"\bHonolulu\b", "Honolulu, HI, USA"),
    (r"\bAnaheim\b", "Anaheim, CA, USA"),
    (r"\bAurora\b(?:,\s*CO)?", "Aurora, CO, USA"),
    (r"\bSanta\s+Ana\b", "Santa Ana, CA, USA"),
    (r"\bCorpus\s+Christi\b", "Corpus Christi, TX, USA"),
    (r"\bRiverside\b(?:,\s*CA)?", "Riverside, CA, USA"),
    (r"\bLexington\b(?:,\s*KY)?", "Lexington, KY, USA"),
    (r"\bStockton\b(?:,\s*CA)?", "Stockton, CA, USA"),
    (r"\bSt\.\s*Paul\b", "St. Paul, MN, USA"),
    (r"\bAnchorage\b", "Anchorage, AK, USA"),
    (r"\bNewark\b(?:,\s*NJ)?", "Newark, NJ, USA"),
    (r"\bPlano\b(?:,\s*TX)?", "Plano, TX, USA"),
    (r"\bHenderson\b(?:,\s*NV)?", "Henderson, NV, USA"),
    (r"\bGilbert\b(?:,\s*AZ)?", "Gilbert, AZ, USA"),
    (r"\bGreensboro\b", "Greensboro, NC, USA"),
    (r"\bLincoln\b(?:,\s*NE)?", "Lincoln, NE, USA"),
    (r"\bBuffalo\b(?:,\s*NY)?", "Buffalo, NY, USA"),
    (r"\bFort\s+Wayne\b", "Fort Wayne, IN, USA"),
    (r"\bMadison\b(?:,\s*WI)?", "Madison, WI, USA"),
    (r"\bLubbock\b", "Lubbock, TX, USA"),
    (r"\bChandler\b(?:,\s*AZ)?", "Chandler, AZ, USA"),
    (r"\bScottsdale\b", "Scottsdale, AZ, USA"),
    (r"\bGlendale\b(?:,\s*(?:AZ|CA))?", "Glendale, AZ, USA"),
    (r"\bWinston.Salem\b", "Winston-Salem, NC, USA"),
    (r"\bNorfolk\b(?:,\s*VA)?", "Norfolk, VA, USA"),
    (r"\bFremont\b(?:,\s*CA)?", "Fremont, CA, USA"),
    (r"\bGarland\b(?:,\s*TX)?", "Garland, TX, USA"),
    (r"\bIrving\b(?:,\s*TX)?", "Irving, TX, USA"),
    (r"\bBaton\s+Rouge\b", "Baton Rouge, LA, USA"),
    (r"\bChesapeake\b(?:,\s*VA)?", "Chesapeake, VA, USA"),
    (r"\bSan\s+Bernardino\b", "San Bernardino, CA, USA"),
    (r"\bBoise\b(?:,\s*ID)?", "Boise, ID, USA"),
    (r"\bSpokane\b", "Spokane, WA, USA"),
    (r"\bTacoma\b", "Tacoma, WA, USA"),
    (r"\bBexar\s+County\b", "Bexar County, TX, USA"),
    (r"\bPalo\s+Alto\b", "Palo Alto, CA, USA"),
    (r"\bSilicon\s+Valley\b", "Silicon Valley, CA, USA"),
    (r"\bBay\s+Area\b", "SF Bay Area, CA, USA"),
    (r"\bWashington,?\s*D\.?C\.?", "Washington DC, USA"),
    (r"\bManhattan\b", "New York City, NY, USA"),
    (r"\bBrooklyn\b", "New York City, NY, USA"),
    (r"\bSanta\s+Clara\b", "Santa Clara, CA, USA"),
    (r"\bSunnyvale\b", "Sunnyvale, CA, USA"),
    (r"\bSan\s+Jose\b", "San Jose, CA, USA"),
    (r"\bOakland\b(?:,\s*CA)?", "Oakland, CA, USA"),
    (r"\bBerkeley\b(?:,\s*CA)?", "Berkeley, CA, USA"),
    (r"\bAnn\s+Arbor\b", "Ann Arbor, MI, USA"),
    (r"\bCambridge\b(?:,\s*MA)?", "Cambridge, MA, USA"),
    (r"\bNew\s+Haven\b", "New Haven, CT, USA"),
    (r"\bProvidence\b(?:,\s*RI)?", "Providence, RI, USA"),
    (r"\bHartford\b(?:,\s*CT)?", "Hartford, CT, USA"),
    (r"\bAlbany\b(?:,\s*NY)?", "Albany, NY, USA"),
    (r"\bSyracuse\b(?:,\s*NY)?", "Syracuse, NY, USA"),
    (r"\bRochester\b(?:,\s*NY)?", "Rochester, NY, USA"),
    (r"\bYonkers\b", "Yonkers, NY, USA"),
    (r"\bJersey\s+City\b", "Jersey City, NJ, USA"),
    (r"\bPaterson\b(?:,\s*NJ)?", "Paterson, NJ, USA"),
    (r"\bElizabeth\b(?:,\s*NJ)?", "Elizabeth, NJ, USA"),
    (r"\bTrenton\b(?:,\s*NJ)?", "Trenton, NJ, USA"),
    (r"\bWilmington\b(?:,\s*(?:DE|NC))?", "Wilmington, DE, USA"),
    (r"\bAkron\b(?:,\s*OH)?", "Akron, OH, USA"),
    (r"\bToledo\b(?:,\s*OH)?", "Toledo, OH, USA"),
    (r"\bDayton\b(?:,\s*OH)?", "Dayton, OH, USA"),
    (r"\bYoungstown\b", "Youngstown, OH, USA"),
    (r"\bSalem\b(?:,\s*OR)?", "Salem, OR, USA"),
    (r"\bEugene\b(?:,\s*OR)?", "Eugene, OR, USA"),
    (r"\bSalt\s+Lake\s+City\b", "Salt Lake City, UT, USA"),
    (r"\bProvo\b(?:,\s*UT)?", "Provo, UT, USA"),
    (r"\bReno\b(?:,\s*NV)?", "Reno, NV, USA"),
    (r"\bFairbanks\b", "Fairbanks, AK, USA"),
    (r"\bJuneau\b", "Juneau, AK, USA"),
    (r"\bFort\s+Collins\b", "Fort Collins, CO, USA"),
    (r"\bBoulder\b(?:,\s*CO)?", "Boulder, CO, USA"),
    (r"\bPueblo\b(?:,\s*CO)?", "Pueblo, CO, USA"),
    (r"\bFargo\b(?:,\s*ND)?", "Fargo, ND, USA"),
    (r"\bSioux\s+Falls\b", "Sioux Falls, SD, USA"),
    (r"\bBillings\b(?:,\s*MT)?", "Billings, MT, USA"),
    (r"\bMontgomery\b(?:,\s*AL)?", "Montgomery, AL, USA"),
    (r"\bBirmingham\b(?:,\s*AL)?", "Birmingham, AL, USA"),
    (r"\bMobile\b(?:,\s*AL)?", "Mobile, AL, USA"),
    (r"\bHuntsville\b(?:,\s*AL)?", "Huntsville, AL, USA"),
    (r"\bLittle\s+Rock\b", "Little Rock, AR, USA"),
    (r"\bFort\s+Smith\b", "Fort Smith, AR, USA"),
    (r"\bJackson\b(?:,\s*MS)?", "Jackson, MS, USA"),
    (r"\bGulfport\b", "Gulfport, MS, USA"),
    (r"\bShreve[a]?port\b", "Shreveport, LA, USA"),
    (r"\bLafayette\b(?:,\s*LA)?", "Lafayette, LA, USA"),
    (r"\bKnoxville\b", "Knoxville, TN, USA"),
    (r"\bChattanooga\b", "Chattanooga, TN, USA"),
    (r"\bClarksville\b(?:,\s*TN)?", "Clarksville, TN, USA"),
    (r"\bMurfreesboro\b", "Murfreesboro, TN, USA"),
    (r"\bFayetteville\b(?:,\s*(?:NC|AR))?", "Fayetteville, NC, USA"),
    (r"\bDurham\b(?:,\s*NC)?", "Durham, NC, USA"),
    (r"\bHighPoint\b|High\s+Point", "High Point, NC, USA"),
    (r"\bColumbia\b(?:,\s*SC)?", "Columbia, SC, USA"),
    (r"\bCharleston\b(?:,\s*(?:SC|WV))?", "Charleston, SC, USA"),
    (r"\bAugusta\b(?:,\s*GA)?", "Augusta, GA, USA"),
    (r"\bSavannah\b(?:,\s*GA)?", "Savannah, GA, USA"),
    (r"\bMacon\b(?:,\s*GA)?", "Macon, GA, USA"),
    (r"\bColumbus\b(?:,\s*GA)?", "Columbus, GA, USA"),
    (r"\bJacksonville\b(?:,\s*FL)?", "Jacksonville, FL, USA"),
    (r"\bSt\.\s*Petersburg\b", "St. Petersburg, FL, USA"),
    (r"\bHialeah\b", "Hialeah, FL, USA"),
    (r"\bFort\s+Lauderdale\b", "Fort Lauderdale, FL, USA"),
    (r"\bPort\s+St\.\s*Lucie\b", "Port St. Lucie, FL, USA"),
    (r"\bCape\s+Coral\b", "Cape Coral, FL, USA"),
    (r"\bTallahassee\b", "Tallahassee, FL, USA"),
    (r"\bGainesville\b(?:,\s*FL)?", "Gainesville, FL, USA"),
    (r"\bPensacola\b", "Pensacola, FL, USA"),
    # US county/region patterns
    (r"\bSioux\s+Falls\b", "Sioux Falls, SD, USA"),
    (r"(?:Los\s+Angeles|LA)\s+County", "Los Angeles County, CA, USA"),
    (r"\bOrange\s+County\b", "Orange County, CA, USA"),
    # Canada
    (r"\bToronto\b", "Toronto, Canada"),
    (r"\bMontreal\b", "Montreal, Canada"),
    (r"\bVancouver\b(?:,\s*BC)?", "Vancouver, Canada"),
    (r"\bCalgary\b", "Calgary, Canada"),
    (r"\bEdmonton\b", "Edmonton, Canada"),
    (r"\bOttawa\b", "Ottawa, Canada"),
    (r"\bWinnipeg\b", "Winnipeg, Canada"),
    (r"\bQuebec\s+City\b|\bQuébec\b", "Quebec, Canada"),
    (r"\bHamilton\b(?:,\s*ON)?", "Hamilton, Canada"),
    (r"\bKitchener\b", "Kitchener, Canada"),
    (r"\bLondon\b(?:,\s*ON)?", "London, ON, Canada"),
    (r"\bHalifax\b", "Halifax, Canada"),
    (r"\bVictoria\b(?:,\s*BC)?", "Victoria, Canada"),
    (r"\bSaskatoon\b", "Saskatoon, Canada"),
    (r"\bRegina\b(?:,\s*SK)?", "Regina, Canada"),
    (r"\bSt\.\s*John'?s\b", "St. John's, Canada"),
    # China
    (r"\bBeijing\b|\bPeking\b", "Beijing, China"),
    (r"\bShanghai\b", "Shanghai, China"),
    (r"\bShenzhen\b", "Shenzhen, China"),
    (r"\bGuangzhou\b|\bCanton\b", "Guangzhou, China"),
    (r"\bChengdu\b", "Chengdu, China"),
    (r"\bHangzhou\b", "Hangzhou, China"),
    (r"\bWuhan\b", "Wuhan, China"),
    (r"\bXi'?an\b", "Xi'an, China"),
    (r"\bChongqing\b", "Chongqing, China"),
    (r"\bTianjin\b", "Tianjin, China"),
    (r"\bNanjing\b", "Nanjing, China"),
    (r"\bSuzhou\b", "Suzhou, China"),
    (r"\bHarbin\b", "Harbin, China"),
    (r"\bQingdao\b", "Qingdao, China"),
    (r"\bZhengzhou\b", "Zhengzhou, China"),
    (r"\bDalian\b", "Dalian, China"),
    (r"\bJinan\b", "Jinan, China"),
    (r"\bXiamen\b", "Xiamen, China"),
    (r"\bChangsha\b", "Changsha, China"),
    (r"\bNingbo\b", "Ningbo, China"),
    (r"\bKunming\b", "Kunming, China"),
    (r"\bHefei\b", "Hefei, China"),
    (r"\bFuzhou\b", "Fuzhou, China"),
    (r"\bUrumqi\b", "Urumqi, China"),
    (r"\bGuiyang\b", "Guiyang, China"),
    (r"\bNanchang\b", "Nanchang, China"),
    (r"\bTaiyuan\b", "Taiyuan, China"),
    (r"\bLanzhou\b", "Lanzhou, China"),
    (r"\bXiaoshan\b", "Xiaoshan, China"),
    (r"\bZhuhai\b", "Zhuhai, China"),
    (r"\bDongguan\b", "Dongguan, China"),
    (r"\bFoshan\b", "Foshan, China"),
    (r"\bWenzhou\b", "Wenzhou, China"),
    (r"\bNantong\b", "Nantong, China"),
    (r"\bHohhot\b", "Hohhot, China"),
    (r"\bChangchun\b", "Changchun, China"),
    (r"\bShenyang\b", "Shenyang, China"),
    (r"\bShenyang\b", "Shenyang, China"),
    (r"\bHunan\b", "Hunan Province, China"),
    (r"\bShandong\b", "Shandong Province, China"),
    (r"\bZhejiang\b", "Zhejiang Province, China"),
    (r"\bJiangsu\b", "Jiangsu Province, China"),
    (r"\bGansu\b", "Gansu Province, China"),
    (r"\bSichuan\b", "Sichuan Province, China"),
    (r"\bYunnan\b", "Yunnan Province, China"),
    (r"\bShaanxi\b", "Shaanxi Province, China"),
    (r"\bHubei\b", "Hubei Province, China"),
    (r"\bAnhui\b", "Anhui Province, China"),
    (r"\bJilin\b", "Jilin Province, China"),
    (r"\bHeilongjiang\b", "Heilongjiang Province, China"),
    # Europe
    (r"\bLondon\b(?!,\s*ON)", "London, UK"),
    (r"\bGlasgow\b", "Glasgow, UK"),
    (r"\bBirmingham\b(?:,\s*UK)?", "Birmingham, UK"),
    (r"\bLeeds\b", "Leeds, UK"),
    (r"\bSheffield\b", "Sheffield, UK"),
    (r"\bManchester\b", "Manchester, UK"),
    (r"\bEdinburgh\b", "Edinburgh, UK"),
    (r"\bBristol\b", "Bristol, UK"),
    (r"\bLiverpool\b", "Liverpool, UK"),
    (r"\bNewcastle\b(?:\s+upon\s+Tyne)?", "Newcastle, UK"),
    (r"\bNotting[h]?am\b", "Nottingham, UK"),
    (r"\bOxford\b", "Oxford, UK"),
    (r"\bCoventry\b", "Coventry, UK"),
    (r"\bSouthampton\b", "Southampton, UK"),
    (r"\bPortsmouth\b", "Portsmouth, UK"),
    (r"\bCardiff\b", "Cardiff, Wales, UK"),
    (r"\bSwansea\b", "Swansea, Wales, UK"),
    (r"\bParis\b", "Paris, France"),
    (r"\bLyon\b", "Lyon, France"),
    (r"\bMarseille\b", "Marseille, France"),
    (r"\bBordeaux\b", "Bordeaux, France"),
    (r"\bToulouse\b", "Toulouse, France"),
    (r"\bNantes\b", "Nantes, France"),
    (r"\bStrasbourg\b", "Strasbourg, France"),
    (r"\bBerlin\b", "Berlin, Germany"),
    (r"\bHamburg\b", "Hamburg, Germany"),
    (r"\bMunich\b|\bMünchen\b", "Munich, Germany"),
    (r"\bCologne\b|\bKöln\b", "Cologne, Germany"),
    (r"\bFrankfurt\b", "Frankfurt, Germany"),
    (r"\bStuttgart\b", "Stuttgart, Germany"),
    (r"\bDüsseldorf\b|\bDusseldorf\b", "Düsseldorf, Germany"),
    (r"\bDortmund\b", "Dortmund, Germany"),
    (r"\bEssen\b", "Essen, Germany"),
    (r"\bBremen\b", "Bremen, Germany"),
    (r"\bHannover\b", "Hannover, Germany"),
    (r"\bDresden\b", "Dresden, Germany"),
    (r"\bLeipzig\b", "Leipzig, Germany"),
    (r"\bNuremberg\b|\bNürnberg\b", "Nuremberg, Germany"),
    (r"\bDuisburg\b", "Duisburg, Germany"),
    (r"\bBochum\b", "Bochum, Germany"),
    (r"\bWuppertal\b", "Wuppertal, Germany"),
    (r"\bBonn\b", "Bonn, Germany"),
    (r"\bMannheim\b", "Mannheim, Germany"),
    (r"\bKarlsruhe\b", "Karlsruhe, Germany"),
    (r"\bAugsburg\b", "Augsburg, Germany"),
    (r"\bWiesbaden\b", "Wiesbaden, Germany"),
    (r"\bGelsenkirchen\b", "Gelsenkirchen, Germany"),
    (r"\bMönchengladbach\b", "Mönchengladbach, Germany"),
    (r"\bBraunschweig\b", "Braunschweig, Germany"),
    (r"\bKiel\b", "Kiel, Germany"),
    (r"\bAachen\b", "Aachen, Germany"),
    (r"\bHalle\b(?:\s+an\s+der\s+Saale)?", "Halle, Germany"),
    (r"\bMagdeburg\b", "Magdeburg, Germany"),
    (r"\bFreiburg\b", "Freiburg, Germany"),
    (r"\bRostock\b", "Rostock, Germany"),
    (r"\bOberhausen\b", "Oberhausen, Germany"),
    (r"\bHamm\b", "Hamm, Germany"),
    (r"\bSaarbrücken\b|\bSaarbrucken\b", "Saarbrücken, Germany"),
    (r"\bHeidel[b]?erg\b", "Heidelberg, Germany"),
    (r"\bMünster\b|\bMunster\b(?:,\s*Germany)?", "Münster, Germany"),
    (r"\bLower\s+Saxony\b|\bNiedersachsen\b", "Lower Saxony, Germany"),
    (r"\bBavaria\b|\bBayern\b", "Bavaria, Germany"),
    (r"\bNorth\s+Rhine.Westphalia\b", "North Rhine-Westphalia, Germany"),
    (r"\bAmsterdam\b", "Amsterdam, Netherlands"),
    (r"\bRotterdam\b", "Rotterdam, Netherlands"),
    (r"\bThe\s+Hague\b", "The Hague, Netherlands"),
    (r"\bUtrecht\b", "Utrecht, Netherlands"),
    (r"\bEindhoven\b", "Eindhoven, Netherlands"),
    (r"\bMadrid\b", "Madrid, Spain"),
    (r"\bBarcelona\b", "Barcelona, Spain"),
    (r"\bValencia\b", "Valencia, Spain"),
    (r"\bSeville\b|\bSevilla\b", "Seville, Spain"),
    (r"\bZaragoza\b", "Zaragoza, Spain"),
    (r"\bMálaga\b|\bMalaga\b", "Malaga, Spain"),
    (r"\bMurcia\b", "Murcia, Spain"),
    (r"\bBilbao\b", "Bilbao, Spain"),
    (r"\bRome\b|\bRoma\b", "Rome, Italy"),
    (r"\bMilan\b|\bMilano\b", "Milan, Italy"),
    (r"\bNaples\b|\bNapoli\b", "Naples, Italy"),
    (r"\bTurin\b|\bTorino\b", "Turin, Italy"),
    (r"\bPalermo\b", "Palermo, Italy"),
    (r"\bGenoa\b|\bGenova\b", "Genoa, Italy"),
    (r"\bFlorence\b|\bFirenze\b", "Florence, Italy"),
    (r"\bBologna\b", "Bologna, Italy"),
    (r"\bVenice\b|\bVenezia\b", "Venice, Italy"),
    (r"\bZurich\b|\bZürich\b", "Zurich, Switzerland"),
    (r"\bGeneva\b|\bGenève\b", "Geneva, Switzerland"),
    (r"\bBern\b", "Bern, Switzerland"),
    (r"\bChur\b", "Chur, Switzerland"),
    (r"\bVienna\b|\bWien\b", "Vienna, Austria"),
    (r"\bGraz\b", "Graz, Austria"),
    (r"\bLinz\b", "Linz, Austria"),
    (r"\bBrussels\b|\bBruxelles\b", "Brussels, Belgium"),
    (r"\bAntwerp\b|\bAntwerpen\b", "Antwerp, Belgium"),
    (r"\bHasselt\b", "Hasselt, Belgium"),
    (r"\bGhent\b|\bGent\b", "Ghent, Belgium"),
    (r"\bCopenhagen\b|\bKøbenhavn\b", "Copenhagen, Denmark"),
    (r"\bStockholm\b", "Stockholm, Sweden"),
    (r"\bGothenburg\b|\bGöteborg\b", "Gothenburg, Sweden"),
    (r"\bMalmö\b|\bMalmo\b", "Malmö, Sweden"),
    (r"\bOslo\b", "Oslo, Norway"),
    (r"\bBergen\b", "Bergen, Norway"),
    (r"\bHelsinki\b", "Helsinki, Finland"),
    (r"\bTampere\b", "Tampere, Finland"),
    (r"\bWarsaw\b|\bWarszawa\b", "Warsaw, Poland"),
    (r"\bKraków\b|\bKrakow\b", "Kraków, Poland"),
    (r"\bLódz\b|\bLodz\b", "Łódź, Poland"),
    (r"\bWrocław\b|\bWroclaw\b", "Wrocław, Poland"),
    (r"\bPoznań\b|\bPoznan\b", "Poznań, Poland"),
    (r"\bPrague\b|\bPraha\b", "Prague, Czech Republic"),
    (r"\bBrno\b", "Brno, Czech Republic"),
    (r"\bBudapest\b", "Budapest, Hungary"),
    (r"\bBucharest\b|\bBucurești\b", "Bucharest, Romania"),
    (r"\bSofia\b", "Sofia, Bulgaria"),
    (r"\bBelgrade\b|\bBeograd\b", "Belgrade, Serbia"),
    (r"\bZagreb\b", "Zagreb, Croatia"),
    (r"\bAthens\b|\bAthen\b", "Athens, Greece"),
    (r"\bThessaloniki\b", "Thessaloniki, Greece"),
    (r"\bLisbon\b|\bLisboa\b", "Lisbon, Portugal"),
    (r"\bPorto\b(?:,\s*Portugal)?", "Porto, Portugal"),
    (r"\bHelsinki\b", "Helsinki, Finland"),
    (r"\bRiga\b", "Riga, Latvia"),
    (r"\bTallinn\b", "Tallinn, Estonia"),
    (r"\bVilnius\b", "Vilnius, Lithuania"),
    (r"\bLjubljana\b", "Ljubljana, Slovenia"),
    (r"\bBratislava\b", "Bratislava, Slovakia"),
    (r"\bReykjavik\b", "Reykjavik, Iceland"),
    # Asia-Pacific
    (r"\bTokyo\b", "Tokyo, Japan"),
    (r"\bOsaka\b", "Osaka, Japan"),
    (r"\bKyoto\b", "Kyoto, Japan"),
    (r"\bNagoya\b", "Nagoya, Japan"),
    (r"\bSapporo\b", "Sapporo, Japan"),
    (r"\bFukuoka\b", "Fukuoka, Japan"),
    (r"\bSeoul\b", "Seoul, South Korea"),
    (r"\bBusan\b", "Busan, South Korea"),
    (r"\bIncheon\b", "Incheon, South Korea"),
    (r"\bDaegu\b", "Daegu, South Korea"),
    (r"\bSingapore\b", "Singapore"),
    (r"\bBangkok\b", "Bangkok, Thailand"),
    (r"\bHo\s+Chi\s+Minh\b|\bSaigon\b", "Ho Chi Minh City, Vietnam"),
    (r"\bHanoi\b", "Hanoi, Vietnam"),
    (r"\bManila\b", "Manila, Philippines"),
    (r"\bJakarta\b", "Jakarta, Indonesia"),
    (r"\bSurabaya\b", "Surabaya, Indonesia"),
    (r"\bBandung\b", "Bandung, Indonesia"),
    (r"\bMedan\b", "Medan, Indonesia"),
    (r"\bKuala\s+Lumpur\b", "Kuala Lumpur, Malaysia"),
    (r"\bKarachi\b", "Karachi, Pakistan"),
    (r"\bLahore\b", "Lahore, Pakistan"),
    (r"\bIslamabad\b", "Islamabad, Pakistan"),
    (r"\bLudhiana\b", "Ludhiana, India"),
    (r"\bDelhi\b|\bNew\s+Delhi\b", "New Delhi, India"),
    (r"\bSouth\s+Delhi\b", "South Delhi, India"),
    (r"\bMumbai\b|\bBombay\b", "Mumbai, India"),
    (r"\bBangalore\b|\bBengaluru\b", "Bangalore, India"),
    (r"\bHyderabad\b", "Hyderabad, India"),
    (r"\bAhmedabad\b", "Ahmedabad, India"),
    (r"\bChennai\b|\bMadras\b", "Chennai, India"),
    (r"\bKolkata\b|\bCalcutta\b", "Kolkata, India"),
    (r"\bPune\b", "Pune, India"),
    (r"\bSurat\b", "Surat, India"),
    (r"\bJaipur\b", "Jaipur, India"),
    (r"\bLucknow\b", "Lucknow, India"),
    (r"\bKanpur\b", "Kanpur, India"),
    (r"\bNagpur\b", "Nagpur, India"),
    (r"\bIndore\b", "Indore, India"),
    (r"\bBhopal\b", "Bhopal, India"),
    (r"\bPatna\b", "Patna, India"),
    (r"\bVisakhapatnam\b", "Visakhapatnam, India"),
    (r"\bVadodara\b", "Vadodara, India"),
    (r"\bGhaziabad\b", "Ghaziabad, India"),
    (r"\bLudhiana\b", "Ludhiana, India"),
    (r"\bAgra\b", "Agra, India"),
    (r"\bNasik\b|\bNashik\b", "Nashik, India"),
    (r"\bFaridabad\b", "Faridabad, India"),
    (r"\bMeerut\b", "Meerut, India"),
    (r"\bRajkot\b", "Rajkot, India"),
    (r"\bKalyan\b", "Kalyan, India"),
    (r"\bVasai-Virar\b", "Vasai-Virar, India"),
    (r"\bVaranasi\b", "Varanasi, India"),
    (r"\bSrinagar\b", "Srinagar, India"),
    (r"\bDhaka\b", "Dhaka, Bangladesh"),
    (r"\bColombo\b", "Colombo, Sri Lanka"),
    (r"\bKathmandu\b", "Kathmandu, Nepal"),
    (r"\bCairo\b|\bAl-Qāhirah\b", "Cairo, Egypt"),
    (r"\bAlexandria\b(?:,\s*Egypt)?", "Alexandria, Egypt"),
    (r"\bNairobi\b", "Nairobi, Kenya"),
    (r"\bLagos\b", "Lagos, Nigeria"),
    (r"\bAbuja\b", "Abuja, Nigeria"),
    (r"\bAccra\b", "Accra, Ghana"),
    (r"\bAddis\s+Ababa\b", "Addis Ababa, Ethiopia"),
    (r"\bCasablanca\b", "Casablanca, Morocco"),
    (r"\bKinshasa\b", "Kinshasa, DRC"),
    (r"\bLuanda\b", "Luanda, Angola"),
    (r"\bDar\s+es\s+Salaam\b", "Dar es Salaam, Tanzania"),
    (r"\bKampala\b", "Kampala, Uganda"),
    (r"\bHarare\b", "Harare, Zimbabwe"),
    (r"\bMaputo\b", "Maputo, Mozambique"),
    (r"\bAntananarivo\b", "Antananarivo, Madagascar"),
    # Middle East
    (r"\bRiyadh\b", "Riyadh, Saudi Arabia"),
    (r"\bJeddah\b", "Jeddah, Saudi Arabia"),
    (r"\bDubai\b", "Dubai, UAE"),
    (r"\bAbu\s+Dhabi\b", "Abu Dhabi, UAE"),
    (r"\bMuscat\b", "Muscat, Oman"),
    (r"\bDoha\b", "Doha, Qatar"),
    (r"\bKuwait\s+City\b", "Kuwait City, Kuwait"),
    (r"\bManama\b", "Manama, Bahrain"),
    (r"\bAmman\b", "Amman, Jordan"),
    (r"\bBeirut\b", "Beirut, Lebanon"),
    (r"\bBaghdad\b", "Baghdad, Iraq"),
    (r"\bBasra\b", "Basra, Iraq"),
    (r"\bTehran\b", "Tehran, Iran"),
    (r"\bMashhad\b", "Mashhad, Iran"),
    (r"\bEsfahan\b|\bIsfahan\b", "Isfahan, Iran"),
    (r"\bTabriz\b", "Tabriz, Iran"),
    (r"\bAnkara\b", "Ankara, Turkey"),
    (r"\bIstanbul\b", "Istanbul, Turkey"),
    (r"\bIzmir\b", "Izmir, Turkey"),
    (r"\bBursa\b", "Bursa, Turkey"),
    (r"\bTel\s+Aviv\b", "Tel Aviv, Israel"),
    (r"\bJerusalem\b", "Jerusalem, Israel"),
    # Latin America
    (r"\bSão\s+Paulo\b|\bSao\s+Paulo\b", "São Paulo, Brazil"),
    (r"\bRio\s+de\s+Janeiro\b", "Rio de Janeiro, Brazil"),
    (r"\bBrasília\b|\bBrasilia\b", "Brasília, Brazil"),
    (r"\bSalvador\b(?:,\s*Brazil)?", "Salvador, Brazil"),
    (r"\bFortaleza\b", "Fortaleza, Brazil"),
    (r"\bBelo\s+Horizonte\b", "Belo Horizonte, Brazil"),
    (r"\bManaus\b", "Manaus, Brazil"),
    (r"\bCuritiba\b", "Curitiba, Brazil"),
    (r"\bRecife\b", "Recife, Brazil"),
    (r"\bPorto\s+Alegre\b", "Porto Alegre, Brazil"),
    (r"\bBuenos\s+Aires\b", "Buenos Aires, Argentina"),
    (r"\bCórdoba\b|\bCordoba\b(?:,\s*Argentina)?", "Córdoba, Argentina"),
    (r"\bRosario\b(?:,\s*Argentina)?", "Rosario, Argentina"),
    (r"\bMendoza\b", "Mendoza, Argentina"),
    (r"\bSantiago\b(?:,\s*Chile)?", "Santiago, Chile"),
    (r"\bLima\b(?:,\s*Peru)?", "Lima, Peru"),
    (r"\bBogotá\b|\bBogota\b", "Bogotá, Colombia"),
    (r"\bMedellín\b|\bMedellin\b", "Medellín, Colombia"),
    (r"\bCali\b(?:,\s*Colombia)?", "Cali, Colombia"),
    (r"\bCaracas\b", "Caracas, Venezuela"),
    (r"\bQuito\b", "Quito, Ecuador"),
    (r"\bMontevideo\b", "Montevideo, Uruguay"),
    (r"\bAsunción\b|\bAsuncion\b", "Asunción, Paraguay"),
    (r"\bLa\s+Paz\b", "La Paz, Bolivia"),
    (r"\bMexico\s+City\b|\bCiudad\s+de\s+México\b", "Mexico City, Mexico"),
    (r"\bGuadalajara\b(?:,\s*Mexico)?", "Guadalajara, Mexico"),
    (r"\bMonterrey\b", "Monterrey, Mexico"),
    (r"\bPuebla\b(?:,\s*Mexico)?", "Puebla, Mexico"),
    # Australia / New Zealand
    (r"\bSydney\b", "Sydney, Australia"),
    (r"\bMelbourne\b", "Melbourne, Australia"),
    (r"\bBrisbane\b", "Brisbane, Australia"),
    (r"\bPerth\b(?:,\s*Australia)?", "Perth, Australia"),
    (r"\bAdelaide\b", "Adelaide, Australia"),
    (r"\bCanberra\b", "Canberra, Australia"),
    (r"\bAuckland\b", "Auckland, New Zealand"),
    (r"\bWellington\b(?:,\s*NZ)?", "Wellington, New Zealand"),
    (r"\bChristchurch\b", "Christchurch, New Zealand"),
    # Russian cities
    (r"\bMoscow\b|\bMoskva\b", "Moscow, Russia"),
    (r"\bSt\.\s*Petersburg\b(?:,\s*Russia)?|\bSaint\s+Petersburg\b", "St. Petersburg, Russia"),
    (r"\bNovosibirsk\b", "Novosibirsk, Russia"),
    (r"\bEkaterinburg\b", "Ekaterinburg, Russia"),
    (r"\bNizhny\s+Novgorod\b", "Nizhny Novgorod, Russia"),
    # Generic US region patterns — catch "in the city of X" / "X metropolitan"
    (r"(?:in|of)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*),\s*(TX|CA|NY|FL|IL|PA|OH|GA|NC|MI|NJ|VA|WA|AZ|MA|TN|IN|MO|MD|WI|MN|CO|AL|SC|LA|KY|OR|OK|CT|UT|NV|AR|KS|NE|ID|NM|ME|RI|MT|DE|SD|ND|AK|VT|HI|WY)\b",
     None),  # dynamic — captured in code
]

# Compiled once
_COMPILED = []
for pat, label in _PLACE_PATTERNS:
    try:
        _COMPILED.append((re.compile(pat, re.IGNORECASE), label))
    except re.error:
        pass


def _search_text_for_location(text: str) -> str | None:
    """Return first matching location label from text."""
    # Priority: figure captions first
    caption_re = re.compile(
        r"(?:Fig(?:ure)?\.?\s*\d+[.:]\s*)(.{0,200})",
        re.IGNORECASE | re.DOTALL,
    )
    caption_texts = [m.group(1) for m in caption_re.finditer(text)]
    priority_text = " ".join(caption_texts) + " " + text

    for cre, label in _COMPILED:
        m = cre.search(priority_text)
        if m:
            if label is None:
                # Dynamic: reconstruct from captured groups
                city = m.group(1)
                state = m.group(2)
                return f"{city}, {state}, USA"
            return label
    return None


def extract_pdf_text(pdf_path: Path, max_pages: int = 40) -> str:
    """Extract plain text from PDF using PyMuPDF, up to max_pages."""
    try:
        doc = pymupdf.open(str(pdf_path))
        pages = min(len(doc), max_pages)
        chunks = []
        for i in range(pages):
            page = doc[i]
            chunks.append(page.get_text("text"))
        doc.close()
        return " ".join(chunks)
    except Exception as e:
        print(f"  [warn] PDF read error {pdf_path.name}: {e}", file=sys.stderr)
        return ""


def main():
    curated: dict[str, str] = json.loads(LOC_FILE.read_text(encoding="utf-8"))
    original_count = len(curated)

    # Collect included paper keys that don't already have curated locations
    meta_files = list(PAPERS_DIR.glob("*_metadata.json"))
    print(f"Total papers: {len(meta_files)}")

    to_scan = []
    for mf in meta_files:
        key = mf.stem.replace("_metadata", "")
        if key in curated:
            continue
        # Check if included
        clf_file = PAPERS_DIR / f"{key}_classification.md"
        if not clf_file.exists():
            continue
        clf_text = clf_file.read_text(encoding="utf-8", errors="replace")
        if "**Included:** Yes" not in clf_text and "**Included:** yes" not in clf_text:
            continue
        to_scan.append(key)

    print(f"Papers to scan (included, no curated location): {len(to_scan)}")

    # For each key, find PDF and extract text
    found = {}
    no_pdf = []
    no_match = []
    for key in sorted(to_scan):
        # Find PDF
        pdf_candidates = list(PAPERS_DIR.glob(f"{key}.pdf")) + list(PAPERS_DIR.glob(f"{key}*.pdf"))
        if not pdf_candidates:
            # Try arxiv-id based PDFs
            meta = json.loads((PAPERS_DIR / f"{key}_metadata.json").read_text(encoding="utf-8"))
            arxiv_id = meta.get("arxiv_id", "")
            if arxiv_id:
                pdf_candidates = list(PAPERS_DIR.glob(f"{arxiv_id}*.pdf"))
        if not pdf_candidates:
            no_pdf.append(key)
            continue

        pdf_path = pdf_candidates[0]
        text = extract_pdf_text(pdf_path)
        if not text.strip():
            no_pdf.append(key)
            continue

        loc = _search_text_for_location(text)
        if loc:
            found[key] = loc
            print(f"  [found] {key:45s} -> {loc}")
        else:
            no_match.append(key)

    print(f"\nFound locations in PDFs: {len(found)}")
    print(f"No PDF available:        {len(no_pdf)}")
    print(f"No location match:       {len(no_match)}")

    if found:
        curated.update(found)
        LOC_FILE.write_text(
            json.dumps(curated, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print(f"\npaper_locations.json updated: {original_count} -> {len(curated)} entries")

    if no_match:
        print("\nPapers with no match (will need study-type fallback):")
        for k in no_match[:30]:
            print(f"  {k}")


if __name__ == "__main__":
    main()
