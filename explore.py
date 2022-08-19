import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import datetime
from datetime import date
from yahoofinancials import YahooFinancials

today = date.today()

def finance_explore():
    st.title('check for stock prices and historic trends')
    stock = st.selectbox(
     'Choose company(only indian)',
     ('RELIANCE', 'TCS', 'HDFCBANK', 'INFY', 'ICICIBANK', 'HINDUNILVR', 'SBIN', 'BAJFINANCE', 'HDFC', 'BHARTIARTL', 'KOTAKBANK', 'WIPRO', 'HCLTECH', 'ITC', 'ADANIGREEN', 'ASIANPAINT', 'BAJAJFINSV', 'ADANITRANS', 'DMART', 'LT', 'ATGL', 'AXISBANK', 'MARUTI', 'TITAN', 'ADANIENT', 'SUNPHARMA', 'ONGC', 'ULTRACEMCO', 'JSWSTEEL', 'ADANIPORTS', 'TATASTEEL', 'POWERGRID', 'VEDL', 'TECHM', 'TATAMOTORS', 'HINDZINC', 'NTPC', 'HINDALCO', 'PIDILITIND', 'DIVISLAB', 'HDFCLIFE', 'COALINDIA', 'SBILIFE', 'IOC', 'GRASIM', 'LTI', 'BAJAJ-AUTO', 'M&M', 'DABUR', 'DLF', 'SHREECEM', 'SIEMENS', 'CIPLA', 'SBICARD', 'NYKAA', 'SRF', 'BPCL', 'INDIGO', 'BRITANNIA', 'GODREJCP', 'TATAPOWER', 'INDUSINDBK', 'HAVELLS', 'ICICIPRULI', 'TATACONSUM', 'DRREDDY', 'ADANIPOWER', 'MINDTREE', 'GAIL', 'BERGEPAINT', 'EICHERMOT', 'AWL', 'ICICIGI', 'MARICO', 'APOLLOHOSP', 'ZOMATO', 'MCDOWELL-N', 'MPHASIS', 'IRCTC', 'INDUSTOWER', 'AMBUJACEM', 'CHOLAFIN', 'UPL', 'NAUKRI', 'BANKBARODA', 'BAJAJHLDNG', 'TATAELXSI', 'JINDALSTEL', 'LODHA', 'LTTS', 'GLAND', 'MUTHOOTFIN', 'PEL', 'BEL', 'JSWENERGY', 'HAL', 'BANDHANBNK', 'PAGEIND', 'NMDC', 'TORNTPHARM', 'PGHH', 'GODREJPROP', 'IDBI', 'HEROMOTOCO', 'HDFCAMC', 'ABB', 'TRENT', 'MOTHERSUMI', 'ALKEM', 'PIIND', 'BOSCHLTD', 'COLPAL', 'CANBK', 'BALKRISIND', 'VOLTAS', 'CONCOR', 'STARHEALTH', 'VBL', 'SAIL', 'ASTRAL', 'ACC', 'BIOCON', 'SONACOMS', 'UBL', 'AUBANK', 'AUROPHARMA', 'PNB', 'HINDPETRO', 'PERSISTENT', 'ZYDUSLIFE', 'POLYCAB', 'HONAUT', 'TATACOMM', 'JUBLFOOD', 'AARTIIND', 'GUJGASLTD', 'ASHOKLEY', 'IOB', 'PAYTM', 'OBEROIRLTY', 'LUPIN', 'MAXHEALTH', 'BHARATFORG', 'TTML', 'LINDEINDIA', 'LAURUSLABS', 'INDHOTEL', 'TIINDIA', 'POLICYBZR', 'CUMMINSIND', 'OFSS', 'YESBANK', 'SRTRANSFIN', 'DEEPAKNTR', 'ATUL', 'SCHAEFFLER', 'FLUOROCHEM', 'PFC', 'TVSMOTOR', 'PETRONET', 'ABFRL', 'RUCHI', 'GLAXO', 'IRFC', 'DALBHARAT', 'NHPC', 'IDEA', 'ZEEL', 'MRF', 'TRIDENT', 'COFORGE', 'IPCALAB', 'MINDAIND', 'RELAXO', 'UNIONBANK', 'IGL', 'MFSL', 'ABCAPITAL', 'SUPREMEIND', 'OIL', 'CGPOWER', 'DIXON', 'SOLARINDS', 'BATAINDIA', 'KANSAINER', 'TATACHEM', 'IDFCFIRSTB', 'RECLTD', 'CRISIL', 'SYNGENE', 'CROMPTON', 'TORNTPOWER', 'COROMANDEL', 'MANYAVAR', 'HATSUN', 'THERMAX', 'APLAPOLLO', 'ESCORTS', 'SUMICHEM', 'NATIONALUM', 'GMRINFRA', '3MINDIA', 'FORTIS', 'LALPATHLAB', 'NAM-INDIA', 'SUNDARMFIN', 'KPRMILL', 'CLEAN', 'DEVYANI', 'POONAWALLA', 'TANLA', 'FEDERALBNK', 'RAJESHEXPO', 'MSUMI', 'AAVAS', 'NAVINFLUOR', 'IEX', 'VINATIORGA', 'ISEC', 'GICRE', 'WHIRLPOOL', 'L&TFH', 'GRINDWELL', 'PFIZER', 'EMAMILTD', 'PRESTIGE', 'LICHSGFIN', 'M&MFIN', 'PHOENIXLTD', 'SUNTV', 'INDIANB', 'SUNDRMFAST', 'BANKINDIA', 'JKCEMENT', 'NIACL', 'RAMCOCEM', 'DCMSHRIRAM', 'CHAMBLFERT', 'SKFINDIA', 'SANOFI', 'BHEL', 'BCG', 'SFL', 'APTUS', 'AFFLE', 'METROBRAND', 'KPITTECH', 'BLUEDART', 'KAJARIACER', 'TIMKEN', 'CENTRALBK', 'CENTURYPLY', 'GILLETTE', 'SUVENPHAR', 'AJANTPHARM', 'GODREJIND', 'HAPPSTMNDS', 'CDSL', 'ENDURANCE', 'ABSLAMC', 'AIAENG', 'NH', 'IRB', 'CARBORUNIV', 'POWERINDIA', 'GRINFRA', 'IIFLWAM', 'GSPL', 'ALKYLAMINE', 'APLLTD', 'ZFCVINDIA', 'UCOBANK', 'NUVOCO', 'NATCOPHARM', 'BASF', 'CREDITACC', 'INDIAMART', 'GNFC', 'EXIDEIND', 'MOTILALOFS', 'BSE', 'ANGELONE', 'INTELLECT', 'BSOFT', 'TV18BRDCST', 'KIOCL', 'UTIAMC', 'VTL', 'ALOKINDS', 'GLENMARK', 'BAJAJELEC', 'FINEORG', 'JBCHEPHARM', 'APOLLOTYRE', 'RATNAMANI', 'MEDPLUS', 'BRIGADE', 'AMBER', 'RADICO', 'PVR', 'CHOLAHLDNG', 'TTKPRESTIG', 'KEI', 'REDINGTON', 'CAMS', 'MAHABANK', 'KIMS', 'HINDCOPPER', 'IIFL', 'HFCL', 'SHRIRAMCIT', 'CGCL', 'SJVN', 'VIPIND', 'LXCHEM', 'CHEMPLASTS', 'ASAHIINDIA', 'METROPOLIS', 'LAXMIMACH', 'CYIENT', 'JSL', 'GALAXYSURF', 'BLUESTARCO', 'BDL', 'CESC', 'BALRAMCHIN', 'CASTROLIND', 'MASTEK', 'RHIM', 'ASTERDM', 'IDFC', 'GRAPHITE', 'QUESS', 'KEC', 'ROUTE', 'EIHOTEL', 'MANAPPURAM', 'FINPIPE', 'ZYDUSWELL', 'CENTURYTEX', 'CUB', 'SAPPHIRE', 'BALAMINES', 'ERIS', 'VGUARD', 'SAREGAMA', 'SHYAMMETL', 'JSLHISAR', 'AMARAJABAT', 'POLYMED', 'BIRLACORPN', 'ITI', 'WELSPUNIND', 'STLTECH', 'NETWORK18', 'ELGIEQUIP', 'DELTACORP', 'ALLCARGO', 'FSL', 'SUPPETRO', 'AKZOINDIA', 'NLCINDIA', 'GODREJAGRO', 'LATENTVIEW', 'FACT', 'SUZLON', 'CANFINHOME', 'NIITLTD', 'ZENSARTECH', 'ANURAS', 'MAPMYINDIA', 'EIDPARRY', 'ECLERX', 'KNRCON', 'VMART', 'SPARC', 'RBLBANK', 'SONATSOFTW', 'MGL', 'SYMPHONY', 'INDIGOPNTS', 'POLYPLEX', 'GRANULES', 'RENUKA', 'BEML', 'BORORENEW', 'TRIVENI', 'TEAMLEASE', 'EASEMYTRIP', 'IBULHSGFIN', 'PRIVISCL', 'PRAJIND', 'MRPL', 'SUNCLAYLTD', 'AEGISCHEM', 'GREENPANEL', 'JUBLINGREA', 'SIS', 'PRINCEPIPE', 'TATAINVEST', 'RVNL', 'ORIENTELEC', 'DEEPAKFERT', 'HOMEFIRST', 'SOBHA', 'GMMPFAUDLR', 'PNCINFRA', 'PGHL', 'MMTC', 'LUXIND', 'GUJALKALI', 'TCIEXP', 'HUDCO', 'TRITURBINE', 'NBCC', 'RAIN', 'MAHINDCIE', 'INDIACEM', 'INOXLEISUR', 'CERA', 'GSFC', 'JMFINANCIL', 'EQUITASBNK', 'SUNTECK', 'ASTRAZEN', 'RTNINDIA', 'PNBHOUSING', 'RITES', 'PSB', 'CHALET', 'JUBLPHARMA', 'VAIBHAVGBL', 'EPL', 'MAHLIFE', 'KALYANKJIL', 'GMDCLTD', 'SWSOLAR', 'BBTC', 'GAEL', 'JUSTDIAL', 'GARFIBRES', 'PRSMJOHNSN', 'FINCABLES', 'RAYMOND', 'JINDWORLD', 'GLS', 'AVANTIFEED', 'JKLAKSHMI', 'SHARDACROP', 'EDELWEISS', 'OLECTRA', 'GOCOLORS', 'KALPATPOWR', 'GPIL', 'JYOTHYLAB', 'MTARTECH', 'SCI', 'CCL', 'NAZARA', 'HEG', 'VARROC', 'GODFRYPHLP', 'GHCL', 'INFIBEAM', 'JBMA', 'SHOPERSTOP', 'JKPAPER', 'CAPLIPOINT', 'TATVA', 'GESHIP', 'BHARATRAS', 'INGERRAND', 'LEMONTREE', 'ROSSARI', 'CRAFTSMAN', 'RBA', 'HIKAL', 'MINDACORP', 'RCF', 'BARBEQUE', 'TEJASNET', 'JINDALPOLY', 'RESPONIND', 'MAZDOCK', 'JCHAC', 'KRBL', 'SWANENERGY', 'SUPRAJIT', 'VSTIND', 'TCNSBRANDS', 'JPPOWER', 'ESABINDIA', 'TCI', 'RALLIS', 'IBREALEST', 'MHRIL', 'KSB', 'RPOWER', 'JSWHL', 'PDSL', 'VIJAYA', 'GREAVESCOT', 'GLOBUSSPR', 'UFLEX', 'GREENLAM', 'MOIL', 'WELCORP', 'VRLLOG', 'NEOGEN', 'FDC', 'PCBL', 'HEIDELBERG', 'HGS', 'IFBIND', 'MAHSCOOTER', 'TINPLATE', 'RELIGARE', 'NOCIL', 'THYROCARE', 'USHAMART', 'ICRA', 'SARDAEN', 'CMSINFO', 'TATACOFFEE', 'MFL', 'SHAREINDIA', 'AARTIDRUGS', 'SUPRIYA', 'JAMNAAUTO', 'DALMIASUG', 'NESCO', 'MANINFRA', 'COCHINSHIP', 'MAITHANALL', 'LAOPALA', 'WOCKPHARMA', 'BOROLTD', 'ISGEC', 'CEATLTD', 'ARVINDFASN', 'HCG', 'DHANI', 'IRCON', 'TARSONS', 'KARURVYSYA', 'MAHSEAMLES', 'STARCEMENT', 'GPPL', 'VAKRANGEE', 'CSBBANK', 'AMIORG', 'DATAPATTNS', 'EQUITAS', 'HGINFRA', 'MAHLOG', 'SUDARSCHEM', 'ENGINERSIN', 'RATEGAIN', 'NCC', 'DHAMPURSUG', 'DBL', 'SANSERA', 'RUPA', 'INDOCO', 'SHILPAMED', 'ASTEC', 'ROLEXRINGS', 'SEAMECLTD', 'PAISALO', 'DHANUKA', 'GATEWAY', 'BANARISUG', 'SEQUENT', 'HEMIPROP', 'NEWGEN', 'ITDC', 'TATASTLLP', 'KSCL', 'AHLUCONT', 'ADVENZYMES', 'COSMOFILMS', 'ICIL', 'INDIAGLYCO', 'DOLLAR', 'TEGA', 'HSCL', 'STAR', 'MIDHANI', 'IPL', 'HATHWAY', 'NILKAMAL', 'VENKEYS', 'J&KBANK', 'DISHTV', 'ARVIND', 'RSYSTEMS', 'HIL', 'RELINFRA', 'MASFIN', 'ORIENTCEM', 'HINDOILEXP', 'DCAL', 'SAGCEM', 'JKTYRE', 'JINDALSAW', 'RTNPOWER', 'ACE', 'FILATEX', 'SCHNEIDER', 'TIPSINDLTD', 'TASTYBITE', 'SOMANYCERA', 'OPTIEMUS', 'PFOCUS', 'TECHNOE', 'TIRUMALCHM', 'SELMC', 'RAILTEL', 'CARTRADE', 'GREENPLY', 'IIFLSEC', 'DODLA', 'MOL', 'SHIL', 'RAJRATAN', 'INDOSTAR', 'NFL', 'GRSE', 'THOMASCOOK', 'AUTOAXLES', 'UJJIVANSFB', 'DBREALTY', 'EKC', 'KIRIINDUS', 'PURVA', 'SSWL', 'ANANDRATHI', 'RKFORGE', 'VALIANTORG', 'DAAWAT', 'APARINDS', 'BUTTERFLY', 'BBOX', 'INOXWIND', 'PARAS', 'IONEXCHANG', 'TATAMETALI', 'EVEREADY', 'PTC', 'JISLJALEQS', 'HERANBA', 'GUFICBIO', 'TIIL', 'BLS', 'BAJAJCON', 'ASHOKA', 'SOLARA', 'GOKEX', 'HCC', 'OAL', 'DWARKESH', 'GET&D', 'IFCI', 'AMRUTANJAN', 'POKARNA', 'HESTERBIO', 'MOLDTKPAC', 'SURYAROSNI', 'KIRLOSBROS', 'IMFA', 'SHARDAMOTR', 'GANESHHOUC', 'TVTODAY', 'ACRYSIL', 'WSTCSTPAPR', 'GRAVITA', 'SAFARI', 'JAYNECOIND', 'IGPL', 'DCBBANK', 'MSTCLTD', 'KOLTEPATIL', 'SUBROS', 'SPANDANA', 'GULFOILLUB', 'BEPL', 'STEELXIND', 'FINOPB', 'VIDHIING', 'IOLCP', 'VSTTILLERS', 'ANDHRSUGAR', 'VESUVIUS', 'NBVENTURES', 'ATFL', 'MMFL', 'JPASSOCIAT', 'BOMDYEING', 'SHK', 'GMRP&UI', 'NAVNETEDUL', 'GATI', 'STOVEKRAFT', 'FCL', 'MUKANDLTD', 'AVTNPL', 'VOLTAMP', 'SBCL', 'SIYSIL', 'FAIRCHEMOR', 'JAICORPLTD', 'GTPL', 'ASTRAMICRO', 'ANANTRAJ', 'PSPPROJECT', 'TIDEWATER', 'MIRZAINT', 'BALMLAWRIE', 'HSIL', 'VISHNU', 'KIRLOSENG', 'APOLLOPIPE', 'CHENNPETRO', 'GTLINFRA', 'PILANIINVS', 'MANALIPETC', 'MARKSANS', 'APCOTEXIND', 'ALEMBICLTD', 'NAHARSPING', 'GENUSPOWER', 'UNICHEMLAB', 'RAMCOIND', 'BAJAJHIND', 'SUBEXLTD', 'JTEKTINDIA', 'SHANKARA', 'GENESYS', 'PUNJABCHEM', 'CAMLINFINE', 'CONFIPET', 'DATAMATICS', 'DEN', 'HBLPOWER', 'INFOBEAN', 'WABAG', 'XPROINDIA', 'STYLAMIND', 'KTKBANK', 'EXCELINDUS', 'INDORAMA', 'EXPLEOSOL', 'INEOSSTYRO', 'JAGRAN', 'ORISSAMINE', 'ELECTCAST', 'FRETAIL', 'LGBBROSLTD', 'KABRAEXTRU', 'KITEX', 'BECTORFOOD', 'GOLDIAM', 'MOREPENLAB', 'NELCO', 'RGL', 'GULPOLY', 'ZENTEC', 'GRWRHITECH', 'DIAMONDYD', 'ELECON', 'GABRIEL', 'NACLIND', 'PANAMAPET', 'MAYURUNIQ', 'SWARAJENG', 'GANECOS', 'PRICOLLTD', 'SOUTHBANK', 'ADFFOODS', 'SHRIPISTON', 'PGEL', 'RPSGVENT', 'SUNDARMHLD', 'MATRIMONY', 'KRSNAA', 'KINGFA', 'MAXVIL', 'KIRLOSIND', 'JSWISPL', 'CARERATING', 'DBCORP', 'CANTABIL', 'THANGAMAYL', 'GEOJITFSL', 'KCP', 'HERITGFOOD', 'DFMFOODS', 'HIMATSEIDE', 'FMGOETZE', 'NDTV', 'OMAXE', 'SPIC', 'AVADHSUGAR', 'SOTL', 'TIMETECHNO', 'GALLISPAT', 'MTNL', 'JYOTISTRUC', 'APTECHT', 'ASHIANA', 'ACCELYA', 'SHANTIGEAR', 'NAHARPOLY', 'SASKEN', 'NURECA', 'GOCLCORP', 'PRAKASH', 'DYNAMATECH', 'NXTDIGITAL', 'KOPRAN', 'AMBIKCO', 'JMCPROJECT', 'SHIVALIK', 'TEXRAIL', 'EIHAHOTELS', 'WONDERLA', 'NEULANDLAB', 'SHRIRAMPPS', 'SANDHAR', 'DPSCLTD', 'GMBREW', 'KSL', 'THEJO', 'SIRCA', 'KESORAMIND', 'NITINSPIN', 'SHALBY', 'JKIL', 'LSIL', 'PRECAM', 'HONDAPOWER', 'SJS', '63MOONS', 'UJJIVAN', 'BODALCHEM', 'WHEELS', 'KDDL', 'POWERMECH', 'KKCL', 'TVSSRICHAK', 'KHAICHEM', 'RAMKY', 'VINDHYATEL', 'CENTENKA', 'TWL', 'INSECTICID', 'ONMOBILE', 'HMT', 'AGSTRA', 'CIGNITITEC', 'NUCLEUS', 'ESTER', 'PATELENG', 'FIEMIND', 'SUVEN', 'RIIL', 'UGROCAP', 'TTKHLTCARE', 'SUTLEJTEX', 'ANDHRAPAP', 'ASHAPURMIN', 'ORCHPHARMA', 'BFUTILITIE', 'AJMERA', 'TNPL', 'VHL', 'COFFEEDAY', 'LUMAXTECH', 'HUHTAMAKI', 'SASTASUNDR', 'SUNFLAG', 'ORIENTHOT', 'IGARASHI', 'SANGAMIND', 'EVERESTIND', 'NRBBEARING', 'GIPCL', 'REPCOHOME', 'SESHAPAPER', 'SANGHIIND', 'WELENT', 'ITDCEM', 'TARC', 'CENTRUM', 'RUSHIL', 'BCLIND', 'PNBGILTS', 'TDPOWERSYS', 'DCW', 'MANGLMCEM', 'MPSLTD', 'ALICON', 'GOKULAGRO', 'CLNINDIA', 'GNA', 'TI', 'ZEEMEDIA', 'PITTIENG', 'QUICKHEAL', 'TNPETRO', 'BFINVEST', 'MANGCHEFER', 'SATIA', 'GEPIL', 'VISAKAIND', '5PAISA', 'VADILALIND', 'WENDT', 'KPIGLOBAL', 'MONTECARLO', 'PFS', 'UNIDT', 'SHREDIGCEM', 'NAHARCAP', 'EMAMIPAP', 'BBL', 'CHEMCON', 'BANCOINDIA', 'PCJEWELLER', 'BHAGERIA', 'ENIL', 'RSWM', 'INDNIPPON', 'TAJGVK', 'CEREBRAINT', 'IMPAL', 'SAKSOFT', 'BAJAJHCARE', 'SURYODAY', 'IFGLEXPOR', 'UNIENTER', 'ASAL', 'RPGLIFE', 'VSSL', 'PARAGMILK', 'PGIL', 'GREENPOWER', 'NSIL', 'URJA', 'FCONSUMER', 'PANACEABIO', 'DHARAMSI', 'HEXATRADEX', 'NDL', 'JETAIRWAYS', 'XCHANGING', 'RADIOCITY', 'AGARIND', 'SIGACHI', 'MBAPL', 'SMCGLOBAL', 'FOSECOIND', 'DREDGECORP', 'PRECWIRE', 'SPAL', 'APEX', 'ARVSMART', 'CREATIVE', 'GFLLIMITED', 'INDIANHUME', 'SHREEPUSHK', 'THEMISMED', '3IINFOLTD', 'ASALCBR', 'SHALPAINTS', 'ADORWELD', 'BHAGCHEM', 'SHAKTIPUMP', 'ARMANFIN', 'RANEHOLDIN', 'DPABHUSHAN', 'LUMAXIND', 'UTTAMSUGAR', 'ARIHANTCAP', 'KRISHANA', 'JAGSNPHARM', 'SHREYAS', 'RAMCOSYS', 'SRHHYPOLTD', 'KELLTONTEC', 'NCLIND', 'DVL', 'DCMSRIND', 'BLISSGVS', 'OCCL', 'MADRASFERT', 'SANGHVIMOV', 'ALLSEC', 'SMSPHARMA', 'ONWARDTEC', 'ANUP', 'MEDICAMEQ', 'IWEL', 'DECCANCE', 'NAGAFERT', 'HTMEDIA', 'UGARSUGAR', 'MANORG', 'SATIN', 'SPECIALITY', 'ARSHIYA', 'ZOTA', 'JAYAGROGN', 'AURIONPRO', 'CAPACITE', 'AWHCL', 'SEPC', 'RCOM', 'ISMTLTD', 'ORIENTBELL', 'DEEPINDS', 'TEXINFRA', 'ORIENTPPR', 'SPENCERS', 'GOODLUCK', 'HPAL', 'BALAJITELE', 'SMLISUZU', 'ROSSELLIND', 'DIGISPICE', 'GICHSGFIN', 'STEELCAS', 'JUBLINDS', 'KUANTUM', 'VIMTALABS', 'FLFL', 'JINDRILL', 'KICL', 'FCSSOFT', 'YUKEN', 'DYNPRO', 'TCPLPACK', 'NAHARINDUS', 'PARSVNATH', 'SUMMITSEC', 'BIGBLOC', 'EQUIPPP', 'IFBAGRO', 'GANESHBE', 'RAJMET', 'LINCOLN', 'KAMDHENU', 'ADSL', 'VLSFINANCE', 'JAYBARMARU', 'HCL-INSYS', 'JASH', 'ARTEMISMED', 'SALASAR', 'HLVLTD', 'UNIVPHOTO', 'BLKASHYAP', 'MONARCH', 'KANORICHEM', 'BGRENERGY', 'KOKUYOCMLN', 'HITECH', 'APCL', 'BINDALAGRO', 'CONTROLPR', 'STCINDIA', 'CENTUM', 'KBCGLOBAL', 'THEINVEST', 'SWELECTES', 'LIKHITHA', 'RML', 'AARTISURF', 'AYMSYNTEX', 'ZUARI', 'ASIANTILES', 'TALBROAUTO', 'SVPGLOB', 'INTLCONV', 'SKIPPER', 'SOUTHWEST', 'SHYAMCENT', 'MANINDS', 'NBIFIN', 'MARATHON', 'BETA', 'TFCILTD', 'SUULD', 'ARIHANTSUP', 'NECLIFE', 'RUBYMILLS', 'MGEL', 'INDRAMEDCO', 'KRITI', 'RAMASTEEL', 'UNITECH', 'ZUARIGLOB', 'DELPHIFX', 'EXXARO', 'MAWANASUG', 'CREST', 'PLASTIBLEN', 'NELCAST', 'BBTCL', 'SNOWMAN', 'VASCONEQ', 'KOTHARIPET', 'CLSEL', 'V2RETAIL', 'REPRO', 'BASML', 'MMP', 'MENONBE', 'DLINKINDIA', 'SANDESH', 'YAARI', 'ORICONENT', 'VIKASLIFE', 'VIKASLIFE', 'PENIND', 'GALLANTT', 'STERTOOLS', 'JAIBALAJI', 'MANAKSIA', 'VINYLINDIA', 'CYBERTECH', 'NAVKARCORP', 'AXISCADES', 'TVSELECT', 'GOACARBON', 'RBL', 'SARLAPOLY', 'MALLCOM', 'BIRLACABLE', 'INNOVANA', 'INDOBORAX', 'SREEL', 'WINDLAS', 'KAYA', 'TBZ', 'SADBHAV', 'NRAIL', 'GANDHITUBE', 'HMVL', 'SEJALLTD', 'CONSOFINVT', 'HERCULES', 'MAGADSUGAR', 'DPWIRES', 'UNIVCABLES', 'RANASUG', 'MIRCELECTR', 'PTL', 'DUCON', 'TRIL', 'SDBL', 'GAYAPROJ', 'ASIANENE', 'DCMNVL', 'VISESHINFO', 'VARDHACRLC', 'BHARATWIRE', 'ANDHRACEMT', 'TAKE', 'MUTHOOTCAP', 'RICOAUTO', 'ADVANIHOTR', 'FOODSIN', 'RELCAPITAL', 'KSOLVES', 'TRIGYN', 'LINC', 'MSPL', 'BSHSL', 'HPL', 'COASTCORP', 'MUNJALAU', 'NATHBIOGEN', 'ZEELEARN', 'XELPMOC', 'HITECHGEAR', 'GODHA', 'KHADIM', 'OMINFRAL', 'MAXIND', 'INDOTHAI', 'INDSWFTLAB', 'MUNJALSHOW', 'HITECHCORP', 'CEBBCO', 'HINDCOMPOS', 'LYKALABS', 'UFO', 'KNAGRI', 'JPINFRATEC', 'KOTHARIPRO', 'DHUNINV', 'VISHWARAJ', 'PRECOT', 'MEGASOFT', 'MARINE', 'GINNIFILA', 'REPL', 'PPL', 'PDMJEPAPER', 'SHEMAROO', 'SHIVAMAUTO', 'OSWALAGRO', 'BANSWRAS', 'PRAXIS', 'ACCURACY', 'VENUSREM', 'GENUSPAPER', 'GSCLCEMENT', 'ATULAUTO', 'ORIENTABRA', 'CLEDUCATE', 'CHEMFAB', 'MEP', 'SILINV', 'BALAXI', 'NRL', 'HDIL', 'SPTL', 'PASUPTAC', 'WEBELSOLAR', 'ASAHISONG', 'AURUM', 'DIL', 'VIKASECO', 'MARALOVER', 'SCHAND', 'BIRLAMONEY', 'PREMEXPLN', 'HUBTOWN', 'ORBTEXP', 'ROHLTD', 'MINDTECK', 'DANGEE', 'PROZONINTU', 'IRISDOREME', 'GKWLIMITED', 'SADBHIN', 'CUPID', 'DICIND', 'GOKUL', 'PODDARMENT', 'PENINLAND', 'GEECEE', 'DHANBANK', 'ROHITFERRO', 'KREBSBIO', 'MAHESHWARI', 'BPL', 'HIRECT', 'BIL', 'ALBERTDAVD', 'JPOLYINVST', 'INVENTURE', 'CINELINE', 'BAFNAPH', 'EMKAYTOOLS', 'EROSMEDIA', 'BIRLATYRE', 'NGIL', 'KOTARISUG', 'SALZERELEC', 'NIPPOBATRY', 'PENTAGOLD', 'KOTYARK', 'RUCHIRA', 'WEALTH', 'EIFFL', 'SELAN', 'AKSHARCHEM', 'PRIMESECU', 'MANAKSTEEL', 'KCPSUGIND', 'SRPL', 'ISFT', 'WANBURY', 'SAKUMA', 'DONEAR', 'DTIL', 'SIMPLEXINF', 'AHLEAST', 'EUROBOND', 'ASHIMASYN', 'ABAN', 'JINDALPHOT', 'KMSUGAR', 'JAYSREETEA', 'PPAP', 'FEL', 'GOLDTECH', 'SHIVATEX', 'SECURKLOUD', 'KILITCH', '20MICRONS', 'KANPRPLA', 'SILVERTUC', 'EMKAY', 'LGBFORGE', 'SREINFRA', 'WINDMACHIN', 'ALMONDZ', 'MBLINFRA', 'JITFINFRA', 'MAHEPC', 'SGIL', 'HINDMOTORS', 'AAKASH', 'RAMANEWS', 'REFEX', 'LIBERTSHOE', 'ZODIACLOTH', 'SITINET', 'STARPAPER', 'UCALFUEL', 'APOLLO', 'GUJAPOLLO', 'HARRMALAYA', 'ARTNIRMAN', 'BRNL', 'CHEMBOND', 'MCLEODRUSS', 'DSSL', 'SINTERCOM', 'NDRAUTO', 'SIGMA', 'PIONDIST', 'RNAVAL', 'SAKAR', 'GULFPETRO', 'INDOTECH', 'INSPIRISYS', 'PANSARI', 'EMAMIREAL', 'ANMOL', 'MOLDTECH', 'MACPOWER', 'ONEPOINT', 'AIRAN', 'GIRRESORTS', 'BEDMUTHA', 'NILAINFRA', 'TEXMOPIPES', 'SORILINFRA', 'KANANIIND', 'GPTINFRA', 'TTL', 'VIPULLTD', 'MODISNME', 'WFL', 'APOLSINHOT', 'DENORA', 'STEL', 'SMSLIFE', 'SPMLINFRA', 'IVC', 'ANSALAPI', 'RPPL', 'PILITA', 'BEWLTD', 'SHIGAN', 'FSC', 'MADHAVBAUG', 'REVATHI', 'AUTOIND', 'RAJTV', 'OSIAHYPER', 'BRFL', 'LOVABLE', 'CAREERP', 'TEMBO', 'ASTRON', 'SHAHALLOYS', 'INDTERRAIN', 'COMPINFO', 'ELGIRUBCO', 'PONNIERODE', 'ALPHAGEO', 'PAR', 'MAZDA', 'GSS', 'IRIS', 'VIPCLOTHNG', 'RUCHINFRA', 'WALCHANNAG', 'PASHUPATI', 'CAPTRUST', 'ALANKIT', 'SPLIL', 'PARACABLES', 'INTENTECH', 'RHFL', 'GRPLTD', 'SETCO', 'TPLPLASTEH', 'IITL', 'MAANALU', 'KERNEX', 'EIMCOELECO', 'BROOKS', 'SUPERHOUSE', 'VISASTEEL', 'ARIES', 'SUNDARAM', 'AJRINFRA', 'COMPUSOFT', 'KECL', 'VETO', 'E2E', 'GTL', 'MODIRUBBER', 'KAKATCEM', 'JOCIL', 'AARVI', 'MANAKCOAT', 'INDIANCARD', 'LASA', 'A2ZINFRA', 'UNITEDTEA', 'PAVNAIND', 'SERVOTECH', 'DEEPENR', 'HINDNATGLS', 'IL&FSTRANS', 'SHREYANIND', 'KAMATHOTEL', 'NITCO', 'GOLDENTOBC', 'NECCLTD', 'AKSHOPTFBR', 'SUVIDHAA', 'MANGALAM', 'WORTH', 'SKMEGGPROD', 'RANEENGINE', 'BALPHARMA', 'SAKHTISUG', 'PREMIERPOL', 'ATLANTA', 'JAINAM', 'NILASPACES', 'MANAKALUCO', 'IVP', 'ASIANHOTNR', 'ESSARSHPNG', 'DCM', 'INDOWIND', 'LAGNAM', '3RDROCK', 'EMMBI', 'ICEMAKE', 'RPPINFRA', 'CORALFINAC', 'SHRENIK', 'JMA', 'BALLARPUR', 'BYKE', 'TRF', 'ARROWGREEN', 'BHARATGEAR', 'ALPA', 'PALREDTEC', 'IL&FSENGG', 'DEVIT', 'ELECTHERM', 'GILLANDERS', 'BHAGYANGR', 'SPECTRUM', 'DAMODARIND', 'SURANAT&P', 'MURUDCERA', 'NOIDATOLL', 'LOKESHMACH', 'PODDARHOUS', 'GENCON', 'SHIVAUM', 'ASPINWALL', 'UMANGDAIRY', 'SUNDRMBRAK', 'RVHL', 'GLOBE', 'GANGESSECU', 'JHS', 'PRITIKAUTO', 'ZODIAC', 'SURYALAXMI', 'MAHAPEXLTD', 'INDOSOLAR', 'AHLADA', 'NDGL', 'SMLT', 'MHLXMIRU', 'MEGASTAR', 'AMJLAND', 'PIONEEREMB', 'ANKITMETAL', 'ARVEE', 'CTE', 'MITCON', 'CCHHL', 'VIVIMEDLAB', 'PVP', 'NIRAJ', 'VCL', 'UNITEDPOLY', 'DUGLOBAL', 'TCIDEVELOP', 'GROBTEA', 'SBC', 'SALONA', 'IMAGICAA', 'RKEC', 'BLBLIMITED', 'BSL', 'PRAENG', 'AARON', 'SMARTLINK', 'DRSDILIP', 'SIGIND', 'IZMO', 'FIBERWEB', 'LOTUSEYE', 'PALASHSECU', 'BAGFILMS', 'RAJSREESUG', 'BHANDARI', 'JBFIND', 'VERTOZ', 'AKASH', 'SARVESHWAR', 'MUKTAARTS', 'AAREYDRUGS', 'ABMINTLLTD', 'TIRUPATIFL', 'KAPSTON', 'SURANASOL', 'SOFTTECH', 'REMSONSIND', 'BHAGYAPROP', 'MAHASTEEL', 'MOTOGENFIN', 'AIROLAM', 'TIL', 'SECL', 'TOTAL', 'FOCE', 'ENERGYDEV', 'AVG', 'PARIN', 'TOUCHWOOD', 'ROML', 'INCREDIBLE', 'WEIZMANIND', 'PKTEA', 'PRESSMN', 'UNIVASTU', 'WELINV', 'INDBANK', 'LPDC', 'GOENKA', 'MRO-TEK', 'BIOFILCHEM', 'SIMBHALS', 'MICEL', 'SOLEX', 'SGL', 'OMAXAUTO', 'LAMBODHARA', 'PRAKASHSTL', 'DBSTOCKBRO', 'SEPOWER', 'DHRUV', 'AUSOMENT', 'STEELCITY', 'SHIVAMILLS', 'FOCUS', 'AMDIND', 'MBECL', 'CCCL', 'KRISHIVAL', 'SVLL', 'OSWALSEEDS', 'SEYAIND', 'TOKYOPLAST', 'VMARCIND', 'ROLTA', 'SALSTEEL', 'BANKA', 'AROGRANITE', 'UJAAS', 'CENTEXT', 'GANGAFORGE', 'SANWARIA', 'ALKALI', 'MCL', 'TREJHARA', 'TARMAT', 'MKPL', 'ANIKINDS', 'RSSOFTWARE', 'MOKSH', 'JETFREIGHT', 'SHREERAMA', 'ARCHIDPLY', 'SUMEETINDS', 'SIL', 'CINEVISTA', 'KEYFINSERV', 'MORARJEE', 'NITIRAJ', 'SAMBHAAV', 'DELTAMAGNT', 'BCONCEPTS', 'TIRUPATI', 'AGRITECH', 'SONAMCLOCK', 'PUNJLLOYD', 'HINDCON', 'AMBANIORG', 'GLOBAL', 'VAISHALI', 'PRECISION', 'GEEKAYWIRE', 'MAHICKRA', 'URAVI', 'SICAL', 'PNC', 'UTTAMSTL', 'TARACHAND', 'PROLIFE', 'CELEBRITY', 'AJOONI', 'HISARMETAL', 'DGCONTENT', 'PRITI', 'NIBL', 'KRITIKA', 'SUPREMEENG', 'SAGARDEEP', 'ORIENTLTD', 'CORDSCABLE', 'JAKHARIA', 'TAINWALCHM', 'BMETRICS', 'EXCEL', 'GLOBALVECT', 'KALYANIFRG', 'SUPERSPIN', 'LEXUS', 'VINNY', 'AVROIND', 'BANARBEADS', 'SIKKO', 'OMKARCHEM', 'PANACHE', 'INDSWFTLTD', 'ARCHIES', 'VASWANI', 'MALUPAPER', 'BEARDSELL', 'AAATECH', 'SECURCRED', 'BDR', 'HPIL', 'MTEDUCARE', 'JAIPURKURT', 'AURDIS', 'MERCATOR', 'AARVEEDEN', 'TERASOFT', 'FLEXITUFF', 'GAL', 'HOVS', 'CALSOFT', 'DHARSUGAR', 'BURNPUR', 'PARTYCRUS', 'ARSSINFRA', 'VARDMNPOLY', 'ICDSLTD', 'ATALREAL', 'EASTSILK', 'SHRADHA', 'ZENITHEXPO', 'BALKRISHNA', 'MDL', 'NPST', 'WEWIN', 'KKVAPOW', 'BVCL', 'MHHL', 'DCI', 'ROLLT', 'TIMESGTY', 'MARSHALL', 'CMICABLES', 'WIPL', 'CYBERMEDIA', 'COOLCAPS', 'AISL', 'VIVIDHA', 'KHFM', 'AGROPHOS', 'MRO', 'MADHAV', 'FMNL', 'NAGREEKEXP', 'NIDAN', 'AMBICAAGAR', 'ABCOTS', 'LCCINFOTEC', 'KRIDHANINF', 'VINEETLAB', 'HAVISHA', 'COUNCODOS', 'BANG', 'EDUCOMP', 'LIBAS', 'RELIABLE', 'MADHUCON', 'MAGNUM', 'ANSALHSG', 'OILCOUNTUB', 'UCL', 'HILTON', 'JETKNIT', 'MANUGRAPH', 'AKG', 'ASLIND', 'SOMICONVEY', 'SHAIVAL', 'SURANI', 'DIGJAMLMTD', 'SWARAJ', 'KARMAENG', 'SANGINITA', 'HECPROJECT', 'PIGL', 'HBSL', 'SUMIT', 'GIRIRAJ', 'MILTON', 'CROWN', 'TREEHOUSE', 'ORIENTALTL', 'PATINTLOG', 'SETUINFRA', 'CUBEXTUB', 'REXPIPES', 'TMRVL', 'SUPREMEINF', 'LAXMICOT', 'SSINFRA', 'VSCL', 'DKEGL', 'NEXTMEDIA', 'KSHITIJPOL', 'TIMESCAN', 'VIVO', 'VIJIFIN', '21STCENMGM', 'PEARLPOLY', 'CADSYS', 'SILGO', 'LGHL', 'LFIC', 'SONAHISONA', 'DNAMEDIA', 'MOHITIND', 'INFOMEDIA', 'GOLDSTAR', 'NARMADA', 'TGBHOTELS', 'ACEINTEG', 'SHANTI', '3PLAND', 'ASCOM', 'LATTEYS', 'ADL', 'TANTIACONS', 'KHANDSE', 'ZENITHSTL', 'SOMATEX', 'UNIINFO', 'RKDL', 'RICHA', 'WILLAMAGOR', 'SILLYMONKS', 'QUADPRO', 'METALFORGE', 'ANTGRAPHIC', 'JALAN', 'GICL', 'MITTAL', 'SIDDHIKA', 'SPENTEX', 'AVSL', 'ADROITINFO', 'DYNAMIC', 'UWCSL', 'RMCL', 'KAVVERITEL', 'PULZ', 'MPTODAY', 'TFL', 'NKIND', 'GUJRAFFIA', 'TNTELE', 'BARTRONICS', 'ORTINLAB', 'TIJARIA', 'PBAINFRA', 'BTML', 'KEERTI', 'TECHIN', 'KHAITANLTD', 'IMPEXFERRO', 'LYPSAGEMS', 'BKMINDST', 'THOMASCOTT', 'SUBCAPCITY', 'ONELIFECAP', 'PREMIER', 'SPRL', 'S&SPOWER', 'CMMIPL', 'VICEROY', 'ALPSINDUS', 'ABINFRA', 'VERA', 'KAUSHALYA', 'WALPAR', 'KALYANI', 'BRIGHT', 'NAGREEKCAP', 'SHUBHLAXMI', 'SANCO', 'UMESLTD', 'INDLMETER', 'MASKINVEST', 'SHYAMTEL', 'CONTI', 'INNOVATIVE', 'MINDPOOL', 'ARENTERP', 'RMDRIP', 'RADAAN', 'PERFECT', 'DRL', 'AHIMSA', 'BLUECOAST', 'DESTINY', 'CANDC', 'ABNINT', 'ACCORD', 'FELIX', 'GLFL', 'SRIRAM', 'CREATIVEYE', 'EASUNREYRL', 'TARAPUR', 'SMVD', 'OMFURN', 'NORBTEAEXP', 'TCIFINANCE', 'SABEVENTS', 'SKSTEXTILE', 'PAEL', 'NIRAJISPAT', 'DCMFINSERV', 'LAKPRE', 'AMJUMBO', 'SABTN', 'AILIMITED', 'HOTELRUGBY', 'BHALCHANDR', 'MELSTAR', 'MANAV', 'GRETEX', 'TRANSWIND', 'JAINSTUDIO', 'RAJRILTD', 'ABHISHEK', 'ABMINTLTD', 'AHLWEST', 'AIFL', 'ALCHEM', 'ARCOTECH', 'ASIL', 'ATCOM', 'ATLASCYCLE', 'ATNINTER', 'AUSTRAL', 'AUTOLITIND', 'BGLOBAL', 'BHARATIDIL', 'BILENERGY', 'BINANIIND', 'BLUEBLENDS', 'BLUECHIP', 'CELESTIAL', 'CHROMATIC', 'CKFSL', 'COX&KINGS', 'DALALSTCOM', 'DIAPOWER', 'DOLPHINOFF', 'DQE', 'DRCSYSTEMS', 'DSKULKARNI', 'EASTSUGIND', 'EMCO', 'EON', 'ESSENTIA', 'EUROCERA', 'EUROMULTI', 'EUROTEXIND', 'FEDDERELEC', 'GAMMONIND', 'GANGOTRI', 'GAYAHWS', 'GBGLOBAL', 'GFSTEELS', 'GISOLUTION', 'GITANJALI', 'GVKPIL', 'ICSA', 'IVRCLINFRA', 'JIKIND', 'JINDCOT', 'JMTAUTOLTD', 'KGL', 'KOHINOOR', 'KSERASERA', 'KSK', 'LAKSHMIEFL', 'LEEL', 'MAFATLAFIN', 'MANPASAND', 'MCDHOLDING', 'METKORE', 'MODTHREAD', 'MOHOTAIND', 'MUKANDENGG', 'MVL', 'NAKODA', 'NATNLSTEEL', 'NITINFIRE', 'NTL', 'NUTEK', 'OISL', 'OPTOCIRCUI', 'ORTEL', 'PARASPETRO', 'PDPL', 'PINCON', 'PRATIBHA', 'PRUDMOULI', 'PSL', 'QUINTEGRA', 'RAINBOWPAP', 'RAJVIR', 'RAMSARUP', 'REGENCERAM', 'RMMIL', 'RUSHABEAR', 'SATHAISPAT', 'SBIHOMEFIN', 'SHARONBIO', 'SHIRPUR-G', 'SINTEX', 'SKIL', 'SPCENET', 'SPYL', 'STAMPEDE', 'STERLINBIO', 'TALWALKARS', 'TALWGYM', 'TECHNOFAB', 'TECILCHEM', 'THIRUSUGAR', 'TULSI', 'TVVISION', 'UNIPLY', 'UNITY', 'VALECHAENG', 'VALUEIND', 'VIDEOIND', 'VISUINTL', 'WINSOME', 'WSI', 'ZICOM', 'ARTEDZ', 'BANSAL', 'BOHRA', 'CKPLEISURE', 'FIVECORE', 'FOURTHDIM', 'OPAL', 'POWERFUL', 'SIIL', 'SONISOYA'))
    stock = stock.upper()

    d = st.date_input(
     "Start Date",
     datetime.date(2015, 7, 6))

    option = st.selectbox(
     'what will be the time interval',
     ('monthly', 'weekly','daily'))

    yahoo_financials = YahooFinancials('{}.NS'.format(stock))
    data = yahoo_financials.get_historical_price_data(start_date=str(d), 
                                                  end_date=str(today), 
                                                  time_interval=option)

    df = pd.DataFrame(data['{}.NS'.format(stock)]['prices'])
    df = df.drop('date', axis=1).set_index('formatted_date')

    daily = yahoo_financials.get_historical_price_data(start_date=str(d), 
                                                  end_date=str(today), 
                                                  time_interval='daily')

    df_metrics = pd.DataFrame(daily['{}.NS'.format(stock)]['prices'])
    df_metrics = df_metrics.drop('date', axis=1).set_index('formatted_date')

    df_metrics = df_metrics.tail()
    
    with st.sidebar:
        st.metric(label="high", value=df_metrics['high'][4], delta=(df_metrics['high'][4] - df_metrics['high'][3]))
        st.metric(label="low", value=df_metrics['low'][4], delta=(df_metrics['low'][4] - df_metrics['low'][3]))
        st.metric(label="volume", value=df_metrics['volume'][4], delta=(int(df_metrics['volume'][4] - df_metrics['volume'][3])))

    if st.button('Show chart'):

        fig = plt.figure(figsize=(40,60))
        ax = sns.pointplot(df.index, df['close'],color = 'blue', label = "close")
        ax = sns.pointplot(df.index, df['open'],color = 'red', label = "open")
        ax = sns.pointplot(df.index, df['high'],color = 'green', label = "high")
        ax = sns.pointplot(df.index, df['low'],color = 'yellow', label = "low")
        ax.legend()
        plt.xlabel("date")
        plt.ylabel("price")
        plt.title("tata motors stock price")      
        st.write("""### Historic trend of {} from {}""".format(stock,d))
        st.pyplot(fig)
                                         
