USE pokemon;

SELECT * FROM information_schema.columns WHERE table_name = 'pokemon_stats';

SHOW CREATE TABLE pokemon_stats;

CREATE TABLE `stats` (
`Number` int(11) DEFAULT NULL,
`Name` text,
`Type_1` text,
`Type_2` text,
`Total` int(11) DEFAULT NULL,
`HP` int(11) DEFAULT NULL,
`Attack` int(11) DEFAULT NULL,
`Defense` int(11) DEFAULT NULL,
`Sp_Atk` int(11) DEFAULT NULL,
`Sp_Def` int(11) DEFAULT NULL,
`Speed` int(11) DEFAULT NULL,
`Generation` int(11) DEFAULT NULL,
`isLegendary` text,
`Color` text,
`hasGender` text,
`Pr_Male` double DEFAULT NULL,
`Egg_Group_1` text,
`Egg_Group_2` text,
`hasMegaEvolution` text,
`Height_m` double DEFAULT NULL,
`Weight_kg` double DEFAULT NULL,
`Catch_Rate` int(11) DEFAULT NULL,
`Body_Style` text);

DROP TABLE pokemon_stats;

