#!/bin/bash
# List all databases in MySQL server
mysql -hlocalhost -uroot -p"$MYSQL_PWD" -e "SHOW DATABASES;"
