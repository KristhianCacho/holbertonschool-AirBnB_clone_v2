-- Create the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
