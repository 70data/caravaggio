/*
SQLyog Ultimate v11.27 (32 bit)
MySQL - 5.7.25 : Database - service_tree
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`service_tree` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `service_tree`;

/*Table structure for table `tree_asset` */

DROP TABLE IF EXISTS `tree_asset`;

CREATE TABLE `tree_asset` (
  `asset_id` int(6) NOT NULL AUTO_INCREMENT,
  `asset_type` varchar(50) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  `asset_identity` varchar(50) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`asset_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

/*Data for the table `tree_asset` */

insert  into `tree_asset`(`asset_id`,`asset_type`,`asset_identity`) values (24,'阿里云','dev01.bj.aliyun'),(25,'阿里云','dev02.bj.aliyun'),(29,'腾讯云','dev01.bj.qcloud'),(30,'腾讯云','dev02.bj.qcloud');

/*Table structure for table `tree_correlation` */

DROP TABLE IF EXISTS `tree_correlation`;

CREATE TABLE `tree_correlation` (
  `correlation_id` int(6) NOT NULL AUTO_INCREMENT,
  `node_name` varchar(50) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  `asset_identity` varchar(50) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`correlation_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

/*Data for the table `tree_correlation` */

insert  into `tree_correlation`(`correlation_id`,`node_name`,`asset_identity`) values (35,'p2p.api.php','dev01.bj.aliyun'),(36,'p2p.db.mysql','dev02.bj.aliyun');

/*Table structure for table `tree_node` */

DROP TABLE IF EXISTS `tree_node`;

CREATE TABLE `tree_node` (
  `node_id` int(5) NOT NULL AUTO_INCREMENT,
  `node_name` varchar(100) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  `node_upstream_name` varchar(100) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  `node_description` varchar(100) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`node_id`) USING BTREE,
  UNIQUE KEY `node_name` (`node_name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

/*Data for the table `tree_node` */

insert  into `tree_node`(`node_id`,`node_name`,`node_upstream_name`,`node_description`) values (1,'p2p','',''),(2,'p2p.api','p2p',''),(4,'p2p.api.php','p2p.api',''),(5,'p2p.db','p2p',''),(6,'p2p.db.mysql','p2p.db',''),(8,'im','',''),(9,'im.api','im',''),(17,'im.api.golang','im.api',''),(18,'im.api.java','im.api',''),(19,'p2p.api.java','p2p.api','');

/*Table structure for table `tree_resource` */

DROP TABLE IF EXISTS `tree_resource`;

CREATE TABLE `tree_resource` (
  `resource_id` int(6) NOT NULL AUTO_INCREMENT,
  `asset_id` int(5) NOT NULL DEFAULT '0',
  `resource_name` varchar(10) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  `resource_tag` varchar(10) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  `resource_value` varchar(100) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`resource_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

/*Data for the table `tree_resource` */

insert  into `tree_resource`(`resource_id`,`asset_id`,`resource_name`,`resource_tag`,`resource_value`) values (31,24,'CPU','size','6'),(32,24,'Memory','size','8192'),(33,24,'OS','version','CentOS 7.5'),(34,24,'Kernel','version','4.19'),(35,24,'eth0','ip','10.10.10.1'),(36,24,'eth0','speed','1000'),(37,24,'/sda','size','20'),(38,25,'CPU','size','8'),(39,25,'Memory','size','16384'),(40,25,'OS','version','CentOS 7.2'),(41,25,'Kernel','version','4.15'),(42,25,'eth1','ip','10.10.10.2'),(43,25,'eth1','speed','10000'),(44,25,'/sdb','size','50');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
