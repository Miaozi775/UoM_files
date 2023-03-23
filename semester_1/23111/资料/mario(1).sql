CREATE TABLE characters (
  character_name varchar(200) PRIMARY KEY,
  size varchar(200) NOT NULL,
  acceleration int NOT NULL,
  top_speed int NOT NULL,
  handling int NOT NULL
);

CREATE TABLE players (
  player_name varchar(200) PRIMARY KEY,
  character_name varchar(200) NOT NULL,
  rating int NOT NULL
);

INSERT INTO characters (character_name, size, acceleration, top_speed, handling) VALUES
  ('Mario', 'Medium', 3,  3,  3),
  ('Luigi', 'Medium', 3,  3,  2),
  ('Toad',  'Small',  5,  2,  4),
  ('Bowser',  'Large',  1,  5,  2);

INSERT INTO players (player_name, character_name, rating) VALUES
  ('Gareth', 'Toad', 3),
  ('Stewart', 'Mario', 2),
  ('Andrea', 'Toad', 5),
  ('Paul', 'Bowser', 1);
