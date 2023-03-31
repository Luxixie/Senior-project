-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: sp01
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `company_profile`
--

DROP TABLE IF EXISTS `company_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company_profile` (
  `profile_id` int NOT NULL,
  `stock_id` int DEFAULT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  `website` varchar(100) DEFAULT NULL,
  `company_description` varchar(2000) DEFAULT NULL,
  PRIMARY KEY (`profile_id`),
  KEY `stock_id_idx` (`stock_id`),
  CONSTRAINT `stock_id` FOREIGN KEY (`stock_id`) REFERENCES `stock` (`stock_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company_profile`
--

LOCK TABLES `company_profile` WRITE;
/*!40000 ALTER TABLE `company_profile` DISABLE KEYS */;
INSERT INTO `company_profile` VALUES (1,1,'2S Metal Public Company Limited','8/5 Moo 14, Tambon Thachang','66 7 480 0111','https://www.ss.co.th','2S Metal Public Company Limited, together with its subsidiaries, manufactures and sells steel pipes, steel plates, light lip channels, and steel wire mesh products in Thailand. It operates through two segments, Production and Trading. The company offers galvanized steel pipes, equal angles, H-beams, I-beams, channel steel products, checkered plates, hot rolled coils, cold round bars, U-channels, cut and bend rebars, galvanized steel battens, annealing wires, steam pipes, welding electrodes, as well as flat bars, metal framework products, and C-line products. It also trades in steel products; and provides transportation services. The company was formerly known as Southern Steel Public Company Limited and changed its name to 2S Metal Public Company Limited in April 2010. 2S Metal Public Company Limited was founded in 1992 and is headquartered in Bang Klam, Thailand.'),(2,2,'Thai Energy Storage Technology Public Company Limited','387, Moo 4, Sukhumvit Road','66 2 709 3535','https://www.3kbattery.com','Thai Energy Storage Technology Public Company Limited manufactures and sells batteries in Thailand and internationally. It provides automotive, motorcycle, traction, EB, forklift, lighting, and golf cart batteries. The company was founded in 1986 and is headquartered in Mueang Samut Prakan, Thailand. Thai Energy Storage Technology Public Company Limited is a subsidiary of Sustainable Battery Solutions, Inc.'),(3,3,'Seven Utilities and Power Public Company Limited','73 Mahachol Building','66 2 741 5700','https://www.sevenup.co.th','Seven Utilities and Power Public Company Limited, together with its subsidiaries, engages in the LPG and oil distribution business in Thailand. It operates LPG stations and water treatment solutions; transports LPG; manages NGV gas stations; produces and distributes biogas electricity; produces and sells energy saving technology; imports and exports energy saving technology; and operates investment business. The company also distributes, develops, and services trunked radio and Internet of Things; and internal communication software. In addition, it is involved in the design, construction, installation, operation, and management of water resources and environmental engineering business; and provision of hazardous and non- hazardous industrial waste treatment services. The company was formerly known as Ferrum Public Company Limited and changed its name to Seven Utilities and Power Public Company Limited in April 2018. Seven Utilities and Power Public Company Limited was incorporated in 1995 and is headquartered in Bangkok, Thailand.'),(4,4,'Areeya Property Public Company Limited','999 Praditmanutham Road','66 2 798 9999','https://www.areeya.co.th','Areeya Property Public Company Limited, together with its subsidiaries, develops real estate projects in Thailand. It primarily develops single detached houses, twinhome, village towns, townhomes, home offices, and condominiums; and community malls. The company is also involved in the provision of after sales services for property; construction services; and property management services, as well as in the restaurant and hotels business. Areeya Property Public Company Limited was founded in 2000 and is headquartered in Bangkok, Thailand.'),(5,5,'Asian Alliance International Public Company Limited','55/2 Moo 2, Rama 2 Road','66 3 484 5575','https://www.asianalliance.co.th','Asian Alliance International Public Company Limited manufactures and sells pet food and ready-to-eat human food products in Thailand. It offers wet pet food products, such as soups, salads, fish and meat dishes, mousse, and pate, as well as granular pet food products for dogs and cats; and ready-to-eat human food products made of tuna, salmon, tilapia, sea bass, mackerel, and shrimp in sealed containers. The company was founded in 2005 and is based in Mueang Samut Sakhon, Thailand.'),(6,6,'Asia Aviation Public Company Limited','Central Office Building','66 2 562 5700','https://www.aavplc.com','Asia Aviation Public Company Limited, through its subsidiary, provides airline services in Thailand. The company operates through Scheduled Flight Operations and Charter Flight Operations segments. The Scheduled Flight Operations segment offers passenger air transportation services to routine destinations for scheduled flights. This segment sells tickets through its distribution channels, including website, sale counters, travel agents, etc. The Chartered Flight Operations segment provides passenger air transportation services to non-routine destinations that serves tourist agency companies. Asia Aviation Public Company Limited was founded in 2004 and is headquartered in Bangkok, Thailand.'),(7,7,'Advanced Connection Corporation Public Company Limited','944 Mitrtown Office Tower','66 2 219 1642','https://acc-plc.com','Advanced Connection Corporation Public Company Limited, together with its subsidiaries, operates in the infrastructure, financial, and cannabis businesses primarily in Thailand. It operates solar rooftop and farm projects. The company also operates in the banquet and restaurant, and property development businesses; and property rental of a factory building at Bangpu Industrial Estate. In addition, it provides factoring with recourse, hire purchase or leasing, and loan and mortgage services; and construction contracting services. Further, the company is involved in the trading business; research, development, production, cultivation, and processing of cannabis; and development of an e-commerce system for online marketing. The company was formerly known as Compass East Industry (Thailand) Public Company Limited and changed its name to Advanced Connection Corporation Public Company Limited in November 2015. Advanced Connection Corporation Public Company Limited was incorporated in 1987 and is headquartered in Bangkok, Thailand.'),(8,8,'Absolute Clean Energy Public Company Limited','140/6 ITF Tower','66 1 104 8821','https://www.ace-energy.co.th','Absolute Clean Energy Public Company Limited, together with its subsidiaries, operates biomass, municipal solid waste, natural gas, and solar energy power plants in Thailand. The company operates through four segments: Biomass Power Plants, Solid Waste Power Plant, Natural Gas Power Plant, and Solar Energy Power Plant. As of December 31, 2021, it has 23 power plants with an installed capacity of 257.57 megawatts. Absolute Clean Energy Public Company Limited was incorporated in 2015 and is headquartered in Bangkok, Thailand.'),(9,9,'Autocorp Holding Public Company Limited','1111, Moo 1, Maliwan Road','66 4 330 6444','https://www.ach.co.th','Autocorp Holding Public Company Limited, a dealer, distributes cars and spare parts in Thailand. It also offers car leasing and insurance services; and maintenance, repair, and after sale services. The company was founded in 2015 and is headquartered in Khon Kaen, Thailand.'),(10,10,'Advanced Info Service Public Company Limited','414 AIS Tower 1','66 2 029 5000','https://www.ais.th','Advanced Info Service Public Company Limited, together its subsidiaries, provides mobile network, fixed broadband, and digital services primarily in Thailand. The company operates through three segments: Mobile Phone Services, Mobile Phone and Equipment Sales, and Datanet and Broadband Services. It is involved in the operation of cellular telephone networks in the frequency of 26 GHz, 700 MHz, 900 MHz, 1800 MHz, 2100 MHz, and 2600 MHz frequencies. The company also distributes handsets, as well as cash cards; and electronic money and electronic payment services. In addition, it provides international telephone service, broadcasting network, and television broadcasting services for various channels, as well as insurance brokerage services. Further, the company offers IT system, content aggregator, and billing and collection outsourcing services; call center services; and land and building rental services, as well as related facilities. Additionally, it provides internet data center, and internet and satellite uplink-downlink services for communications; distributes internet equipment; publishes telephone directories and advertising; offers mobile contents; and provides training and online advertising services. The company was founded in 1986 and is headquartered in Bangkok, Thailand.'),(11,11,'AEON Thana Sinsap (Thailand) Public Company Limited','388, Exchange Tower','66 2 689 7197','https://www.aeon.co.th','AEON Thana Sinsap (Thailand) Public Company Limited provides various retail finance services in Thailand. The company operates through Retail Finance Services and Other Business segments. It offers credit card, hire purchase, personal loans, and other services. The company also provides debt collection and insurance brokerage services. As of February 28, 2022, it had 101 branches. The company was incorporated in 1992 and is headquartered in Bangkok, Thailand. AEON Thana Sinsap (Thailand) Public Company Limited is a subsidiary of AEON Bank, Ltd.'),(12,12,'Asia Fiber Public Company Limited','Wall Street Tower','66 2 632 7071','https://www.asiafiber.com','Asia Fiber Public Company Limited manufactures and sells nylon products in Thailand. The company operates through four segments: Nylon Chip, Filament Yarn, Textured Yarn, and Other. It offers nylon chips, nylon filament yarns, nylon textured yarns, nylon taffeta fabrics, grey fabrics, and dyed and finished fabrics, as well as provides other services. The company also exports its products. Asia Fiber Public Company Limited was incorporated in 1970 and is headquartered in Bangkok, Thailand.'),(13,13,'Asia Green Energy Public Company Limited','273/1 Rama 2 Road','66 2 894 0088','https://www.agecoal.com','Asia Green Energy Public Company Limited engages in the distribution of coal for industrial use in Thailand. It also provides transportation and management, water transportation and port, and cargo services, as well as consultancy services for coal extraction and water transportation. In addition, the company generates and supplies electricity; and distributes fuel. It also imports and exports coal. It serves power plants, steel plants, cement plants, and paper factories; and industrial factories relating to textile, food, rubber, and alternative energy products. The company exports coal to China, India, Vietnam, and Taiwan. Asia Green Energy Public Company Limited was founded in 2004 and is headquartered in Bangkok, Thailand.'),(14,14,'AAPICO Hitech Public Company Limited','99 Moo 1 Hitech Industrial Estate','66 3 535 0880','https://www.aapico.com','AAPICO Hitech Public Company Limited engages in the manufacture and distribution of automobile parts, dies, and jigs in Thailand, China, Malaysia, and Portugal. It operates in three segments: Manufacture of Auto Parts; Sales of Automobiles and Provision of Automobiles Repair Service; and Others. The company offers stamped or pressed parts, including chassis frame components, housing axles parts, pressed and stamped body parts, door check link, and brake lines, fuel lines, engine, and brazing parts; forged and machined parts, such as transmission, power train, steering and suspension systems, engine, shafts, wheel hubs, and other parts, as well as connecting rods and copper forged parts; and plastic parts and plastic fuel tanks. It also provides roof ditch mouldings, belt line mouldings, door sash products, brazed steel tubing, door checks and hinges, and parking brake lever products; assembly jigs; and stamping dies. In addition, the company is involved in the sale of automobiles; provision of automobile repair, training, technical support, and information technology consulting and advisory services; venture capital business; investment in other companies; and import and export of vehicles and parts. Further, it manufactures 3D car navigation and digital map solutions under the POWERMAP brand with voice activation software, as well as Oracle ERP systems; and operates car dealership service centers. The company was founded in 1996 and is headquartered in Phra Nakhon Si Ayutthaya, Thailand.'),(15,15,'Aikchol Hospital Public Company Limited','68/3 Moo 2','66 3 827 3840','https://www.aikchol.com','Aikchol Hospital Public Company Limited provides medical and nursing care services under the Aikchol Hospital trademark in Thailand. The company offers various hospital services comprising diseases protection, medical treatment, health strengthening, and health rehabilitation services with 310 beds in service. It serves primarily individuals, group of policyholders of the insurance company, group of contract parties\' company, and group of insured on social security. Aikchol Hospital Public Company Limited was founded in 1978 is headquartered in Chonburi, Thailand.'),(16,16,'Asian Insulators Public Company Limited','254 Seri Thai Road','66 2 517 1451','https://www.asianinsulators.com','Asian Insulators Public Company Limited, together with its subsidiaries, manufactures and distributes porcelain insulators products for electricity distribution and transmission in Thailand. It offers spool, strain, line post type, pin post type, suspension, station post type, cleat, porcelain, and horizontal mounting solid core line post insulators; and underground cable support products, as well as ceramic glazed porcelain cable spacers. The company also provides services for design, supply, and installation of high voltage substation, distribution, and transmission line systems; and project management, industrial maintenance, construction, and engineering services to the water, power, and communications industries. It is also involved in producing and distributing biodiesel, vegetable oil, and animal oil fats; and exporting vegetable oil under the Pamola brand. In addition, it trades in electrical equipment. Asian Insulators Public Company Limited was founded in 1981 and is headquartered in Bangkok, Thailand.'),(17,17,'AI Energy Public Company Limited','55/2 Moo 8 Sethakit 1 Road','66 3 487 7485','https://www.aienergy.co.th','AI Energy Public Company Limited produces and distributes bio diesel, and vegetable/animal oil and fats. The company also offers refined glycerin; and palm fatty acid distillate and glycerin pitch, as well as domestic and international logistics services for passengers, merchandise, parcels, and other materials. It also provides port and terminal services; and storage tank farm rental services. The company was incorporated in 2006 and is headquartered in Samut Sakhon, Thailand. AI Energy Public Company Limited is a subsidiary of Asian Insulators Public Company Limited.'),(18,18,'AIM Commercial Growth Freehold And Leasehold Real Estate Investment Trust','Unit 803, 8th Floor','66 2254 0441 2','https://www.aimcgreit.com/en',NULL),(19,19,'AIM Industrial Growth Freehold and Leasehold Real Estate Investment Trust','62 The Millennia Tower','66 2 254 0441','https://www.aimirt.com','AIM Industrial Growth Freehold and Leasehold Real Estate Investment Trust focuses on investing in freehold right of land, cold storage buildings, and immovable assets related to cold storage and warehouses in Thailand. These are located in Samut Sakhon and Chachoengsao areas with total leasable area of 36,908.00 sq.m. It also intends to invest in freehold right of land and warehouses, including 5 units of warehouses with total leasable area of 21,651 sq.m. in Bang Phi, Samut Prakan. The company is based in Bangkok, Thailand.'),(20,20,'Advanced Information Technology Public Company Limited','37/2 Suthisarnvinijchai Road','66 2 275 9400','https://www.ait.co.th','Advanced Information Technology Public Company Limited, together with its subsidiaries, designs, sells, installs, services, repairs, maintains, and trains information and communication technology network systems in Thailand. The company operates in two segments, Sales and Service, and Rental of Equipment. It provides solutions, including carrier grade router/switch, Web/video caching, DDOS protection, software-defined networking or the network controlled by the program to work as defined, network function virtualization, and other. The company also offers data center and cloud solutions, such as consolidation and virtualization, unified data center, converged and hyper converged infrastructure, private and public cloud infrastructure, software-defined networking or the network controlled by the program, and other. In addition, it provides collaboration solutions comprising communication through IP/VoIP system or unified communication, video and Web conferencing, contact center, and others; and various enterprise network solutions consisting of router, switch, wireless LAN, WAN optimization, security, application delivery control, DNS server, identity system, network management, and other. Further, the company offers the services in the development of information technology systems to various projects with the combination of concepts in applying technology with the framework in developing the system accordingly. Additionally, it provides managed services managing complicated IT system; and maintenance service on checking the operational condition of the system, which enables the system to operate continually and reduce the downtime period, and preventing problem to occur simultaneously, as well as spare parts for saving the time in solving the problem and mitigating the risks from the damage of equipment. The company was founded in 1992 and is headquartered in Bangkok, Thailand.');
/*!40000 ALTER TABLE `company_profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-17 14:17:36