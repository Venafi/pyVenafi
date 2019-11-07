-- DROP TABLE States;
DROP TABLE JobHistory;
DROP TABLE TestHistory;
DROP TABLE Runs;
DROP TABLE Tests;
DROP TABLE Jobs;
DROP TABLE Frameworks;


CREATE TABLE Frameworks (
  frameworkId int identity(1,1) not null,
  name nchar(32) not null,
  lastUpdated datetime,
  PRIMARY KEY (frameworkId)
);

INSERT INTO Frameworks VALUES ('Python', CURRENT_TIMESTAMP);
INSERT INTO Frameworks VALUES ('Integration', CURRENT_TIMESTAMP);

CREATE TABLE Runs (
  runId int identity(1,1),
  newJobs int,
  newTests int,
  created datetime not null
  PRIMARY KEY (runId)
);

CREATE TABLE Jobs (
  jobId int identity(1,1) not null,
  name nchar(255) not null,
  frameworkId int not null,
  created datetime not null,
  lastUpdated datetime not null,
  lastBuildNo int not null,
  PRIMARY KEY (jobId),
  FOREIGN KEY (frameworkId) REFERENCES Frameworks (frameworkId)
);

CREATE TABLE JobHistory (
  jobId int not null,
  runId int not null,
  buildNo int not null,
  build nchar(64),
  releaseVersion nchar(8) not null,
  gitBranch nchar(64),
  totalTests int not null,
  passed int not null,
  failed int not null,
  skipped int not null,
  lapse int, -- in seconds
  FOREIGN KEY (runId) REFERENCES Runs (runId),
  FOREIGN KEY (jobId) REFERENCES Jobs (jobId)
  
);

CREATE TABLE Tests (
  testId int identity(1,1),
  jobId int not null,
  className nchar(255) not null,
  testName nchar(255) not null,
  feature nchar(128) not null,
  owner nchar(32) not null,
  created datetime not null,
  lastUpdated datetime not null,
  PRIMARY KEY (testId),
  FOREIGN KEY (jobId) REFERENCES Jobs (jobId)
);

CREATE TABLE TestHistory (
  testId int not null,
  runId int not null,
  testResult nchar(16) not null,
  reason nvarchar(max),
  age int not null,
  resolution nchar(32) not null,
  lapse int, -- in seconds
  FOREIGN KEY (testId) REFERENCES Tests (testId),
  FOREIGN KEY (runId) REFERENCES Runs (runId)
);

CREATE INDEX jobName ON Jobs (name);
CREATE INDEX className ON Tests (className);
CREATE INDEX jobId ON Tests (jobId);
CREATE UNIQUE INDEX uq_TestHistory ON  TestHistory(testId, runId);
CREATE UNIQUE INDEX uq_JobHistory ON  JobHistory(jobId, runId);

SELECT *
FROM Runs;

SELECT *
FROM Tests;

SELECT *
FROM TestHistory;

SELECT *
FROM Jobs;

SELECT *
FROM JobHistory;

SELECT *
FROM Frameworks;










