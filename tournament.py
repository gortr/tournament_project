#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<Error: Unable to communicate with database.>")

def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()

    query = "DELETE FROM matches WHERE match_id IS NOT NULL;"
    c.execute(query)
    
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()

    query = "DELETE FROM players WHERE player_id IS NOT NULL;"
    c.execute(query)
    
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()

    query = "SELECT count(player_id) AS num FROM players;"
    c.execute(query)
    count = int(c.fetchone()[0])
    
    db.close()
    return count

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()

    query = "INSERT INTO players (name) VALUES (%s);"
    param = (name,)
    c.execute(query, param)
    
    db.commit()
    db.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()

    query = "SELECT * FROM view_standings"
    c.execute(query)
    standings = c.fetchall()
    
    db.close()
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()

    query = "INSERT INTO matches (winner, loser) values (%s, %s);"
    param = (int(winner), int(loser))
    c.execute(query, param)
    
    db.commit()
    db.close()

def breakIntoGroups(list, size = 2):
    size = max(1, size)
    return [list[i:i + size] for i in range(0, len(list), size)]

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    grouped_pool = breakIntoGroups(standings, 2)
    matched_pairs = list()

    for pair in grouped_pool:
        pairing = list()
        for player in pair:
            pairing.append(player[0])
            pairing.append(player[1])
        matched_pairs.append(pairing)

    return matched_pairs

