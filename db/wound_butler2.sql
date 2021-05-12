--
-- 由SQLiteStudio v3.2.1 产生的文件 周二 4月 6 20:11:13 2021
--
-- 文本编码：GBK
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- 表：report
CREATE TABLE report (
    id        INTEGER      PRIMARY KEY,
    name      VARCHAR (20) UNIQUE,
    gender    VARCHAR,
    age       VARCHAR,
    height    VARCHAR,
    weight    VARCHAR,
    area      VARCHAR,
    perimeter VARCHAR
);

INSERT INTO report (id, name, gender, age, height, weight, area, perimeter) VALUES (1, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
