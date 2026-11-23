CREATE DATABASE  IF NOT EXISTS `law` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `law`;
-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: law
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `law_uzbekistan`
--

DROP TABLE IF EXISTS `law_uzbekistan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `law_uzbekistan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` varchar(100) DEFAULT NULL,
  `article_section_no` varchar(255) DEFAULT NULL,
  `title` text,
  `description` longtext,
  `part_chapter` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `law_uzbekistan`
--

LOCK TABLES `law_uzbekistan` WRITE;
/*!40000 ALTER TABLE `law_uzbekistan` DISABLE KEYS */;
INSERT INTO `law_uzbekistan` VALUES (1,'Preamble','Preamble','PREAMBLE','The people of Uzbekistan:\nsolemnly declaring their adherence to human rights and principles of state sovereignty, aware of their ultimate responsibility to the present and the future generations,\nrelying on historical experience in the development of Uzbek statehood, affirming their commitment to the ideals of democracy and social justice, recognizing priority of the generally accepted norms of the international law, aspiring to a worthy life for the citizens of the Republic,\nsetting forth the task of creating a humane and democratic rule of law,\naiming to ensure civil peace and national accord, represented by their plenipotentiary deputies adopt the present Constitution of the Republic of Uzbekistan.',''),(2,'Structure','PART ONE. FUNDAMENTAL PRINCIPLES','PART ONE. FUNDAMENTAL PRINCIPLES','',''),(3,'Structure','Chapter 1. State Sovereignty','Chapter 1. State Sovereignty','',''),(4,'Articles','Article 1','Article 1.','Uzbekistan is a sovereign democratic republic. Both names of the state - the Republic of Uzbekistan and Uzbekistan - shall be equivalent.',''),(5,'Structure','Chapter 2. Democracy','Chapter 2. Democracy','',''),(6,'Articles','Article 7','Article 7.','The people are the sole source of state power.\nState power in the Republic of Uzbekistan shall be exercised in the interests of the people and solely by the bodies empowered therefore by the Constitution of the Republic of Uzbekistan and the laws passed on its basis.\nAny seizure of powers belonging to state authority, suspension or termination of activity of the bodies of state authority contrary to the procedure prescribed by the Constitution, as well as the formation of any new or parallel bodies of state authority shall be regarded as unconstitutional and punishable by law.',''),(7,'Structure','Chapter 3. Supremacy of the Constitution and the L','Chapter 3. Supremacy of the Constitution and the Law','',''),(8,'Articles','Article 15','Article 15.','The Constitution and the laws of the Republic of Uzbekistan shall have absolute supremacy in the Republic of Uzbekistan.\nThe state, its bodies, officials, public associations and citizens shall act in accordance with the Constitution and the laws.',''),(9,'Structure','Chapter 4. Foreign Policy','Chapter 4. Foreign Policy','',''),(10,'Articles','Article 17','Article 17.','The Republic of Uzbekistan shall have full rights in international relations. Its foreign policy shall be based on the principles of sovereign equality of the states, non-use of force or threat of its use, inviolability of frontiers, peaceful settlement of disputes, non-interference in the internal affairs of other states, and other universally recognized norms of international law.\nThe Republic may form alliances, join or withdraw from unions and other inter-state organizations proceeding from the ultimate interests of the state and the people, their well-being and security.','');
/*!40000 ALTER TABLE `law_uzbekistan` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-30 22:51:38
