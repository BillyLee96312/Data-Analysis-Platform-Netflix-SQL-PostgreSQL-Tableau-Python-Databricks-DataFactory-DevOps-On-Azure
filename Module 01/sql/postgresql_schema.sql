-- PostgreSQL schema for `netflix` data
-- Create analytics database and netflix schema

CREATE SCHEMA IF NOT EXISTS netflix;

CREATE TABLE IF NOT EXISTS netflix.netflix_shows (
    show_id VARCHAR(50) PRIMARY KEY,
    type VARCHAR(50),
    title VARCHAR(500),
    director VARCHAR(500),
    cast TEXT,
    country VARCHAR(200),
    date_added DATE,
    release_year INTEGER
);

-- Example: user and table creation steps (do not keep credentials in code; use Key Vault or parameterization)
-- CREATE USER netflix_user WITH PASSWORD '<password>';
-- GRANT CONNECT ON DATABASE analytics TO netflix_user;
-- GRANT USAGE ON SCHEMA netflix TO netflix_user;
-- GRANT INSERT, SELECT ON ALL TABLES IN SCHEMA netflix TO netflix_user;

-- Sample quick query to check for row counts
-- SELECT COUNT(*) FROM netflix.netflix_shows;
