SELECT * FROM `Character` WHERE `handling` < 3

SELECT `character_name`, `size` FROM `Character`

ALTER TABLE `Character` CHANGE `new_name` `size` varchar(20)

SELECT `character_name` FROM `Character` UNION SELECT `character_name` FROM `Player`

SELECT * FROM `Character` CROSS JOIN `Player`

SELECT * FROM `Character`, `Player` WHERE `Character`.`acceleration` > `Player`.`rating`

SELECT * FROM `Character`, `Player` WHERE `Character`.`acceleration` = `Player`.`rating`

SELECT * FROM `Character` NATURAL JOIN `Player`

SELECT * FROM `Character` LEFT JOIN `Player` ON `Character`.`character_name` = `Player`.`character_name`

SELECT * FROM `Character` RIGHT JOIN `Player` ON `Character`.`character_name` = `Player`.`character_name`

SELECT * FROM `Character` CROSS JOIN `Player` ON `Character`.`character_name` = `Player`.`character_name`

SELECT DISTINCT `Character`.`character_name`, `Player`.`player_name` FROM `Character`, `Player` WHERE `Character`.`acceleration` < `Player`.`rating`

SELECT DISTINCT `Character`.`character_name`, `Character`.`handling`, `Player`.`player_name`, `Player`.`rating` FROM `Player` INNER JOIN `Character` ON `Character`.`handling` < `Player`.`rating`;

SELECT DISTINCT MIN(`Player`.`rating`) AS `WorstPlayer` FROM `Player` WHERE `Player`.`character_name` = 'Toad';

