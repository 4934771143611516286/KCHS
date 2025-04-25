USE importtestdb;
CREATE TABLE IF NOT EXISTS logininfotable(
	ID INTEGER,
    username TEXT,
    passcode TEXT,
    PRIMARY KEY (ID)
);

SELECT * FROM logininfotable;
