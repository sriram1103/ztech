CREATE DATABASE info_db;
use info_db;

CREATE TABLE info_table(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	ip VARCHAR(20),
	iptype VARCHAR(10),
	continent_code VARCHAR(10),
	continent_name VARCHAR(10),
	country_code VARCHAR(10),
	country_name VARCHAR(20),
	region_code VARCHAR(20),
	region_name VARCHAR(20),
	city VARCHAR(20),
	zip VARCHAR(20),
	latitude FLOAT,
	longitude FLOAT,
	location JSON
);
