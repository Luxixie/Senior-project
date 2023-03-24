from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'tester'

mysql = MySQL(app)

company_profiles = {
    # 1-20
    '2S.BK': {
        'name': '2S Metal Public Company Limited',
        'address': 'No. 8/5 Moo 14, Tha-chang Bang Klam 90110 Thailand',
        'phone': '66 7 480 0111',
        'website': 'https://www.ss.co.th',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': '2S Metal Public Company Limited, together with its subsidiaries, engages in the production and distribution of steel products in Thailand. It operates through two segments, Production and Trading. The company offers galvanized steel pipes, equal angles, H-beams, I-beams, channel steel, gutters, bars, checkered plates, hot rolled coils, deformed bars, cold round bars, C- and U-channels, light lip channels, cut and bend rebars, galvanized steel battens, annealing wires, and chain link and crimped wire meshes, as well as flat bars, metal framework products, and C-line products. It also trades in steel products; and provides transportation services. The company was formerly known as Southern Steel Public Company Limited and changed its name to 2S Metal Public Company Limited in April 2010. 2S Metal Public Company Limited was founded in 1992 and is headquartered in Bang Klam, Thailand.'
    },
    '3K-BAT.BK': {
        'name': 'Thai Energy Storage Technology Public Company Limited',
        'address': '387, Moo 4, Sukhumvit Road Phraek Sa Sub-district Mueang Samut Prakan 10280 Thailand',
        'phone': '66 2 709 3535',
        'website': 'https://www.3kbattery.com',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'Thai Energy Storage Technology Public Company Limited manufactures and distributes batteries in Thailand and internationally. It provides automotive, motorcycle, traction, EB, forklift, lighting, and golf cart batteries. The company was founded in 1986 and is based in Mueang Samut Prakan, Thailand. Thai Energy Storage Technology Public Company Limited is a subsidiary of Sustainable Battery Solutions, Inc.'
    },
    '7UP.BK': {
        'name': 'Seven Utilities and Power Public Company Limited',
        'address': '73 Mahachol Building Soi Sukhumvit 62 Sukhumvit Road Prakhanong Tai, Prakhanong Bangkok 10260 Thailand',
        'phone': '66 2 741 5700',
        'website': 'https://www.sevenup.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Specialty Retail',
        'description': 'Seven Utilities and Power Public Company Limited, together with its subsidiaries, operates as a renewable energy and public utility company in Thailand. It operates LPG stations and water treatment solutions; transports LPG; manages NGV gas stations; and produces and distributes biogas electricity. The company is also involved in the design, construction, installation, operation, and management of water resources and environmental engineering business; and provision of hazardous and non- hazardous industrial waste treatment services. The company was formerly known as Ferrum Public Company Limited and changed its name to Seven Utilities and Power Public Company Limited in April 2018. Seven Utilities and Power Public Company Limited was incorporated in 1995 and is headquartered in Bangkok, Thailand.'
    },
    'A.BK': {
        'name': 'Areeya Property Public Company Limited',
        'address': '999 Praditmanutham Road Saphansong Wangthonglang Bangkok 10310 Thailand',
        'phone': '66 2 798 9999',
        'website': 'https://www.areeya.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Areeya Property Public Company Limited, together with its subsidiaries, develops real estate projects in Thailand. It primarily develops single detached houses, twinhome, village towns, townhomes, home offices, and condominiums; and community malls. The company is also involved in the provision of after sales services for property; construction services; and property management services, as well as in the restaurant and hotels business. Areeya Property Public Company Limited was founded in 2000 and is headquartered in Bangkok, Thailand.'
    },
    'AAI.BK': {
        'name': 'Asian Alliance International Public Company Limited',
        'address': '55/2 Moo 2, Rama 2 Road Bang Krachao Subdistrict Mueang District Mueang Samut Sakhon 74000Thailand',
        'phone': '66 3 484 5575-87',
        'website': 'https://www.asianalliance.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Asian Alliance International Public Company Limited manufactures and sells pet food and ready-to-eat human food products in Thailand. It offers wet pet food products, such as soups, salads, fish and meat dishes, mousse, and pate, as well as dry pet food products for dogs and cats under the monchou, monchou balanced, Hajiko, and PRO brand names ; and ready-to-eat human food products made of tuna, salmon, tilapia, sea bass, mackerel, and shrimp in sealed containers. The company was founded in 2005 and is based in Mueang Samut Sakhon, Thailand.'
    },
    'AAV.BK': {
        'name': 'Asia Aviation Public Company Limited',
        'address': 'Central Office Building Room No. 3200, 3rd Floor No.222, Don Mueang International Airport Vibhavadee Rangsit Road, Don Mueang Bangkok 10210 Thailand',
        'phone': '66 2 562 5700',
        'website': 'https://www.aavplc.com',
        'sector': 'Industrials',
        'industry': 'Airlines',
        'description': 'Asia Aviation Public Company Limited provides airline services in Thailand. The company operates through Scheduled Flight Operations and Charter Flight Operations segments. The Scheduled Flight Operations segment offers passenger air transportation services to routine destinations for scheduled flights. This segment sells tickets through its distribution channels, including website, sale counters, travel agents, etc. The Chartered Flight Operations segment provides passenger air transportation services to non-routine destinations that serves tourist agency companies. It also operates an academy institution of learning and competency development for aviation tourism and hospitality industries. Asia Aviation Public Company Limited was founded in 2004 and is headquartered in Bangkok, Thailand.'
    },
    'ACC.BK': {
        'name': 'Advanced Connection Corporation Public Company Limited',
        'address': '944 Mitrtown Office Tower 16th Floor Rama 4 Road, Wangmai Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 219 1642',
        'website': 'https://acc-plc.com',
        'sector': 'Industrials',
        'industry': 'Conglomerates',
        'description': 'Advanced Connection Corporation Public Company Limited, together with its subsidiaries, operates in the infrastructure, financial, and cannabis businesses primarily in Thailand. It operates solar rooftop and farm projects. The company also operates in the banquet and restaurant, and property development businesses; and property rental. In addition, it provides consignment and non-performing loan services; financing and factoring; and construction contracting services. Further, the company is involved in the trading business; research, development, production, cultivation, processing, import, distribution, and export of cannabis; and development of an e-commerce system for online marketing. Additionally, it is engaged in manufacturing and distribution of ceiling fan; and production and distribution of electricity from solar power. The company was formerly known as Compass East Industry (Thailand) Public Company Limited and changed its name to Advanced Connection Corporation Public Company Limited in November 2015. Advanced Connection Corporation Public Company Limited was incorporated in 1987 and is headquartered in Bangkok, Thailand.'
    },
    'ACE.BK': {
        'name': 'Absolute Clean Energy Public Company Limited',
        'address': '140/6 ITF Tower 7th Floor Silom Road Suriyawong, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 233 2559',
        'website': 'https://www.ace-energy.co.th',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'Absolute Clean Energy Public Company Limited, together with its subsidiaries, operates biomass, municipal solid waste, natural gas, and solar energy power plants in Thailand. The company operates through four segments: Biomass Power Plants, Solid Waste Power Plant, Natural Gas Power Plant, and Solar Energy Power Plant. As of December 31, 2021, it has 23 power plants with an installed capacity of 257.57 megawatts. Absolute Clean Energy Public Company Limited was incorporated in 2015 and is headquartered in Bangkok, Thailand.'
    },
    'ACG.BK': {
        'name': 'Autocorp Holding Public Company Limited',
        'address': '1111, Moo 1, Maliwan Road Ban Thum Mueang Khon Kaen Khon Kaen 40000 Thailand',
        'phone': '66 4 330 6333',
        'website': 'https://www.ach.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Auto & Truck Dealerships',
        'description': 'Autocorp Holding Public Company Limited, a investment holding company, operates in distribution of cars and spare parts, and services center dealership in Thailand. It operates through Cars and accessories dealership, and Repair and maintenance service and spare parts dealership segments. The company also engages in manufacturing and distribution of Honda cars including selecting a dealer, setting price policies, and organize promotional programs, as well as supply orders from dealers. In addition, it offers oil changes, tires, maintenance of brake systems, batteries, shock absorbers, suspensions, and air conditioning systems, as well as suggestion for car insurance services. The company was founded in 2015 and is headquartered in Khon Kaen, Thailand.'
    },
    'ADVANC.BK': {
        'name': 'Advanced Info Service Public Company Limited',
        'address': '414 AIS Tower 1 Phaholyothin Road Samsen Nai Phayathai Bangkok 10400 Thailand',
        'phone': '66 2 029 5000',
        'website': 'https://www.ais.th',
        'sector': 'Communication Services',
        'industry': 'Telecom Services',
        'description': 'Advanced Info Service Public Company Limited, together its subsidiaries, provides mobile network, fixed broadband, and digital services primarily in Thailand. The company operates through three segments: Mobile Phone Services, Mobile Phone and Equipment Sales, and Datanet and Broadband Services. It is involved in the operation of cellular telephone networks. The company also distributes handsets, as well as cash cards; and electronic money and electronic payment services. In addition, it provides international telephone service, broadcasting network, and television broadcasting services for various channels, as well as insurance brokerage services. Further, the company offers IT system, content aggregator, and billing and collection outsourcing services; call center services; and land and building rental services, as well as related facilities. Additionally, it provides internet data center, and internet and satellite uplink-downlink services for communications; distributes internet equipment; publishes telephone directories and advertising; offers mobile contents; and provides training and online advertising services. The company was founded in 1986 and is headquartered in Bangkok, Thailand.'
    },
    'AEONTS.BK': {
        'name': 'AEON Thana Sinsap (Thailand) Public Company Limited',
        'address': '388, Exchange Tower 27th Floor Sukhumvit Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 665 0123',
        'website': 'https://www.aeon.co.th',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'AEON Thana Sinsap (Thailand) Public Company Limited provides various retail finance services in Thailand. The company operates through Retail Finance Services and Other Business segments. It offers credit card, hire purchase, personal loans, and other services. The company also provides debt collection and insurance brokerage services. As of February 28, 2022, it had 101 branches. The company was incorporated in 1992 and is headquartered in Bangkok, Thailand. AEON Thana Sinsap (Thailand) Public Company Limited is a subsidiary of AEON Bank, Ltd.'
    },
    'AFC.BK': {
        'name': 'Asia Fiber Public Company Limited',
        'address': 'Wall Street Tower 27th Floor 33/133-136 Surawongse Road Suriyawongse, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 632 7071-79',
        'website': 'https://www.asiafiber.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Textile Manufacturing',
        'description': 'Asia Fiber Public Company Limited manufactures and sells nylon products in Thailand. The company offers nylon chips, filament, textured, and recycled textured yarns, as well as nylon taffeta fabrics. It also provides daily use products, which include threads, fishing nets, ropes, ribbons, carpets, elastic tapes, gauzes, gloves, socks, laces, and swim wears, as well as brassier tapes, flags, garments and jackets, pants and tracksuits, bags, luggages, and umbrellas. The company was incorporated in 1970 and is headquartered in Bangkok, Thailand.'
    },
    'AGE.BK': {
        'name': 'Asia Green Energy Public Company Limited',
        'address': '273/1 Rama 2 Road Samaedam Bangkhunthian Bangkok 10150 Thailand',
        'phone': '66 2 894 0088',
        'website': 'https://www.age.co.th/',
        'sector': 'Energy',
        'industry': 'Thermal Coal',
        'description': 'Asia Green Energy Public Company Limited engages in the distribution of coal business in Thailand. It offers coal transportation and jetty services. The company provides boiler and chartering services, as well as involved in sourcing of steam coal activities. It also engages in export business. Asia Green Energy Public Company Limited was founded in 2004 and is based in Bangkok, Thailand.'
    },
    'AH.BK': {
        'name': 'AAPICO Hitech Public Company Limited',
        'address': '99 Moo 1 Hitech Industrial Estate Tambol Ban Lane Ampur Bang Pa-in Phra Nakhon Si Ayutthaya 13160 Thailand',
        'phone': '66 3 535 0880',
        'website': 'https://www.aapico.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Auto Parts',
        'description': 'AAPICO Hitech Public Company Limited engages in the manufacture and distribution of automobile parts, dies, and jigs in Thailand, China, Malaysia, and Portugal. It operates in three segments: Manufacture of Auto Parts; Sales of Automobiles and Provision of Automobiles Repair Service; and Others. The company offers stamped and pressed parts, including floor parts, cross members, side sills, brackets, clips, and sub-assembly parts; chassis frame components; housing axles parts; forged and machined parts, such as transmission, power train, steering and suspension systems, engine, shafts, wheel hubs, and other parts, as well as camber link for chassis systems, braking pawn for braking systems, copper forged parts; and plastic parts and plastic fuel tanks. It also provides casting parts; assembly jigs; and stamping dies. In addition, the company is involved in the sale of automobiles; provision of automobile repair, training, technical support, and information technology consulting and advisory services; venture capital business; investment in other companies; and import and export of vehicles and parts. Further, it manufactures car navigation systems and digital map solutions, as well as Oracle ERP systems; car accessories; and operates car dealership service centers. The company was founded in 1996 and is headquartered in Phra Nakhon Si Ayutthaya, Thailand.'
    },
    'AHC.BK': {
        'name': 'Aikchol Hospital Public Company Limited',
        'address': '68/3 Moo 2 Phrayasatja Road Amphoe Muang Chonburi 20000 Thailand',
        'phone': '66 38 939 999',
        'website': 'https://www.aikchol.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Aikchol Hospital Public Company Limited provides medical and nursing care services under the Aikchol Hospital trademark in Thailand. The company offers various hospital services comprising disease protection, medical treatment, health strengthening, and health rehabilitation services with 310 beds in service. It serves primarily individuals, group of policyholders of the insurance company, group of contract parties companies, and group of insured on social security. Aikchol Hospital Public Company Limited was founded in 1978 and is headquartered in Chonburi, Thailand.'
    }
    ,
    'AI.BK': {
        'name': 'Asian Insulators Public Company Limited',
        'address': '254 Seri Thai Road Kannayaow Bangkok 10230 Thailand',
        'phone': '66 2 517 1451',
        'website': 'https://www.asianinsulators.com',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'Asian Insulators Public Company Limited, together with its subsidiaries, manufactures and distributes porcelain insulators products for electricity distribution and transmission in Thailand. It offers spool, strain, line post type, pin post type, suspension, station post type, cleat, porcelain, and horizontal mounting solid core line post insulators; and underground cable support products, as well as ceramic glazed porcelain cable spacers. The company also provides services for design, supply, and installation of high voltage substation, distribution, and transmission line systems; and project management, industrial maintenance, construction, and engineering services to the water, power, and communications industries. It is also involved in producing and distributing biodiesel, vegetable oil, and animal oil fats; and exporting vegetable oil under the Pamola brand. In addition, it trades in electrical equipment, as well as provides port services. Asian Insulators Public Company Limited was founded in 1981 and is headquartered in Bangkok, Thailand.'
    },
    'AIE.BK': {
        'name': 'AI Energy Public Company Limited',
        'address': '55/2 Moo 8 Sethakit 1 Road Tambol Klongmadua Amphur Krathum Baen Samut Sakhon 74110 Thailand',
        'phone': '66 3 487 7485-8',
        'website': 'https://www.aienergy.co.th',
        'sector': 'Energy',
        'industry': 'Oil & Gas Refining & Marketing',
        'description': 'AI Energy Public Company Limited produces and distributes bio diesel and vegetable oil in Thailand. It also offers refined glycerin; and palm fatty acid distillate and glycerin pitch. The company was incorporated in 2006 and is headquartered in Samut Sakhon, Thailand. AI Energy Public Company Limited is a subsidiary of Asian Insulators Public Company Limited.'
    },
    'AIMCG.BK': {
        'name': 'AIM Commercial Growth Freehold And Leasehold Real Estate Investment Trust',
        'address': 'Unit 803, 8th Floor Tower B, GPF Witthayu Building, No. 93/1 Witthayu Road, Lumpini Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2254 0441-2',
        'website': 'https://www.aimcgreit.com/en',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'Investing in the leasehold and sublease rights of land and buildings consisting of 3 projects namely UD Town Project, 72 Courtyard Project and Porto Chino Project, and the ownership right in condominium for commercial use in Noble Solo Project.'
    #description from SET, sector & industry same with AIMIRT.BK
    },
    'AIMIRT.BK': {
        'name': 'AIM Industrial Growth Freehold and Leasehold Real Estate Investment Trust',
        'address': 'Unit 803, 8th floor,Tower B, GPF Witthayu Building, No. 93/1, Witthayu Road, Lumpini, Pathumwan Bangkok 10330',
        'phone': '66 2 254 0441-2',
        'website': 'https://www.aimirt.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'AIM Industrial Growth Freehold and Leasehold Real Estate Investment Trust focuses on investing in freehold right of land, cold storage buildings, and immovable assets related to cold storage and warehouses in Thailand. These are located in Samut Sakhon and Chachoengsao areas with total leasable area of 36,908.00 sq.m. It also intends to invest in freehold right of land and warehouses, including 5 units of warehouses with total leasable area of 21,651 sq.m. in Bang Phi, Samut Prakan. The company is based in Bangkok, Thailand.'
    },
    'AIT.BK': {
        'name': 'Advanced Information Technology Public Company Limited',
        'address': '37/2 Suthisarnvinijchai Road Samseannok HuayKwang Bangkok 10320 Thailand',
        'phone': '66 2 275 9400',
        'website': 'https://www.ait.co.th',
        'sector': 'Technology',
        'industry': 'Information Technology Services',
        'description': 'Advanced Information Technology Public Company Limited, together with its subsidiaries, designs, sells, installs, services, repairs, maintains, and trains information and communication technology network systems in Thailand. The company operates through two segments, Sales and Service, and Rental of Equipment. It provides IT solutions, including carrier grade router/switch, Web/video caching, DDOS protection, software-defined networking or the network controlled by the program to work as defined, network function virtualization, and other. The company also offers data center and cloud solutions, such as consolidation and virtualization, unified data center, converged and hyper converged infrastructure, private and public cloud infrastructure, software-defined networking or the network controlled by the program, and other. In addition, it provides collaboration solutions comprising communication through IP/VoIP system or unified communication, video and Web conferencing, contact center, and others; IoT solutions; and various enterprise network solutions consisting of router, switch, wireless LAN, WAN optimization, security, application delivery control, DNS server, identity system, network management, and other. Further, the company offers the services in the development of information technology systems to various projects with the combination of concepts in applying technology with the framework in developing the system accordingly. Additionally, it provides managed services managing complicated IT system; and maintenance service on checking the operational condition of the system, as well as spare parts for saving the time in solving the problem and mitigating the risks from the damage of equipment. The company was founded in 1992 and is headquartered in Bangkok, Thailand.'
    }
    ,

    # 21-40
    'AJ.BK': {
        'name': 'A.J. Plast Public Company Limited',
        'address': 'No. 95, Thakarm Road Kwaeng Samaedam Khet Bangkhuntien Bangkok 10150 Thailand',
        'phone': '66 2 415 0035',
        'website': 'https://www.ajplast.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Packaging & Containers',
        'description': 'A.J. Plast Public Company Limited manufactures, sells, and exports plastic films and scrap products in Thailand and internationally. It offers biaxially oriented polypropylene (BOPP), biaxially oriented polyester (BOPET), biaxially oriented polyamide (BOPA), biaxially oriented poly lactic acid (BOPLA), and cast polypropylene (CPP) films, as well as metallized BOPP, BOPET, BOPA, BOPLA, and CPP films; and Krystalox and Krystalent films. The companys products are primarily used in packaging, adhesive tapes, cassette tapes, frozen food industry etc. A.J. Plast Public Company Limited was founded in 1987 and is headquartered in Bangkok, Thailand.'
    },
    'AJA.BK': {
        'name': 'AJ Advance Technology Public Company Limited',
        'address': 'No. 427/2 Rama 2 Road Kwaeng Samaedum Khet Bangkuntien Bangkok 10150 Thailand',
        'phone': '66 2 451 6888',
        'website': 'https://www.ajthai.com',
        'sector': 'Technology',
        'industry': 'Electronics & Computer Distribution',
        'description': 'AJ Advance Technology Public Company Limited, together with its subsidiaries, engages in the wholesale and retail of electric appliances under the AJ brand in Thailand. It retails and wholesales audio and visual products, such as home theatre sets, micro-components, speakers, portable radios, audio amplifiers, Bluetooth speakers, music boxes, karaoke audio sets and players, and other audio and visual products; home appliances, including air conditioners, refrigerators, washing machines, air purifiers, thermal bottles, blenders, induction cookers, electric pots, oil-free fryers, irons, steam iron blenders, water purifies, fans, gas stoves, and solar LEDs; and electric motorcycle bikes. The company also provides top-up services for prepaid phone and service prepaid kiosks. In addition, it is also involved in the distribution of sport shoes; retail of top-up machines; logistic and export business, including TV drama programs and other entertainment media businesses; provision of e-money services and accept payment through electronic methods; investment in digital assets; and mining and trading of digital assets, including investment or providing other services about cryptocurrency and digital token transactions. The company was formerly known as Crown Tech Advance Public Company Limited and changed its sport shoes name to AJ Advance Technology Public Company Limited in June 2017. AJ Advance Technology Public Company Limited was founded in 2001 and is headquartered in Bangkok, Thailand.'
    },
    'AKR.BK': {
        'name': 'Ekarat Engineering Public Company Limited',
        'address': '9/291 U.M. Tower Building 28th Floor Ramkhamhaeng Road Suanluang Sub-Dist., Suanluang Dist. Bangkok 10250 Thailand',
        'phone': '66 2 719 8777',
        'website': 'https://www.ekarat.co.th',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'Ekarat Engineering Public Company Limited manufactures and distributes transformers and solar farms in Thailand. The company is involved in the manufacture and sale of solar cells and solar panels, including the design, construction, installation, maintenance of electricity systems from solar cells and other renewable energy; and electrical maintenance and repair, and substation construction activities. It also engages in bidding and tendering activities, as well as provision of investment advisory, engineering, and energy management services. In addition, the company distributes solar modules; and produces and sells electricity from solar cells, as well as provides consulting services on energy conservation. Ekarat Engineering Public Company Limited was incorporated in 1981 and is headquartered in Bangkok, Thailand.'
    },
    'ALLA.BK': {
        'name': 'Alla Public Company Limited',
        'address': '933, 935,937,939 Soi Onnut46 Onnut Road Onnut Suanluang Bangkok 10250 Thailand',
        'phone': '66 2 322 0777',
        'website': 'https://alla.co.th',
        'sector': 'Industrials',
        'industry': 'Industrial Distribution',
        'description': 'Alla Public Company Limited imports, manufactures, and distributes cranes and electric hoists, industrial doors, loading docks, electronic lifts, racking and automated storage and retrieval system, and related parts and other equipment in Thailand. It provides crane and hoist, includes overhead, gantry and semi gantry crane, jib, wall traveling, monorail, suspension, and explosion proof cranes; and electric chain and wire, manual chain, and explosion proof hoists. The company also offers loading dock and equipment comprises electric hydraulic, mechanical dock, airbag, dock seal, inflatable dock, and retractable dock shelter; overhead sectional, high speed, traffic, and cold storage doors; and PVC strip and air curtains. In addition, it provides warehouse systems, include warehouse management systems and accessories, automated sorting and retrieving systems, warehouse control systems, transportation management systems, conveyors, picking and sorting systems, racking systems, high volume low speed fans, and warehouse LED systems; and distributes and install solar cell panels. Further, it provides installation and after-sales services. Alla Public Company Limited was founded in 1990 and is headquartered in Bangkok, Thailand.'
    },
    'ALLY.BK': {
        'name': 'Ally Leasehold Real Estate Investment Trust',
        'address': '888 Crystal Design Center, E Building, Praditmanutham Road, Klongjan, Bangkok, Thailand 10240',
        'phone': '66 2 101 5888',
        'website': 'http://www.allyreit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Retail',
        'description': 'Investing in leasehold rights/sub-leasehold rights of 13 projects as follows 1. The Crystal Design Center 2. The Crystal Ekamai-Ramindra 3. The Crystal SB Ratchapruek 4. Amorini 5. Im Park 6. Plearnary Mall 7. Sammakorn Place Ramkhamhaen 8. Sammakorn Place Rangsit 9. Sammakorn Place Ratchapruek 10. The Scene 11. Kad Farang Village 12. The Crystal Chaiyapruek 13. The Prime Hua Lamphong'
    
    },
    'ALT.BK': {
        'name': 'ALT Telecom Public Company Limited',
        'address': '52/1 Moo 5, Bang Kruay-Sai Noi Road Bang Si Thong Sub-district Bang Kruai 11130 Thailand',
        'phone': '66 2 863 8999',
        'website': 'https://www.alt.co.th',
        'sector': 'Technology',
        'industry': 'Communication Equipment',
        'description': 'ALT Telecom Public Company Limited engages in the manufacture, installation, maintenance, rental, and sale of telecommunication network equipment in Thailand and internationally. The company operates through three segments: Network Equipment and Electricity Meter Distribution, Network Equipment Installation Business, and Network Equipment Rental Business. It also manufactures, assembles, installs, and distributes electricity meters; and offers telecommunication products comprising fiber optic cables, telecom shelters, cell-on-wheel vehicles, antennas, tappers, splitters, repeaters, wireless range extenders, optical cables, and outdoor enclosures, as well as rapid deployment products. In addition, it is involved in the construction of base stations; installation and repairing of telecommunication, digital, and renewable energy equipment; sale, installation, and maintenance of electrical equipment and systems; leasing and management of telecommunication basic structures. The company was incorporated in 2001 and is headquartered in Bang Kruai, Thailand.'
    },
    'ALUCON.BK': {
        'name': 'Alucon Public Company Limited',
        'address': '500 Moo 1, Soi Sirikam Sukhumvit Road Samrong Nua Sub-district Mueang Samut Prakan 10270 Thailand',
        'phone': '66 2 398 0147',
        'website': 'https://www.alucon.th.com',
        'sector': 'Basic Materials',
        'industry': 'Aluminum',
        'description': 'Alucon Public Company Limited produces and distributes aluminum containers primarily in Thailand. It operates in two segments, Can and Tube, and Slug. The company offers aluminum collapsible tubes, monobloc aerosol cans, bottles, and rigid wall containers, as well as marker pen bodies. It also provides technical impact extrusions, aluminium slugs, aluminium coils, aluminium pellets, strips, plates, etc. The company exports its products to approximately 40 countries, including Japan, Australia, the United States, Indonesia, and South Africa. Alucon Public Company Limited was founded in 1961 and is headquartered in Mueang Samut Prakan, Thailand.'
    },
    'AMANAH.BK': {
        'name': 'Amanah Leasing Public Company Limited',
        'address': '16-16/1 Soi Kasemsan 1 Phayathai Road Wangmai Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 091 6456',
        'website': 'https://www.amanah.co.th',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Amanah Leasing Public Company Limited provides hire purchase, financial and operating lease, and inventory finance services to consumers and corporates in Thailand. It operates in two segments, Hire Purchase and Others. The company also offers quick loans for used cars, and car leasing business, as well as auto to money services. It operates 46 branches in the central region, northeastern region, northern region, and southern region across the country. The company was formerly known as Nava Leasing Public Company Limited and changed its name to Amanah Leasing Public Company Limited in October 2010. Amanah Leasing Public Company Limited was founded in 1992 and is headquartered in Bangkok, Thailand.'
    },
    'AMARIN.BK': {
        'name': 'Amarin Printing and Publishing Public Company Limited',
        'address': '378 Chaiyaphruk Road Taling Chan Bangkok 10170 Thailand',
        'phone': '66 2 422 9999',
        'website': 'https://www.amarin.co.th',
        'sector': 'Communication Services',
        'industry': 'Publishing',
        'description': 'Amarin Printing and Publishing Public Company Limited, together with its subsidiaries, engages in the publishing, advertising, and publications distribution businesses in Thailand. It offers a range of printing services, such as artwork creative design, photography, and image retouching, as well as digital and packaging printing service. The company also conceptualizes, compiles, designs, publishes, and delivers offline content, including books, magazines/newsletters, cards/leaflets/brochures/posters, annual reports, anniversary books, pocket books, and gifts; online content, including e-books, video clips, websites, and applications, as well as augmented reality and social network content; and visual content comprising infographics, illustrations, picture, and photography content. In addition, it engages in the organization of events, fairs, and seminars, as well as offsite training programs for private companies and SMEs; purchase, procurement, lease, and leasehold of various assets; and production, distribution, retail, and wholesale of various publication formats that include Thai and translated foreign language books, Praew and Sudsapda magazines for women, electronic creative media comprising video and multimedia teaching materials, and other printed materials. The company was formerly known as Amarin Printing Group Company Limited and changed its name to Amarin Printing and Publishing Public Company Limited in 1993. Amarin Printing and Publishing Public Company Limited was founded in 1976 and is headquartered in Bangkok, Thailand.'
    },
    'AMATA.BK': {
        'name': 'Amata Corporation Public Company Limited',
        'address': '2126 Kromadit Building New Petchburi Road Bangkapi Huaykwang Bangkok 10310 Thailand',
        'phone': '66 2 792 0000',
        'website': 'https://www.amata.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Amata Corporation Public Company Limited, together with its subsidiaries, engages in the planning, developing, managing, and marketing of industrial estates in Thailand and internationally. The company also produces, distributes, and treats water for industrial use; provides management services in common area; operates a school; and constructs factory for rent. In addition, it operates as a REIT manager. The company was founded in 1989 and is headquartered in Bangkok, Thailand.'
    },
    'AMATAR.BK': {
        'name': 'Amata Summit Growth Freehold and Leasehold Real Estate Investment Trust',
        'address': '2126 Kromadit Building New Petchburi Road Bangkapi Huay Kwang Bangkok 10310 Thailand',
        'phone': '66 2 792 0089',
        'website': 'https://www.amatareit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'Amata Summit Growth Freehold and Leasehold Real Estate Investment Trust is a real estate investment trust externally managed by Amata Summit REIT Management Co., Ltd. It invests in the real estate markets. Amata Summit Growth Freehold and Leasehold Real Estate Investment Trust is based in Bangkok, Thailand.'
    },
    'AMATAV.BK': {
        'name': 'Amata VN Public Company Limited',
        'address': '2126, Kromadit Building New Petchburi Road Bangkapi Huay Kwang Bangkok 10310 Thailand',
        'phone': '66 2 792 0000',
        'website': 'https://www.amatavn.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate Services',
        'description': 'Amata VN Public Company Limited, through its subsidiaries, engages in the development of industrial estate and related business in Vietnam. It is also involved in the leasing of industrial land, ready built factories, and commercial and residential land, as well as office rental activities. In addition, the company provides utility services. The company was incorporated in 2012 and is headquartered in Bangkok, Thailand.'
    },
    'AMC.BK': {
        'name': 'Asia Metal Public Company Limited',
        'address': '55, 55/1 Moo 2 Soi Watnamdaeng Srinakarin Road T.Bangkeaw Bang Phli 10540 Thailand',
        'phone': '66 2 338 7222',
        'website': 'https://www.asiametal.co.th',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'Asia Metal Public Company Limited produces and sells processed steel products in Thailand. It offers hot-rolled, pickled and oiled, and cold-rolled products to steel wholesalers and end user factories; and round, square, and rectangular steel pipes, as well as light lips channels and C-shaped furring. The company also trades in round-bars and deformed-bars, as well as square and round steel tubes. In addition, it provides steel cutting and modifying services. The company was founded in 1993 and is headquartered in Bang Phli, Thailand.'
    },
    'AMR.BK': {
        'name': 'AMR Asia Public Company Limited',
        'address': '469 Soi Prawit Lae Phuaen Prachachuen Road Las Yao Chatuchak 10900 Thailand',
        'phone': '66 2 589 9955',
        'website': 'https://www.amrasia.com',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'AMR Asia Public Company Limited provides construction services for telecommunication, and electronic and computer systems in Thailand. It also offers equipment installation and related services. The company was incorporated in 1999 and is headquartered in Chatuchak, Thailand.'
    },
    'ANAN.BK': {
        'name': 'Ananda Development Public Company Limited',
        'address': 'No. 99/1 Moo 14 Soi Windmill Housing Estate Bangna-Trad Road (K.M.10.5) Bangpleeyai Sub-district, Bangplee Dist.  Bang Phli 10540 Thailand',
        'phone': '66 2 317 1155',
        'website': 'https://www.ananda.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Ananda Development Public Company Limited, together with subsidiaries, engages in the development and sale of various real estate projects in Thailand. It operates through Real Estate Development, Management of Real Estate Development Project, and Other segments. The company provides management services for real estate projects; house construction services; and real estate brokerage services, as well as acts as a property agent. It is also involved in the juristic person management; media production; and property rental, as well as provision of academic seminar services. The company develops condominium projects under the Ashton, Ideo Q, Venio, Ideo Mobi, Ideo, Elio, and Unio brands; and housing projects and townhouses under the Artale, Airi, Atoll, Arden, Urbanio, and Unio Town brands. Ananda Development Public Company Limited was founded in 1999 and is headquartered in Bang Phli, Thailand.'
    },
    'AOT.BK': {
        'name': 'Airports of Thailand Public Company Limited',
        'address': 'No. 333, Cherdwutagard Road Srikan Don Mueang Bangkok 10210 Thailand',
        'phone': '66 2 535 1192',
        'website': 'https://www.airportthai.co.th',
        'sector': 'Industrials',
        'industry': 'Airports & Air Services',
        'description': 'Airports of Thailand Public Company Limited, together with its subsidiaries, engages in the airport business in Thailand. The company operates through Airport Management Business, Hotel Business, Ground Aviation Services, Security Business, and Project on Perishable Goods Business segments. It operates 6 international airports, including Suvarnabhumi Airport, Don Mueang International Airport, Chiang Mai International Airport, Hat Yai International Airport, Phuket International Airport and Mae Fah Luang - Chiang Rai International Airport. The company is also involved in the hotel and restaurant business; and operation and management of the project on perishable goods at Suvarnabhumi Airport. In addition, it apron services, ground equipment, ground passenger services, security services at airports, and other airport related services; aircraft maintenance, repair, and overhaul services; catering services for airlines; hydrant dispenser and aircraft refueling services; aviation depot; electronics information exchange services; and cargo depot services. Airports of Thailand Public Company Limited was incorporated in 2002 and is headquartered in Bangkok, Thailand.'
    },
    'AP.BK': {
        'name': 'AP (Thailand) Public Company Limited',
        'address': 'Ocean Tower I Building 18th Floor 170/57 New Ratchadapisek Road Klongtoey District Bangkok 10110 Thailand',
        'phone': '66 2 261 2518',
        'website': 'https://www.apthai.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'AP (Thailand) Public Company Limited, together with its subsidiaries, engages in the real estate development in Thailand. It operates through LowRise, HighRise, and Other segments. The Low-rise segment develops single detached houses and townhouses. The High-rise segment develops condominiums. The Other segment provides after-sales, property brokerage, and construction services. This segment also offers education and training services. The company was formerly known as Asian Property Development Public Company Limited and changed its name to AP (Thailand) Public Company Limited in May 2013. AP (Thailand) Public Company Limited was founded in 1991 and is headquartered in Bangkok, Thailand.'
    },
    'APCO.BK': {
        'name': 'Asian Phytoceuticals Public Company Limited',
        'address': '84/3 Moo 4 Northern Region Ind. Est (W. Super Highway No.11 Road Banklang Subdistrict Muang Lamphun District Lamphun 51000 Thailand',
        'phone': '66 5 358 1374',
        'website': 'https://www.apco.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Household & Personal Products',
        'description': 'Asian Phytoceuticals Public Company Limited engages in the research and development, manufacture, and distribution of healthcare and natural extracts-based beauty products in Thailand and internationally. Its products include dietary supplements, cosmetics, and personal care products that are developed from natural plant and botanical extracts. The company also provides slimming, anti-wrinkle, and skin care products, as well as products for balancing immunity. It distributes its products through call centers, direct service method, large drug stores, distributors, and digital and multi-level-marketing channels. The company was formerly known as Natural Cosmetics Research Co., Ltd. and changed its name to Asian Phytoceuticals Public Company Limited in July 2005. Asian Phytoceuticals Public Company Limited was founded in 1988 and is headquartered in Lamphun, Thailand.'
    },
    'APCS.BK': {
        'name': 'Asia Precision Public Company Limited',
        'address': 'Amata Nakorn Industrial Estate 700/331 Moo 6 Donhualor Muang Chonburi Chonburi 20000 Thailand',
        'phone': '66 3 846 8300',
        'website': 'https://www.apcs.co.th',
        'sector': 'Industrials',
        'industry': 'Metal Fabrication',
        'description': 'Asia Precision Public Company Limited, together with its subsidiaries, manufactures and sells precision metal parts and components in Thailand and internationally. The company is also involved in the design, engineering, consultation, construction, maintenance, system testing, and sale of construction related equipment for various power plant projects, such as renewable power plants, power sub-stations, and raw water distributing facilities; production and distribution of raw water; distribution of materials, tools, equipment, and spare parts for the construction of power plants; and other energy businesses. It serves automotive, air conditioning and refrigeration compressor, digital camera, and medical sectors. The company was founded in 1994 and is headquartered in Chonburi, Thailand.'
    },
    'APEX.BK': {
        'name': 'Apex Development Public Company Limited',
        'address': 'Zone A, 900 Tonson Tower 18th Floor Ploenchit Road Lumpini, Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 636 2465',
        'website': 'https://www.apexpcl.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Apex Development Public Company Limited develops and sells real estate properties. The company develops residential condominiums, villas, and hotels, as well as resorts and land. It also provides services for customers to operate apartments and villas for rent. In addition, the company engages in the operation of rental management. The company was formerly known as Sun Tech Group Public Company Limited and changed its name to Apex Development Public Company Limited in August 2007. Apex Development Public Company Limited was founded in 1988 and is headquartered in Bangkok, Thailand.'
    }
    ,

    # 41-60
    'APURE.BK': {
        'name': 'Agripure Holdings Public Company Limited',
        'address': 'The Ruamjaipattana Foundation Building No. 70, Moo 6 Klong 1 District Klong Luang Pathum Thani 12120 Thailand',
        'phone': '66 2 516 0941',
        'website': 'https://www.apureholdings.com',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'Agripure Holdings Public Company Limited, through its subsidiaries, manufactures and distributes agro products in Thailand. The company offers canned and pouched sweet corn products; fresh vegetable and fruit products; and commercial seeds, as well as breeds and distributes corn seeds. It also exports its products to approximately 50 countries. The company was founded in 1986 and is based in Pathum Thani, Thailand.'
    },
    'AQ.BK': {
        'name': 'AQ Estate Public Company Limited',
        'address': 'AQ Square Building 102 Rimklongbangkapi Road Bang Kapi Sub-District Huai Khwang District Bangkok 10310 Thailand',
        'phone': '66 2 033 5555',
        'website': 'https://www.aqestate.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'AQ Estate Public Company Limited develops and sells properties in Thailand. It operates in four segments: Property Development Low Rise, Property Development High Rise, Services, and Property Rental and Service. The company primarily develops single house, condominium, town home, and hospitality projects. It also provides recreational and sale management services; operates hotels and resorts; manages commercial space; and offers real estate trading and rental services. The company was formerly known as Krisdamahanakorn Public Company Limited and changed its name to AQ Estate Public Company Limited in April 2014. AQ Estate Public Company Limited was founded in 1982 and is headquartered in Bangkok, Thailand.'
    },
    'AQUA.BK': {
        'name': 'Aqua Corporation Public Company Limited',
        'address': 'R.S. Tower 21st Floor 121/68-69, Ratchadapisek Road Dindaeng Bangkok 10400 Thailand',
        'phone': '66 2 694 8888',
        'website': 'https://www.aquacorp.co.thSector',
        'sector': 'Communication Services',
        'industry': 'Advertising Agencies',
        'description': 'Aqua Corporation Public Company Limited provides out of home media services in Bangkok. The company operates through Out of Home Media; and Property for Rent and Service segments. It provides real estate rental services and warehouse rental services. The company was formerly known as P Plus P Public Company Limited and changed its name to Aqua Corporation Public Company Limited in April 2012. Aqua Corporation Public Company Limited was founded in 1994 and is based in Bangkok, Thailand.'
    },
    'AS.BK': {
        'name': 'Asiasoft Corporation Public Company Limited',
        'address': 'No.51, Major Tower Rama 9 - Ramkumhang 18th Floor, Room No.3-8 Rama 9 Road, Hua Mak Sub-District Bangkapi District Bangkok 10240 Thailand',
        'phone': '66 2 769 8888',
        'website': 'https://www.asiasoft.co.th',
        'sector': 'Communication Services',
        'industry': 'Electronic Gaming & Multimedia',
        'description': 'Asiasoft Corporation Public Company Limited, together with its subsidiaries, engages in the provision of established community platform and expansive distribution network for game developers in Thailand, Vietnam, Indonesia, Singapore, Malaysia, the Philippines, and internationally. The company operates through two segments, Online Game and Distribution. The Online Game segment offers online games, including massive multiplayer online role-playing, casual, first person shooting, and mobile games. The Distribution segment provides payment channel services. The company publishes the games under the PlayPark brand. It also offers @Cafe programme, which brings online games to Internet cafe gamers, as well as promotional media and various marketing services for its member shops; and @Cash that is an in-game credits top-up system. The company was formerly known as B.M. Media (Thailand) Company Limited. Asiasoft Corporation Public Company Limited was incorporated in 2001 and is headquartered in Bangkok, Thailand.'
    },
    'ASAP.BK': {
        'name': 'Synergetic Auto Performance Public Company Limited',
        'address': '149 Moo 3 Theparak Road Theparak, A Mueang Samut Prakan 10270 Thailand',
        'phone': '66 2 091 8181',
        'website': 'https://www.asapcarrent.com',
        'sector': 'Industrials',
        'industry': 'Rental & Leasing Services',
        'description': 'Synergetic Auto Performance Public Company Limited provides car rental services in Thailand. The company offers operating leasing services for corporate customers; short-term car rental services for ordinary customers; limousine rental services for corporate customers; and car rental services through an asap application. It also operates Lifestyle Mall, a car rental center and complete used cars, which include food and beverage outlets; and asap select franchises that are service centers for short-term car rentals and second-hand car sales. In addition, the company provides car maintenance services. It offers services under asap brand name. Synergetic Auto Performance Public Company Limited is headquartered in Mueang Samut Prakan, Thailand.'
    },
    'ASEFA.BK': {
        'name': 'Asefa Public Company Limited',
        'address': '5 Moo 1, Rama II Road Khok-Krabue Muang Samutsakhon Samut Sakhon 74000 Thailand',
        'phone': '66 2 686 7777',
        'website': 'https://www.asefa.co.th',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'Asefa Public Company Limited manufactures and provides electrical power distribution, switchboard, trunking, lighting, automation, and energy management solutions in Thailand. The company manufactures and sells modular switchboards, such as electric control panels, automation devices, motor panels, substation units, and other panels related to electrical distribution system; licensed type tested switchboards; metal trunking products comprising wire ways, cable trays, cable ladders, flush floor, underfloor ducts, and perforated trunking products; and fluorescent-lamp luminaires for recessed and pendant installation applications under the ASEFA brand. It also distributes and supplies electrical and control, electrical power distribution, lighting and equipment, and mineral insulated metal sheated cables. In addition, the company offers design, consulting, planning and equipment selection, installation and modification, test and commissioning, and ETAP electrical engineering software solutions; integrated solutions comprising electrical power distribution solutions, data center and redundancy electrical power system, energy management and monitoring systems, automation and communication system, power quality solutions, and lighting solutions; and after sales services. It serves infrastructure, industry, commercial building, residential, healthcare, data center and telecommunication, and power generation sectors. Asefa Public Company Limited was incorporated in 1997 and is based in Samut Sakhon, Thailand.'
    },
    'ASIA.BK': {
        'name': 'Asia Hotel Public Company Limited',
        'address': 'No. 296 Phayathai Road ThanonPetchari Rajathevi Bangkok 10400 Thailand',
        'phone': '66 2 217 0808',
        'website': 'https://www.asiahotel.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'Asia Hotel Public Company Limited, together with its subsidiaries, engages in the hotel and restaurant business in Thailand and internationally. The company is involved in the rental of a shopping center and hotel; and provision of utility, security, and cleaning services. Asia Hotel Public Company Limited was incorporated in 1964 and is based in Bangkok, Thailand.'
    },
    'ASIAN.BK': {
        'name': 'Asian Sea Corporation Public Company Limited',
        'address': '55/2 Moo 2 Rama 2 Road Bangkrajao Muang Samut Sakhon 74000 Thailand',
        'phone': '66 3 482 2700',
        'website': 'https://www.asiansea.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Asian Sea Corporation Public Company Limited, together with its subsidiaries, engages in the production and distribution of processed frozen seafood and provision of cold storage services in Thailand and internationally. The company operates through three segments: Frozen and Packaged Food Products, Feedstuff, and Other Business. Its frozen food includes shrimp, squid, Sillago fish, octopus, and cuttle fish. The company is also involved in the production of frozen ready-to-eat foods, packaged seafoods, fishmeal, and feedstuff; production and distribution of animal feeds; and provision of marketing and management services. In addition, it offers wet pet food products, such as soups, salads, fish and meat dishes, mousse, and pate; aquaculture feed pellets; canned and pouch tuna products; and dry feed products for pets, including cats and dogs. The company offers its products under the Monchou, Monchou Balanced, and Hajiko brand names. Asian Sea Corporation Public Company Limited was founded in 1964 and is headquartered in Mueang Samut Sakhon, Thailand.'
    },
    'ASIMAR.BK': {
        'name': 'Asian Marine Services Public Company Limited',
        'address': '128 Moo 3 Suksawad Road Laemfapa Prasamutjedee Samut Prakan 10290 Thailand',
        'phone': '66 2 815 2060',
        'website': 'https://www.asimar.com',
        'sector': 'Industrials',
        'industry': 'Aerospace & Defense',
        'description': 'Asian Marine Services Public Company Limited, together with its subsidiaries, engages in the ship building and ship repairing businesses in Thailand. The company constructs various types of ships; undertakes ship conversion projects; and offers a range of offshore support services, as well as engineering services. It also operates as an agent of machinery and equipment for marine service; and subcontractor of ship repair, as well as provides pollution control and environmental management services. The company was founded in 1981 and is headquartered in Samut Prakan, Thailand.'
    },
    'ASK.BK': {
        'name': 'Asia Sermkij Leasing Public Company Limited',
        'address': 'Sathorn City Tower 24th Floor 175, South Sathorn Road Tungmahamek, Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 679 6226',
        'website': 'https://www.ask.co.th',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Asia Sermkij Leasing Public Company Limited provides auto hire purchase services primarily in Thailand. It operates through five segments: Hire Purchase, Leasing, Loan, Factoring, and Insurance Broker. The company provides automobile hire purchase services for new and used automobiles, including passenger and commercial cars, such as pickup, van, truck, taxi, etc.; auto and machine leasing services for commercial customers; personal loans, sale and hire purchase back, and floor plan financing to hire purchase customers, entrepreneurs, and automotive dealers; and factoring services to commercial customers in various industries. It also offers insurance brokerage services to hire purchase and finance lease customers; and auto registration and tax renewal services. The company was founded in 1984 and is headquartered in Bangkok, Thailand. Asia Sermkij Leasing Public Company Limited is a subsidiary of Chailease Holding Company Limited.'
    },
    'ASP.BK': {
        'name': 'Asia Plus Group Holdings Public Company Limited',
        'address': 'Sathorn City Tower Floors 3,9 and 11 No. 175, South Sathorn Road Thungmahamek, Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 680 1111',
        'website': 'https://www.asiaplusgroup.co.th',
        'sector': 'Financial Services',
        'industry': 'Capital Markets',
        'description': 'Asia Plus Group Holdings Public Company Limited, together with its subsidiaries, engages in the securities business in Thailand. It operates through four segments: Securities and Derivatives Brokerage, Investment Banking, Fund Management, and Investment Trading. The company provides securities and derivatives brokering services for local and foreign investors; investment advisory; security underwriting; securities borrowing and lending; venture capital management; financial advisory; and private, derivatives, and mutual fund management services. It also invests in unit trusts; and buys, sells, and exchanges securities. The company was formerly known as Asia Plus Group Holdings Securities Public Company Limited and changed its name to Asia Plus Group Holdings Public Company Limited in July 2015. Asia Plus Group Holdings Public Company Limited was incorporated in 1974 and is based in Bangkok, Thailand.'
    },
    'ASW.BK': {
        'name': 'Assetwise Public Company Limited',
        'address': '9 Soi Ramintra 5 Junction 23 Anusawari Bang Khen Bangkok 10220 Thailand',
        'phone': '66 2 521 9533',
        'website': 'https://assetwise.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Asset Wise Public Company Limited develops and sells residential real estate properties in Thailand. It develops condominiums and low-rise real estate projects consisting of housing estates, townhomes, and home offices. The company also rents real estate properties; and offers management and real estate brokerage services. Asset Wise Public Company Limited was incorporated in 2005 and is headquartered in Bangkok, Thailand.'
    },
    'AURA.BK': {
        'name': 'Aurora Design Public Company Limited',
        'address': '444 Soi Udomsuk 26 Bang Na Nuea Subdistrict Bang Na District Bangkok 10260 Thailand',
        'phone': '66 2 749 5044',
        'website': 'http://www.auroradesign.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Luxury Goods',
        'description': 'Retail business of gold jewelries, diamond and gemstone jewelries and other relating businesses providing one-stop service'
    },
    'AWC.BK': {
        'name': 'Asset World Corp Public Company Limited',
        'address': 'Empire Tower 54th Floor 1 South Sathorn Road Yannawa, Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 180 9999',
        'website': 'https://www.assetworldcorp-th.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate Services',
        'description': 'Asset World Corp Public Company Limited invests in, develops, and manages real estate properties in Thailand. The company operates in two segments: Hotel and Related Services, and Rental and Rendering of Commercial Building Services. Its business portfolio consists of hotels; lifestyle destinations, community shopping malls, and community markets; and mixed-use properties. The company also operates digital platforms; and engages in property leasing activities. Asset World Corp Public Company Limited was incorporated in 2018 and is headquartered in Bangkok, Thailand.'
    },
    'AYUD.BK': {
        'name': 'Allianz Ayudhya Capital Public Company Limited',
        'address': '898 Ploenchit Tower 7th Floor Ploenchit Road, Lumpini Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 305 7374',
        'website': 'https://www.ayud.co.th',
        'sector': 'Financial Services',
        'industry': 'Insurance—Property & Casualty',
        'description': 'Allianz Ayudhya Capital Public Company Limited, an investment holding company, provides non-life insurance products in Thailand. It operates in three segments: Non-Life Insurance Business, Investment Business, and Service Business. The company offers fire, marine, motor, and miscellaneous insurance products. It also provides health services. The company was formerly known as Sri Ayudhya Capital Public Company Limited and changed its name to Allianz Ayudhya Capital Public Company Limited in April 2019. Allianz Ayudhya Capital Public Company Limited was incorporated in 1950 and is headquartered in Bangkok, Thailand.'
    },
    'B.BK': {
        'name': 'Begistics Public Company Limited',
        'address': '52 Thaniya Plaza Building 28th Floor Silom Road Suriyawongse, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 096 4999',
        'website': 'https://www.begistics.co.th',
        'sector': 'Industrials',
        'industry': 'Marine Shipping',
        'description': 'Begistics Public Company Limited, together with its subsidiaries, engages in the operation of a port in Bangpakong, Thailand. The company offers container depot, warehousing, wharf, and other related services. It also provides logistics services, which consist of domestic transportation services with trucks, trailers, containers, bulk cargoes, large cargoes, and cranes; crane rental services, international freight management services; logistics and project management services; and truck sales and maintenance services. In addition, the company engages in buying, selling, renting, exchanging condominiums, apartments, and other real estate, as well as provides loan and factoring services. Further, it distributes raw water, tap water, PVC pipes, and plastic pipes; and offers repairs, maintains, installs, and assembles sewer and wastewater pipes, as well as car rental services; and trade consultant services. The company was formerly known as Bangpakong Terminal Public Company Limited and changed its name to Begistics Public Company Limited in March 2018. Begistics Public Company Limited was incorporated in 1995 and is headquartered in Bangkok, Thailand.'
    },
    'B52.BK': {
        'name': 'B-52 Capital Public Company Limited',
        'address': '973 President Tower 7th Floor, Unit 7B, 7C, 7D and 7I Ploenchit Road, Lumpini Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 656 0189',
        'website': 'https://b52.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate Services',
        'description': 'B-52 Capital Public Company Limited, together with its subsidiary, provides wholesale distribution, retail sales, and advertising media solutions in Thailand. It offers logistical planning, product distribution, and warehousing solutions to retailers; operates e-commerce marketing solutions under the TANJAI-D name; media and marketing solutions; and network marketing solutions. The company also provides commercial and small business loans, as well as insurance policies. The company was formerly known as Digital Tech Planet Public Company Limited and changed its name to B-52 Capital Public Company Limited in May 2019. B-52 Capital Public Company Limited was founded in 1964 and is based in Bangkok, Thailand.'
    },
    'BA.BK': {
        'name': 'Bangkok Airways Public Company Limited',
        'address': 'Vibhavadirangsit Road 99 Mu 14 Chom Phon Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 265 5678',
        'website': 'https://www.bangkokair.com',
        'sector': 'Industrials',
        'industry': 'Airlines',
        'description': 'Bangkok Airways Public Company Limited, together with its subsidiaries, provides air transportation and airport services. The company operates through three segments: Airline, Airport, and Supporting Airline Business. The Airline segment engages in the sale of tickets, as well as the provision of services for passengers. The Airport segment offers location services for passengers and airlines. The Supporting Airline Business segment provides ground handling, cargo, and catering services for airlines and customers. The company also offers aviation training, and REIT and other management services; development and management services for public airports; operates restaurants; distributes souvenirs; and produces and processes food for distribution. Bangkok Airways Public Company Limited was founded in 1968 and is headquartered in Bangkok, Thailand.'
    },
    'BAFS.BK': {
        'name': 'Bangkok Aviation Fuel Services Public Company Limited',
        'address': '171/2 Kamphaeng Phet 6 Road Don Mueang Khet Don Mueang Bangkok 10210 Thailand',
        'phone': '66 2 834 8900',
        'website': 'https://www.bafsthai.com',
        'sector': 'Industrials',
        'industry': 'Airports & Air Services',
        'description': 'Bangkok Aviation Fuel Services Public Company Limited provides aviation fuel storage and aircraft refueling services at Bangkok International Airport in Thailand. The company offers into-plane, hydrant network, and fuel pipeline transportation services, as well as assembles and maintains hydrant dispensers. It also manufactures and distributes electricity from solar power; invests in solar power business; and provides property rental services. The company was incorporated in 1983 and is headquartered in Bangkok, Thailand.'
    },
    'BAM.BK': {
        'name': 'Bangkok Commercial Asset Management Public Company Limited',
        'address': '99, Surasak Road Silom Sub-district Bangrak District Bangkok 10500 Thailand',
        'phone': '66 2 267 1900',
        'website': 'https://www.bam.co.th',
        'sector': 'Financial Services',
        'industry': 'Asset Management',
        'description': 'Bangkok Commercial Asset Management Public Company Limited operates as an asset management company. It purchases non-performing loans (NPLs) from financial institutions in Thailand, including banks and other financial institutions; and manages NPLs through debt restructuring negotiations with debtors. The company also acquires non-performing assets (NPAs) through various means, such as negotiating with debtors for the transfer of the guarantee or repayment property, foreclosing the debt settlement, and purchasing NPAs directly from other financial institutions. Its NPLs are primarily guaranteed by real estate properties, secured by the first mortgage registration; and NPAs are primarily real estate assets, such as empty lands, hotels, commercial buildings, movable assets, and other securities, as well as residential properties, including detached houses, townhouses, and condominiums. The company was founded in 1998 and is headquartered in Bangkok, Thailand.'
    },

    # 61-80
    'BANPU.BK': {
        'name': 'Banpu Public Company Limited',
        'address': 'Thanapoom Tower 27th Floor 1550 New Petchburi Road Makkasan, Ratchathewi Bangkok 10400 Thailand',
        'phone': '66 2 694 6600',
        'website': 'https://www.banpu.com',
        'sector': 'Energy',
        'industry': 'Thermal Coal',
        'description': 'Banpu Public Company Limited engages in the coal mining and power businesses. The company operates various coal project in Mongolia; thermal power plants in Thailand, Lao PDR, and China; wind farm in Vietnam; and solar farms in Japan. It provides solar rooftop solutions and installation for industries and large businesses; energy storage solutions; electric vehicle and fleet management services; consultation services on customized energy management system; and renewable energy ecosystem for clean energy. The company also involved in the power and steam production, purchase, and trading business; provident fund management; solar power generation; logistics; sales and marketing activities; natural gas business; investment in power and renewable energy; and research and development business. In addition, it provides coal mining and trading; and business consultancy services, as well as fuel trading services. The company was formerly known as Ban Pu Coal Company Limited and changed its name to Banpu Public Company Limited in July 1993. Banpu Public Company Limited was founded in 1983 and is headquartered in Bangkok, Thailand.'
    },
    'BAREIT.BK': {
        'name': 'BA Airport Leasehold Real Estate Investment Trust',
        'address': '99 Moo 14 Vibhavadi Rangsit Road, Chom Phon, Chatuchak, Bangkok 10900 Thailand',
        'phone': '66 2 265 5709',
        'website': 'http://www.bareit.co.th',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'nvestment in the leasehold rights over the land, structures, and components of certain parts of the assets used in the operation of the airport in the Samui Airport'
    },
    'BAY.BK': {
        'name': 'Bank of Ayudhya Public Company Limited',
        'address': '1222 Rama III Road Bang Phongphang Subdistrict Yannawa District Bangkok 10120 Thailand',
        'phone': '66 2 296 2000',
        'website': 'https://www.krungsri.com',
        'sector': 'Financial Services',
        'industry': ' Banks—Regional',
        'description': 'Bank of Ayudhya Public Company Limited, together with its subsidiaries, provides commercial banking products and services to individuals, corporates, small and medium-sized businesses, and financial institutions. Its Retail segment offers a range of banking and related financial services, including current and savings accounts, fixed deposits, bills of exchange, housing loans, credit cards, personal loans and sale finance loans, hire-purchase and leasing, wealth management, and bancassurance products. The companys Commercial segment provides financial services and products comprising the range of credit facilities, which comprise short-term working capital, cash management, trade finance, transactional banking, advisory services, and treasury and money markets products. It also offers refinancing and venture capital services; car rental, collection, and personnel services; mutual funds and private fund management services; factoring and information technology services; and microfinance, real estate lease, and securities services, as well as operates as a life, non-life, and general insurance broker. In addition, the company develops, manages, and sells non-performing assets and other assets transferred from financial institutions. Bank of Ayudhya Public Company Limited was founded in 1945 and is headquartered in Bangkok, Thailand. Bank of Ayudhya Public Company Limited is a subsidiary of MUFG Bank, Ltd.'
    },
    'BBGI.BK': {
        'name': 'BBGI Public Company Limited',
        'address': '2098 M Tower Building 5th Floor Sukhumvit Road, Phra Khanong Tai Phra Khanong Bangkok 10260 Thailand',
        'phone': '66 2 335 8899',
        'website': 'https://www.bbgigroup.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'BBGI Public Company Limited manufactures and distributes biofuel and related products in Thailand. It operates through three segments: Biodiesel, Ethanol, and Others. The company offers biodiesel products, including crude glycerine and methyl ester products; and bioethanol products. It also provides bio-based products, such as ASTA  IMMU, a supplement for aesthetic and antiviral benefits; ASTA  ViS for vision and healthy eyes; and Calcium LT for bone and joint care. The company is headquartered in Bangkok, Thailand. BBGI Public Company Limited is a subsidiary of Bangchak Corporation Public Company Limited.'
    },
    'BBL.BK': {
        'name': 'Bangkok Bank Public Company Limited',
        'address': '333 Silom Road Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 645 5555',
        'website': 'https://www.bangkokbank.com',
        'sector': 'Financial Services',
        'industry': 'Banks—Regional',
        'description': 'Bangkok Bank Public Company Limited provides various commercial banking products and services in Thailand and internationally. The company operates through Domestic Banking, International Banking, Investment Banking, and Others segments. It offers various personal banking products and services, including savings, current, fixed deposit, foreign currency, and other accounts; home and personal loans, as well as loans for pensioners; mutual funds; investments products and services, such as bonds and debentures, as well as agency services; life and non-life bancassurance products; payment, funds transfer, currency exchange and foreign instrument, and SMS services; debit, credit, and prepaid cards; and phone and Internet banking, mobile banking, ATMs, and other services. The company also provides business banking products and services comprising operating accounts; loans for SMEs, international trade, investment banking, and e-guarantee services; securities services, such as custodian, mutual fund supervisor, provident fund registrar, securities registrar, and debenture holders representative services; personal loans for small businesses; payment, collection, and merchant services; digital banking services; and commercial cards. In addition, it offers trade finance, remittances, export and import, project, corporate finance, electronic services, and financial advisory services, as well as liquidity, fund, and asset management services. The company was founded in 1944 and is headquartered in Bangkok, Thailand.'
    },
    'BCH.BK': {
        'name': 'Bangkok Chain Hospital Public Company Limited',
        'address': '44 Moo 4, Chaengwattana Road Pakkred Nonthaburi 11120 Thailand',
        'phone': '66 2 836 9907',
        'website': 'https://www.bangkokchainhospital.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Bangkok Chain Hospital Public Company Limited, together with its subsidiaries, operates private hospitals in Thailand. It offers diagnosis, treatment, prevention, rehabilitation services for heart disease; open heart surgery to provide heart care and clinical treatment by cardiologists; and medical supports. The company also operates diagnostic imaging center; eye center that provide a full range of eye examination, treatment, and surgery services; and cancer center that offers services ranging from screening, diagnosis, and chemotherapy. In, addition it operates fertility center for infertility treatment, as well as diabetic wound treatment center. The company was founded in 1984 and is based in Nonthaburi, Thailand.'
    },
    'BCP.BK': {
        'name': 'Bangchak Corporation Public Company Limited',
        'address': '2098 M Tower Building 8th Floor Sukhumvit Road Phra Kanong Tai, Phra Kanong Bangkok 10260 Thailand',
        'phone': '66 2 335 8888',
        'website': 'https://www.bangchak.co.th',
        'sector': 'Energy',
        'industry': 'Oil & Gas Refining & Marketing',
        'description': 'Bangchak Corporation Public Company Limited, an energy company, engages in the refining and marketing of petroleum products in Thailand, Singapore, Norway, Korea, and internationally. It operates through six segments: Refinery and Oil Trading, Marketing, Electricity, Bio-Based Product, Natural Resource, and Others. The company explores and produces petroleum products; produces biodiesel, ethanol, and biogas; produces and distributes electricity from solar cells; invests in alternative energy business; manufactures and distributes biofuel products; operates service stations; and mines lithium. It serves consumers in various sectors comprising transportation, aviation, shipping, construction, industrial, and agriculture. The company was formerly known as The Bangchak Petroleum Public Company Limited and changed its name to Bangchak Corporation Public Company Limited in April 2017. Bangchak Corporation Public Company Limited was founded in 1984 and is headquartered in Bangkok, Thailand.'
    },
    'BCPG.BK': {
        'name': 'BCPG Public Company Limited',
        'address': '2098 M Tower Building 12th Floor Sukhumvit Road Phra Khanong Tai, Phra Khanong Bangkok 10260 Thailand',
        'phone': '66 2 335 8999',
        'website': 'https://www.bcpggroup.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'CPG Public Company Limited, together with its subsidiaries, engages in the production and distribution of electric power from renewable resources in Thailand, Japan, Taiwan, Laos, Vietnam, Indonesia, and the Philippines. It generates electricity from solar, wind, and hydro power. The company was founded in 2015 and is headquartered in Bangkok, Thailand. BCPG Public Company Limited operates as a subsidiary of Bangchak Corporation Public Company Limited.'
    },
    'BCT.BK': {
        'name': 'Birla Carbon (Thailand) Public Company Limited',
        'address': '888/122, 188/128, Mahatun Plaza Bldg. 12th Floor Ploenchit Road Lumpini, Pratumwan Bangkok 10330 Thailand',
        'phone': '66 2 253 6745',
        'website': 'https://www.birlacarbon.com/investor-relations/',
        'sector': 'Basic Materials',
        'industry': 'Specialty Chemicals',
        'description': 'Birla Carbon (Thailand) Public Company Limited is involved in the manufacture and sale of carbon black for rubber and specialty applications. The company sells its products under the Birla Carbon brand name. It has operations in Thailand, Japan, Indonesia, Vietnam, Malaysia, and internationally. The company was formerly known as Thai Carbon Black Public Company Limited and changed its name to Birla Carbon (Thailand) Public Company Limited in July 2018. Birla Carbon (Thailand) Public Company Limited was incorporated in 1978 and is headquartered in Bangkok, Thailand.'
    },
    'BDMS.BK': {
        'name': 'Bangkok Dusit Medical Services Public Company Limited',
        'address': '2, Soi Soonvijai 7 New Petchburi Road Bang Kapi Huaykwang Bangkok 10310 Thailand',
        'phone': '66 2 310 3000',
        'website': 'https://www.bdms.co.th',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Bangkok Dusit Medical Services Public Company Limited, together with its subsidiaries, operates hospitals in Thailand and internationally. The company owns and manages 6 hospital groups, including Bangkok Hospital Group, Samitivej Hospital Group, BNH Hospital, Phyathai Hospital Group, Paolo Hospital Group, and Royal Hospital Group. It operates holistic clinical wellness. In addition, the company operates hotels and restaurant; sells health and cosmetic products; provides accounting, health insurance, laboratory services, investment, information technology, training, skin and aesthetics telemedicine, genome sequencing, insurance brokerage, air transportation, facility management, and property management services, as well as asset management services; and manufactures and distributes medicine and pharmaceutical products and medical equipment. Further, it is involved in the e-commerce and real estate business. Bangkok Dusit Medical Services Public Company Limited was incorporated in 1969 and is based in Bangkok, Thailand.'
    },
    'BEAUTY.BK': {
        'name': 'Beauty Community Public Company Limited',
        'address': '50/1-3 Soi Nuanchan 34 nuanchan Road, Nuanchan Subdistrict, Buengkum District Bangkok 10230',
        'phone': '66 2 946 0700',
        'website': 'https://www.beautycommunity.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Household & Personal Products',
        'description': 'Beauty Community Public Company Limited engages in the retail sale and distribution of cosmetic and skincare products under the Beauty Buffet, Beauty Cottage, Beauty Market, Beauty Plaza, and Made In Nature names in Thailand and internationally. It provides make up, facial care, body care, hair care, and beauty drink and food supplement products, as well as beauty accessories. The company sells its products through retail and non-retail channels, as well as franchises; and e-commerce channel. It operates through 21 branches in Indonesia, 2 branches in Vietnam, 3 branches in the Philippines, 29 branches in India, 14 branches in Myanmar, 4 branches in Malaysia, 5 branches in Laos, 1 branch in Brunei, and 1 branch in Japan, as well as 34,000 points of sale in the Peoples Republic of China. The company was formerly known as Monopolitan Co., Ltd. and changed its name to Beauty Community Public Company Limited in July 2012. Beauty Community Public Company Limited was founded in 1998 and is headquartered in Bangkok, Thailand.'
    },
    'BEC.BK': {
        'name': 'BEC World Public Company Limited',
        'address': '3199 Maleenont Tower Floor 2, 3, 4, 9, 10, 30-34 Rama 4 Road Klongton, Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 262 3333',
        'website': 'https://www.becworld.com',
        'sector': 'Communication Services',
        'industry': 'Broadcasting',
        'description': 'BEC World Public Company Limited, together with its subsidiaries, engages in the entertainment and recreation business in Thailand and internationally. The company provides content on various platforms, such as television and digital platform, global content licensing, and supporting business; provides and produces TV and news programs; and sells airtime for advertising. It also provides information technology and maintenance services; retails computer accessories; and invests in digital platform businesses. In addition, the company operates digital TV business. BEC World Public Company Limited was founded in 1967 and is headquartered in Bangkok, Thailand.'
    },
    'BEM.BK': {
        'name': 'Bangkok Expressway and Metro Public Company Limited',
        'address': '587 Sutthisarn Road Ratchadaphisek Subdistrict Dindaeng District Bangkok 10400 Thailand',
        'phone': '66 2 641 4611',
        'website': 'https://www.bemplc.co.th',
        'sector': 'Industrials',
        'industry': 'Railroads',
        'description': 'Bangkok Expressway and Metro Public Company Limited, together with its subsidiaries, engages in the construction and management of expressways and rail mass rapid transit system projects in Thailand. The company operates through four segments: Expressway Business, Rail Business, Commercial Development Business, and Others. It undertakes commercial developments relating to the expressway and operates metro services. The company also operates and manages the Si Rat Expressway, the Si Rat - Outer Ring Road Expressway, and the Udon Ratthaya Expressway, as well as the MRT Blue Line and MRT Chalong Ratchadham Line projects. In addition, it engages in the rental of retail space, and provision of advertising services, as well as offers telecommunication services for underground train stations and on expressways. Bangkok Expressway and Metro Public Company Limited was founded in 1998 and is headquartered in Bangkok, Thailand.'
    },
    'BEYOND.BK': {
        'name': 'Bound and Beyond Public Company Limited',
        'address': 'No. 130–132 Sindhorn Tower 2 15th Floor Wireless Road Lumpini Sub-District, Pathum Wan Distric Bangkok 10330 Thailand',
        'phone': '66 2 028 2626',
        'website': 'https://www.boundandbeyond.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'Bound and Beyond Public Company Limited, together with its subsidiaries, owns and operates hotels in Thailand. It owns and manages the Four Seasons Hotel Bangkok and Capella Bangkok. The company was formerly known as Padaeng Industry Public Company Limited and changed its name to Bound and Beyond Public Company Limited in October 2021. Bound and Beyond Public Company Limited was founded in 1981 and is headquartered in Bangkok, Thailand.'
    },
    'BGC.BK': {
        'name': 'BG Container Glass Public Company Limited',
        'address': '47/1 Moo 2, Rangsit-Nakornnayok Road Km.7 Buengyeetho Pathumthani Thanyaburi 12130 Thailand',
        'phone': '66 2 834 7000',
        'website': 'https://www.bgc.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Packaging & Containers',
        'description': 'BG Container Glass Public Company Limited, together with its subsidiaries, manufactures and distributes glass bottles and other packaging in Thailand and internationally. It offers containers, plastic bottles and caps, plastic crates, wrap and shrink films, corrugated boxes and sheets, product trays, and corrugated box separator. The company also generates and distributes electricity from solar power. It serves customers in various industries, such as beverage bottles, alcoholic beverage, food, insecticide and drugs, and others. The company was founded in 1974 and is headquartered in Thanyaburi, Thailand. BG Container Glass Public Company Limited is a subsidiary of Bangkok Glass Public Company Limited.'
    },
    'BGRIM.BK': {
        'name': 'B.Grimm Power Public Company Limited',
        'address': 'Dr. Gerhard Link Building Krungthepkreetha Road Huamark Bangkapi Bangkok 10240 Thailand',
        'phone': '66 2 710 3400',
        'website': 'https://www.bgrimmpower.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Independent Power Producers',
        'description': 'B.Grimm Power Public Company Limited, an energy company, engages in the development, financing, construction, and operation of green-field power plants in Thailand, Laos PDR, Cambodia, the Philippines, The Republic of Korea, and Malaysia. It operates in two segments, Electricity Generating and Other Businesses. The Electricity Generation segment generates and distributes electricity for the government sectors and industrial users. The Other Businesses segment provides maintenance and operating services for power plants. The company generates electricity through co-generation, solar, hydro, wind, hybrid, and waste to energy sources. The company was founded in 1878 and is headquartered in Bangkok, Thailand.'
    },
    'BH.BK': {
        'name': 'Bumrungrad Hospital Public Company Limited',
        'address': '33 Sukhumvit Soi 3 (Nana Nua) Sukhumvit Road Klongtoey Nua Sub District Wattana Distric Bangkok 10110 Thailand',
        'phone': '66 2 066 8888',
        'website': 'https://www.bumrungrad.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Bumrungrad Hospital Public Company Limited owns and operates healthcare-related entities in Thailand and internationally. It operates allergy centers, arrhythmia centers, behavioral health centers, breast centers, breastfeeding clinics, home service centers, clinics yangon, COVID-19 recovery clinics, heart valve centers, robotic surgery centers, spine institute, rehabilitation centers, childrens (pediatrics) centers, colorectal surgery centers, complex coronary artery intervention centers, comprehensive sleep clinics, cornea transplant centers, dental centers, diagnostic centers, diagnostic radiology and nuclear medicine, dialysis centers, digestive disease centers, ear, nose and throat centers, emergency centers, endocrinology, diabetes and clinical nutrition centers, esperance, expatriate liaison centers, eye centers, fertility centers and IVF clinics, gastrointestinal motility centers, health screening centers, hearing and balance clinics, heart institute, holistic wound care centers, horizon regional cancer centers, hyperbaric oxygen therapy centers, intensive care unit, and medical clinics. The company also operates memory clinics, nephrology centers, neurocritical care, neuroscience centers, new life healthy aging clinics, nutrition services, orthopedic centers, parkinsons disease and movement disorders clinics, perinatal centers, pharmacy services, plastic (cosmetic) surgery centers, preventive genomics and integrative medicine, pride clinics, pulmonary (lung) centers, refractive surgery centers, robotic scoliosis centers, skin (dermatology) centers, sports medicine & joint centers, surgery clinics and surgery centers, travel medicine centers, urology centers, vaccine clinics, scientific wellness centers, vitallife skin and aesthetic centers, and womens centers. The company was founded in 1980 and is headquartered in Bangkok, Thailand.'
    },
    'BIG.BK': {
        'name': 'Big Camera Corporation Public Company Limited',
        'address': '115, 115/1 Sawatdikarn 1 Road Nongkheam Subdistrict Nongkheam District Bangkok 10160 Thailand',
        'phone': '66 2 809 9956',
        'website': 'https://www.bigcamera.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Specialty Retail',
        'description': 'Big Camera Corporation Public Company Limited, together with its subsidiaries, distributes cameras and photography-related products in Thailand. The company offers digital cameras, lens, action cameras/360 cameras, VDOs, drones, instant cameras/instant films, camera bags, straps, flashes, gimbal stabilizers, broadcast accessories, tripods, memory cards, filters, printers, binoculars, batteries, and others. It also provides mobile phones, and photography and mobile phone related products; and related services, including photographic processing and photographic equipment repair services, etc. In addition, the company is involved in the printing business. It operates approximately 200 branches. The company was founded in 1997 and is based in Bangkok, Thailand.'
    },
    'BIOTEC.BK': {
        'name': 'Bio Green Energy Tech Public Company Limited',
        'address': '153 Mano Tower Soi Sukumvit 39 Sukumvit Road Klongtonnua, Wattana Bangkok 10110 Thailand',
        'phone': '66 2 260 0050',
        'website': 'https://www.jutha.co.th',
        'sector': 'Industrials',
        'industry': 'Marine Shipping',
        'description': 'Bio Green Energy Tech Public Company Limited, together with its subsidiaries, provides marine transportation services in Thailand and internationally. It offers time charter; ship management services, including vessel operation and manning; and semi-liner services. The company also provides marine-related services, such as cargo booking brokerage, sale and purchase of ship brokerage, and ship charter brokerage services. In addition, it is involved in the manufacture and distribution of biodiesel and glycerin products. The company was formerly known as Jutha Maritime Public Company Limited and changed its name to Bio Green Energy Tech Public Company Limited in May 2022. Bio Green Energy Tech Public Company Limited was founded in 1976 and is headquartered in Bangkok, Thailand.'
    },
    'BIZ.BK': {
        'name': 'Business Alignment Public Company Limited',
        'address': '92/45 Sathorn Thani Building 2 16th Floor North Sathorn Road Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 636 6828',
        'website': 'https://www.bizalignment.com',
        'sector': 'Healthcare',
        'industry': 'Medical Devices',
        'description': 'Business Alignment Public Company Limited engages in the distribution and installation of medical equipment and software system for cancer treatment through radiotherapy in Thailand. It is also involved in the construction of building for locating medical equipment; and providing repair and maintenance services for medical equipment. In addition, the company operates cancer specialized hospital. Business Alignment Public Company Limited was incorporated in 2000 and is headquartered in Bangkok, Thailand.'
    },

    # 81-100
    'BJC.BK': {
        'name': 'Berli Jucker Public Company Limited',
        'address': 'Berli Jucker House, 99 Soi Rubia, Sukhumvit 42 Road Phrakanong Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2146 5999',
        'website': 'https://www.bjc.co.th',
        'sector': 'Industrials',
        'industry': 'Conglomerates',
        'description': 'Berli Jucker Public Company Limited manufactures, distributes, and services in the areas of packaging, consumer, healthcare and technical, modern retail supply chain, and other group businesses in Thailand. It designs, manufactures, markets, and distributes glass and plastic packaging products, and aluminum cans. The company is involved in the distribution of personal care products, including Cellox facial tissues and toilet papers, Zilk toilet papers, Maxmo multi-purpose papers, Tasto potato chips, Dozo rice crackers, Party and Campus extruded snacks, Parrot soaps, and Dermapon baby soaps, as well as provides logistics management services, such as warehouse, transportation, customs brokerage, and freight forwarding representative services. In addition, it offers food products comprises snacks, beverages, packaged fruits, and dairy and yogurt products; and non-food products, which includes personal care, household products, stationery and office equipment, and others. Further, the company imports and distributes medicines, medical supplies, cosmeceuticals, pharmaceuticals, food supplements, and health products; medicines for treatment of various diseases such as kidney, hematology, cardiovascular, endocrine system, genitourinary system, skeleton, infection, oncology and tumors, pediatric medicines, and beauty products. It also offers medical devices, such as computed radiography systems, ultrasound systems, digital mammography systems, X-ray systems, 3D medical image processing systems, and laboratory information systems. Additionally, the company engages in bakery, food and nutraceutical, and cosmetic ingredients; industrial chemicals and refrigerants; e-commerce business; consultancy, design, installation, and the after-sales services for cranes and solar rooftop system; and weighing control system. The company was founded in 1882 and is headquartered in Bangkok, Thailand. Berli Jucker Public Company Limited is a subsidiary of TCC Corporation Company Limited.'
    },
    'BJCHI.BK': {
        'name': 'BJC Heavy Industries Public Company Limited',
        'address': 'No. 594 Moo 4 Makhamkoo Sub-district Nikompattana District Rayong 21180 Thailand',
        'phone': '66 3 301 7345',
        'website': 'https://www.bjc1994.com',
        'sector': 'Industrials',
        'industry': 'Metal Fabrication',
        'description': 'BJC Heavy Industries Public Company Limited manufactures and sells fabricated steel and equipment, and provides modularization services in Thailand and internationally. It fabricates steel into various steel structures by cutting, bending, welding, and assembling structural steel, pipes, and components based on client design and specifications; executes large-scale modularization projects; builds steel structures for mines, power plants, and industrial plants; and manufactures a range of precast concrete products, including breakwater and port construction materials, railway sleepers, pre-stressed concrete panels, and large files for use in the construction of harbors, bridges, and railways. The company also provides built-up beams, as well as grating, galvanizing, and post-weld heat treatment services. It serves oil and gas, petrochemical, refining, mining, renewable energy, power, and other industries. BJC Heavy Industries Public Company Limited was incorporated in 1994 and is headquartered in Rayong, Thailand.'
    },
    'BKD.BK': {
        'name': 'Bangkok Dec-Con Public Company Limited',
        'address': '52/3 Moo 8 Bangbuathong-Suphanburi Road, Lahan, Bangbuathong Nonthaburi 11110',
        'phone': '66 2 925 5777',
        'website': 'http://www.bangkokdeccon.com',
        'sector': 'Industrials',
        'industry': 'Specialty Business Services',
        'description': 'The Bangkok Wooden was established in 1985. In 1992, rebranded to Bangkok Dec-Con with a registered capital of 437 million Baht by running the business as the interior design and renovation contractor and furniture manufacturers such as condominiums, hotels, office buildings, department stores, universities, hospitals, and government buildings. The company has a long experience, expertise, and availability of services. Responsible for all aspects of interior design and renovation with the expertise teams to achieve the requirements of our valuable customers. By attention to the detail and process that consideration of the customer satisfaction according to operation policies which are focused on honesty, accuracy and verifiable and safety in the workplace and necessary to be completed as the period with the quality as specified standards and on customer budget requirements. The company has two main target customers, which are state enterprises and private enterprises. We are the first interior construction company to be listed in both MAI, and later on, SET Market of Thailand.'
    },
    'BKI.BK': {
        'name': 'Bangkok Insurance Public Company Limited',
        'address': 'Bangkok Insurance Building No. 25 South Sathon Road Thung Maha Mek Sathon Bangkok 10120 Thailand',
        'phone': '66 2 285 8888',
        'website': 'https://www.bangkokinsurance.com',
        'sector': 'Financial Services',
        'industry': 'Insurance—Property & Casualty',
        'description': 'angkok Insurance Public Company Limited is involved in the non-life insurance business in Thailand. It offers fire, marine and transportation, cargo, motor, travel accident, personal accident, residential and commercial property, health, property, third party liability, business all risks, engineering, and miscellaneous insurance products. The company was incorporated in 1947 and is headquartered in Bangkok, Thailand.'
    },
    'BKKCP.BK': {
        'name': 'Bangkok Commercial Property Fund',
        'address': 'Siam Tower 24th Floor 989 Rama 1 Road Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 659 8888',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Office',
        'description': 'Bangkok Commercial Property Fund specializes in real estate investments. The Fund has invested in freehold right on 1) office and commercial strata title units in Charn Issara Tower and 2) office and commercial strata title units in Charn Issara Tower 2.'
    },
    'BLA.BK': {
        'name': 'Bangkok Life Assurance Public Company Limited',
        'address': '415 Krungthep - Nonthaburi Road Wongsawang Bangsue Bangkok 10800 Thailand',
        'phone': '66 2 777 8888',
        'website': 'https://www.bangkoklife.com',
        'sector': 'Financial Services',
        'industry': 'Insurance—Life',
        'description': 'Bangkok Life Assurance Public Company Limited, together with its subsidiaries, provides life insurance services to individuals and corporates in Thailand. Its life insurance products include protection, savings, education, pension, accident plans, total permanent disability, and health and critical illness products. The company also provides general insurance products comprise personal insurance and business all risks insurance products, including fire, motor, burglary, personal accident, accident and personal health, travel accident, cancer, golfers indemnity, home multicover, medical malpractice liability, business interruption, marine, hull, workmens compensation, money, contractors plant and equipment, contractors all risks, erection all risks, boiler and pressure vessel, electronic equipment, industrial all risks, public liability, neon-sign, plate glass, fidelity guarantee, group accident and health, and shop multicover insurance products. In addition, it offers bancassurance products; and equity, long term equity, mixed, foreign investment, fixed income, money market, fixed income, and retirement mutual funds. Bangkok Life Assurance Public Company Limited was founded in 1951 and is headquartered in Bangkok, Thailand.'
    },
    'BLAND.BK': {
        'name': 'Bangkok Land Public Company Limited',
        'address': 'New Geneva Building 47/569-576 Moo 3, 10th Floor Popular 3 Road, Tambol Bannmai Amphur Pakkred Nonthaburi 11120 Thailand',
        'phone': '66 2 504 4949',
        'website': 'https://www.bangkokland.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Diversified',
        'description': 'Bangkok Land Public Company Limited, together with its subsidiaries, engages in the real estate development, exhibition and convention, food and beverage, and hotel investment businesses in Thailand. The company develops, rents, and sells residential housings and commercial properties, including single houses, townhouses, condominiums, shophouses, high rise office buildings, shopping complex, community, and retail malls; operates hotel and various restaurants, as well as catering facilities; and operates retail shops, food courts, fresh food market, and car parks. It also provides financing services; project and infrastructure management services; building management and maintenance services; landscaping and waste treatment services; and real estate investment trust management services, as well as issues foreign currency bonds. Bangkok Land Public Company Limited was founded in 1973 and is based in Nonthaburi, Thailand.'
    },
    'BLISS.BK': {
        'name': 'Bliss Intelligence Public Company Limited (Listed company which has possibility to be delisted)',
        'address': 'office No. 96 Chaloem Phrakiat RatchakanThi 9 Road, Pravet, Nongbon Bangkok 10250',
        'phone': 'N/A',
        'website': 'http://www.blisstel.co.th',
        'sector': 'Technology',
        'industry': 'Information Technology Services',
        'description': 'Operating business in information technology, telecommunications and infrastructure. Which provides both software and hardware services'
    },
    'BOFFICE.BK': {
        'name': 'Bhiraj Office Leasehold Real Estate Investment Trust',
        'address': '591 United Business Center II Building 7th floor Sukhumvit Road Khlong Nuea Vadhana 10110 Thailand',
        'phone': '66 2 261 0170',
        'website': 'https://www.bofficereit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'To invest in long-term leasehold right over Bhiraj Tower at EmQuartier office building and ownership of movable properties related with office operation. Leasehold period is approximately 26 years and 9 months counted from register date. To invest in long-term leasehold right over Bhiraj Tower at BITEC office building and ownership of movable properties related with office operation. Leasehold period is 30 years counted from register date .'
    },
    'BPP.BK': {
        'name': 'Banpu Power Public Company Limited',
        'address': '1550 Thanapoom Tower 26th Floor New Petchburi Road Makkasan, Ratchathewi Bangkok 10400 Thailand',
        'phone': '66 2 007 6000',
        'website': 'https://www.banpupower.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Independent Power Producers',
        'description': 'Banpu Power Public Company Limited engages in thermal and renewable power business in Thailand and internationally. It produces and sells power using solar, wind, coal, and natural gas. The company is also involved in the production and sale of steam; and provision of solar rooftops, electric vehicles, energy storage, and energy management systems. It owns and operates 42 power plants and projects. The company was founded in 1996 and is headquartered in Bangkok, Thailand. Banpu Power Public Company Limited is a subsidiary of Banpu Public Company Limited.'
    },
    'BR.BK': {
        'name': 'Bangkok Ranch Public Company Limited',
        'address': '18/1 Moo 12 Langwatbangpleeyainai Rd Bangphliyai Bang Phli 10540 Thailand',
        'phone': '66 2 337 3280',
        'website': 'https://investor.bangkokranch.com',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'Bangkok Ranch Public Company Limited produces and supplies duck meat products in Thailand and internationally. The company also offers processed foods and by-products. In addition, it provides animal feed; and operates duck farms, hatcheries, feed mills, and distribution centers. Further, the company engages in the duck slaughtering and duck meat trading businesses. Bangkok Ranch Public Company Limited was founded in 1984 and is headquartered in Bang Phli, Thailand.'
    },
    'BRI.BK': {
        'name': 'Britania Public Company Limite',
        'address': '4345 Bhiraj Tower, 21st Floor, BITEC Bangna, Sukhumvit Road, Bangna, Bangna Bangkok 10260',
        'phone': '66 2 161 3000',
        'website': 'https://www.britania.co.th/',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Britania Public Company Limited engages in residential property development business in Thailand. It develops detached and semidetached houses, townhomes, townhouses, and other properties under four brand names, including Belgravia, Grand Britania, Britania, and Brighton. The company was formerly known as Origin House Company Limited. The company was incorporated in 2016 and is based in Samut Prakan, Thailand. Britania Public Company Limited is a subsidiary of Origin Property Public Company Limited.'
    },
    'BROCK.BK': {
        'name': 'Baan Rock Garden Public Company Limited',
        'address': '601 Soi Ramkhamhaeng 39, Pracha-Uthit Road Wang Thonglang Bangkok 10310 Thailand',
        'phone': '66 2 934 7000',
        'website': 'https://www.rockgarden.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Baan Rock Garden Public Company Limited engages in the real estate development business in Thailand. It develops and sells townhouses, single detached houses, and commercial buildings under the Baan Rock Garden brand. The company was formerly known as Chucheep South Group, Co., Ltd. Baan Rock Garden Public Company Limited was founded in 1990 and is headquartered in Bangkok, Thailand.'
    },
    'BRR.BK': {
        'name': 'Buriram Sugar Public Company Limited',
        'address': 'No. 237 Moo 2 Baan Sao-Ae Tambol Hin Lek Fai Amphur Kumueug Buriram 31190 Thailand',
        'phone': '66 4 466 6592',
        'website': 'https://www.buriramsugar.com',
        'sector': 'Consumer Defensive',
        'industry': 'Confectioners',
        'description': 'Buriram Sugar Public Company Limited, together with its subsidiaries, manufactures and distributes sugar and molasses in Thailand and internationally. It operates through Sugar and Molasses Business, Trading Agriculture Products, Electricity and Steam Generation and Distribution, and Others segments. The company offers refined, brown, white, cane, and raw sugar; bagasse; and filter cakes. It is also involved in trading of agricultural products; generation and distribution of electricity using biomass; and production and distribution of organic and organic chemical fertilizers using filter cakes, as well as provision of research and development services to improve the efficiency of sugarcane farming and nourishment. In addition, the company provides logistics services, which consists of land and water product transportation services, both domestic and international. Further, it is involved in the manufacture and distribution of packaging products, which are made from bagasse; and steam generation and distribution activities, as well as invests wood pellet business. The company was incorporated in 1963 and is headquartered in Buriram, Thailand. Buriram Sugar Public Company Limited operates as a subsidiary of Buriram Capital Co., Ltd.'
    },
    'BRRGIF.BK': {
        'name': 'Buriram Sugar Group Power Plant Infrastructure Fund',
        'address': '175 Sathorn City Tower, 7th , 21st and 26th Floor, South Sathorn Road, Thung Mahamek Sub-district, Sathorn District Bangkok 10120',
        'phone': '66 2 674 6488',
        'website': 'https://brrgif.com/home.html',
        'sector': 'Utilities',
        'industry': 'Utilities—Independent Power Producers',
        'description': 'BRRGIF is to invest in the right to the Net Revenue by entering into the Net Revenue Purchase and Transfer Agreement of Buriram Energy Co.,Ltd. and Buriram Power Co.,Ltd. , a subsidiary of Buriram Sugar Public Company Limited (BRR), for the period of approximately 18 years until the Expiry Date, which is April 6, 2035 .'
    },
    'BSBM.BK': {
        'name': 'Bangsaphan Barmill Public Company Limited',
        'address': '28/1 Prapawit Building 8th Floor Surasak Road Kwang Silom, Khet Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 630 0590',
        'website': 'https://www.bsbm.co.th',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'Bangsaphan Barmill Public Company Limited manufactures and distributes deformed and round steel bars for concrete building structures in Thailand. The company was incorporated in 1994 and is based in Bangkok, Thailand.'
    },
    'BTG.BK': {
        'name': 'Betagro Public Company Limited',
        'address': '323 Betagro Tower(North Park) Moo 6, Vibhavadi Rangsit Road Kwaeng Thungsonghong Ket Laksi Bangkok 10210 Thailand',
        'phone': '66 2833 8000',
        'website': 'https://www.betagro.com',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'Betagro Public Company Limited manufactures and distributes animal feed and health, and livestock products in Thailand, the Southeast Asia, other Asian countries, and internationally. It operates through nine segments: Agro Business, Export Business, Consumer Food Business, Non-Package Meat Business, Co & By-Products and Other Food Business, Livestock Business, International Business, Pet Business, and Others. The company produces and distributes livestock and aquaculture feed under the Betagro, Balance, and MASTER brands; animal pharmaceutical, supplements, and hygienic products under the Better Pharma and Nexgen brand names; packaged fresh and frozen chicken meat, pork meat, eggs, and processed food and meat under the BETAGRO, S-Pure, and ITOHAM brands; poultry meat, pork meat, egg, processed food, processed meat, and other food products; fresh pork and poultry products; and pet food products, including snacks for dogs and cats, as well as pet care products, such as medicine, supplementary food, and shampoo. It also engages in the sale and provision of farm equipment installation service comprising ventilation system, feeding system, water system, layer cage system, cooling pads, heating system, composter system, and silometric sensor; provision of laboratory testing services; sale of leftover animal parts from the slaughterhouse processes; rearing and sale of live chickens, pigs and fish to farms and industrial processors; swine and egg production; and operation of feed mill, grandparent and parent pig farms, fattening farms, layer farm, fattening pig contract farms, broiler contract farms with local farmers, poultry farms, Betagro shops, and slaughterhouse; and swine breeder trading. The company was founded in 1967 and is based in Bangkok, Thailand.'
    },
    'BTNC.BK': {
        'name': 'Boutique Newcity Public Company Limited',
        'address': '1112/53-75 Soi Sukhumvit 48 (Piyavat) Sukhumvit Road Phra Khanong Khlong Toei Bangkok 10110 Thailand',
        'phone': '66 2 391 3320',
        'website': 'https://www.btnc.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Apparel Retail',
        'description': 'Boutique Newcity Public Company Limited, manufactures and distributes womens fashion products in Thailand. It operates through four segments: Domestic Retail, Online, Foreign Retail, and Uniform. The company offers its products under the Uniform Specializer, GSP, C&D, Jousse, LOF-FI-CIEL, FLIP, and Guy Laroche brands. The company also operates AMAZE, a multi-brand store. The company was founded in 1974 and is headquartered in Bangkok, Thailand.'
    },
    'BTS.BK': {
        'name': 'BTS Group Holdings Public Company Limited',
        'address': 'TST Tower 21 Soi Choei Phuang 15th Floor Viphavadi-Rangsit Road Chomphon, Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 273 8611',
        'website': 'https://www.btsgroup.co.th',
        'sector': 'Industrials',
        'industry': 'Railroads',
        'description': 'BTS Group Holdings Public Company Limited, together with its subsidiaries, engages in mass transit, property, media, and service businesses in Thailand. The company operates in three segments: Move, Mix, and Match. It operates and maintains BTS Sky Train system; constructs, operates, installs, and maintains electric rails; and train procurement services and other related services, as well as provides bus rapid transit services. The company also offers marketing solutions through offline and online media; advertising, digital, and sales services; system installation and integration services; and insurance brokerage services for offline and online distribution channels, as well as services related to rabbit card. In addition, the company offers investment in various businesses, such as restaurant operations, construction services, golf course services, and other services businesses. Further, it invests in the securities of other companies; provides architecture and engineering work consultancy services; and manages food and beverage businesses; provides electronic payment, electronic money, and bill payment services; develops software and provides technology and system integration services; and offers CRM loyalty program and coupon kiosks. The company was formerly known as Tanayong Public Company Limited and changed its name to BTS Group Holdings Public Company Limited in May 2010. BTS Group Holdings Public Company Limited was founded in 1968 and is based in Bangkok, Thailand.'
    },
    'BTSGIF.BK': {
        'name': 'BTS Rail Mass Transit Growth Infrastructure Fund',
        'address': '175 Sathorn City Tower 7th, 21st, and 26th Floor South Sathorn Road Sathorn Bangkok 10120 Thailand',
        'phone': '66 2 674 6488',
        'website': 'http://www.btsgif.com',
        'sector': 'Industrials',
        'industry': 'Railroads',
        'description': 'The Fund has invested in the Sale Revenue to be generated from the operation of the Core BTS SkyTrain System (being the original lines of the BTS SkyTrain System covering 23.5 kilometres, consisting of the 17 kilometre Sukhumvit line from Mo-Chit to On-Nut, and the 6.5 kilometre Silom line from National Stadium to Taksin Bridge) pursuant to the Concession Agreement, from the Closing Date until the Concession Expiry Date, which is December 4 2029,the term of the Concession Agreement of which is 30 years.'
    },

    # 101-120
    'BUI.BK': {
        'name': 'Bangkok Union Insurance Public Company Limited',
        'address': '175–177 Bangkok Union Insurance Bldg Surawong Road Suriyawong Sub-District Bangrak District Bangkok 10500 Thailand',
        'phone': '66 2 233 6920',
        'website': 'https://www.bui.co.th',
        'sector': 'Financial Services',
        'industry': 'Insurance—Property & Casualty',
        'description': 'Bangkok Union Insurance Public Company Limited provides non-life insurance products for retail and corporate customers in Thailand. The company underwrites fire, marine and transportation, and motor insurance, as well as reinsurance products. It also underwrites miscellaneous insurance comprising property all risks, health, personal accident, public liability, plat glass, golfers indemnity, burglary, money, and fidelity guarantee insurance products; and engineer liability policies, including contract work, machinery, boiler, contractors equipment, and electronic equipment insurance products. In addition, it is also involved in the rental of office space. The company was incorporated in 1929 and is headquartered in Bangkok, Thailand.'
    },
    'BWG.BK': {
        'name': 'Better World Green Public Company Limited',
        'address': '488 Soi Ladprao 130 (Mahatthai 2) Ladprao Road Klongchan Sub-District Bangkapi District Bangkok 10240 Thailand',
        'phone': '66 2 012 7888',
        'website': 'https://www.bwg.co.th',
        'sector': 'Industrials',
        'industry': 'Waste Management',
        'description': 'Better World Green Public Company Limited, together with its subsidiaries, engages in integrated waste treatment and disposal of the industrial waste in Thailand. The company offers landfill disposal systems; chemical and biological wastewater treatment services for industrial factories; and solid waste-to-renewable energy systems. It also provides burning systems; analysis systems for laboratory operations; and waste management consulting services in the areas of waste management and disposal methods, transportation and collection system, wastewater treatment, waste manifest system, and social activities. In addition, the company offers construction, transportation and agency, and incinerating services; and acts as a broker or agent for the treatment of industrial waste, and hazardous or non-hazardous waste. Further, it engages in the generation and distribution of electricity; property development activities; and purchase and sale of real estate properties for industrial plants or commercial business. The company was founded in 1997 and is headquartered in Bangkok, Thailand.'
    },
    'B-WORK.BK': {
        'name': 'Bualuang Office Leasehold Real Estate Investment Trust',
        'address': '175 Sathorn City Tower, 7th, 21st and 26th Floor, South Sathorn Road, Sathorn Bangkok 10120',
        'phone': '66 2 674 6488',
        'website': 'http://www.bworkreit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'To invest in 30 years leasehold right of True Tower 1 and True Tower 2 office buildings'
    },
    'BYD.BK': {
        'name': 'Beyond Securities Public Company Limited',
        'address': '46/7 Rungrojthanakul 11th,12th Floor Ratchadaphisek Road Huai Khwang Bangkok 10310 Thailand',
        'phone': '66 2 820 0100',
        'website': 'https://www.beyondsecurities.co.th',
        'sector': 'Financial Services',
        'industry': 'Capital Markets',
        'description': 'Beyond Securities Public Company Limited provides securities brokerage services to individual and institutional investors in Thailand. The company offers securities brokerage services through securities trading accounts comprising cash, cash balance, and credit balance accounts; derivatives brokerage; internet trading; investment banking, including financial advisory, mergers and acquisitions, initial public offerings, debt financing and restructuring, real estate investment trust/infrastructure fund, corporate structuring, and capital restructuring; mutual funds; securities borrowing and lending; private funds; and fixed income products. The company was formerly known as AEC Securities Public Company Limited and changed its name to Beyond Securities Public Company Limited in August 2021. Beyond Securities Public Company Limited was incorporated in 1971 and is based in Bangkok, Thailand.'
    },
    'CBG.BK': {
        'name': 'Carabao Group Public Company Limited',
        'address': '393 Silom Building 7th - 10th floor 393, Silom Road Silom, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 636 6111',
        'website': 'https://www.carabaogroup.com',
        'sector': 'Consumer Defensive',
        'industry': 'Beverages—Non-Alcoholic',
        'description': 'Carabao Group Public Company Limited, through its subsidiaries, manufactures, markets, distributes, and sells beverages in Thailand and internationally. Its products primarily include carbonated and non-carbonated energy drinks, drinking water, ready-to-drink coffee, instant powder 3-in-1 coffee, vitamin C drinks, and sport drinks under the Carabao, Carabao Sport, and Woody C+ Lock brands. The company also manufactures and distributes bottles and glass products and aluminum cans; and packaging products for energy drinks and other beverages. In addition, it is involved in the investment, data management, and trading activities. Carabao Group Public Company Limited was founded in 2001 and is headquartered in Bangkok, Thailand.'
    },
    'CCET.BK': {
        'name': 'Cal-Comp Electronics (Thailand) Public Company Limited',
        'address': 'CTI Tower 191/54, 191/57, 18th Floor Rachadapisek Road Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 261 5033',
        'website': 'https://www.calcomp.co.th',
        'sector': 'Technology',
        'industry': 'Computer Hardware',
        'description': 'Cal-Comp Electronics (Thailand) Public Company Limited, together with its subsidiaries, manufactures electronic products worldwide. The company offers computers and computer peripherals, such as mainboards, external hard disk drives, NAS and PCBA for hard disk drives, USB pen drives, storage server PCBA, and assembly products, as well as ink-jet printers, laser printers, multi-function printers, dot-matrix printers, and large format printers; telecommunication products, including set-top boxes and their component parts, and Bluetooth headsets; and smart appliances that comprise smart TV, mirrors, and POS machines, as well as digital camera PCBA and media players. It also provides consumer electronics, which include facial cleaning brushes, iron brushes, cordless airbrush makeup kits, displays, electronic keyboards, hubs, rovers, and calculators; intelligent warehouse, machinery, and robotics, as well as smart factory products; smart beauty products comprising facial moisturizing sprays, facial cleaning brushes, facial massagers, mirror, smart body scale, and electric toothbrushes; and healthcare and wearable devices. In addition, the company offers semiconductor design and packaging services; and robotic applications for edutainment and smart service products. Cal-Comp Electronics (Thailand) Public Company Limited was founded in 1989 and is headquartered in Bangkok, Thailand.'
    },
    'CCP.BK': {
        'name': 'Chonburi Concrete Product Public Company Limited',
        'address': '39/1 Moo 1 Sukhumvit Road Tambol Huaykapi Amphur Muang Chonburi 2000 Thailand',
        'phone': '66 61 409 8877',
        'website': 'https://www.ccp.co.th',
        'sector': 'Basic Materials',
        'industry': 'Building Materials',
        'description': 'Chonburi Concrete Product Public Company Limited manufactures and distributes concrete products in Thailand. The company offers ready-mixed concrete and precast concrete for work system structure decoration. It also distributes construction materials and home decoration equipment; and manufactures and distributes autoclaved aerated concrete blocks and concrete blocks, as well as provides real estate leasing services. Chonburi Concrete Product Public Company Limited was founded in 1983 and is based in Chonburi, Thailand.'
    },
    'CEN.BK': {
        'name': 'Capital Engineering Network Public Company Limited',
        'address': '1011, Supalai Grand Tower 17th Floor Rama 3 Road Chongnonsi, Yannawa Bangkok 10120 Thailand',
        'phone': '66 2 049 1041',
        'website': 'https://www.cenplc.com',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'Capital Engineering Network Public Company Limited, through its subsidiaries, manufactures and distributes prestressed concrete wires and strand wires, and welding wires in Thailand. It also manufactures and distributes industrial equipment, transmission line towers, and telecommunication towers, as well as electricity and heat energy; and distributes substation steel structures. In addition, the company engages in the construction and tunnel excavation, trading and investing, and fabrication construction and design activities; distributes fuel for power plants; and operates biogas power plants. Further, it manufactures and sells woodchips; manages human resource functions; and leases a telecommunication tower. The company was formerly known as Eastern Wire Public Company Limited and changed its name to Capital Engineering Network Public Company Limited in May 2009. Capital Engineering Network Public Company Limited was founded in 1988 and is based in Bangkok, Thailand.'
    },
    'CENTEL.BK': {
        'name': 'Central Plaza Hotel Public Company Limited',
        'address': '1695 Phaholyothin Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 541 1234',
        'website': 'https://www.centarahotelsresorts.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Resorts & Casinos',
        'description': 'Central Plaza Hotel Public Company Limited, together with its subsidiaries, engages in the hotel business in Thailand and internationally. It operates in two segments, Hotel and Related Services Operation; and Food and Ice-Cream. It is also involved in the food and beverage, hotel management, and import and export businesses, as well as operates a spa and learning centre. The company was founded in 1980 and is based in Bangkok, Thailand.'
    },
    'CFRESH.BK': {
        'name': 'Seafresh Industry Public Company Limited',
        'address': '402 Moo 8 Chumphon-Paknam Road Paknam Mueang Chumphon 86000 Thailand',
        'phone': '66 2 637 8888',
        'website': 'https://www.seafresh.com',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Seafresh Industry Public Company Limited, together with its subsidiaries, engages in the manufacture and distribution of frozen raw shrimp, processed shrimp, vegetable and fruit, and others seafood products in Thailand and internationally. It provides raw, cooked, sushi, and value added shrimp products, as well as shrimp powder and peeled head shrimp products. The company offers its products under the Seafresh, Sea Angel, GO-GO, Thai Chia, Phoenix, C Angel, and Ultra brands. In addition, the company provides managerial, technical, supporting, and financial management services; sale of chilled seafood products; and develops, produce, and supply aqua feed solutions for aquaculture industry. Further, it offers project management and support services; integrated shrimp production facilities; retail and food services of seafood; produce and sell animal feed and nutrition; and operates seafood business, primarily offers warm water prawns. The company was founded in 1982 and is headquartered in Mueang Chumphon, Thailand.'
    },
    'CGD.BK': {
        'name': 'Country Group Development Public Company Limited',
        'address': 'No. 898 Ploenchit Tower 20th floor Ploenchit Road Lumpini, Pathum Wan Bangkok 10330 Thailand',
        'phone': '66 2 658 7888',
        'website': 'https://www.cgd.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Country Group Development Public Company Limited, together with its subsidiaries, engages in the real estate development business in Thailand and internationally. The company trades, rents, and operates real estate properties; wholesales equipment and furniture used in construction; and manages real estate properties. It also engages in the construction business. The company was formerly known as Dragon One Public Company Limited and changed its name to Country Group Development Public Company Limited in May 2010. Country Group Development Public Company Limited was incorporated in 1995 and is headquartered in Bangkok, Thailand.'
    },
    'CGH.BK': {
        'name': 'Country Group Holdings Public Company Limited',
        'address': '132, Sindhorn Tower 3 20th Floor Wireless Road Lumpini, Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 256 7999',
        'website': 'https://www.cgholdings.co.th',
        'sector': 'Financial Services',
        'industry': 'Capital Markets',
        'description': 'Country Group Holdings Public Company Limited, through its subsidiaries, primarily engages in the securities business in Thailand. It operates through three segments: Securities and Derivatives Brokerage, Investment Banking, and Securities Trading. The company offers securities brokerage, securities trading, securities underwriting, investment advisory, mutual fund management, private fund management, stock borrowing and lending, and venture capital management services. It is also involved in the derivatives brokerage, dealer, and advisor activities; and investment manager of derivative product. The company was incorporated in 2014 and is based in Bangkok, Thailand.'
    },
    'CH.BK': {
        'name': 'Chin Huay Public Company Limited',
        'address': 'No. 181 Thakham Road Samae-Dam Subdistrict Bangkhuntien District Bangkok 10150 Thailand',
        'phone': '66 2 416 0708',
        'website': 'https://chinhuay.com',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Chin Huay Public Company Limited manufactures and distributes canned food, dried fruits, and fried vegetables and fruits. It operates in Thailand, the United States of America, Japan, Canada, Italy, Mauritius, China, Myanmar, India, the Netherlands, and internationally. The company was founded in 1925 and is headquartered in Bangkok, Thailand.'
    },
    'CHARAN.BK': {
        'name': 'Charan Insurance Public Company Limited',
        'address': '408/1 Ratchadapisak Road Samsennok Huaykwang Bangkok 10310 Thailand',
        'phone': '66 2 276 1024',
        'website': 'https://charaninsurance.co.th',
        'sector': 'Financial Services',
        'industry': 'Insurance—Property & Casualty',
        'description': 'Charan Insurance Public Company Limited provides non-life insurance products in Thailand. The company offers fire, marine and transport, motor, personal accident, and miscellaneous insurance products. It also provides motor, compulsory, marine cargo, SME risks, property, engineering, and other insurance products. The company was founded in 1949 and is headquartered in Bangkok, Thailand.'
    },
    'CHASE.BK': {
        'name': 'Chase Asia Public Company Limited',
        'address': '8/9-10 Soi Vibhavadi Rangsit 44 Ladyao Subdistrict Chatuchak District Bangkok 10900 Thailand',
        'phone': '66 2 558 9009',
        'website': 'https://www.chase.co.th',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Chase Asia Public Company Limited provides debt collection and financial advisory services in Thailand. The company offers advice on debt resolution planning; debt negotiation, tracking, and debt collection services for financial institutions and companies, including telecommunication; and credit card, home, land, and auto loan provider companies, as well as insurance, hotel, and other microfinance companies. It also provides litigation, letter, and training services. The company was founded in 1998 and is based in Bangkok, Thailand.'
    },
    'CHAYO.BK': {
        'name': 'Chayo Group Public Company Limited',
        'address': '44/499-504 Phahonyothin Road Anusawari Subdistrict Bang Khen District Bangkok 10220 Thailand',
        'phone': '66 2 004 5555',
        'website': 'https://chayo555.com',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Chayo Group Public Company Limited, together with its subsidiaries, invests in and manages non-performing loans. It also provides debt tracking and collection, personal loan, and call center services, as well as product distribution through call center, TV Shopping, and online channels. The company was formerly known as Khien and Clay Company Limited and changed its name to Chayo Group Public Company Limited in December 2015. The company was founded in 1997 and is headquartered in Bangkok, Thailand.'
    },
    'CHG.BK': {
        'name': 'Chularat Hospital Public Company Limited',
        'address': '88/8-9, Teparak Km. 15 Road Tambol Bangpla Amphur Bangplee Samut Prakan 10540 Thailand',
        'phone': '66 2 033 2900',
        'website': 'https://www.chularat.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Chularat Hospital Public Company Limited operates clinics and hospitals in Thailand. It operates through two segments, Hospital Operations and Other Businesses. The company also distributes medical instruments and dietary supplement products. It operates branches of clinics and hospitals. The company was founded in 1986 is headquartered in Samut Prakan, Thailand.'
    },
    'CHOTI.BK': {
        'name': 'Kiang Huat Sea Gull Trading Frozen Food Public Company Limited',
        'address': '4/2 Moo 3, Asia 43 Road Tambol Namom Amphur Namom Songkhla 90310 Thailand',
        'phone': '66 7 422 2333',
        'website': 'https://www.kst-hatyai.com',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Kiang Huat Sea Gull Trading Frozen Food Public Company Limited, through its subsidiary, Teppitak Seafood Company Limited, manufactures and sells frozen seafood in Thailand, rest of Asia, Europe, and the United States. The company offers various block, semi-IQF, IQF, and vacuum packed items comprising raw and cooked head-on, headless, and peeled shrimps; extended shrimps; cooked tail-on butterfly, breaded, and easy peeled shrimps; and slipper lobster tail and meat. It sells its products under the Sea King, Sea Champion, Eagle, Sea Queen, Sea Flower, and Blue Gulf brands. The company was founded in 1978 and is headquartered in Songkhla, Thailand.'
    },
    'CI.BK': {
        'name': 'Charn Issara Development Public Company Limited',
        'address': '2922/200, Charn Issara Tower 2 10th Floor New Petchburi Road, Bangkapi Sub-Dist. Huaykwang District Bangkok 10310 Thailand',
        'phone': '66 2 308 2020',
        'website': 'https://www.charnissara.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Charn Issara Development Public Company Limited, together with its subsidiaries, primarily engages in real estate development activities in Thailand. The company operates through four segments: Real Estate Development, Lease of Office Condominium Units, Hotel Operations, and Sales of Goods. It develops and sells residential properties, such as single-detached houses, townhomes, condominiums, and luxury villas; operates spas and hotels; sells or leases office condominiums; and provides REIT management services. The company also engages in the dining and entertainment activities. Charn Issara Development Public Company Limited was founded in 1989 and is based in Bangkok, Thailand.'
    },
    'CIMBT.BK': {
        'name': 'CIMB Thai Bank Public Company Limited',
        'address': 'Langsuan Building 44 Langsuan Road Lumpini Patumwan Bangkok 10330 Thailand',
        'phone': '66 2 638 8000',
        'website': 'https://www.cimbthai.com',
        'sector': 'Financial Services',
        'industry': 'Banks—Regional',
        'description': 'CIMB Thai Bank Public Company Limited, together with its subsidiaries, provides various banking and financial products and services to individuals and commercial customers in Thailand. It operates through Consumer Banking and Wholesale Banking segments. The Consumer Banking segment offers consumer sales and distribution, retail financial, and commercial banking and personal financing services. The Wholesale Banking segment provides investment banking services, such as financial advisory, trade securities transactions, and asset management businesses; and corporate lending and deposit taking, transaction banking, and treasury and market services. The company also offers savings, foreign currency, and current accounts, as well as fixed deposits; personal and home loans, and multi-purpose loans; cards; and life and non-life insurance. The company was formerly known as Bank Thai Public Company Limited and changed its name to CIMB Thai Bank Public Company Limited in May 2009. CIMB Thai Bank Public Company Limited was founded in 1949 and is headquartered in Bangkok, Thailand. CIMB Thai Bank Public Company Limited is a subsidiary of CIMB Bank Berhad.'
    },

    # 121-140
    'CITY.BK': {
        'name': 'City Steel Public Company Limited',
        'address': '88/3 Moo 4, Bypass Road Tumbol Nongmaidaeng Amphur Muang Chonburi 20000 Thailand',
        'phone': '66 8 1359 6942',
        'website': 'http://www.citysteelpcl.com',
        'sector': 'Industrials',
        'industry': 'Metal Fabrication',
        'description': 'City Steel Public Company Limited, together with its subsidiaries, primarily engages in the manufacture and sale of metal structures, storage systems and material handling equipment, and fabricated metal parts in Thailand. It also provides steel service center and processing services. The companys storage systems and material handling equipment consist of racking, modular, special, mobile shelving system, pipe rack, shelving, and conveyor systems, as well as mezzanine platform, cabinets and lockers, carts and dollies, pallets, and dock and handling equipment. Further, it sells metal products, industrial materials, and equipment. The company was founded in 1995 and is headquartered in Chonburi, Thailand. City Steel Public Company Limited is a subsidiary of WKP Asset Plus Company Limited.'
    },
    'CIVIL.BK': {
        'name': 'Civil Engineering Public Company Limited',
        'address': '68/12 CEC Building 7th Floor Kampaengpet 6 Road Ladyao, Jatujak Bangkok 10900 Thailand',
        'phone': '66 2 589 8888',
        'website': 'https://www.civilengineering.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'Civil Engineering Public Company Limited provides construction services in Thailand. It constructs highways and roads, high speed and double track rail systems, airports and ports, and water infrastructure and industrial projects, as well as other projects, such as waste ponds and wastewater treatment systems. The company also manufactures and sells reinforced concrete pipes for drainage works; prefabricated hollow concrete bridge sections, reinforced concrete parts, and prefabricated products; concrete products; and asphaltic products, as well as corrugated steel railing products that are used for highway works. In addition, it trades in construction materials; and engages in the investment and real estate development business that covers rental of office buildings. The company was founded in 1966 and is headquartered in Bangkok, Thailand. Civil Engineering Public Company Limited is a subsidiary of Atsavasirisuk Holding Company Limited.'
    },
    'CK.BK': {
        'name': 'CH. Karnchang Public Company Limited',
        'address': '587 Viriyathavorn Building Sutthisarnvinitchai Road Ratchadaphisek Subdistrict Dindaeng District Bangkok 10400 Thailand',
        'phone': '66 2 277 0460',
        'website': 'https://www.ch-karnchang.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'CH. Karnchang Public Company Limited, together with its subsidiaries, provides construction services in Thailand and the Lao Peoples Democratic Republic. It operates through Construction and Related Service; and Investment in Infrastructure Business segments. The companys construction business engages in construction by accepting engagements from government agencies, state enterprises, and private entities in the form of main contractor and sub-contractor. In addition, it invests in infrastructure project development business, which includes transportation, mass rapid transit, water infrastructure, and electric power systems through operate-transfer, build-transfer-operate, build-own-operate, build-own-operate-transfer, etc.; and engages in the sale of construction materials and rents construction. The company was founded in 1972 and is headquartered in Bangkok, Thailand.'
    },
    'CKP.BK': {
        'name': 'CK Power Public Company Limited',
        'address': 'No. 587 Viriyathavorn Buildin 19th Floor Sutthisan Winitchai Road Ratchadaphisek Subdistrict, Dindaeng Sub Bangkok 10400 Thailand',
        'phone': '66 2 691 9720',
        'website': 'https://www.ckpower.co.th',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'CK Power Public Company Limited, through its subsidiaries, generates and sells electricity and steam in Thailand. The company operates through three segments: Generation of Electricity from Hydroelectric Power, Generation of Electricity from Solar Power, and Generation of Electricity from Thermal Power. It also operates 2 hydro power plants with a capacity of 1,900 MW; 9 solar power plant with a capacity of 29 MW; and 2 cogeneration power plants with installed capacity of 238 MW. In addition, the company provides consulting and other services related to electricity generating projects. CK Power Public Company Limited was incorporated in 2011 and is based in Bangkok, Thailand.'
    },
    'CM.BK': {
        'name': 'Chiangmai Frozen Foods Public Company Limited',
        'address': '149/34 Soi Anglo Plaza 3rd-4th Floor Surawongse Road Surawongse, Bangrak Bangkok 10500 Thailand',
        'phone': 'Consumer Defensive',
        'website': 'Packaged Foods',
        'sector': '149/34 Soi Anglo Plaza 3rd-4th Floor Surawongse Road Surawongse, Bangrak Bangkok 10500 Thailand',
        'industry': '66 2 238 4091',
        'description': 'https://www.cmfrozen.com'
    },
    'CMAN.BK': {
        'name': 'Chememan Public Company Limited',
        'address': '195/11-12 Lake Rajada Office Complex 2 10th-11th Floor Rajadapisek Road Klongtoey District Bangkok 10110 Thailand',
        'phone': '66 2 661 9734',
        'website': 'https://www.chememan.com',
        'sector': 'Basic Materials',
        'industry': 'Specialty Chemicals',
        'description': 'Chememan Public Company Limited manufactures and distributes mineral lime and chemical products in Thailand. The companys products include quicklime, hydrated lime, and limestone and grinded limestone. Its lime products are used in industrial, agricultural, environmental, and household applications. The company also provides dump and tank trucks transportation services, as well as technical support services. It also exports its products. The company was incorporated in 2003 and is headquartered in Bangkok, Thailand.'
    },
    'CMC.BK': {
        'name': 'Chaoprayamahanakorn Public Company Limited',
        'address': '909/1, CMC Tower 6th Floor, Unit 601-602 Somdejprachaotaksin Road, Dao Khanong Khet Thonburi District Bangkok 10600 Thailand',
        'phone': '66 2 468 9000',
        'website': 'https://www.cmc.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Diversified',
        'description': 'Chaoprayamahanakorn Public Company Limited engages in the residential real estate development activities in Thailand. It is also involved in the real estate rental, construction, hospitality, and mecial equipment and herbal medical supply businesses. The company was founded in 1994 and is based in Bangkok, Thailand.'
    },
    'CMR.BK': {
        'name': 'Chiang Mai Ram Medical Business Public Company Limited',
        'address': '1, Sukkasem Road Nakhon Ping Subdistrict Patan Subdistrict Mueang District Chiang Mai 50300 Thailand',
        'phone': '66 5 213 4777',
        'website': 'https://www.lanna-hospital.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Chiang Mai Ram Medical Business Public Company Limited, together with its subsidiaries, operates a medical care center in Thailand. It offers medical services in the areas of internal medicine, cardiology, general practice, pediatric, orthopedic and general surgery, pediatric surgery, obstetrics-gynecology, radiology, dentistry, anesthetic, ENT, and eye; and operates sub-specialty clinics for urology, neurology, endocrinology, oncology, hematology, plastic surgery, GI tract, and dermatology, as well as infertile and gynecologic oncology clinics. The company also provides dental, X-ray, CT colonoscopy, cardiac catheterization, gynecologic cancer, back pain, physical therapy, operating theatre, laboratory examination, real-time PCR, ambulance, and CRD and health check-up services; and insurance products. It operates a medical care center under the Lanna Hospital name. The company was founded in 1974 and is headquartered in Chiang Mai, Thailand. Chiang Mai Ram Medical Business Public Company Limited is a subsidiary of Vibhavadi Medical Center Public Company Limited.'
    },
    'CNT.BK': {
        'name': 'Christiani & Nielsen (Thai) Public Company Limited',
        'address': '727 La Salle Road Bangna-Tai Subdistrict Bangna Bangkok 10260 Thailand',
        'phone': '66 2 338 8000',
        'website': 'https://www.cn-thai.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'Christiani & Nielsen (Thai) Public Company Limited, together with its subsidiaries, provides construction services for government and private sectors in Thailand, Myanmar, and Cambodia. The company operates in two segments, Construction Services and Sales and Service. It engages in the design and construction of building and civil engineering projects; and design, fabrication, and erection of steel structures, and mechanical and electrical installations. The company also provides services for energy solutions in solar, wind, and other renewable energy sectors; develops renewable energy based power producing facilities; and develops office buildings, residential buildings, and commercial and industry buildings. The company was formerly known as Christiani & Nielsen (Siam) Ltd. and changed its name to Christiani & Nielsen (Thai) Public Company Limited in November 1992. The company was founded in 1904 and is headquartered in Bangkok, Thailand. Christiani & Nielsen (Thai) Public Company Limited is a subsidiary of Globex Corporation Limited.'
    },
    'COM7.BK': {
        'name': 'Com7 Public Company Limited',
        'address': '549/1 Sanphawut Road Bangna Tai Bangkok 10260 Thailand',
        'phone': '66 2 017 7777',
        'website': 'https://www.comseven.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Specialty Retail',
        'description': 'Com7 Public Company Limited, together with its subsidiaries, engages in the retail business of information technology products in Thailand. The companys products include laptop computers, desktop computers, mobiles, phones, tablets, and IT products and accessories. The company also develops computer software; provides repair and other services, as well as training services. In addition, it engages in distribution activities. The company offers products through its retail outlets and bnn.in.th website, as well as apple product repair centers. Com7 Public Company Limited was founded in 2004 and is headquartered in Bangkok, Thailand.'
    },
    'COTTO.BK': {
        'name': 'SCG Ceramics Public Company Limited',
        'address': '1 Siam Cement Road Bangsue Bangkok 10800 Thailand',
        'phone': '66 2 586 3333',
        'website': 'https://www.scgceramics.com',
        'sector': 'Industrials',
        'industry': 'Building Products & Equipment',
        'description': 'SCG Ceramics Public Company Limited manufactures, distributes, sells, and installs ceramic tiles in Thailand and internationally. Its products include ceramic floor and wall tiles. The company offers its ceramic tiles under the COTTO, SOSUCO, and CAMPANA brands. It is also involved in the development of industrial estate; and installation of solar equipment, as well as real estate business. The company was incorporated in 2018 and is headquartered in Bangkok, Thailand. SCG Ceramics Public Company Limited is a subsidiary of SCG Building Materials Co., Ltd.'
    },
    'CPALL.BK': {
        'name': 'CP ALL Public Company Limited',
        'address': '313 C.P. Tower 24th Floor, Silom Road Bangrak District Bangkok 10500 Thailand',
        'phone': '66 2 071 9000',
        'website': 'https://www.cpall.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Grocery Stores',
        'description': 'CP ALL Public Company Limited, together with its subsidiaries, operates and franchises convenience stores under the 7-Eleven name to other retailers primarily in Thailand. It operates through three segments: Wholesale Business, Retail Business, and Management of Rental Spaces in Shopping Centers. The Wholesale Business segment engages in import, export, and distribution of frozen and chilled food with delivery services and focuses on selling consumer products, including fresh food, dry food, and consumer products under Makro brand. Its Retail Business segment is involved in domestic supply chain, distribution system, logistics network, and brand equity businesses. This segment also sells its products under various domestic, international, and small and medium enterprises brands. The companys Management of Rental Spaces in Shopping Centers segment manages buildings and retail spaces in shopping malls. In addition, the company is involved in sale and maintenance of retail equipment; cash and carry, catalog, and e-commerce businesses; marketing and advertising activities; provision of information technology and research and development services, as well as engaged in bill payment collection, life insurance, and non-life insurance broker business. Further, the company offers educational institution, training, business seminar services, as well as healthcare and medical specialists consultation services. The company was formerly known as C.P. Seven Eleven Public Company Limited. CP ALL Public Company Limited was founded in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'CPF.BK': {
        'name': 'Charoen Pokphand Foods Public Company Limited',
        'address': '313 C.P. Tower Silom Road Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 766 8000',
        'website': 'https://www.cpfworldwide.com',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'Charoen Pokphand Foods Public Company Limited, together with its subsidiaries, operates in the agro-industrial and integrated food businesses in Thailand and internationally. It operates in two segments, Livestock Business and Aquaculture Business. The company produces and sells swine, chicken, duck, pigs, shrimp, and fish feed; and breeds and farms swine, broiler, layer, duck, and shrimp. It is also involved in the animal feed raw materials distribution, investment and international trading, food products wholesale and retail, property investment, property lease-out, shrimp hatchery, and animal feedmill businesses. In addition, the company produces and distributes elite seeds, pet food, chlortetracycline, aquatic feed, and sea food products; and imports and distributes eggs, processed meat, milk products, and ready meals. Further, it offers economic and trade consulting, management and advisory, financial guarantee, biological waste management, information technology, food research and development, logistics, and financial services. Additionally, the company engages in the operation of food processing plants, hotels and restaurants, slaughterhouses, and training centers; broiler chicken integration business; provision and development of Asian food products; and swine farm construction activities. It provides its products primarily under the CP brand. The company also exports its products. Charoen Pokphand Foods Public Company Limited was incorporated in 1978 and is headquartered in Bangkok, Thailand.'
    },
    'CPH.BK': {
        'name': 'Castle Peak Holdings Public Company Limited',
        'address': 'CPH Tower 9-14th Floor 899 Petchkasem Road Khet Bangkae, Bangkae District Bangkok 10160 Thailand',
        'phone': '66 2 455 0300',
        'website': 'https://www.castlepeak.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Apparel Manufacturing',
        'description': 'Castle Peak Holdings Public Company Limited, together with its subsidiaries, manufactures and exports garments in Thailand. It operates in two segments, Garment Manufacturing, and Development of Real Estate for Sale. The company primarily offers jackets, fashion coats, shorts, pants, skirts, skorts, dressed, pets wear, and outerwear. It exports its garments to the United States, Europe and other countries. The company was founded in 1976 and is headquartered in Bangkok, Thailand.'
    },
    'CPI.BK': {
        'name': 'Chumporn Palm Oil Industry Public Company Limited',
        'address': '296, Moo 2, Phet Kasem Road Tambon Salui Salui Sub District Thasae District Tha Sae 86140 Thailand',
        'phone': '66 7 761 1000',
        'website': 'https://www.cpi-th.com',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'Chumporn Palm Oil Industry Public Company Limited, together with its subsidiaries, manufactures and distributes palm oil products in Thailand. It also provides palm seeds and sprouts, palm seedling products, and crude palm oil and crude palm kernel oil; refined bleached deodorized (RBD) palm oil, palm kernel oil, palm olein, and palm stearin; and palm fatty acid distillate, palm kernel fatty acid distillate, and kernel meal for the use in soap, food, and margarine and shortening industries, as well as used as a raw material for animal feed. The company offers oils in PET bottles, tins, and pouches under the LEELA brand, as well as acts as an original equipment manufacturer. In addition, it produces and distributes biodiesel, and electricity from biogas. The company also exports its products. Chumporn Palm Oil Industry Public Company Limited was incorporated in 1979 and is headquartered in Tha Sae, Thailand.'
    },
    'CPL.BK': {
        'name': 'CPL Group Public Company Limited',
        'address': '700 Moo 6 Sukhumvit Road Bang Poo Mai Muang Samutprakran Samut Prakan 10280 Thailand',
        'phone': '66 2 709 5633',
        'website': 'https://www.cpl.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Footwear & Accessories',
        'description': 'CPL Group Public Company Limited manufactures and distributes leather products in Thailand. It offers leather products, which include full grain and suede split leather products comprising nubuck, oil and wax, pigment, sued, and waterproof leather for shoe factories; and aniline and cow splits leather. The company also provides tanning services; and manufactures and distributes personal protective equipment. The company also exports its products to China, Vietnam, Indonesia, India, etc. CPL Group Public Company Limited was founded in 1989 and is headquartered in Samutprakarn, Thailand.'
    },
    'CPN.BK': {
        'name': 'Central Pattana Public Company Limited',
        'address': 'the Offices at CentralWorld 31st Floor 999/9 Rama I Road Patumwan District Bangkok 10330 Thailand',
        'phone': '66 2 667 5555',
        'website': 'https://www.centralpattana.co.th/en',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Diversified',
        'description': 'Central Pattana Public Company Limited invests in, develops, and manages real estate properties in Thailand. It develops and rents shopping centers, office buildings, condominiums, and residential buildings; offers property management consulting and corporate services; and sells land, houses, and condominium units. The company also offers utility services for shopping centers; and sells food and beverages. In addition, the company operates play land, water theme parks, and hotels; manages real estate investment trust, condominium juristic person, and housing estate juristic person; and provides training and personnel development services. Central Pattana Public Company Limited was founded in 1980 and is headquartered in Bangkok, Thailand.'
    },
    'CPNCG.BK': {
        'name': 'CPN Commercial Growth Leasehold Property Fund',
        'address': 'SCB Park Plaza 1 7-8th Floor 18 Ratchadapisek Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 949 1500',
        'website': 'https://www.cpncg.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Diversified',
        'description': 'CPN Commercial Growth Leasehold Property Fund invests in real estate. The fund focuses on prime office buildings in Bangkoks Central Business District.'
    },
    'CPNREIT.BK': {
        'name': 'CPN Retail Growth Leasehold REIT',
        'address': 'No. 999/9 Rama I Road Pathumwan Sub-district Pathumwan District Bangkok 10900 Thailand',
        'phone': '66 2 667 5555',
        'website': 'https://www.cpnreit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Diversified',
        'description': 'CPN Retail Growth Leasehold REIT (CPNREIT) is Thailands largest retail-focused real estate investment trust listed on the Stock Exchange of Thailand (SET). CPNREIT was established from the conversion of CPN Retail Growth Leasehold Property Fund (CPNRF) which was set up and publicly traded on the SET since 2005. Upon conversion on 1 December 2017, CPNREIT acquired all CPNRFs quality portfolio, and invested in a new mix-used project consisting of CentralFestival Pattaya Beach shopping center and Hilton Pattaya. At present, CPNREIT invested in a well-diversified portfolio of 5 shopping centers and 1 hotel across Thailands prime destinations.'
    },
    'CPT.BK': {
        'name': 'CPT Drives and Power Public Company Limited',
        'address': 'No.230/7, Thetsabarnrungruknuer Road Ladyao Jattujak Bangkok 10900 Thailand',
        'phone': '66 2 954 2590',
        'website': 'https://www.cptthailand.com',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'CPT Drives and Power Public Company Limited, together with its subsidiaries, provides electrical power and control systems in Thailand. The company offers drives and automation products, such as DC drives, LV and MV inverters, and starters; PLC, SCADA, and HMI products; speed feedback devices; and motion-controllers. It also provides electrical power components, including MCCB and ELCB, contactors and relays, air circuit and vacuum circuit breakers, vacuum contactors, power fuses, ring main units, motor protection relays, MV switchgears, transformers, and bus ducts; liquid and oil-cooled starters/NGR products; and power capacitors. In addition, the company offers electric motor products, such as AC and DC motors. CPT Drives and Power Public Company Limited was founded in 1995 and is headquartered in Bangkok, Thailand.'
    },

    # 141-160
    'CPTGF.BK': {
        'name': 'C.P. Tower Growth Leasehold Property Fund',
        'address': 'Empire Tower 32nd Floor 195 South Sathon Road Yannawa, Sathon Bangkok 10120 Thailand',
        'phone': '66 2 686 6100',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'The Fund has invested in the leasehold rights to land, buildings, components of land and buildings, and systems which are necessary for utilizing the buildings, and ownership of equipment and other assets which are and necessary for the utilizing of the office buildings. There are 30-year leasehold rights to 3 (three) buildings which the Fund has invested in, as follows 1) C.P. Tower 1 (Silom) Building 2) C.P. Tower 2 (Fortune Town) Building and 3) C.P. Tower 3 (Phayathai) Building.'
    },
    'CPW.BK': {
        'name': 'Copperwired Public Company Limited',
        'address': '159/6 Serm-Mit Tower Unit 201-202, 2nd Floor Sukhumvit 21 (Asoke) road North Klongtoey, Wattana Bangkok 10110 Thailand',
        'phone': '66 2 665 2950',
        'website': 'https://www.copperwired.co.th',
        'sector': 'Technology',
        'industry': 'Electronics & Computer Distribution',
        'description': 'Copperwired Public Company Limited distributes and repairs computers, mobile phones, and related accessories in Thailand. It also engages in the import, purchase, sale, and retail of computer and electronic accessories. The company was incorporated in 2019 and is based in Bangkok, Thailand. Copperwired Public Company Limited operates as a subsidiary of Vnet Capital Co., Ltd.'
    },
    'CRANE.BK': {
        'name': 'Chukai Public Company Limited',
        'address': '44/88 Moo 1 , Sisa Chorakhe Ya Bangsaothong Samut Prakan 10570 Thailand',
        'phone': '66 2 715 0000',
        'website': 'https://www.chukai.co.th',
        'sector': 'Industrials',
        'industry': 'Rental & Leasing Services',
        'description': 'Chukai Public Company Limited, together with its subsidiaries, engages in the heavy duty machinery business. It sells truck cranes, all terrain cranes, rough terrain cranes, crawler cranes, drilling rigs, wall grabs, and excavators. The company is also involved in the rental of heavy duty machinery, such as forklifts, container handlers, trucks, trailers, and tail trailers; and foundation construction business, including bored piles, barrette piles, diaphragm walls, high-pressure cement injection, and general construction work. In addition, it provides repair services for heavy duty machinery. The company was incorporated in 1997 and is headquartered in Samut Prakan, Thailand.'
    },
    'CRC.BK': {
        'name': 'Central Retail Corporation Public Company Limited',
        'address': '22 Soi Somkid Ploenchit Road Lumpini Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 650 3600',
        'website': 'https://www.centralretail.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Department Stores',
        'description': 'Central Retail Corporation Public Company Limited operates as a multi-format and multi-category retailing platform in Southeast Asia and Italy. It operates through Fashion, Hardline, Food and Property segments. The company focuses on apparel, accessories, electronics, and home improvement products, as well as groceries. It also provides vitamins, dietary supplements, and medical supplies by doctors, as well as leases retail property to third parties. Central Retail Corporation Public Company Limited was founded in 1947 and is headquartered in Bangkok, Thailand.'
    },
    'CSC.BK': {
        'name': 'Crown Seal Public Company Limited',
        'address': '5 Soi Rangsit-Nakornnayok 46 Prachatipat Thanyaburi 12130 Thailand',
        'phone': '66 2 533 0450',
        'website': 'https://www.crownseal.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Packaging & Containers',
        'description': 'Crown Seal Public Company Limited manufactures and distributes caps for bottles in Thailand and internationally. It operates through Manufacture and Sale of Caps; and Hire of Printing Sheets for Can segments. The companys products include crown, pilfer-proof, maxi crown, ring pull, maxi, maxi-PG, plastic, and composite caps, which are used as container seals for various drinks, such as soft drink, tea, soy milk and juice, health beverage, energy and sport drink, alcohol, drug, green tea drink, drinking water, beer, liquor, soda, chicken essences, birds nests, concentrated juice, and medical supplies, etc. It also provides hand-crowner; maxi crimping; and pilfer-proof cap crimping machines, as well as coating and printing services on steel and aluminum sheets. In addition, the company offers pre-sales and after-sales services; supplies spare parts; and equipment sale and services. Crown Seal Public Company Limited was incorporated in 1968 and is headquartered in Thanyaburi, Thailand.'
    },
    'CSP.BK': {
        'name': 'CSP Steel Center Public Company Limited',
        'address': 'No. 475 Rama 3 Road Bangklo Bangkolaem Bangkok 10120 Thailand',
        'phone': '66 2 291 6314',
        'website': 'https://www.cspsteel.com',
        'sector': 'Basic Materials',
        'industry': 'Steel',
        'description': 'CSP Steel Center Public Company Limited manufactures and distributes steel products in Thailand. It offers steel sheets, such as master coil, cutting sheet, slitting coil, and tolling for processing steel. The company also provides hot-rolled and cold-rolled steel sheets and pipes; and specializes in customizing steel sheets to other shapes. It serves clients in the automobiles, home and electric appliances, steel furniture, general usage, and structure and construction industries. The company was formerly known as CSP Trading Company Limited and changed its name to CSP Steel Center Public Company Limited in July 2005. CSP Steel Center Public Company Limited was founded in 1992 and is headquartered in Bangkok, Thailand.'
    },
    'CSR.BK': {
        'name': 'City Sports and Recreation Public Company Limited',
        'address': '22 Navatanee Road Ramindra Kannayao Bangkok 10230 Thailand',
        'phone': '66 2 376 1818',
        'website': 'http://www.navatanee.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Leisure',
        'description': 'City Sports and Recreation Public Company Limited operates golf courses, restaurants, and sport clubs in Thailand. The company was founded in 1970 and is headquartered in Bangkok, Thailand.'
    },
    'CSS.BK': {
        'name': 'Communication & System Solution Public Company Limited',
        'address': '329 Moo 3 Banmai Sub-district Pakkred District Nonthaburi 11120 Thailand',
        'phone': '66 2 018 1111',
        'website': 'https://www.cssthai.com',
        'sector': 'Technology',
        'industry': 'Electronics & Computer Distribution',
        'description': 'Communication & System Solution Public Company Limited, together with its subsidiaries, distributes and installs production equipment for electricity, water, air conditioning, and telecommunication systems in Thailand. The company operates through two segments: Distribution Electrical Equipment and Installation Service segment. The Distribution Electrical Equipment segment supplies electronic cables and other electrical systems equipment, and fire protection equipment. The Installation Service segment designs and installs telecommunication and fire protection systems. The company also distributes and installs tubes. Communication & System Solution Public Company Limited was founded in 1994 and is headquartered in Nonthaburi, Thailand.'
    },
    'CTARAF.BK': {
        'name': 'Centara Hotels and Resorts Leasehold Property Fund',
        'address': '400/22 KASIKORNBANK Building 6th and 12th floor Phahon Yothin Road Samsen Nai Sub-District, Phaya Thai District Bangkok Thailand',
        'phone': '66 2 673 3999',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'Centara Hotels and Resorts Leasehold Property Fund is a fund of Kasikorn Asset Management Co.,Ltd. The Fund has invested in propertys leasehold right named Centara Grand Beach Resort Samui.'
    },
    'CTW.BK': {
        'name': 'Charoong Thai Wire and Cable Public Company Limited',
        'address': '589/71, Central City Tower 12A Floor Debaratana Road North Bangna Sub-District, Bangna Dist. Bangkok 10260 Thailand',
        'phone': '66 2 745 6118',
        'website': 'https://www.ctw.co.th',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'Charoong Thai Wire and Cable Public Company Limited, together with its subsidiaries, manufactures and distributes electric wires and cables, and telephone cables under the CTW brand in Thailand, India, China, and internationally. It operates in four segments: Power Cable, Communication Cable, Fiber Optic Cable, and Enameled and Non-Enameled Wire. The company offers aluminum electrical wires and cables, copper electrical wires, high-voltage and low voltage power cables, telecommunication cables, fire resistance and flame-retardant cables, and control and instrument cables, as well as aluminum/copper conductor cables. Further, it manufactures and distributes fiber optic cables; and enameled and non-enameled wires, including enameled copper and aluminum wires, and non-enameled copper wires. In addition, the company engages in the fabrication of copper rods; and designing and manufacturing of custom OEM products. It serves government and private sector clients. Charoong Thai Wire and Cable Public Company Limited was founded in 1967 and is headquartered in Bangkok, Thailand.'
    },
    'CV.BK': {
        'name': 'Clover Power Public Company Limited',
        'address': 'No. 159 Soi Rama IX 57/1 (Wiset Suk 2) Phatthanakan Suanluang Bangkok 10250 Thailand',
        'phone': '66 2 731 7999',
        'website': 'https://www.cloverpower.co.th',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'Clover Power Public Company Limited engages in generation and sale of electricity. It operates power plant and waste power plants. The company is involved in the design, construction, maintenance, and management of power plants; supplying and trading of machinery and equipment; operation of waste recycling and waste power plant to produce and distribute waste fuel; and supplying and distributing biomass fuel. It operates in Thailand and Australia. Clover Power Public Company Limited was incorporated in 2013 and is headquartered in Bangkok, Thailand.'
    },
    'CWT.BK': {
        'name': 'Chai Watana Tannery Group Public Company Limited',
        'address': 'No. 176/1,1480 Moo 1 Tannery Industrial District (K.M. 30) Sukhumwit Road Thambon Thaiban Mueang Samut Prakan 10280 Thailand',
        'phone': '66 2 703 7880',
        'website': 'http://www.cwt.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Auto Parts',
        'description': 'Chai Watana Tannery Group Public Company Limited, together with its subsidiaries, manufactures and exports leather-based products. It operates through six segments: Tannery Hide, Automotive Leather Cutting, Dog Chewable Toys, Furniture, Energy Business, and Design and Distribution of Aluminum Boat and Mini Bus. The company offers trim seat covers, steering wheels and gear knobs, and dog chews, as well as quilting, cutting, spray, and beam house and tanning services. In addition, it is involved in the design and distribution of boats and minibuses made from aluminum; property rental business; provision of consulting services for renewable energy projects; wholesale of wood chips; and generation and sale of electricity using waste. Further, the company provides services on waste disposal plants. Chai Watana Tannery Group Public Company Limited was founded in 1972 and is headquartered in Mueang Samut Prakan, Thailand.'
    },
    'DCC.BK': {
        'name': 'Dynasty Ceramic Public Company Limited',
        'address': '37/7 DCC Building Suthisarn-Vinijchai Road Samsen-Nok Sub-district HuayKwang District Bangkok 10310 Thailand',
        'phone': '66 2 276 9275',
        'website': 'https://www.dynastyceramic.com',
        'sector': 'Industrials',
        'industry': 'Building Products & Equipment',
        'description': 'Dynasty Ceramic Public Company Limited engages in the manufacture and sale of ceramic wall and floor tiles in Thailand and internationally. It offers its products under the Dynasty, Tile Top, Jaguar, Value, Mustang, Chicken, Birdie, Ducky, Swan, M, Cosmo, Rover, and Monte brand names. The company was formerly known as Royal Floor Tile Co. Ltd. and changed its name to Dynasty Ceramic Public Company Limited. Dynasty Ceramic Public Company Limited was founded in 1989 and is headquartered in Bangkok, Thailand.'
    },
    'DCON.BK': {
        'name': 'Dcon Products Public Company Limited',
        'address': '3300/57 Chang Tower B Building 8th Floor Phaholyothin Road Chomphon Subdistrict, Chatuchak District Bangkok 10900 Thailand',
        'phone': '66 2 937 3312',
        'website': 'https://www.dconproduct.com',
        'sector': 'Basic Materials',
        'industry': 'Building Materials',
        'description': 'Dcon Products Public Company Limited, together with its subsidiaries, manufactures and sells construction supplies in Thailand. It operates through Sales of Construction Supplies; Sales of Real Estate; and Real Estate for Lease segments. The company provides pre-stressed planks and piles, corrugated planks, cowboy and concrete fences, blocks, hallow core, hexagon piles, and footing products under the DCON name; and precast walls and floors, concrete posts, and other products. It is also involved in the sale and lease of real estate properties. The company was incorporated in 1996 and is headquartered in Bangkok, Thailand.'
    },
    'DDD.BK': {
        'name': 'Do Day Dream Public Company Limited',
        'address': 'No. 32, Keharomklao Road Ratpattana Saphansung Bangkok 10240 Thailand',
        'phone': '66 2 917 3055',
        'website': 'https://www.dodaydream.com',
        'sector': 'Consumer Defensive',
        'industry': 'Household & Personal Products',
        'description': 'Do Day Dream Public Company Limited, together with its subsidiaries, manufactures and distributes skin care products and supplements in Thailand. The company operates through Skincare business and Beauty Products business segments. It offers acne-prone and sensitive skin products under OXECURE; skin care and deep-nourishing products under SOS; hair styling appliance under LESASHA; oral care products, including toothpastes and toothbrushes under SPARKLE; and fitness equipment under JASON brands. In addition, the company provides home electrical appliance under AT HOME; hair removal devices under EMJOI; intense pulse light hair removal devices under SMOOTH SKIN; beauty innovation products under Kuron; and electrical appliance for cooking under BEAR brands. Do Day Dream Public Company Limited was incorporated in 2010 and is headquartered in Bangkok, Thailand.'
    },
    'DELTA.BK': {
        'name': 'Delta Electronics (Thailand) Public Company Limited',
        'address': '909 Soi 9, Moo 4, E.P.Z. Bangpoo Industrial Estate Tambon Prakasa Amphur Muangsamutprakarn Samut Prakan 10280 Thailand',
        'phone': '66 2 709 2800',
        'website': 'https://www.deltathailand.com',
        'sector': 'Industrials',
        'industry': 'Electrical Equipment & Parts',
        'description': 'Delta Electronics (Thailand) Public Company Limited, together with its subsidiaries, researches and develops, manufactures, and distributes electronic products. It operates through Power Electronics, Infrastructure, and Automation segments. It offers inductors, RF inductors, transformers, networking products, EMI filters, solenoids, current sensing resistors, and power modules; switching power supplies, standard power modules, and lighting ballasts and LED drivers; DC brushless fans and blowers, motors, thermal management products, cabinet thermal solutions, and indoor air quality and automotive fans; EV/HEV powertrain solutions and power electronics components comprise of on-board chargers and DC/DC converters; and display and visualization, mobile power, industrial power, and medical power products, as well as healthcare devices. The company also provides industrial automation products and solutions, including drives and power quality products, motion control solutions, control systems, robots, software systems, and manufacturing equipment, as well as field devices that include temperature controllers, machine vision systems, power meters, and smart and vision sensors. In addition, it offers building automation products comprising building management and control system, LED lighting, intelligent surveillance, and building energy management system products; telecom power systems, networking systems, and UPS and datacenter infrastructure solutions; and EV charging and energy storage systems, renewable energy, industrial battery charging, healthcare devices, industrial equipment, energy IoT, and display and visualization products. Further, the company rents properties. It operates in the United States, China, Germany, India, Ireland, Mexico, Singapore, Norway, Taiwan, the Netherlands, and internationally. Delta Electronics (Thailand) Public Company Limited was incorporated in 1988 and is based in Samut Prakan, Thailand.'
    },
    'DEMCO.BK': {
        'name': 'Demco Public Company Limited',
        'address': '59 Moo 1, Tambol Suanphrikthai Amphur Muangpathumthani Pathum Thani 12000 Thailand',
        'phone': '66 2 959 5811',
        'website': 'https://www.demco.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'Demco Public Company Limited, together with its subsidiaries, engages in the provision of electric system construction and service works in the fields of electric engineering and telecommunication in Thailand. The company operates through six segments: Sales, Electricity from Solar Power, Electrical Work Services, Electrical and Mechanical Work Services, Engagement Work Services, and Other Services. The Sales segment produces and sells steel structure fabrications for electrical and telecommunication works, as well as supplies water. The Electricity from Solar Power segment generates and sells electricity from solar power. The Electrical Work Services segment designs, constructs, and manages electrical work. The Electrical and Mechanical Work Services segment designs, constructs, and manages mechanical and electric systems and facilities, such as electrical, water management, air-conditioning and ventilation, and steam and hot water systems. The Engagement Work Services segment produces and installs fabricated steel structures and high pressure vessels. The Other Services segment provides civil work, communication, and other services. It also manufactures and trades in steel structures and steel towers; and trades in assembled telecommunication equipment, communication equipment, and electrical equipment, as well as sells construction materials. The company was incorporated in 1992 and is headquartered in Pathum Thani, Thailand.'
    },
    'DIF.BK': {
        'name': 'Digital Telecommunications Infrastructure Fund',
        'address': '7-8th Floor. SCB Park Plaza 1 18 Ratchadapisek Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 949 1500',
        'website': 'N/A',
        'sector': 'Technology',
        'industry': 'Information Technology Services',
        'description': 'Digital Telecommunications Infrastructure Fund specializes in infrastructure investments in the digital telecommunications sector. We own or are entitled to the net revenues generated from a portfolio of 16,059 telecommunications towers comprising 9,727 towers owned by the Fund (comprising True Tower Assets and TUC Towers for Additional Investment No. 2, No.3 and No. 4) and 6,332 towers from which the Fund is entitled to the net revenue (comprising the BFKT Towers, AWC Towers, AWC Towers for Additional Investment No. 1 and No. 2), including the ownership in the certain BFKT Telecom Assets after the expiry of the HSPA Agreements and certain AWC Towers after the expiry of the AWC Leasing Agreement, Additional AWC Leasing Agreement No. 1 and Additional AWC Leasing Agreement No. 2. and FOC and Upcountry Broadband System'
    },
    'DMT.BK': {
        'name': 'Don Muang Tollway Public Company Limited',
        'address': '40/40, Viphavadi-Rangsit Road Sanambin Don Muang Bangkok 10210 Thailand',
        'phone': '66 2 792 6500',
        'website': 'https://www.tollway.co.th',
        'sector': 'Industrials',
        'industry': 'Infrastructure Operations',
        'description': 'Don Muang Tollway Public Company Limited provides elevated toll road service in Thailand. The company operates a toll road from Din Daeng to National Memorial Monument with total length of 21.9 kilometers. It offers a range of services to the tollway users comprising toll collection, traffic management, rescue, and maintenance services. Don Muang Tollway Public Company Limited was incorporated in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'DOHOME.BK': {
        'name': 'Dohome Public Company Limited',
        'address': '60 Soi Ruam Mit, Din Daeng Road, Sam Sen Nai Sub-district, Phaya Thai District Bangkok 10400',
        'phone': '66 2 027 8787',
        'website': 'https://www.dohome.co.th',
        'sector': 'Consumer Cyclical',
        'industry': 'Home Improvement Retail',
        'description': 'Dohome Public Company Limited, together with its subsidiaries, engages in the retailing and wholesaling of construction materials, office equipment, and household products in Thailand. The company offers construction materials products, such as steel sections, skirting boards, cement and other infrastructure products, etc.; repair materials products, including tools agriculture, gardening and plumbing equipment, electric equipment, sanitary equipment, etc.; and decoration materials products comprising electrical appliances, home furniture appliances, home decorations, bedding, gift shops, etc. It is also involved in the production and distribution of electricity; and property investment activities. The company was founded in 1983 and is based in Ubon Ratchathani, Thailand.'
    },

    # 161-180
    'DREIT.BK': {
        'name': 'Dusit Thani Freehold and Leasehold Real Estate Investment Trust',
        'address': 'No. 319 Chamchuri Square Building 29th Floor Phayathai Road Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 200 9999',
        'website': 'https://www.dtcreit.com',
        'sector': 'Real Estate',
        'industry': 'REIT—Hotel & Motel',
        'description': 'Dusit Thani Freehold and Leasehold Real Estate Investment Trust is a real estate investment trust. The firm focuses on investing in high potential freehold or leasehold properties especially in hotel properties, as well as investing in other assets that favor hotel-related business, such as meeting and convention room, restaurants, fitness center, spa, swimming pool, tennis court etc. The firm is based in Bangkok, Thailand.'
    },
    'DRT.BK': {
        'name': 'Diamond Building Products Public Company Limited',
        'address': '69-70 Moo 1 Mitraphab Km. 115 Thambon Talingchan Tambon Talingchan Amphur Muang Sara Buri 18000 Thailand',
        'phone': '66 3 622 4171',
        'website': 'https://www.dbp.co.th',
        'sector': 'Industrials',
        'industry': 'Building Products & Equipment',
        'description': 'Diamond Building Products Public Company Limited, together with its subsidiaries, manufactures and distributes roof tiles, artificial woods, and autoclaved aerated concrete products in Thailand and internationally. The company offers roofing products, wall sidings and ceilings, and artificial boards, as well as equipment for installation of roofs and house structural members. It also provides other roof accessories and non-roof products; and services for design and installation of roofs under the Diamond Roof, Adamas, and Jearanai names. The company was formerly known as Diamond Roofing Tiles Public Company Limited and changed its name to Diamond Building Products Public Company Limited in January 2011. The company was founded in 1985 and is headquartered in Saraburi, Thailand. Diamond Building Products Public Company Limited is a subsidiary of Myriad Materials Co., Ltd'
    },
    'DTCENT.BK': {
        'name': 'D.T.C. Enterprise Public Company Limited',
        'address': '63 Soi Sukhumvit 68 Sukhumvit Road Bangna Nuea Subdistrict Bangna District Bangkok 10260 Thailand',
        'phone': '1176',
        'website': 'https://www.dtc.co.th',
        'sector': 'Technology',
        'industry': 'Scientific & Technical Instruments',
        'description': 'D.T.C. Enterprise Public Company Limited produces and deals in satellite land vehicle tracking devices and black box sets, and IoT solutions in Thailand and internationally. The company provides real-time GPS tracking, blue box real time GPS tracking, container tracking, motorcycle tracking, and device options for GPS tracking systems; mobile DVR smart eye model, driving, mobile CCTV online model MDVR, and in vehicle monitoring systems; and software solutions, including transport management, business activity management, online map system, DTC fleet maintenance, and smart farm solutions. It also offers excise departments gauge systems, information technology systems for internal office system development, information and DVR camera systems for fire engines and rescue departments, administrative agency resources management systems, smart vending machine IoT solutions, and fire detection systems; and monitoring, controlling, and tracking systems for oil handling along border zone, as well as to draw up database of liquor sale located close by or around schools. In addition, the company exports its products to China, Philippines, Indonesia, India, Laos, Bangladesh, Vietnam, Kenya, Malaysia, Hong Kong, Myanmar, Cambodia, and other countries. The company was founded in 1996 and is based in Bangkok, Thailand.'
    },
    'DTCI.BK': {
        'name': 'D.T.C. Industries Public Company Limite',
        'address': '176, D.T.C. Building Sukhumvit 64 Sukhumvit Road Bangchak, Prakhanong Bangkok Thailand',
        'phone': '66 2 311 1371',
        'website': 'N/A',
        'sector': 'Industrials',
        'industry': 'Business Equipment & Supplies',
        'description': 'D.T.C. Industries Public Company Limited produces and distributes pens and related products in Thailand and internationally. It also provides space rental. The company was incorporated in 1971 and is headquartered in Bangkok, Thailand.'
    },
    'DUSIT.BK': {
        'name': 'Dusit Thani Public Company Limited',
        'address': '319 Chamchuri Square Building 29th Floor Phyathai Road Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 200 9999',
        'website': 'https://dusit-international.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'Dusit Thani Public Company Limited, together with its subsidiaries, owns and operates hotels and resorts in Thailand and internationally. The company operates through five segments: Hotel and Hotel Management, Education, Foods, Property development, and Others. It operates hotels under the Dusit Thani, Dusit Devarana, dusitD2, Dusit Princess, ASAI Hotels, and Elite Havens brands; spas under the Devarana Spa and Namm Spa brands; and healthy food restaurants. The company also provides hotel management and consultancy services; and engages in the food and beverage catering, and distribution business. In addition, it operates Dusit Thani College; Dusit Thani Excellence Centre; Le Cordon Bleu Dusit Culinary School; and The Food School. Further, the company operates as a REIT manager for real estate investment trust; and distributor of bakery and franchise business. Additionally, it is involved in the property leasing and sub-leasing; and property development businesses, as well as operates culinary schools and hospitality colleges in Thailand. Dusit Thani Public Company Limited was founded in 1948 and is headquartered in Bangkok, Thailand.'
    },
    'EA.BK': {
        'name': 'Energy Absolute Public Company Limited',
        'address': 'AIA Capital Center Building 16th Floor No. 89, Ratchadaphisek Road Dindaeng Bangkok 10400 Thailand',
        'phone': '66 2 248 2488',
        'website': 'https://www.energyabsolute.co.th',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'Energy Absolute Public Company Limited, together with its subsidiaries, engages in the manufacturing and distribution of crude palm oil, biodiesel products, and glycerol in Thailand. The company provides phase change materials, as well as electric buses, car, ferry, and boats; and development, manufacture, and distribution of lithium-ion polymer batteries. It also generates electricity through solar, wind, and biogas power plants; provides construction projects consulting, hire purchase of electric vehicles, shore tank rental, and crude palm oil pipeline transport services; and operates charging stations. The company was formerly known as Suntech Palm Oil Ltd. and changed its name to Energy Absolute Public Company Limited in 2008. Energy Absolute Public Company Limited was incorporated in 2006 and is headquartered in Bangkok, Thailand.'
    },
    'EASON.BK': {
        'name': 'Eason & Co Public Company Limited',
        'address': '7/1-2 Moo 1 Tombol Panthong Amphur Panthong Phan Thong 20160 Thailand',
        'phone': '66 3 845 1833',
        'website': 'http://www.easonplc.com',
        'sector': 'Basic Materials',
        'industry': 'Specialty Chemicals',
        'description': 'Eason & Co Public Company Limited manufactures and sells industrial and automotive paints primarily in Thailand. It offers packaging coatings for interior and exterior application to crown caps, ROPP, screw caps, lug caps, and other closures. The company also provides offset inks comprising metal decorating inks for 2-piece cans; and conventional and UV metal decorating inks for 3-piece cans. In addition, it offers motorcycle coatings, including poly urethane, acrylic, and air dry paints, as well as trades in industrial paints. The company was formerly known as Eason Paint Public Company Limited and changed its name to Eason & Co Public Company Limited in May 2020. Eason & Co Public Company Limited was incorporated in 1965 and is headquartered in Phan Thong, Thailand.'
    },
    'EASTW.BK': {
        'name': 'Eastern Water Resources Development and Management Public Company Limited',
        'address': 'East Water Building 23rd-26th Floors 1 Vipavadeerangsit 5 Vipavadeerangsit Rd,Jomphol, Jatujak Bangkok 10900 Thailand',
        'phone': '66 2 272 1600',
        'website': 'https://www.eastwater.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Regulated Water',
        'description': 'Eastern Water Resources Development and Management Public Company Limited, together with its subsidiaries, engages in the development and management of water distribution pipeline systems in the eastern seaboard area of Thailand. It produces and supplies tap water; provides waste treatment, waterworks management, engineering services, operation and maintenance management, and renewable energy management services; recycles water; and supplies raw water. The company was founded in 1992 and is headquartered in Bangkok, Thailand.'
    },
    'ECL.BK': {
        'name': 'Eastern Commercial Leasing Public Company Limited',
        'address': '976/1 Soi Rama IX Hospital Rim Klong Samsen Road Bangkapi Sub-District Huay Kwang District Bangkok 10310 Thailand',
        'phone': '66 2 641 5252',
        'website': 'https://www.ecl.co.th',
        'sector': 'Financial Services',
        'industry': 'Credit Services',
        'description': 'Eastern Commercial Leasing Public Company Limited engages in the provision of credit services to personal and juristic person in the form of hire purchase, loans, and sale with right of redemption agreement in Thailand. It also provides vehicle registration, vehicle insurance, vehicle third party liability insurance, and life insurance renewal services. The company was founded in 1982 and is headquartered in Bangkok, Thailand.'
    },
    'EE.BK': {
        'name': 'Eternal Energy Public Company Limited',
        'address': '888 I Tower Building 8th Floor Vibhavadi Rangsit Road Chatuchak Bangkok 10900 Thailand',
        'phone': '66 2 554 8000',
        'website': 'http://www.eternalenergy.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Farm Products',
        'description': 'Eternal Energy Public Company Limited, together with its subsidiaries, engages in the cassava plantation activities in Thailand. The company is involved in the plantation of tapioca and other energy crops. It also rents real estate properties. The company was formerly known as Sea Horse Public Company Limited and changed its name to Eternal Energy Public Company Limited in October 2009. Eternal Energy Public Company Limited was incorporated in 1987 is headquartered in Bangkok, Thailand.'
    },
    'EGATIF.BK': {
        'name': 'Electricity Generating Authority Of Thailand- North Bangkok Power Plant Block 1 Infrastructure Fund',
        'address': 'No. 1, Empire Tower, 32nd Floor, South Sathorn Road, Yannawa Subdistrict, Sathorn District Bangkok 10120',
        'phone': '66 2 686 6100',
        'website': 'N/A',
        'sector': 'Utilities',
        'industry': 'Utilities—Independent Power Producers',
        'description': 'EGATIF invest in the future Availability Revenue obtainable from North Bangkok Power Plant Block 1, a Contracted Capacity of 670 MW , for the period of 20 years'
    },
    'EGCO.BK': {
        'name': 'Electricity Generating Public Company Limited',
        'address': 'EGCO Tower 14th and 15th floor 222, Vibhavadi Rangsit Road Tungsonghong, Laksi Bangkok 10210 Thailand',
        'phone': '66 2 998 5000',
        'website': 'https://www.egco.com/th/',
        'sector': 'Utilities',
        'industry': 'Utilities—Independent Power Producers',
        'description': 'Electricity Generating Public Company Limited, together with its subsidiaries, generates and sells electricity to government sector and industrial users primarily in Thailand, the Philippines, Australia, South Korea, Taiwan, the United States, Laos, and Indonesia. The company operates in two segments, Electricity Generation and Other Businesses. It generates electricity from various resources, such as natural gas, liquefied natural gas, coal, biomass, hydro, solar, wind, geothermal, and fuel cell. As of December 31, 2022, the company operated 31 domestic and overseas power plants with total capacity of 6,202 MW equity; operating power plants with a total capacity of 5,972 MW equity and projects under construction with total equity contracted capacity of 230 MW. It also provides operation, maintenance, engineering, and construction services to power plants, petrochemical plants, oil refineries, and other industries. The company was incorporated in 1992 and is headquartered in Bangkok, Thailand.'
    },
    'EKH.BK': {
        'name': 'Ekachai Medical Care Public Company Limited',
        'address': '99/9 Moo 4, Ekachai Road Tambol Khokkham Amphur Muang 74000 Thailand',
        'phone': '66 3 441 7999',
        'website': 'https://www.ekachaihospital.com',
        'sector': 'Healthcare',
        'industry': 'Medical Care Facilities',
        'description': 'Ekachai Medical Care Public Company Limited, together with its subsidiaries, operates Ekachai hospital in Thailand. It offers plastic surgery, fertility and genetic, pediatric, obstetrics and gynecology, general medicine clinic, general surgery, orthopedics, ophthalmology, emergency, health promotion, hemodialysis, dental, physical, mobile checkup, pre-employment checkup, aesthetic and dermatology center, and child and teen development center services, as well as mobile checkup and physical therapy services. Ekachai Medical Care Public Company Limited was incorporated in 2003 and is headquartered in Muang, Thailand.'
    },
    'EMC.B': {
        'name': 'EMC Public Company Limited',
        'address': '140/66-67, ITF Tower 28th-30th Floor Silom Road Suriyawong, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 615 6100',
        'website': 'http://www.emc.co.th',
        'sector': 'Industrials',
        'industry': 'Engineering & Construction',
        'description': 'EMC Public Company Limited, together with its subsidiaries, engages in the construction contracting and real estate development businesses in Hong Kong. It offers construction for skyscrapers and industrial construction; and barrage construction, waterway construction, soil destruction prevention, roadway construction, etc. The company also provides electrical and mechanical engineering services, such as installation of electrical systems, plumbing systems, and ventilation systems for hotels, hospitals, condominiums, offices, shopping malls, and industrial factories. In addition, it develops various projects, including house, twin house, town house, commercial buildings, condominium, etc. The company was formerly known as EMC Engineering Limited Partnership. EMC Public Company Limited was incorporated in 1979 and is headquartered in Bangkok, Thailand.'
    },
    'EP.BK': {
        'name': 'Eastern Power Group Public Company Limited',
        'address': '51/29, 51/61Soi. Soi Viphavadee Rangsit 66 (Siamsamakee) Vibhavadi Rangsit Road Talad Bang Khen Subdistrict, Lak Si Dist Bangkok 10210 Thailand',
        'phone': '66 2 551 0541',
        'website': 'https://epgroup.co.th',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'Eastern Power Group Public Company Limited engages in the solar power generation business. It also involved in the maintenance and installation service contract in solar power project. The company was formerly known as Eastern Printing Public Company Limited and changed its name to Eastern Power Group Public Company Limited in April 2020. Eastern Power Group Public Company Limited was incorporated in 1993 and is headquartered in Bangkok, Thailand.'
    },
    'EPG.BK': {
        'name': 'Eastern Polymer Group Public Company Limited',
        'address': '770 Moo 6, Theparak Road Theparak Muang Samutprakarn Mueang Samut Prakan 10270 Thailand',
        'phone': '66 2 383 6599',
        'website': 'https://www.epg.co.th',
        'sector': 'Basic Materials',
        'industry': 'Specialty Chemicals',
        'description': 'Eastern Polymer Group Public Company Limited, through its subsidiaries, engages in the manufacture and distribution of rubber insulation, automotive, plastic packing, and research and development business in Thailand and internationally. It also manufactures bed liners and covers of pickup trucks, as well as automotive accessories products. In addition, the company is involved in the import and export of machinery and chemicals; manufacture of rubber for cars, machinery, buildings, and other products; assembly and distribution of molded plastic parts; and injection and molding of plastic parts. Further, it designs, manufactures, and trades in accessories for 2, 4WD, light commercial, and heavy transportation vehicles, as well as provides calibration services. The company was formerly known as Eastern Polymer Industry Company Limited. The company was incorporated in 1978 and is headquartered in Mueang Samut Prakan, Thailand. Eastern Polymer Group Public Company Limited is a subsidiary of Vitoorapakorn Holding Co., Ltd.'
    },
    'ERW.BK': {
        'name': 'The Erawan Group Public Company Limited',
        'address': 'Ploenchit Center 6th Floor 2 Sukhumvit Road Kwang Klongtoey, Khet Klongtoey Bangkok 10110 Thailand',
        'phone': '66 2 257 4588',
        'website': 'https://www.theerawan.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Lodging',
        'description': 'The Erawan Group Public Company Limited, through its subsidiaries, engages in hotel, and building rental and management businesses in Thailand. The company operates hotels and resorts under the Grand Hyatt Erawan Bangkok, JW Marriott Bangkok, The Naka Island, Renaissance Koh Samui Resort and Spa, Courtyard by Marriott Bangkok, Holiday Inn Pattaya, Mercure Bangkok Siam, ibis Hotel, Novotel Bangkok Sukhumvit 4, Mercure Bangkok Sukhumvit 24, ibis Styles Bangkok Sukhumvit 4, ibis Bangkok Siam, ibis Styles Krabi Ao Nang, ibis Pattaya, ibis Phuket Patong, ibis Phuket Kata, ibis Samui Bophut, ibis Hua Hin, and HOP INN names. It also owns and operates retail property under the name Erawan Bangkok, and manages Ploenchit Center a luxury retail property adjacent to Grand Hyatt Erawan Hotel, and manages Ploenchit Center. The company is also involved in the development of properties; retail space rental; and provision of office buildings management services. The Erawan Group Public Company Limited was incorporated in 1982 and is headquartered in Bangkok, Thailand.'
    },
    'ERWPF.BK': {
        'name': 'Erawan Hotel Growth Property Fund',
        'address': 'The 9th Towers Grand Rama 9 Floor 18 33/4 Rama 9 Road Huaykwang Bangkok 10310 Thailand',
        'phone': '66 2 949 1500',
        'website': 'https://www.scbam.com/en/fund/property-fund/fund-information/erwpf',
        'sector': 'Real Estate',
        'industry': 'REIT—Hotel & Motel',
        'description': 'The Fund has invested in Freehold right of the ibis Patong Hotel and the ibis Pattaya Hotel. The properties consist of land with construction, buildings, public utility system in relation to the hotel business and furniture, fixtures and fittings and equipment.'
    },
    'ESSO.BK': {
        'name': 'Esso (Thailand) Public Company Limited',
        'address': '3195/17-29 Rama IV Road Klong Ton Klong Toey District Bangkok 10110 Thailand',
        'phone': '66 2 407 4000',
        'website': 'https://www.esso.co.th',
        'sector': 'Energy',
        'industry': 'Oil & Gas Refining & Marketing',
        'description': 'Esso (Thailand) Public Company Limited refines and markets petroleum products in Thailand and internationally. It operates through two segments, Downstream and Petrochemicals. The company provides liquefied petroleum gas, gasoline, naphtha, jet fuel/kerosene, diesel, fuel oil, and asphalt; and other petroleum products comprising mineral and synthetic lubricants under the Mobil brand. It sells refined petroleum products through retail service stations under the Esso brand; and commercial channels that consist of sales to industrial end users, wholesalers, and customers in the aviation and marine industries. The company also offers hydrocarbon solvents, such as hexane used in edible oil seed extractions and as a carrier in petrochemical production; rubber solvents that are used as adhesives and rubber cement for manufacturing of tires; white spirits for coating and paint industries; and Exxsol D80 for household, industrial, and metal working applications. In addition, it imports and markets aromatic solvents that are used in the automotive paint coating industry; sells plasticizers; and leases real estate properties. The company was formerly known as Esso Standard Thailand Co., Ltd. and changed its name to Esso (Thailand) Public Company Limited in 1996. The company was founded in 1894 and is based in Bangkok, Thailand. Esso (Thailand) Public Company Limited is a subsidiary of ExxonMobil Asia Holding Private Limited.'
    },
    'ESTAR.BK': {
        'name': 'Eastern Star Real Estate Public Company Limited',
        'address': '898 Ploenchit Tower 5th Floor Ploenchit Road Lumpini Sub-dist, Pathumwan Bangkok 10330 Thailand',
        'phone': '66 91 949 0000',
        'website': 'https://www.estarpcl.com',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Eastern Star Real Estate Public Company Limited, together with its subsidiaries, engages in the property development business in Thailand. The company operates in three segments: Real Estate Business, Golf Course Business, and Rental Business. It develops and sells land, houses, and residential condominium units; and rents properties. The company also operates golf courses, as well as offers sport memberships. Eastern Star Real Estate Public Company Limited was founded in 1989 and is headquartered in Bangkok, Thailand.'
    },

    # 181-200
    'ETC.BK': {
        'name': 'Earth Tech Environment Public Company Limited',
        'address': 'No. 88,88/1 Moo 1 Ban That Subdistrict Kaeng Khoi District Kaeng Khoi 18110 Thailand',
        'phone': '66 3 620 9294',
        'website': 'https://www.etcenvi.com',
        'sector': 'Utilities',
        'industry': 'Utilities—Renewable',
        'description': 'Earth Tech Environment Public Company Limited generates and distributes electricity using processed municipal and industrial waste in Thailand. The company operates power plants with an installed capacity of 9.4 MW located in Kaeng Khoi industrial estate, Kaeng Khoi district; 7.0 MW installed capacity in NakornLuang industrial estate, Nakhon Luang district; and 5.5 MW located in Phra Nakhon Si Ayutthaya. It is also involved in the procurement of machinery and equipment, and integrated plant construction, operation, and maintenance, as well as provision of engineering design services. The company was incorporated in 2004 and is headquartered in Kaeng Khoi, Thailand.'
    },
    'EVER.BK': {
        'name': 'Everland Public Company Limited',
        'address': '223/96 Country Complex Tower Building A 21st Floor Sanphawut Road Kwang Bangna, Khet Bangna Bangkok 10260 Thailand',
        'phone': '66 2 361 6156',
        'website': 'https://www.everland.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Everland Public Company Limited, together with its subsidiaries, engages in the property development business in Thailand. It operates in two segments, Property Development, and Hospital and Dental Clinic. The company develops various projects, such as townhomes, single houses, and condominiums, as well as commercial buildings. It is also involved in the operation of private hospitals and dental clinics; and provision of land and hospital buildings for rent. The company was founded in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'F&D.BK': {
        'name': 'Food and Drinks Public Company Limited',
        'address': '15th Floor, Regent House Bldg., 183 Rajdamri Rd., Lumpini, Patumwan Bangkok 10330',
        'phone': '66 2 253 5232',
        'website': 'http://www.foodanddrinks.co.th',
        'sector': 'Consumer Defensive',
        'industry': 'Packaged Foods',
        'description': 'Food and Drinks Public Company Limited manufactures and sells foods products, beverages, and frozen foods in Thailand. It offers curry paste, curry sauce, spices, and cooking sauces; aloe vera, bamboo shoot, mango, and mixed fruits, and vegetables, as well as spices, such as lemon grass, chilli, and coriander; and brine, vinegar, syrup, or water for fruits and vegetables. The company also provides fruit and vegetable juices, and ready-to-drink tea; and ready to eat products comprising rice with chicken basil stir fried, minced chicken hot yellow curry paste, steamed glutinous rice in banana leaf, and papaya salad. It also exports its products. Food and Drinks Public Company Limited was founded in 1985 and is headquartered in Chonburi, Thailand.'
    },
    'FANCY.BK': {
        'name': 'Fancy Wood Industries Public Company Limited',
        'address': '357 Moo 12, Soi Suksawat 84 (Kusang) Suksawad Road Naikhlongbangplakot Sub-district Prasamutjaedee District Samut Prakan 10290 Thailand',
        'phone': '66 2 578 2823',
        'website': 'http://www.fancywood.th.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Furnishings, Fixtures & Appliances',
        'description': 'Fancy Wood Industries Public Company Limited, together with its subsidiaries, manufactures and sells rubber wood products in Thailand and internationally. The company offers particle board, modified rubber wood, and services related to rubber wood. It is also involved in the real estate development activities, as well as rental of property. The company was founded in 1970 and is headquartered in Samut Prakan, Thailand.'
    },
    'FE.BK': {
        'name': 'Far East Fame Line DDB Public Company Limited',
        'address': '465/1-467 Si Ayutthaya Rd Thungphayathai Ratchathewi District Bangkok 10400 Thailand',
        'phone': '66 2 354 3333',
        'website': 'https://www.fareastfamelineddb.com',
        'sector': 'Communication Services',
        'industry': 'Advertising Agencies',
        'description': 'Far East Fame Line DDB Public Company Limited, together with its subsidiaries, engages in the advertising agency business in Thailand. The company offers digital marketing, creative communication, campaign management, graphic design, production, media and performance, branding, data analysis and transformation, CX solutions, and social media management services. The company was formerly known as Far East DDB Public Company Limited and changed its name to Far East Fame Line DDB Public Company Limited in January 2018. Far East Fame Line DDB Public Company Limited was incorporated in 1964 and is headquartered in Bangkok, Thailand.'
    },
    'FMT.BK': {
        'name': 'Fine Metal Technologies Public Company Limited',
        'address': '183 Regent House Building 14th Floor Rajdamri Road Lumpini, Pathumwan Bangkok 10330 Thailand',
        'phone': '66 2 256 0641',
        'website': 'https://www.fmt.co.th',
        'sector': 'Industrials',
        'industry': 'Metal Fabrication',
        'description': 'Fine Metal Technologies Public Company Limited engages in the manufacturing and distributing of seamless copper tubes in Thailand, Malaysia, Singapore, Japan, and internationally. The company offers smooth tubes for heat exchanger and piping; multi-grooved tubes to produce the air conditioners; accumulator tubes for use as the pressure reservoir tank or refrigerant; and capillary tubes. The company was formerly known as Furukawa Metal (Thailand) Public Company Limited and changed its name to Fine Metal Technologies Public Company Limited in November 2020. The company was incorporated in 1988 and is headquartered in Bangkok, Thailand.'
    },
    'FN.BK': {
        'name': 'FN Factory Outlet Public Company Limited',
        'address': '991 FN Building Rama 9 Road Suan Luang Sub-District Suan Luang District Bangkok 10250 Thailand',
        'phone': '66 2 300 4951',
        'website': 'https://www.fnoutlet.com',
        'sector': 'Consumer Cyclical',
        'industry': 'Apparel Retail',
        'description': 'FN Factory Outlet Public Company Limited merchandises clothing and consumer products in Thailand. The company retails apparel and non-apparel goods through factory outlets. Its stores also offer clothes, beddings, leather, furniture, cosmetics, and household products; and accessories, such as shoes, bags, belt, and jewelries, as well as snacks. The company offers its products under the Inco Men, Monsieur Inco, Inco Women, Madame Inco, Cheval, Cheval Black Collection, Lady De Cheval, Cheval Kid, Sleepmate, Rollica, Prim, Cushy, and Cherish brands. FN Factory Outlet Public Company Limited was founded in 2000 and is headquartered in Bangkok, Thailand.'
    },
    'FNS.BK': {
        'name': 'FNS Holdings Public Company Limited',
        'address': '345 Surawong Building 6th Floor 345 Surawong Road Suriyawong, Bangrak Bangkok 10500 Thailand',
        'phone': '66 2 697 3700',
        'website': 'https://www.fnsplc.com',
        'sector': 'Financial Services',
        'industry': 'Asset Management',
        'description': 'FNS Holdings Public Company Limited, together with its subsidiaries, provides various financial services in Thailand. It operates through three segments: Investment, Advisory and Management Business; Securities Business; and Warehouse and Factory Leasing Business. The company invests in and provides finance and management advisory services; and offers warehouse and factory leasing services. It also provides investment banking; underwriting; mutual fund selling agency; bond trading; and investment advisory services, as well as private equity investment services. The company was formerly known as Finansa Public Company Limited. FNS Holdings Public Company Limited was incorporated in 1989 and is based in Bangkok, Thailand.'
    },
    'FORTH.BK': {
        'name': 'Forth Corporation Public Company Limited',
        'address': '1053/1, Phaholyothin Road Phayathai Bangkok 10400 Thailand',
        'phone': '66 2 265 6700',
        'website': 'https://www.forth.co.th',
        'sector': 'Technology',
        'industry': 'Electronic Components',
        'description': 'Forth Corporation Public Company Limited, together with its subsidiaries, manufactures and distributes electronic equipment in Thailand. It operates through three segments: Electronics Manufacturing Service Business; Enterprise Solutions Business; and Smart Service Business. It offers Forth Taglock EM, a tracking device made for prisoners; nurse call systems; GPS devices and GPS tracking systems; lighting system solutions; smart traffic light systems; smart grids; multi-service access network telephone exchange equipment; EV charging stations; smart meter systems, including digital meters that show energy/water consumptions digitally, as well as smart software, which pulls data from meters automatically; and small gas station and oil vending machines. The company also provides top-up and payment kiosks; Boonterm Counter Service that has a touch screen with a data acquisition system that helps monitor usage and print receipts backwards; Boonterm water dispensers; automated cup beverage vending machines; smart vending machines; and KODIAK, a high performance aircraft, as well as operates commercial aircraft maintenance center. In addition, it engages in the trading of electronic parts; sale and installation of light boards and traffic systems; provision of consulting service for information management and computer software management, as well as engineering services; sale of aircraft, aircraft hangar and maintenance business, and flight training; electronic commerce business; and turnkey on installation of CCTV. Additionally, the company offers nano finance and personal loan services; and distributes goods. Forth Corporation Public Company Limited was founded in 1989 and is headquartered in Bangkok, Thailand.'
    },
    'FPT.BK': {
        'name': 'Frasers Property (Thailand) Public Company Limited',
        'address': 'No. 944 Mitrtown Office Tower 20th Floor Rama 4 Road, Wangmai Subdistrict Pathumwan District Bangkok 10330 Thailand',
        'phone': '66 2 483 0000',
        'website': 'https://www.frasersproperty.co.th',
        'sector': 'Real Estate',
        'industry': 'Real Estate—Development',
        'description': 'Frasers Property (Thailand) Public Company Limited, together with its subsidiaries, primarily develops industrial real estate properties in Thailand. The company develops and sells range of residential properties, which include single-detached and semi-detached houses, and townhomes. It also provides development of industrial properties including factory and warehouses, such as ready-build factory and warehouse, built-to-suit factory and warehouse, investment and property management, trust management, and other services comprising modification of factory/warehouse building, procurement of utilities and authority permits and other related services. In addition, the company engages commercial property business, which include serviced apartments, hotels, and office buildings. The company was formerly known as TICON Industrial Connection Public Company Limited and changed its name to Frasers Property (Thailand) Public Company Limited in January 2019. Frasers Property (Thailand) Public Company Limited was founded in 1990 and is based in Bangkok, Thailand.'
    },
    'FSS.BK': {
        'name': 'Finansia Syrus Securities Public Company Limited',
        'address': 'No. 999/9, The Offices at Centralworld 18th and 25th Floors Rama I Road Pathumwan Sub-district, Pathumwan Dist. Bangkok 10330 Thailand',
        'phone': '66 2 658 9000',
        'website': 'https://www.fnsyrus.com',
        'sector': 'Financial Services',
        'industry': 'Capital Markets',
        'description': 'Finansia Syrus Securities Public Company Limited, together with its subsidiaries, engages in the securities and derivatives brokerage business in Thailand. The company operates in three segments: Securities and Derivatives Brokerage, Investment Banking, and Proprietary Trading. It offers securities brokerage and trading, investment and financial advisory, securities underwriting, derivative brokerage, securities borrowing and lending, and mutual fund and private fund management services. As of December 31, 2021, the company had 24 branches. The company was formerly known as Syrus Securities Public Company Limited and changed its name to Finansia Syrus Securities Public Company Limited in June 2009. Finansia Syrus Securities Public Company Limited was founded in 2002 and is headquartered in Bangkok, Thailand.'
    },
    'FTE.BK': {
        'name': 'Firetrade Engineering Public Company Limited',
        'address': 'No. 1198/5 Rama 9 Road Phatthanakan Sub-district Suan Luang District Bangkok 10250 Thailand',
        'phone': '66 2 026 0470',
        'website': 'https://firetrade.co.th',
        'sector': 'Industrials',
        'industry': 'Security & Protection Services',
        'description': 'Firetrade Engineering Public Company Limited designs, sells, installs, repairs, and maintains fire protection equipment and systems in Thailand. The company operates in two segments, Sales of Fire Protection Equipment and Systems, and Project Works and Services. Its products include fire protection valves, grooved couplings and fittings, fire hose cabinets and internal accessories, portable fire extinguishers, switches, fire pumps, and pressure gauges; fire suppression systems; fire extinguishing systems; clean agent extinguishing systems; gaseous systems; fire smoke detection equipment; heat detectors; fire alarm equipment; fire alarm control panels; uninterruptible power supplies; and equipment for data center. Firetrade Engineering Public Company Limited was founded in 1999 and is headquartered in Bangkok, Thailand.'
    },
    'FTI.BK': {
        'name': 'Function International Public Company Limited',
        'address': '313 Charoen Phatthana Rd Bang Chan Khlong Sam Wa 10510 Thailand',
        'phone': '66 2 540 6263',
        'website': 'https://www.functioninter.co.th',
        'sector': 'Industrials',
        'industry': 'Pollution & Treatment Controls',
        'description': 'Function International Public Company Limited engages in manufacturing, importing, and wholesaling water purifiers and water systems in Thailand and internationally. It offers household water purifiers, water purifier RO systems, and water filters; commercial water purifiers, water dispensers, water vending machines, and water makers; industrial RO systems and tanks; and pumps and valves. The company sells its products under the Aquatek, Star Pure, Hydro Max, Treatton, Unipure, Fast Pure, BIO MAX, Dosag Pump, Ultratek, CNP, HP Watermaker, PENTAIR, RUN-XIN, SUEZ, and VONTRON brands. Function International Public Company Limited was founded in 1997 and is based in Khlong Sam Wa, Thailand.'
    },
    'FTREIT.BK': {
        'name': 'Frasers Property Thailand Industrial Freehold & Leasehold REIT',
        'address': 'No.944 Mitrtown Office Tower, 22nd - 23rd Floor, Rama 4 Road, Wang Mai Sub-district, Pathum Wan District Bangkok 10330',
        'phone': '66 2 483 0000',
        'website': 'http://www.ftreit.co.th',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'Investing in the freehold and leasehold right of warehouses and factories.'
    },
    'FUTUREPF.BK': {
        'name': 'Future Park Leasehold Property Fund',
        'address': '175 Sathorn City Tower 21st South Sathorn Road Thung Maha Mek, Sathorn Bangkok 10120 Thailand',
        'phone': '662 674 6488',
        'website': 'https://investor.futurepark.co.th/en',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'The Fund has invested in the leasehold right for some portions of the Future Park Rangsit complex. It encompasses all the commercial space and the open area within the shopping complex as well as the wall surfaces outside the building.'
    },
    'GAHREIT.BK': {
        'name': 'Grande Hospitality Real Estate Investment Trust',
        'address': 'Siam Piwat Tower Building 9th and 24th Floors 989 Rama 1 Road Patumwan Bangkok Thailand',
        'phone': '66 2 659 8888',
        'website': 'N/A',
        'sector': 'Real Estate',
        'industry': 'REIT—Industrial',
        'description': 'GAHREIT invests in the freehold right of land, building and construction as well as system, fixtures and facilities and movable properties of Sheraton Huahin Resort & Spa Project.'
    },
    'GBX.BK': {
        'name': 'Globlex Holding Management Public Company Limited',
        'address': '87/2 CRC All Seasons Place 12th Floor Wireless Road, Lumpini Patumwan Bangkok 10330 Thailand',
        'phone': '66 2 672 5995',
        'website': 'https://www.globlexholding.co.th',
        'sector': 'Financial Services',
        'industry': 'Capital Markets',
        'description': 'Globlex Holding Management Public Company Limited, an investment holding company, engages in securities, investment, and financial advisory businesses in Thailand. The company operates through three segments: Holding Business, Securities Business, and Other Business. The company was incorporated in 2003 and is headquartered in Bangkok, Thailand.'
    },
    'GC.BK': {
        'name': 'Global Connections Public Company Limited',
        'address': '13/1 Moo 2 King-Kaew Road Rachateva Bang Phli 10540 Thailand',
        'phone': '66 2 763 7999',
        'website': 'https://www.gc.co.th',
        'sector': 'Basic Materials',
        'industry': 'Specialty Chemicals',
        'description': 'Global Connections Public Company Limited operates as distributing agent of plastic and plastic-related products in Thailand. It offers commodity polymers and special additive products; engineering plastic, synthetic rubber, special chemicals, biosurfactant chemicals, and petrochemicals and additives, which are used in petrochemical and plastic transformation process. The company also produces and distributes solar power installed on roof. Global Connections Public Company Limited was founded in 1994 and is headquartered in Bang Phli, Thailand.'
    },
    'GEL.BK': {
        'name': 'General Engineering Public Company Limited',
        'address': '44/2, Moo 2, Tivanon Road Bangkadi Muang Pathumthani Pathum Thani 12000 Thailand',
        'phone': '66 2 501 2020',
        'website': 'https://www.gel.co.th',
        'sector': 'Basic Materials',
        'industry': 'Building Materials',
        'description': 'General Engineering Public Company Limited manufactures and distributes construction materials in Thailand and internationally. The Company operates through three segments: Manufacturing and Distribution of Concrete Products; Construction Services; and Manufacturing and Distribution of PC Wire and PC Strand. It offers prestressed concrete pile products, such as square, I shape, and square hollow core piles; bored piles; soil cement columns; spun concrete piles; precast concrete; segments and girders; post-tensioned slabs; biaxial slabs; and glassfiber reinforced concrete for roofing, cladding, interior decoration, landscape, and other projects. The company also provides construction chemical products for grouting, concrete repair and protection, tiling work, waterproofing, rebar embedding, joint sealant, concrete surface strengthening work, and concrete admixture; and PC wires and strands. In addition, it offers construction and installation, as well as engineering services, including waterproofing system, crack repair, structural reinforcement work, reinforcement steel embedding work, and specialized repair work. General Engineering Public Company Limited was incorporated in 1962 and is headquartered in Pathum Thani, Thailand.'
    },
    'GENCO.BK': {
        'name': 'General Environmental Conservation Public Company Limited',
        'address': '447 Bondstreet Road Bangpood Parkkred Nonthaburi 11120 Thailand',
        'phone': '66 2 502 0900',
        'website': 'http://www.genco.co.th',
        'sector': 'Industrials',
        'industry': 'Waste Management',
        'description': 'General Environmental Conservation Public Company Limited, together with its subsidiaries, engages in the treatment of industrial waste and unavoidable by-products of manufacturing processes in Thailand. The company operates through Treatment of Industrial Waste Business; Property Development Business; and Other Business segments. It collects, stores, and transports hazardous and non-hazardous industrial waste. The company also develops and sells various real estate properties, including residential townhouses, commercial buildings, and condominiums primarily in the greater Bangkok Metropolitan area, as well as buys and sells land. In addition, it develops and operates solar energy power plants, as well as distributes medical equipment. The company was founded in 1994 and is headquartered in Nonthaburi, Thailand.'
    }
    # ,

    # 201-220
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
    # 'NAME': {
    #     'name': '',
    #     'address': '',
    #     'phone': '',
    #     'website': '',
    #     'sector': '',
    #     'industry': '',
    #     'description': ''
    # },
}


@app.route('/')
def insert_profiles():
    try:
        cur = mysql.connection.cursor()

        for ticker, profile in company_profiles.items():
            name = profile['name']
            address = profile.get('address', None)
            phone = profile.get('phone', None)
            website = profile.get('website', None)
            sector = profile.get('sector', None)
            industry = profile.get('industry', None)
            description = profile['description']

            # check if the record already exists
            cur.execute("SELECT * FROM company_profiles WHERE ticker=%s", (ticker,))
            record = cur.fetchone()
            if record:
                # update the existing record
                cur.execute("UPDATE company_profiles SET name=%s, address=%s, phone=%s, website=%s, sector=%s, industry=%s, description=%s WHERE ticker=%s", (name, address, phone, website, sector, industry, description, ticker))
            else:
                # insert a new record
                cur.execute("INSERT INTO company_profiles (ticker, name, address, phone, website, sector, industry, description) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ticker, name, address, phone, website, sector, industry, description))

            mysql.connection.commit()

        cur.close()
        return 'Company profiles inserted successfully!'

    except Exception as e:
        return str(e)



if __name__ == '__main__':
    app.run(debug=True)