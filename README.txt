Author: Rigoberto J Gort
Date: 04/03/2017

---------- Project Info ----------
Filename: README.txt
Main Project File: tournament.py
Connected Module Files: tournament.sql

---------- Configuration Instructions ----------
- tournament.py -
This is the primary file that calls on the SQL commands from tournament.sql.

It uses these commands to build a database, insert tables and allow for the addition
and removal or players from the database. It also permits the tracking of each
individual players standings during the tournament as well.

---------- Operating Instructions ----------
If you would like to run this script you will need to do the following.

Please make sure the following software is installed on your machine prior to running.

- List of Necessary Software -
> Vagrant [https://www.vagrantup.com/]
> VM Virtual Box [https://www.virtualbox.org/]
> An operating system (Preferably Ubuntu)
> PostgreSQL [https://www.postgresql.org/]
> Pyscopg2 (Make sure you have Python installed globally and run 'pip install psycopg2')

After you have completed installing the previously mentioned software then follow these steps. You will need to run these commands first in the command line or terminal.

1) Change your directory to the folder that contains the tournament files.
2) Run 'vagrant up' to launch the virtual machine necessary.
3) Run 'vagrant ssh' to connect to said virtual machine.
4) Enter the PSQL mode by running 'psql' or 'psql postgre' which will connect you to the default database.
5) Once it shows you in psql (it will show the database name of postgres=#) you will run the command \i tournament.sql
6) Once it imports that script you can then test the python tournmanet_test.py script. You will do this by running the command 'python tournament_test.py'

---------- END OF README.TXT FILE ----------