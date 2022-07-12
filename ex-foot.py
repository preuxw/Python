import doctest
import csv
from collections import defaultdict

FILENAME = './data/ligue1_1718.csv'


def read_data(filename):
    """
    Args:
        filename (str) : the file name containing data

    Returns:
        list: a list of dict. One per file row except the first one used for key definition

    >>> raw_data = read_data('./data/ligue1_1718.csv')
    >>> type(raw_data)
    <class 'list'>
    >>> len(raw_data)
    380
    >>> type(raw_data[0])
    <class 'dict'>
    >>> len(raw_data[0])
    22
    >>> raw_data[10].get("Date")
    '110817'
    >>> raw_data[20].get("HomeTeam")
    'Metz'
    >>> raw_data[30].get("AwayTeam")
    'St Etienne'
    >>> raw_data[40].get("FTHG")
    '0'
    >>> raw_data[50].get("FTAG")
    '1'
    >>> raw_data[60].get("FTR")
    'A'
    >>> raw_data[70].get("HTHG")
    '1'
    >>> raw_data[80].get("HTAG")
    '0'
    >>> raw_data[90].get("HTR")
    'D'
    >>> raw_data[100].get("HS")
    '12'
    >>> raw_data[110].get("HST")
    '3'
    >>> raw_data[120].get("AST")
    '3'
    >>> raw_data[130].get("HF")
    '14'
    >>> raw_data[140].get("HC")
    '3'
    >>> raw_data[150].get("AC")
    '4'
    >>> raw_data[160].get("HY")
    '3'
    >>> raw_data[170].get("AY")
    '0'
    >>> raw_data[180].get("HR")
    '0'
    >>> raw_data[190].get("AR")
    '0'

    """
    l = []

    # Your code here... use csv.DictReader()
    with open(FILENAME,'r') as f:   
        reader = csv.DictReader(f,delimiter=";") 
        for row in reader :
            l.append(dict(row))
            
    return l


def get_result(game_data):
    """extract home and away team data from a single game data

    Args:
        dict game_data : data relative to a game between home team and away team

    Returns:
        dict of dicts : key=team, value=dict(stat_key,value)
            stat_keys : Played : number of played games
                        Home : 'H' for the home team, 'A' for the away team
                        Won : 1 if won, 0 in the other cases
                        Drawn : 1 if drawn, 0 in the other cases
                        Lost : 1 if lost, 0 in the other cases
                        FTGF : Full Time Goals For
                        FTGA : Full Time Goals Against
                        HTGF : Half Time Goals For
                        HTGA : Half Time Goals Against
                        S : Shots
                        ST : Shots on Target
                        C : Corners
                        F : Fouls
                        Y : Yellow cards
                        R : Red cards

    >>> data = read_data('./data/ligue1_1718.csv')
    >>> d = data[0]
    >>> res = get_result(d)
    >>> type(res)
    <class 'collections.defaultdict'>
    >>> len(res)
    2
    >>> keys = res.keys()
    >>> 'Monaco' in keys
    True
    >>> 'Toulouse' in keys
    True
    >>> 'Bordeaux' in keys
    False
    >>> res['Monaco']['Played']
    1
    >>> res['Monaco']['Home']
    'H'
    >>> res['Monaco']['Won']
    1
    >>> res['Monaco']['Drawn']
    0
    >>> res['Monaco']['Lost']
    0
    >>> res['Monaco']['FTGF']
    3
    >>> res['Monaco']['FTGA']
    2
    >>> res['Monaco']['HTGF']
    1
    >>> res['Monaco']['HTGA']
    1
    >>> res['Monaco']['S']
    17
    >>> res['Monaco']['ST']
    7
    >>> res['Monaco']['C']
    8
    >>> res['Monaco']['F']
    12
    >>> res['Monaco']['Y']
    1
    >>> res['Monaco']['R']
    0
    >>> res['Toulouse']['Played']
    1
    >>> res['Toulouse']['Home']
    'A'
    >>> res['Toulouse']['Won']
    0
    >>> res['Toulouse']['Drawn']
    0
    >>> res['Toulouse']['Lost']
    1
    >>> res['Toulouse']['FTGF']
    2
    >>> res['Toulouse']['FTGA']
    3
    >>> res['Toulouse']['HTGF']
    1
    >>> res['Toulouse']['HTGA']
    1
    >>> res['Toulouse']['S']
    6
    >>> res['Toulouse']['ST']
    3
    >>> res['Toulouse']['C']
    2
    >>> res['Toulouse']['F']
    23
    >>> res['Toulouse']['Y']
    3
    >>> res['Toulouse']['R']
    0
    >>> d = data[10]
    >>> res = get_result(d)
    >>> res['Nice']['Home']
    'H'
    >>> res['Troyes']['Won']
    1
    >>> d = data[20]
    >>> res = get_result(d)
    >>> res['Metz']['Drawn']
    0
    >>> res['Monaco']['Drawn']
    0
    >>> d = data[30]
    >>> res = get_result(d)
    >>> res['Paris SG']['Lost']
    0
    >>> res['St Etienne']['Lost']
    1
    >>> d = data[40]
    >>> res = get_result(d)
    >>> res['Lille']['FTGF']
    0
    >>> res['Bordeaux']['FTGF']
    0
    >>> d = data[50]
    >>> res = get_result(d)
    >>> res['Toulouse']['FTGA']
    1
    >>> res['Bordeaux']['FTGA']
    0
    >>> d = data[60]
    >>> res = get_result(d)
    >>> res['Lille']['HTGF']
    0
    >>> res['Monaco']['HTGF']
    2
    >>> d = data[70]
    >>> res = get_result(d)
    >>> res['Monaco']['HTGA']
    0
    >>> res['Montpellier']['HTGA']
    1
    >>> d = data[80]
    >>> res = get_result(d)
    >>> res['Caen']['S']
    22
    >>> res['Angers']['S']
    12
    >>> d = data[90]
    >>> res = get_result(d)
    >>> res['Amiens']['ST']
    4
    >>> res['Bordeaux']['ST']
    4
    >>> d = data[100]
    >>> res = get_result(d)
    >>> res['Bordeaux']['C']
    6
    >>> res['Monaco']['C']
    2
    >>> d = data[110]
    >>> res = get_result(d)
    >>> res['Angers']['F']
    8
    >>> res['Paris SG']['F']
    13
    >>> d = data[120]
    >>> res = get_result(d)
    >>> res['Lille']['Y']
    2
    >>> res['St Etienne']['Y']
    3
    >>> d = data[130]
    >>> res = get_result(d)
    >>> res['St Etienne']['R']
    0
    >>> res['Strasbourg']['R']
    0
    """
    result = defaultdict(dict) # returned data structure will be a dict of dict

    # 1. Initialise ``home_team`` and ``away_team`` from ``game_data``
    home_team = game_data.get('HomeTeam')
    away_team = game_data.get('AwayTeam')

    result[home_team] = {
        "Played": 1,
        "Home": "H",
        "Won": int(game_data["FTR"] == "H"),
        "Drawn": int(game_data["FTR"] == "D"),
        "Lost": int(game_data["FTR"] == "A"),
        "FTGF": int(game_data["FTHG"]),
        "FTGA": int(game_data["FTAG"]),
        "HTGF": int(game_data["HTHG"]),
        "HTGA": int(game_data["HTAG"]),
        "S": int(game_data["HS"]),
        "ST": int(game_data["HST"]),
        "C": int(game_data["HC"]),
        "F": int(game_data["HF"]),
        "Y": int(game_data["HY"]),
        "R": int(game_data["HR"])
    }
    result[away_team] = {
        "Played": 1,
        "Home": "A",
        "Won": int(game_data["FTR"] == "A"),
        "Drawn": int(game_data["FTR"] == "D"),
        "Lost": int(game_data["FTR"] == "H"),
        "FTGF": int(game_data["FTAG"]),
        "FTGA": int(game_data["FTHG"]),
        "HTGF": int(game_data["HTAG"]),
        "HTGA": int(game_data["HTHG"]),
        "S": int(game_data["AS"]),
        "ST": int(game_data["AST"]),
        "C": int(game_data["AC"]),
        "F": int(game_data["AF"]),
        "Y": int(game_data["AY"]),
        "R": int(game_data["AR"])
    }

    return result    


def aggregate(raw_data, matchdays=range(1, 39)):
    """build aggregated data (matchday based) within a range

    Args:
        raw_data (list[dict] : list of dict returned by read_data()
        matchdays (Iterable[int]) : matchdays used for aggregation. Default=all

    Returns
        dict(dict) : key = team, value = dict( key = stat, value = list of stats for corresponding matchdays)

    >>> raw_data = read_data(FILENAME)
    >>> agg_data = aggregate(raw_data, matchdays=range(1,3))
    >>> type(agg_data)
    <class 'dict'>
    >>> len(agg_data)
    20
    >>> len(agg_data['Amiens']['Played'])
    2
    >>> agg_data['Amiens']['Home']
    ['A', 'H']
    >>> agg_data['Angers']['Won']
    [0, 1]
    >>> agg_data['Bordeaux']['Drawn']
    [1, 0]
    >>> agg_data['Caen']['Lost']
    [1, 1]
    >>> agg_data['Amiens']['FTGF']
    [0, 0]
    >>> agg_data['Dijon']['FTGA']
    [3, 4]
    >>> agg_data['Guingamp']['HTGF']
    [1, 0]
    >>> agg_data['Lille']['HTGA']
    [0, 0]
    >>> agg_data['Lyon']['S']
    [12, 17]
    >>> agg_data['Marseille']['ST']
    [5, 10]
    >>> agg_data['Metz']['C']
    [3, 1]
    >>> agg_data['Monaco']['F']
    [12, 12]
    >>> agg_data['Montpellier']['Y']
    [2, 3]
    >>> agg_data['Nantes']['R']
    [0, 0]
    >>> agg_data = aggregate(raw_data, matchdays=range(15,17))
    >>> agg_data['Nice']['Won']
    [1, 1]
    >>> agg_data['Paris SG']['Drawn']
    [0, 0]
    >>> agg_data['Rennes']['Lost']
    [0, 0]
    >>> agg_data['St Etienne']['FTGF']
    [0, 1]
    >>> agg_data['Strasbourg']['FTGA']
    [0, 1]
    >>> agg_data['Toulouse']['HTGF']
    [1, 0]
    >>> agg_data['Troyes']['HTGA']
    [0, 1]
    """
    agg_data = dict()

    # Your code here...

    # 1. Build teams set
    teams = []
    
    for i in matchdays:
        if raw_data[i].get('HomeTeam') not in teams :
            teams.append(raw_data[i]['HomeTeam'])
        if raw_data[i]['AwayTeam'] not in teams :
            teams.append(raw_data[i]['AwayTeam'])
    
    # 2. aggregated data will be a dict whose values are a defaultdict(list)
    agg_data = dict(defaultdict(list))
    # 3. build empty structure

    # 4. for each game
            # skip if matchday not included in matchdays
            # extract dict of team stats with ``get_result()`` 
    #       populate returned dict
    #          for team, team_stat in ...:
    #              for stat, value in ...:
    props = ['Played', 'Home', 'Won', 'Drawn', 'Lost', 'FTGF', 'FTGA', 'HTGF', 'HTGA', 'S', 'ST', 'C', 'F', 'Y', 'R']
    
    for data in raw_data:
        if int(data["Matchday"]) not in matchdays:
            continue

        results = get_result(data)

        for (k, v) in results.items():
            if k not in agg_data:
                agg_data[k] = defaultdict(list)

            for prop in props:
                agg_data[k][prop].append(v[prop])

    return agg_data


def summarize(agg_data):
    """build summarised stats (team based) from aggregated data
    
        Args:
            agg_data (dict) : aggregated data for each team

        Returns:
            dict : key=team, value = dict<stat, stat_value>

    >>> raw_data = read_data(FILENAME)
    >>> agg_data = aggregate(raw_data, matchdays=range(1,20))
    >>> sum_data = summarize(agg_data)
    >>> type(sum_data)
    <class 'collections.defaultdict'>
    >>> len(sum_data)
    20
    >>> sum_data['Amiens']['Played']
    19
    >>> sum_data['Angers']['Won']
    3
    >>> sum_data['Bordeaux']['Drawn']
    5
    >>> sum_data['Caen']['Lost']
    9
    >>> sum_data['Dijon']['FTGA']
    33
    >>> sum_data['Guingamp']['HTGF']
    7
    >>> sum_data['Lille']['HTGA']
    17
    >>> sum_data['Lyon']['S']
    263
    >>> sum_data['Marseille']['ST']
    109
    >>> sum_data['Metz']['C']
    85
    >>> sum_data['Monaco']['F']
    270
    >>> sum_data['Montpellier']['Y']
    43
    >>> sum_data['Nantes']['R']
    3
    >>> agg_data = aggregate(raw_data, matchdays=range(20,39))
    >>> sum_data = summarize(agg_data)
    >>> sum_data['Nice']['Won']
    7
    >>> sum_data['Paris SG']['Drawn']
    4
    >>> sum_data['Rennes']['Lost']
    4
    >>> sum_data['St Etienne']['FTGF']
    29
    >>> sum_data['Strasbourg']['FTGA']
    36
    >>> sum_data['Toulouse']['HTGF']
    9
    >>> sum_data['Troyes']['HTGA']
    11

    """
    sum_data = defaultdict(dict)

    props = ['Played', 'Won', 'Drawn', 'Lost', 'FTGF', 'FTGA', 'HTGF', 'HTGA', 'S', 'ST', 'C', 'F', 'Y', 'R']
    for key, value in agg_data.items():
        for prop in props:
            sum_data[key][prop] = sum(value[prop])

    return sum_data


def order_results(sum_data, stat):
    """
    Args:
        sum_data (dict) : summarized data (team based) returned by summarize()
        stat (str) : stat used for ordering ('Played', 'Won, ...)

    Returns:
        list of tuples : ordered list of <team, stat_value> (the best first)

    >>> raw_data = read_data(FILENAME)
    >>> agg_data = aggregate(raw_data, matchdays=range(1,20))
    >>> sum_data = summarize(agg_data)
    >>> ord_data = order_results(sum_data, 'Won')
    >>> type(ord_data)
    <class 'list'>
    >>> len(ord_data)
    20
    >>> type(ord_data[0])
    <class 'tuple'>
    >>> len(ord_data[0])
    2
    >>> ord_data[0]
    ('Paris SG', 16)
    >>> ord_data[1]
    ('Monaco', 13)
    >>> ord_data[2]
    ('Lyon', 12)
    >>> ord_data[8]
    ('Guingamp', 7)
    >>> ord_data[9]
    ('Rennes', 7)
    >>> ord_data[10]
    ('Amiens', 6)
    >>> ord_data[11]
    ('Montpellier', 6)
    >>> ord_data[12]
    ('Strasbourg', 6)
    >>> ord_data[17]
    ('Toulouse', 5)
    >>> ord_data[18]
    ('Angers', 3)
    >>> ord_data[19]
    ('Metz', 3)
    """
    l = []
    
    # 1. build a list of tuples <team, stat value>
    for k,v in sum_data.items() :
        l.append((k,v[stat]))
    # l = [(k, v[stat]) for k, v in sum_data.items()]

    # 2. sort list
    l.sort(key=lambda val: val[1], reverse = True)
    
    return l

def get_team_rank(team_stat):
    """compute team rank from team stats Win=3 Drawn=1 Lost =0

    Args:
        team_stat (dict) : dict of stat for team of interest

    Returns:
        int : team rank (number of points corresponding to won, drawn and lost games)

    >>> raw_data = read_data('ligue1_1718.csv')
    >>> agg_data = aggregate(raw_data)
    >>> sum_data = summarize(agg_data)
    >>> get_team_rank(sum_data['Amiens'])
    45
    >>> get_team_rank(sum_data['Angers'])
    41
    >>> get_team_rank(sum_data['Bordeaux'])
    55
    >>> get_team_rank(sum_data['Caen'])
    38
    >>> get_team_rank(sum_data['Dijon'])
    48
    >>> get_team_rank(sum_data['Guingamp'])
    47
    >>> get_team_rank(sum_data['Lille'])
    38
    >>> get_team_rank(sum_data['Lyon'])
    78
    >>> get_team_rank(sum_data['Marseille'])
    77
    >>> get_team_rank(sum_data['Metz'])
    26
    >>> get_team_rank(sum_data['Monaco'])
    80
    >>> get_team_rank(sum_data['Montpellier'])
    51
    >>> get_team_rank(sum_data['Nantes'])
    52
    >>> get_team_rank(sum_data['Nice'])
    54
    >>> get_team_rank(sum_data['Paris SG'])
    93
    >>> get_team_rank(sum_data['Rennes'])
    58
    >>> get_team_rank(sum_data['St Etienne'])
    55
    >>> get_team_rank(sum_data['Strasbourg'])
    38
    >>> get_team_rank(sum_data['Toulouse'])
    37
    >>> get_team_rank(sum_data['Troyes'])
    33
    """
    rank = 0
    # Votre code ici...

    return rank

def compute_final_table(sum_data):
    """compute final table, best team first

    Args:
        sum_data (dict) : summarized data (team based) returned by summarize()

    Returns:
        list(tuple) : ordered list of tuples (team, rank)

    >>> raw_data = read_data('ligue1_1718.csv')
    >>> agg_data = aggregate(raw_data)
    >>> sum_data = summarize(agg_data)
    >>> table = compute_final_table(sum_data)
    >>> type(table)
    <class 'list'>
    >>> len(table)
    20
    >>> type(table[0])
    <class 'tuple'>
    >>> len(table[0])
    2
    >>> table[0][0]
    'Paris SG'
    >>> table[0][1]
    93
    >>> table[1][0]
    'Monaco'
    >>> table[1][1]
    80
    >>> table[2][0]
    'Lyon'
    >>> table[2][1]
    78
    >>> table[17][0]
    'Toulouse'
    >>> table[17][1]
    37
    >>> table[18][0]
    'Troyes'
    >>> table[18][1]
    33
    >>> table[19][0]
    'Metz'
    >>> table[19][1]
    26

    """
    l = []
    # Votre code ici...

    # 1. build list
    # 2. sort list

    return l

def main():
    raw_data = read_data(FILENAME)
    #test pour la premiere fonction
    print(len(raw_data))
    print("len de raw_data[0] = ",len(raw_data[0]))
    print(type(raw_data))
    print(type(raw_data[0]))
    print(raw_data[0])
    print(raw_data[20].get("HomeTeam"))
    print(raw_data[110].get("HST"))
    #test pour la deuxieme fonction
    data = read_data('./data/ligue1_1718.csv')
    d = data[0]
    res = get_result(d)
    print(res)
    # test aggregate
    raw_data = read_data(FILENAME)
    agg_data = aggregate(raw_data, matchdays=range(1,3))
    print(len(agg_data['Amiens']['Played']))
    print(agg_data['Amiens']['Home'])
    # test summarize
    raw_data = read_data(FILENAME)
    agg_data = aggregate(raw_data, matchdays=range(1,20))
    sum_data = summarize(agg_data)
    print(sum_data['Amiens']['Played'])
    print(sum_data['Angers']['Won'])
    # test order result
    raw_data = read_data(FILENAME)
    agg_data = aggregate(raw_data, matchdays=range(1,20))
    sum_data = summarize(agg_data)
    ord_data = order_results(sum_data, 'Won')

if __name__ == '__main__':
    DOCTESTS = False
    if not DOCTESTS: main()

    functions = [ read_data, get_result, aggregate, summarize, order_results, get_team_rank, compute_final_table] #
    if DOCTESTS:
        for f in functions:
            doctest.run_docstring_examples(f, globals(), name=f.__name__)