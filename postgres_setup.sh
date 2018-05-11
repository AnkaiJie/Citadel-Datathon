#https://www.quora.com/How-can-I-install-PostgreSQL-on-AWS-EC2-and-how-can-I-access-that
sudo yum update
sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs
sudo service postgresql initdb
sudo vim /var/lib/pgsql9/data/pg_hba.conf
sudo vim /var/lib/pgsql9/data/postgresql.conf



# then after edits, do this
sudo service postgresql start
sudo su - postgres
psql -U postgres

ALTER USER postgres WITH PASSWORD 'postgres';
CREATE USER datathon SUPERUSER;
ALTER USER datathon WITH PASSWORD 'datathon';
CREATE DATABASE datathonDb;
GRANT ALL PRIVILEGES ON DATABASE datathonDb TO datathon;

