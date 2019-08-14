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

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `permission_id` int(6) NOT NULL AUTO_INCREMENT,
  `server_name` varchar(50) COLLATE utf8_swedish_ci NOT NULL,
  `method` varchar(10) COLLATE utf8_swedish_ci NOT NULL,
  `url` varchar(100) COLLATE utf8_swedish_ci NOT NULL,
  PRIMARY KEY (`permission_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`permission_id`,`server_name`,`method`,`url`) values (51,'tree','GET','/tree/node/downstream/'),(54,'tree','GET','/tree/node/'),(55,'tree','GET','/tree/asset/');

/*Table structure for table `auth_role` */

DROP TABLE IF EXISTS `auth_role`;

CREATE TABLE `auth_role` (
  `role_id` int(6) NOT NULL AUTO_INCREMENT,
  `role_name` varchar(20) COLLATE utf8_swedish_ci NOT NULL,
  `role_description` varchar(100) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`role_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

/*Data for the table `auth_role` */

insert  into `auth_role`(`role_id`,`role_name`,`role_description`) values (51,'admin','tree'),(52,'dev','tree');

/*Table structure for table `auth_role_permission` */

DROP TABLE IF EXISTS `auth_role_permission`;

CREATE TABLE `auth_role_permission` (
  `role_id` int(6) NOT NULL,
  `permission_id` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

/*Data for the table `auth_role_permission` */

insert  into `auth_role_permission`(`role_id`,`permission_id`) values (51,51),(51,54),(51,55);

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `user_id` int(6) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(20) COLLATE utf8_swedish_ci NOT NULL,
  `mail` varchar(100) COLLATE utf8_swedish_ci NOT NULL,
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`user_id`,`user_name`,`mail`) values (50,'yuchang','70data@gamil.com');

/*Table structure for table `auth_user_role` */

DROP TABLE IF EXISTS `auth_user_role`;

CREATE TABLE `auth_user_role` (
  `user_id` int(6) NOT NULL,
  `server_name` varchar(100) COLLATE utf8_swedish_ci NOT NULL,
  `role_id` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

/*Data for the table `auth_user_role` */

insert  into `auth_user_role`(`user_id`,`server_name`,`role_id`) values (50,'tree',51);

/*Table structure for table `tree_asset` */

DROP TABLE IF EXISTS `tree_asset`;

CREATE TABLE `tree_asset` (
  `asset_id` int(6) NOT NULL AUTO_INCREMENT,
  `asset_source` varchar(50) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  `asset_type` varchar(50) COLLATE utf8_swedish_ci NOT NULL,
  `asset_identity` varchar(50) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  `asset_description` varchar(100) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`asset_id`) USING BTREE,
  UNIQUE KEY `index_asset_identity` (`asset_identity`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

/*Data for the table `tree_asset` */

insert  into `tree_asset`(`asset_id`,`asset_source`,`asset_type`,`asset_identity`,`asset_description`) values (24,'阿里云','virtual_machine','dev01.bj.aliyun','dev01.bj.aliyun'),(25,'阿里云','virtual_machine','dev02.bj.aliyun',''),(29,'腾讯云','virtual_machine','dev01.bj.qcloud',''),(30,'腾讯云','virtual_machine','dev02.bj.qcloud','');

/*Table structure for table `tree_correlation` */

DROP TABLE IF EXISTS `tree_correlation`;

CREATE TABLE `tree_correlation` (
  `correlation_id` int(6) NOT NULL AUTO_INCREMENT,
  `node_name` varchar(50) COLLATE utf8_swedish_ci NOT NULL,
  `asset_id` int(6) NOT NULL,
  PRIMARY KEY (`correlation_id`) USING BTREE,
  KEY `index_node_name` (`node_name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

/*Data for the table `tree_correlation` */

insert  into `tree_correlation`(`correlation_id`,`node_name`,`asset_id`) values (35,'p2p.api.php',24),(36,'p2p.db.mysql',25);

/*Table structure for table `tree_node` */

DROP TABLE IF EXISTS `tree_node`;

CREATE TABLE `tree_node` (
  `node_id` int(5) NOT NULL AUTO_INCREMENT,
  `node_name` varchar(100) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  `node_upstream_name` varchar(100) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  `node_description` varchar(100) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`node_id`) USING BTREE,
  UNIQUE KEY `index_node_name` (`node_name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

/*Data for the table `tree_node` */

insert  into `tree_node`(`node_id`,`node_name`,`node_upstream_name`,`node_description`) values (1,'p2p','',''),(2,'p2p.api','p2p',''),(4,'p2p.api.php','p2p.api',''),(5,'p2p.db','p2p',''),(6,'p2p.db.mysql','p2p.db',''),(8,'im','',''),(9,'im.api','im',''),(17,'im.api.golang','im.api',''),(18,'im.api.java','im.api',''),(19,'p2p.api.java','p2p.api','');

/*Table structure for table `tree_resource` */

DROP TABLE IF EXISTS `tree_resource`;

CREATE TABLE `tree_resource` (
  `resource_id` int(6) NOT NULL AUTO_INCREMENT,
  `asset_id` int(5) NOT NULL DEFAULT '0',
  `resource_type` varchar(10) COLLATE utf8_swedish_ci NOT NULL,
  `resource_name` varchar(10) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  `resource_tag` varchar(10) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  `resource_value` varchar(100) COLLATE utf8_swedish_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`resource_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8 COLLATE=utf8_swedish_ci;

/*Data for the table `tree_resource` */

insert  into `tree_resource`(`resource_id`,`asset_id`,`resource_type`,`resource_name`,`resource_tag`,`resource_value`) values (31,24,'CPU','CPU','size','6'),(32,24,'Memory','Memory','size','8192'),(33,24,'OS','OS','version','CentOS 7.5'),(34,24,'OS','Kernel','version','4.19'),(35,24,'Network','eth0','ip','10.10.10.1'),(36,24,'Network','eth0','speed','1000'),(37,24,'Disk','/sda','size','20'),(38,25,'Memory','CPU','size','8'),(39,25,'Memory','Memory','size','16384'),(40,25,'OS','OS','version','CentOS 7.2'),(41,25,'OS','Kernel','version','4.15'),(42,25,'Network','eth1','ip','10.10.10.2'),(43,25,'Network','eth1','speed','10000'),(44,25,'Disk','/sdb','size','50');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
