-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Drops tournament database if it exists
drop database if exists tournament;

-- Creates tournament database
create database tournament;

-- Connect to the tournament database
\c tournament

-- Create the players table for tracking players stats.
create table players(
	player_id serial primary key,
	name text);

-- Create the matches table for tracking matches.
create table matches(
	match_id serial primary key,
	winner integer references players(player_id),
	loser integer references players(player_id));

-- Create Wins View
create view view_wins as
	select players.player_id as player, count(matches.winner) as wins
	from players left join matches
		on players.player_id = matches.winner
	group by player_id, matches.loser
	order by player_id;

-- Create Losses View
create view view_losses as
	select players.player_id as player, count(matches.loser) as losses
	from players left join matches
		on players.player_id = matches.loser
	group by players.player_id
	order by players.player_id asc;

-- Create Rounds View
create view view_matches as
	select players.player_id as player, count(matches) as matches
	from players left join matches
		on (players.player_id = matches.winner) or (players.player_id = matches.loser)
	group by players.player_id
	order by players.player_id asc;

-- Create Standings View
create view view_standings as
	select players.player_id, players.name, view_wins.wins, view_matches.matches
    from players left join view_wins 
    	on players.player_id = view_wins.player
    left join view_matches 
    	on players.player_id = view_matches.player
    group by players.player_id, players.name, view_wins.wins, view_matches.matches
    order by view_wins.wins desc;