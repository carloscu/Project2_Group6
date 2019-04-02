USE pokemon;

CREATE TABLE `stats` (
`Number` int(11) DEFAULT NULL,
`Name` text DEFAULT NULL,
`Type_1` text DEFAULT NULL,
`Type_2` text DEFAULT NULL,
`Total` int(11) DEFAULT NULL,
`HP` int(11) DEFAULT NULL,
`Attack` int(11) DEFAULT NULL,
`Defense` int(11) DEFAULT NULL,
`Sp_Atk` int(11) DEFAULT NULL,
`Sp_Def` int(11) DEFAULT NULL,
`Speed` int(11) DEFAULT NULL,
`Generation` int(11) DEFAULT NULL,
`isLegendary` text DEFAULT NULL,
`Color` text DEFAULT NULL,
`hasGender` text DEFAULT NULL,
`Pr_Male` double DEFAULT NULL,
`Egg_Group_1` text DEFAULT NULL,
`Egg_Group_2` text DEFAULT NULL,
`hasMegaEvolution` text DEFAULT NULL,
`Height_m` double DEFAULT NULL,
`Weight_kg` double DEFAULT NULL,
`Catch_Rate` int(11) DEFAULT NULL,
`Body_Style` text DEFAULT NULL);



