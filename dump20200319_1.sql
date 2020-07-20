-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: recommendsys
-- ------------------------------------------------------
-- Server version	8.0.19

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add post',7,'add_post'),(26,'Can change post',7,'change_post'),(27,'Can delete post',7,'delete_post'),(28,'Can view post',7,'view_post'),(29,'Can add auth group',8,'add_authgroup'),(30,'Can change auth group',8,'change_authgroup'),(31,'Can delete auth group',8,'delete_authgroup'),(32,'Can view auth group',8,'view_authgroup'),(33,'Can add auth group permissions',9,'add_authgrouppermissions'),(34,'Can change auth group permissions',9,'change_authgrouppermissions'),(35,'Can delete auth group permissions',9,'delete_authgrouppermissions'),(36,'Can view auth group permissions',9,'view_authgrouppermissions'),(37,'Can add auth permission',10,'add_authpermission'),(38,'Can change auth permission',10,'change_authpermission'),(39,'Can delete auth permission',10,'delete_authpermission'),(40,'Can view auth permission',10,'view_authpermission'),(41,'Can add auth user',11,'add_authuser'),(42,'Can change auth user',11,'change_authuser'),(43,'Can delete auth user',11,'delete_authuser'),(44,'Can view auth user',11,'view_authuser'),(45,'Can add auth user groups',12,'add_authusergroups'),(46,'Can change auth user groups',12,'change_authusergroups'),(47,'Can delete auth user groups',12,'delete_authusergroups'),(48,'Can view auth user groups',12,'view_authusergroups'),(49,'Can add auth user user permissions',13,'add_authuseruserpermissions'),(50,'Can change auth user user permissions',13,'change_authuseruserpermissions'),(51,'Can delete auth user user permissions',13,'delete_authuseruserpermissions'),(52,'Can view auth user user permissions',13,'view_authuseruserpermissions'),(53,'Can add category l',14,'add_categoryl'),(54,'Can change category l',14,'change_categoryl'),(55,'Can delete category l',14,'delete_categoryl'),(56,'Can view category l',14,'view_categoryl'),(57,'Can add category m',15,'add_categorym'),(58,'Can change category m',15,'change_categorym'),(59,'Can delete category m',15,'delete_categorym'),(60,'Can view category m',15,'view_categorym'),(61,'Can add category s',16,'add_categorys'),(62,'Can change category s',16,'change_categorys'),(63,'Can delete category s',16,'delete_categorys'),(64,'Can view category s',16,'view_categorys'),(65,'Can add django admin log',17,'add_djangoadminlog'),(66,'Can change django admin log',17,'change_djangoadminlog'),(67,'Can delete django admin log',17,'delete_djangoadminlog'),(68,'Can view django admin log',17,'view_djangoadminlog'),(69,'Can add django content type',18,'add_djangocontenttype'),(70,'Can change django content type',18,'change_djangocontenttype'),(71,'Can delete django content type',18,'delete_djangocontenttype'),(72,'Can view django content type',18,'view_djangocontenttype'),(73,'Can add django migrations',19,'add_djangomigrations'),(74,'Can change django migrations',19,'change_djangomigrations'),(75,'Can delete django migrations',19,'delete_djangomigrations'),(76,'Can view django migrations',19,'view_djangomigrations'),(77,'Can add django session',20,'add_djangosession'),(78,'Can change django session',20,'change_djangosession'),(79,'Can delete django session',20,'delete_djangosession'),(80,'Can view django session',20,'view_djangosession'),(81,'Can add voice recognition post',21,'add_voicerecognitionpost'),(82,'Can change voice recognition post',21,'change_voicerecognitionpost'),(83,'Can delete voice recognition post',21,'delete_voicerecognitionpost'),(84,'Can view voice recognition post',21,'view_voicerecognitionpost');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category_l`
--

DROP TABLE IF EXISTS `category_l`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category_l` (
  `ctgr_lid` int NOT NULL AUTO_INCREMENT,
  `ctgr_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`ctgr_lid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category_l`
--

LOCK TABLES `category_l` WRITE;
/*!40000 ALTER TABLE `category_l` DISABLE KEYS */;
INSERT INTO `category_l` VALUES (1,'먹거리'),(2,'놀거리');
/*!40000 ALTER TABLE `category_l` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category_m`
--

DROP TABLE IF EXISTS `category_m`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category_m` (
  `ctgr_mid` int NOT NULL AUTO_INCREMENT,
  `ctgr_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `large_id` int DEFAULT NULL,
  PRIMARY KEY (`ctgr_mid`),
  KEY `ctgr_lid_idx` (`large_id`),
  CONSTRAINT `large_id_m` FOREIGN KEY (`large_id`) REFERENCES `category_l` (`ctgr_lid`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category_m`
--

LOCK TABLES `category_m` WRITE;
/*!40000 ALTER TABLE `category_m` DISABLE KEYS */;
INSERT INTO `category_m` VALUES (1,'분식',1),(2,'한식',1),(3,'일식',1),(4,'중식',1),(5,'양식',1),(6,'아시안식',1),(7,'관광지',2),(8,'문화시설',2),(9,'공연행사',2),(10,'레포츠',2),(11,'엔조이',2),(12,'면',1),(13,'생선',1),(14,'밥',1),(15,'빵',1),(16,'고기',1),(17,'생선',1),(18,'해물',1),(19,'해산물',1),(20,'국',1),(21,'국밥',1),(22,'전',1),(23,'찌개',1),(24,'튀김',1),(25,'덮밥',1),(26,'만두',1);
/*!40000 ALTER TABLE `category_m` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category_s`
--

DROP TABLE IF EXISTS `category_s`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category_s` (
  `ctgr_sid` int NOT NULL AUTO_INCREMENT,
  `ctgr_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `large_id` int DEFAULT NULL,
  `middle_id` int DEFAULT NULL,
  PRIMARY KEY (`ctgr_sid`),
  UNIQUE KEY `name_middle` (`ctgr_name`,`middle_id`),
  KEY `middle_id_idx` (`middle_id`),
  KEY `large_id_s_idx` (`large_id`),
  CONSTRAINT `large_id_s` FOREIGN KEY (`large_id`) REFERENCES `category_m` (`large_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `middle_id_s` FOREIGN KEY (`middle_id`) REFERENCES `category_m` (`ctgr_mid`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=268 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category_s`
--

LOCK TABLES `category_s` WRITE;
/*!40000 ALTER TABLE `category_s` DISABLE KEYS */;
INSERT INTO `category_s` VALUES (1,'떡볶이',1,1),(2,'라볶이',1,1),(3,'쫄볶이',1,1),(4,'순대',1,1),(5,'어묵',1,1),(6,'냉면',1,1),(7,'비빔밥',1,1),(8,'칼국수',1,1),(9,'잔치국수',1,1),(10,'비빔국수',1,1),(11,'콩국수',1,1),(12,'수제비',1,1),(13,'쫄면',1,1),(14,'김밥',1,1),(15,'주먹밥',1,1),(16,'핫도그',1,1),(17,'김치볶음밥',1,1),(18,'육회',1,2),(19,'닭발',1,2),(20,'고등어구이',1,2),(21,'아구찜',1,2),(22,'해물찜',1,2),(23,'갈비',1,2),(24,'떡국',1,2),(25,'만두국,만둣국',1,2),(26,'추어탕',1,2),(27,'파전',1,2),(28,'김치전',1,2),(29,'대창',1,2),(30,'막창',1,2),(31,'곱창',1,2),(32,'주꾸미,쭈꾸미',1,2),(33,'찜닭',1,2),(34,'불고기',1,2),(35,'닭갈비',1,2),(36,'갈비찜',1,2),(37,'삼겹살',1,2),(38,'오겹살',1,2),(39,'제육',1,2),(40,'오징어볶음',1,2),(41,'낙지볶음',1,2),(42,'오리구이',1,2),(43,'닭볶음탕',1,2),(44,'갈비탕',1,2),(45,'돼지국밥',1,2),(46,'소고기국밥',1,2),(47,'육개장',1,2),(48,'감자탕',1,2),(49,'순대국밥',1,2),(50,'뼈해장국',1,2),(51,'곰탕',1,2),(52,'설렁탕',1,2),(53,'부대찌개',1,2),(54,'김치찌개',1,2),(55,'된장찌개',1,2),(56,'청국장찌개',1,2),(57,'삼계탕',1,2),(58,'순두부찌개',1,2),(59,'빈대떡',1,2),(60,'죽',1,2),(61,'돈까스,돈카츠',1,3),(62,'새우까스,새우카츠',1,3),(63,'생선까스',1,3),(64,'히레까스,히레카츠',1,3),(65,'로스까스,로스카츠',1,3),(66,'호르몬동',1,3),(67,'규동',1,3),(68,'사케동',1,3),(69,'가츠동',1,3),(70,'카레',1,3),(71,'소바',1,3),(72,'메밀',1,3),(73,'우동',1,3),(74,'라멘',1,3),(75,'나베,스키야키',1,3),(76,'초밥',1,3),(77,'회,우럭,광어,참치',1,3),(78,'타코야키,타코야끼',1,3),(79,'오코노미야키,오코노미야끼',1,3),(80,'샤브샤브',1,3),(81,'양장피',1,4),(82,'팔보채',1,4),(83,'유산슬',1,4),(84,'동파육',1,4),(85,'라조육',1,4),(86,'라조기',1,4),(87,'깐풍기',1,4),(88,'잡탕',1,4),(89,'해파리냉채',1,4),(90,'꿔바로우',1,4),(91,'칠리새우',1,4),(92,'탕수육',1,4),(93,'짜장면,자장면',1,4),(94,'짬뽕',1,4),(95,'울면',1,4),(96,'볶음밥',1,4),(97,'마라탕',1,4),(98,'마라샹궈',1,4),(99,'고추잡채',1,4),(100,'누룽지탕',1,4),(101,'양꼬치',1,4),(102,'치킨',1,5),(103,'피자',1,5),(104,'햄버거',1,5),(105,'파스타',1,5),(106,'까르보나라',1,5),(107,'리조또',1,5),(108,'스테이크',1,5),(109,'퀘사디아',1,5),(110,'브리또',1,5),(111,'필라프',1,5),(112,'월남쌈',1,6),(113,'쌀국수',1,6),(114,'팟타이',1,6),(115,'딤섬',1,6),(116,'공원',2,7),(117,'사찰',2,7),(118,'유적지',2,7),(119,'체험',2,7),(120,'박물관',2,8),(121,'미술관',2,8),(122,'도서관',2,8),(123,'영화관',2,8),(124,'공연장',2,8),(125,'연극',2,9),(126,'뮤지컬',2,9),(127,'오페라',2,9),(128,'전시회',2,9),(129,'캠핑장',2,10),(130,'스케이트장',2,10),(131,'당구장',2,10),(132,'볼링장',2,10),(133,'PC방',2,11),(134,'노래방',2,11),(135,'카페',2,11),(136,'술집',2,11),(137,'라볶이',1,12),(138,'쫄볶이',1,12),(139,'어묵',1,13),(140,'냉면',1,12),(141,'비빔밥',1,14),(142,'칼국수',1,12),(143,'잔치국수',1,12),(144,'비빔국수',1,12),(145,'콩국수',1,12),(146,'쫄면',1,12),(147,'김밥',1,14),(148,'주먹밥',1,14),(149,'핫도그',1,15),(150,'김치볶음밥',1,14),(151,'육회',1,16),(152,'닭발',1,16),(153,'고등어구이',1,17),(154,'아구찜',1,17),(155,'해물찜',1,18),(156,'갈비',1,16),(157,'떡국',1,20),(158,'만두국,만둣국',1,20),(159,'추어탕',1,20),(160,'파전',1,22),(161,'김치전',1,22),(162,'대창',1,16),(163,'막창',1,16),(164,'곱창',1,16),(165,'주꾸미,쭈꾸미',1,18),(166,'찜닭',1,16),(167,'불고기',1,16),(168,'닭갈비',1,16),(169,'갈비찜',1,16),(170,'삼겹살',1,16),(171,'오겹살',1,16),(172,'제육',1,16),(173,'오징어볶음',1,18),(174,'낙지볶음',1,18),(175,'오리구이',1,16),(176,'닭볶음탕',1,16),(177,'갈비탕',1,20),(178,'돼지국밥',1,20),(179,'소고기국밥',1,20),(180,'육개장',1,20),(181,'감자탕',1,20),(182,'순대국밥',1,20),(183,'뼈해장국',1,20),(184,'곰탕',1,20),(185,'설렁탕',1,20),(186,'부대찌개',1,23),(187,'김치찌개',1,23),(188,'된장찌개',1,23),(189,'청국장찌개',1,23),(190,'삼계탕',1,20),(191,'순두부찌개',1,23),(192,'빈대떡',1,22),(193,'죽',1,14),(194,'돈까스,돈카츠',1,24),(195,'새우까스,새우카츠',1,24),(196,'생선까스',1,24),(197,'히레까스,히레카츠',1,24),(198,'로스까스,로스카츠',1,24),(199,'호르몬동',1,25),(200,'규동',1,25),(201,'사케동',1,25),(202,'가츠동',1,25),(203,'카레',1,25),(204,'소바',1,12),(205,'메밀',1,12),(206,'우동',1,12),(207,'라멘',1,12),(208,'나베,스키야키',1,16),(209,'초밥',1,14),(210,'회,우럭,광어,참치',1,13),(211,'타코야키,타코야끼',1,19),(212,'오코노미야키,오코노미야끼',1,22),(213,'샤브샤브',1,16),(214,'양장피',1,18),(215,'팔보채',1,18),(216,'유산슬',1,18),(217,'동파육',1,16),(218,'라조육',1,16),(219,'라조기',1,16),(220,'깐풍기',1,16),(221,'잡탕',1,18),(222,'해파리냉채',1,18),(223,'꿔바로우',1,16),(224,'칠리새우',1,16),(225,'탕수육',1,16),(226,'짜장면,자장면',1,12),(227,'짬뽕',1,12),(228,'울면',1,12),(229,'볶음밥',1,14),(230,'마라탕',1,12),(231,'마라샹궈',1,12),(232,'고추잡채',1,16),(233,'누룽지탕',1,18),(234,'양꼬치',1,16),(235,'치킨',1,16),(236,'피자',1,15),(237,'햄버거',1,15),(238,'파스타',1,12),(239,'까르보나라',1,12),(240,'리조또',1,14),(241,'스테이크',1,16),(242,'퀘사디아',1,15),(243,'브리또',1,15),(244,'필라프',1,14),(245,'쌀국수',1,12),(246,'팟타이',1,12),(247,'딤섬',1,26),(248,'해물찜',1,19),(249,'추어탕',1,21),(250,'주꾸미,쭈꾸미',1,19),(251,'오징어볶음',1,19),(252,'낙지볶음',1,19),(253,'갈비탕',1,21),(254,'돼지국밥',1,21),(255,'소고기국밥',1,21),(256,'육개장',1,21),(257,'감자탕',1,21),(258,'순대국밥',1,21),(259,'뼈해장국',1,21),(260,'곰탕',1,21),(261,'설렁탕',1,21),(262,'양장피',1,19),(263,'팔보채',1,19),(264,'유산슬',1,19),(265,'잡탕',1,19),(266,'해파리냉채',1,19),(267,'누룽지탕',1,19);
/*!40000 ALTER TABLE `category_s` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(8,'voice_recognition','authgroup'),(9,'voice_recognition','authgrouppermissions'),(10,'voice_recognition','authpermission'),(11,'voice_recognition','authuser'),(12,'voice_recognition','authusergroups'),(13,'voice_recognition','authuseruserpermissions'),(14,'voice_recognition','categoryl'),(15,'voice_recognition','categorym'),(16,'voice_recognition','categorys'),(17,'voice_recognition','djangoadminlog'),(18,'voice_recognition','djangocontenttype'),(19,'voice_recognition','djangomigrations'),(20,'voice_recognition','djangosession'),(7,'voice_recognition','post'),(21,'voice_recognition','voicerecognitionpost');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-03-16 13:55:45.961109'),(2,'auth','0001_initial','2020-03-16 13:55:48.801390'),(3,'admin','0001_initial','2020-03-16 13:55:49.557321'),(4,'admin','0002_logentry_remove_auto_add','2020-03-16 13:55:49.585248'),(5,'admin','0003_logentry_add_action_flag_choices','2020-03-16 13:55:49.603199'),(6,'contenttypes','0002_remove_content_type_name','2020-03-16 13:55:49.897418'),(7,'auth','0002_alter_permission_name_max_length','2020-03-16 13:55:50.180657'),(8,'auth','0003_alter_user_email_max_length','2020-03-16 13:55:50.276399'),(9,'auth','0004_alter_user_username_opts','2020-03-16 13:55:50.314298'),(10,'auth','0005_alter_user_last_login_null','2020-03-16 13:55:50.593556'),(11,'auth','0006_require_contenttypes_0002','2020-03-16 13:55:50.605558'),(12,'auth','0007_alter_validators_add_error_messages','2020-03-16 13:55:50.642419'),(13,'auth','0008_alter_user_username_max_length','2020-03-16 13:55:50.885906'),(14,'auth','0009_alter_user_last_name_max_length','2020-03-16 13:55:51.173049'),(15,'sessions','0001_initial','2020-03-16 13:55:51.328631'),(16,'voice_recognition','0001_initial','2020-03-16 13:55:51.724531'),(17,'voice_recognition','0002_auto_20200311_1301','2020-03-16 13:55:52.199255'),(18,'voice_recognition','0003_auto_20200311_1323','2020-03-16 13:55:52.734863'),(19,'voice_recognition','0004_auto_20200316_2321','2020-03-16 14:21:34.169151'),(20,'voice_recognition','0005_auto_20200316_2344','2020-03-16 14:44:37.636368');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `voice_recognition_post`
--

DROP TABLE IF EXISTS `voice_recognition_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `voice_recognition_post` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `voice_recognition_post`
--

LOCK TABLES `voice_recognition_post` WRITE;
/*!40000 ALTER TABLE `voice_recognition_post` DISABLE KEYS */;
INSERT INTO `voice_recognition_post` VALUES (1,'안녕하세요,여러분,이거,ㄹ,추천,하,아,드리,ㄹ게요,.'),(2,'안녕하세요,여러분,이거,ㄹ,추천,하,아,드리,ㄹ게요,.'),(3,'안녕하세요,여러분,이거,ㄹ,추천,하,아,드리,ㄹ게요,.'),(4,'떡볶이,라볶이,칼국수,여러분,이거,ㄹ,추천,하,아,드리,ㄹ게요,.'),(5,'떡볶이,라볶이,칼국수,여러분,이거,ㄹ,추천,하,아,드리,ㄹ게요,.'),(6,'떡볶이,라볶이,칼국수,여러분,이거,ㄹ,추천,하,아,드리,ㄹ게요,.'),(7,'떡볶이,라볶이,칼국수,여러분,이거,ㄹ,추천,하,아,드리,ㄹ게요,.');
/*!40000 ALTER TABLE `voice_recognition_post` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-19 17:03:09
