-- MySQL script to set up the test database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Check if the user exists
DROP USER IF EXISTS 'hbnb_test'@'localhost';

CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
