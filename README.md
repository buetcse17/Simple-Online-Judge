Online Judge With Database

How to build?

step 1 : [install oracle 11g](Oracle-Installation-Guideline.pptx)

step 2 : login to sql plus as SYSTEM using password during installation 

If "OJ" user already exists then run 

```
DROP USER OJ CASCADE ;
```

run command from below

```
CREATE USER OJ IDENTIFIED BY OJ;

GRANT ALL PRIVILEGES TO OJ;

```
step 3: run ddl.sql from project folder

step 4: install python , run command from below

```
pip install django

pip install cx_oracle

```
