import socket, re, sys, argparse
import concurrent.futures


parser = argparse.ArgumentParser()
parser.add_argument("target", help="Scans ports of selected target.")
parser.add_argument("-c", help="Scans only common ports.", action="store_true", dest="common_ports", default=False)
parser.add_argument("-s", help="Starting port.", type=int,dest="start_port")
parser.add_argument("-e", help="End port.", type=int, dest="end_port")



args = parser.parse_args()
print(args.target)

target = args.target
common_ports = args.common_ports
start_port = args.start_port
end_port = args.end_port
open_ports = []


if (common_ports == False):
    print("-"* 60)
    print("Scanning target: " + target)
    print("-"* 60)

    try:
        with ThreadPoolExecutor(200) as executor:
        	fs =[executor.submit(scan, target, p) for p in range(start_port, end_port)]
        	futures.wait(fs)

    except KeyboardInterrupt:
            print ("\nKeyboard Interrupt, quitting the program.")
            exit()
    except Exception as e:
            print ("\nUnknown error occured"), e
            exit()

    print("-"* 60)
    print("Scan Complete")
    print("-"* 60)
    
    sorted_ports = sorted(open_ports)
    for item in sorted_ports:
        service = service(item)
        print("\nPort {} is {}, Service : {}".format(item,sorted_ports[item]))
else:
    print("-"* 60)
    print("Scanning target: " + target)
    print("-"* 60)

    try:
        with ThreadPoolExecutor(200) as executor:
        	fs =[executor.submit(scan, target, p) for p in range(1, 33435)]
        	futures.wait(fs)

    except KeyboardInterrupt:
            print ("\nKeyboard Interrupt, quitting the program.")
            exit()
    except Exception as e:
            print ("\nUnknown error occured"), e
            exit()

    print("-"* 60)
    print("Scan Complete")
    print("-"* 60)

    sorted_ports = sorted(open_ports)
    for item in sorted_ports:
        service = service(item)
        print("\nPort {} is {}, Service : {}".format(item,sorted_ports[item]))

#target = socket.gethostbyname(input("Enter Hostname Here: "))

def Scan(target, port): 
        
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:   
        result = sock.connect_ex((target, port))

    except socket.gaierror as e:
        print("Hostname could not be resolved.\n"), e
        error.append('Hostname could not be resolved.\n')
        sys.exit()

    except socket.error as e:
        print("Couldn't connect to server\n")
        error.append("Couldn't connect to server.\n")
        sys.exit()

    except Exception as e:
        print("Unknown error occured\n"), e
        error.append('Unknown error occured\n')
        sys.exit()

    if (result == 0):
        open_ports[port] = 'open'

    elif (result == 10035):
        open_ports[port] = 'filtered'

    sock.close()

def service(port):
    services = {
        1:'TCPPortServiceMultiplexer(TCPMUX)',
        5:'RemoteJobEntry(RJE)',7:'ECHO',18:'MessageSendProtocol(MSP)',20:'FTP--Data',21:'FTP--Control',22:'SSHRemoteLoginProtocol',
        23:'Telnet',25:'SimpleMailTransferProtocol(SMTP)',29:'MSGICP',37:'Time',42:'HostNameServer(Nameserv)',43:'WhoIs',
        49:'LoginHostProtocol(Login)',53:'DomainNameSystem(DNS)',69:'TrivialFileTransferProtocol(TFTP)',70:'GopherServices',79:'Finger',
        80:'HTTP',103:'X.400Standard',108:'SNAGatewayAccessServer',109:'POP2',110:'POP3',115:'SimpleFileTransferProtocol(SFTP)',118:'SQLServices',
        119:'Newsgroup(NNTP)',137:'NetBIOSNameService',139:'NetBIOSDatagramService',143:'InterimMailAccessProtocol(IMAP)',150:'NetBIOSSessionService',
        156:'SQLServer',161:'SNMP',179:'BorderGatewayProtocol(BGP)',190:'GatewayAccessControlProtocol(GACP)',194:'InternetRelayChat(IRC)',
        197:'DirectoryLocationService(DLS)',389:'LightweightDirectoryAccessProtocol(LDAP)',396:'NovellNetwareoverIP',443:'HTTPS',
        444:'SimpleNetworkPagingProtocol(SNPP)',445:'Microsoft-DS',458:'AppleQuickTime',546:'DHCPClient',547:'DHCPServer',563:'SNEWS',569:'MSN',
        1080:'Socks', 1083:'ansoft-lm-1',1084:'ansoft-lm-2',1103:'xaudio',1109:'kpop',1110:'nfsd-status',1112:'msql',1127:'supfiledbg',1139:'cce3x',1155:'nfa',1158:'lsnr',1178:'skkserv',1212:'lupa',1214:'fasttrack',1220:'quicktime',1222:'nerv',1234:'hotline',1241:'nessus',1248:'hermes',1337:'waste',1346:'alta-ana-lm',1347:'bbn-mmc',1348:'bbn-mmx',1349:'sbook',1350:'editbench',1351:'equationbuilder',1352:'lotusnotes',1353:'relief',1354:'rightbrain',1355:'intuitive-edge',
        1356:'cuillamartin',1357:'pegboard',1358:'connlcli',1359:'ftsrv',1360:'mimer',1361:'linx',1362:'timeflies',1363:'ndm-requester',1364:'ndm-server',1365:'adapt-sna',1366:'netware-csp',1367:'dcs',1368:'screencast',1369:'gv-us',1370:'us-gv',1371:'fc-cli',1372:'fc-ser',1373:'chromagrafx',1374:'molly',1375:'bytex',1376:'ibm-pps',1377:'cichlid',1378:'elan',1379:'dbreporter',1380:'telesis-licman',1381:'apple-licman',1383:'gwha',1384:'os-licman',1385:'atex_elmd',1386:'checksum',1387:'cadsi-lm',1388:'objective-dbc',1389:'iclpv-dm',1390:'iclpv-sc',1391:'iclpv-sas',1392:'iclpv-pm',1393:'iclpv-nls',1394:'iclpv-nlc',1395:'iclpv-wsm',1396:'dvl-activemail',1397:'audio-activmail',1398:'video-activmail',1399:'cadkey-licman',1400:'cadkey-tablet',1401:'goldleaf-licman',1402:'prm-sm-np',1403:'prm-nm-np',1404:'igi-lm',1405:'ibm-res',1406:'netlabs-lm',1407:'dbsa-lm',1408:'sophia-lm',1409:'here-lm',1410:'hiq',1411:'af',1412:'innosys',1413:'innosys-acl',1414:'ibm-mqseries',1415:'dbstar',1416:'novell-lu6.2',1417:'timbuktu-srv1',1418:'timbuktu-srv2',1419:'timbuktu-srv3',1420:'timbuktu-srv4',1421:'gandalf-lm',1422:'autodesk-lm',1423:'essbase',1424:'hybrid',1425:'zion-lm',1426:'sas-1',1427:'mloadd',1428:'informatik-lm',1429:'nms',1430:'tpdu',1431:'rgtp',1432:'blueberry-lm',1433:'ms-sql-s',1434:'ms-sql-m',1435:'ibm-cics',1436:'sas-2',1437:'tabula',1438:'eicon-server',1439:'eicon-x25',1440:'eicon-slp',1441:'cadis-1',1442:'cadis-2',1443:'ies-lm',1444:'marcam-lm',1445:'proxima-lm',1446:'ora-lm',1447:'apri-lm',1448:'oc-lm',1449:'peport',1450:'dwf',1451:'infoman',1452:'gtegsc-lm',1453:'genie-lm',1454:'interhdl_elmd',1455:'esl-lm',1456:'dca',1457:'valisys-lm',1458:'nrcabq-lm',1459:'proshare1',1460:'proshare2',1461:'ibm_wrless_lan',1462:'world-lm',1463:'nucleus',1464:'msl_lmd',1465:'pipes',1466:'oceansoft-lm',1467:'csdmbase',1468:'csdm',1469:'aal-lm',
        1470:'uaiact',1471:'csdmbase',1472:'csdm',1473:'openmath',1474:'telefinder',1475:'taligent-lm',1476:'clvm-cfg',1477:'ms-sna-server',1478:'ms-sna-base',1479:'dberegister',1480:'pacerforum',1481:'airs',1482:'miteksys-lm',1483:'afs',1484:'confluent',1485:'lansource',1486:'nms_topo_serv',1487:'localinfosrvr',1488:'docstor',1489:'dmdocbroker',1490:'insitu-conf',1491:'anynetgateway',1492:'stone-design-1',1493:'netmap_lm',1494:'citrix-ica',1495:'cvc',1496:'liberty-lm',1497:'rfx-lm',1498:'watcom-sql',1499:'fhc',1500:'vlsi-lm',1501:'sas-3',1502:'shivadiscovery',1503:'imtc-mcs',1504:'evb-elm',1505:'funkproxy',1506:'utcd',1507:'symplex',1508:'diagmond',1509:'robcad-lm',1510:'mvx-lm',1511:'3l-l1',1512:'wins',1513:'fujitsu-dtc',1514:'fujitsu-dtcns',1515:'ifor-protocol',1516:'vpad',1517:'vpac',1518:'vpvd',1519:'vpvc',1520:'atm-zip-office',1521:'oracle',1522:'rna-lm',1523:'cichild-lm',1524:'ingreslock',1525:'orasrv',1526:'pdap-np',1527:'tlisrv',1528:'mciautoreg',1529:'support',1530:'rap-service',1531:'rap-listen',1532:'miroconnect',1533:'virtual-places',1534:'micromuse-lm',1535:'ampr-info',1536:'ampr-inter',1537:'sdsc-lm',1538:'3ds-lm',1539:'intellistor-lm',1540:'rds',1541:'rds2',1542:'gridgen-elmd',1543:'simba-cs',1544:'aspeclmd',1545:'vistium-share',1546:'abbaccuray',1547:'laplink',1548:'axon-lm',1549:'shivahose',1550:'3m-image-lm',1551:'hecmtl-db',1552:'pciarray',1600:'issd',1650:'nkd',1651:'shiva_confsrvr',1652:'xnmp',1661:'netview-aix-1',1662:'netview-aix-2',1663:'netview-aix-3',1664:'netview-aix-4',1665:'netview-aix-5',1666:'netview-aix-6',1667:'netview-aix-7',1668:'netview-aix-8',1669:'netview-aix-9',1670:'netview-aix-10',1671:'netview-aix-11',1672:'netview-aix-12',1680:'CarbonCopy',1720:'H.323/Q.931',1723:'pptp',1755:'wms',1761:'landesk-rc',1762:'landesk-rc',1763:'landesk-rc',1764:'landesk-rc',1827:'pcm',1900:'UPnP',1935:'rtmp',
        1984:'bigbrother',1986:'licensedaemon',1987:'tr-rsrb-p1',1988:'tr-rsrb-p2',1989:'tr-rsrb-p3',1990:'stun-p1',1991:'stun-p2',1992:'stun-p3',1993:'snmp-tcp-port',1993:'snmp-tcp-port',1994:'stun-port',1995:'perf-port',1996:'tr-rsrb-port',1997:'gdp-port',1998:'x25-svc-port',1999:'tcp-id-port',1999:'tcp-id-port',2000:'callbook',2001:'dc',2002:'globe',2003:'cfingerd',2004:'mailbox',2005:'deslogin',2006:'invokator',2007:'dectalk',2008:'conf',2009:'news',2010:'search',2011:'raid-cc',2012:'ttyinfo',2013:'raid-am',2014:'troff',2015:'cypress',2016:'bootserver',2017:'cypress-stat',2018:'terminaldb',2019:'whosockami',2020:'xinupageserver',2021:'servexec',2022:'down',2023:'xinuexpansion3',2024:'xinuexpansion4',2025:'ellpack',2026:'scrabble',2027:'shadowserver',2028:'submitserver',2030:'device2',2032:'blackboard',2033:'glogger',2034:'scoremgr',2035:'imsldoc',2038:'objectmanager',2040:'lam',2041:'interbase',2042:'isis',2043:'isis-bcast',2044:'rimsl',2045:'cdfunc',2046:'sdfunc',2047:'dls',2048:'dls-monitor',2049:'nfs',2064:'dnet-keyproxy',2053:'knetd',2065:'dlsrpn',2067:'dlswpn',2068:'advocentkvm',2105:'eklogin',2106:'ekshell',2108:'rkinit',2111:'kx',2112:'kip',2120:'kauth',2121:'ccproxy-ftp',2201:'ats',2232:'ivs-video',2241:'ivsd',2301:'compaqdiag',2307:'pehelp',2401:'cvspserver',2430:'venus',2431:'venus-se',2432:'codasrv',2433:'codasrv-se',2500:'rtsserv',2501:'rtsclient',2564:'hp-3000-telnet',2600:'zebrasrv',2601:'zebra',2602:'ripd',2603:'ripngd',2604:'ospfd',2605:'bgpd',2627:'webster',2628:'dict',2638:'sybase',2766:'listen',2784:'www-dev',2809:'corbaloc',2903:'extensisportfolio',2998:'iss-realsec',3000:'ppp',3001:'nessusd',3005:'deslogin',3006:'deslogind',3049:'cfs',3052:'PowerChute',3064:'dnet-tstproxy',3086:'sj3',3128:'squid-http',3141:'vmodem',3264:'ccmail',3268:'globalcatLDAP',
        3269:'globalcatLDAPssl',3292:'meetingmaker',3306:'mysql',3333:'dec-notes',3372:'msdtc',3389:'ms-term-serv',3421:'bmap',3455:'prsvp',3456:'vat',3457:'vat-control',3462:'track',3531:'peerenabler',3632:'distccd',3689:'rendezvous',3900:'udt_os',3984:'mapper-nodemgr',3985:'mapper-mapethd',3986:'mapper-ws_ethd',3999:'remoteanything',4000:'remoteanything',4008:'netcheque',4045:'lockd',4125:'rww',4132:'nuts_dem',4133:'nuts_bootp',4144:'wincim',4224:'xtell',4321:'rwhois',4333:'msql',4343:'unicall',4444:'krb524',4480:'proxy-plus',4500:'sae-urn',4557:'fax',4559:'hylafax',4660:'mosmig',4672:'rfa',4827:'squid-htcp',4899:'radmin',4987:'maybeveritas',4998:'maybeveritas',5000:'UPnP',5001:'commplex-link',5002:'rfe',5003:'filemaker',5010:'telelpathstart',5011:'telelpathattack',5050:'mmcc',5100:'admd',5101:'admdog',5102:'admeng',5145:'rmonitor_secure',5060:'sip',5190:'aol',5191:'aol-1',5192:'aol-2',5193:'aol-3',5232:'sgi-dgl',5236:'padl2sim',5300:'hacl-hb',5301:'hacl-gs',5302:'hacl-cfg',5303:'hacl-probe',5304:'hacl-local',5305:'hacl-test',5308:'cfengine',5400:'pcduo-old',5405:'pcduo',5490:'connect-proxy',5432:'postgres',5510:'secureidprop',5520:'sdlog',5530:'sdserv',5540:'sdreport',5550:'sdadmind',5555:'freeciv',5560:'isqlplus',5631:'pcanywheredata',5632:'pcanywherestat',5680:'canna',5679:'activesync',5713:'proshareaudio',5714:'prosharevideo',5715:'prosharedata',5716:'prosharerequest',5717:'prosharenotify',5800:'vnc-http',5801:'vnc-http-1',5802:'vnc-http-2',5803:'vnc-http-3',5900:'vnc',5901:'vnc-1',5902:'vnc-2',5903:'vnc-3',5977:'ncd-pref-tcp',5978:'ncd-diag-tcp',5979:'ncd-conf-tcp',5997:'ncd-pref',5998:'ncd-diag',5999:'ncd-conf',
        6000:'X11',6001:'X11:1',6002:'X11:2',6003:'X11:3',6004:'X11:4',6005:'X11:5',6006:'X11:6',6007:'X11:7',6008:'X11:8',6009:'X11:9',6017:'xmail-ctrl',6050:'arcserve',6101:'VeritasBackupExec',6103:'RETS-or-BackupExec',6105:'isdninfo',6106:'isdninfo',6110:'softcm',6111:'spc',6112:'dtspc',6141:'meta-corp',6142:'aspentec-lm',6143:'watershed-lm',6144:'statsci1-lm',6145:'statsci2-lm',6146:'lonewolf-lm',6147:'montage-lm',6148:'ricardo-lm',6346:'gnutella',6400:'crystalreports',6401:'crystalenterprise',6543:'mythtv',6544:'mythtv',6547:'PowerChutePLUS',6548:'PowerChutePLUS',6502:'netop-rc',6558:'xdsxdm',6588:'analogx',6666:'irc-serv',6667:'irc',6668:'irc',6969:'acmsoda',6699:'napster',7000:'afs3-fileserver',7001:'afs3-callback',7002:'afs3-prserver',7003:'afs3-vlserver',7004:'afs3-kaserver',7005:'afs3-volser',7006:'afs3-errors',7007:'afs3-bos',7008:'afs3-update',7009:'afs3-rmtsys',7010:'ups-onlinet',7070:'realserver',7100:'font-service',7200:'fodms',7201:'dlip',7273:'openmanage',7326:'icb',7464:'pythonds',7597:'qaz',7937:'nsrexecd',7938:'lgtomapper',8000:'http-alt',8007:'ajp12',8009:'ajp13',8021:'ftp-proxy',8080:'http-proxy',8081:'blackice-icecap',8082:'blackice-alerts',8443:'https-alt',8888:'sun-answerbook',8892:'seosload',9090:'zeus-admin',9100:'jetdirect',9111:'DragonIDSConsole',
        9152:'ms-sql2000',9535:'man',9876:'sd',9991:'issa',9992:'issc',9999:'abyss',
        10000:'snet-sensor-mgmt',10005:'stel'
        }
    try:
        return servicees[port]
    except:
        return "unknown"

