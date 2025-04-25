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
SELECT * FROM imageimporttable;
