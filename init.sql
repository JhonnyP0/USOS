CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    password VARCHAR(100),
    permissions VARCHAR(100)
);

INSERT INTO users (name, password, permissions) VALUES
('admin','topsecretsecurepass','admin'),
('Jan','maslo','user'),
('Kowalski', 'maslo','professor');