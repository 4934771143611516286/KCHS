USE importtestdb;
CREATE TABLE IF NOT EXISTS imageimporttable(
	ID INTEGER,
    dateTaken TEXT,
    Title TEXT,
    Link TEXT,
    Descript TEXT,
    dateAdded TEXT,
    PRIMARY KEY (ID)
);

LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ImportTester.csv'
INTO TABLE imageimporttable
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT * FROM imageimporttable;
