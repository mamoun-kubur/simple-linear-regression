#!bin/bash
exec git init
exec git add -A
exec git commit -m 'updated'
exec git remote add origin https://github.com/mamoun-kubur/simple-linear-regression.git
exec git push -u -f origin master
