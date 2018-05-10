import sys
import sqlite3
from lxml import etree
sys.path.append("..")


'''function to get test results and write it to db'''
def parse():
    test_case_status = {}
    parse_document = './output.xml'
    with open (parse_document) as parse_text:
        xml = parse_text.read()
        root = etree.fromstring(xml)
        for elem in root.getchildren():
            if elem.tag == 'suite':
                for node in elem.getchildren():
                    if node.tag == "status":
                        # get result of whole test suite: status (ok or not), date (start and end)
                        suite_status = node.attrib["status"]
                        endtime = node.attrib["endtime"]
                        starttime = node.attrib["starttime"]
                        print node.attrib["status"]
                    # # geting results of each test
                    # if node.tag == 'test':
                    #     for test in node.getchildren():
                    #         if test.tag == "status":
                    #             case_status = test.node.attrib["status"]
    conn = sqlite3.connect("db/Statistics.db")
    temp = []
    temp.append((str(starttime), str(endtime), str(suite_status)))
    conn.executemany("INSERT INTO SuitStatistics(startTime, endTime, suiteStat) VALUES(?,?,?)", temp)
    conn.commit()
    conn.close()
    print "save"
