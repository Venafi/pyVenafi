DROP TABLE TestAnnotations;
DROP TABLE TestResults;
DROP TABLE TestResultValues;
DROP TABLE TestInfo;
DROP TABLE TestAnnotationLabels;
DROP TABLE TestAnnotationValues;


CREATE TABLE TestInfo (
	testId int identity(1,1),
	testGuid nchar(38) not null,
	testName nchar(48) not null,
	filePath nchar(64) not null,
	created datetime not null,
	lastRun datetime not null,
	PRIMARY KEY (testId)
);

CREATE TABLE TestAnnotationLabels (
	labelId int identity(1,1),
	annotationLabel nchar(32) not null,
	PRIMARY KEY (labelId)
)

CREATE TABLE TestAnnotationValues (
	valueId int identity(1,1),
	annotationValue nchar(32) not null,
	PRIMARY KEY (valueId)
)

CREATE TABLE TestResultValues (
	resultId int identity(1,1),
	resultValue nchar(16) not null,
	PRIMARY KEY (resultId)
)

CREATE TABLE TestResults (
	testId int not null,
	testResult int not null,
	logFile nchar(64),
	consecutiveFailures int not null,
	runDate datetime not null,
	timeLapse int, -- in seconds
	FOREIGN KEY (testId) REFERENCES TestInfo (testId),
	FOREIGN KEY (testResult) REFERENCES TestResultValues (resultId)
);

CREATE TABLE TestAnnotations (
	testId int not null,
	labelId int not null,
	valueId int not null,
	FOREIGN KEY (testId) REFERENCES TestInfo (testId),
	FOREIGN KEY (labelId) REFERENCES TestAnnotationLabels (labelId),
	FOREIGN KEY (valueId) REFERENCES TestAnnotationValues (valueId)
)


CREATE UNIQUE INDEX uq_TestAnnotations ON TestAnnotations(testId, labelId, valueId);

INSERT INTO TestResultValues VALUES ('Passed');
INSERT INTO TestResultValues VALUES ('Failed');
INSERT INTO TestResultValues VALUES ('Skipped');
INSERT INTO TestAnnotationLabels VALUES ('Owner');
INSERT INTO TestAnnotationLabels VALUES ('Feature');
