#!/usr/bin/env python


def merge_tables(tab1, tab2):
    result_table = []
    count = 0
    for i in tab1:
        for j in tab2:
            count += 1
            if i == j:
                result_table.append(i)

    print count
    return result_table


def merge_tables_tuned(tab1, tab2):
    result_table = pivot = tested = []
    count = i = j = 0

    if len(tab1) <= len(tab2):
        pivot = tab1
        tested = tab2
    else:
        pivot = tab2
        tested = tab1

    len_pivot = len(pivot)
    len_tested = len(tested)

    for i in xrange(len_pivot):
        for j in xrange(j, len_tested):
            count += 1
            if pivot[i] == tested[j]:
                result_table.append(pivot[i])
            elif pivot[i] < tested[j]:
                break

    print count
    return result_table


def main():
    tab1 = [1,4,22,32,49,62,79,84,99,106,121,125,131,144,161,200,202,206,216,234,247,268,277,296,322,325,328,330,341,351,383,391,421,425,429,441,444,448,457,464,469,491,510,518,521,530,556,572,575,578,583,612,620,626,632,640,642,645,649,661,673,677,693,708,715,720,724,739,740,741,743,748,757,762,763,765,770,775,779,780,787,801,807,825,830,833,838,871,895,896,908,910,911,947,948,955,957,965,968,972,977,978,983,991,1000,1002,1023,1041,1045,1055,1073,1093,1099,1101,1108,1112,1153,1155,1166,1170,1177,1182,1191,1200,1206,1208,1232,1233,1245,1266,1273,1278,1280,1281,1306,1321,1327,1364,1383,1392,1417,1440,1442,1455,1467,1468,1483,1491,1514,1520,1525,1528,1529,1536,1541,1557,1576,1585,1587,1589,1602,1603,1614,1621,1624,1628,1640,1642,1648,1655,1660,1685,1706,1720,1721,1732,1739,1747,1748,1750,1768,1777,1796,1811,1820,1828,1852,1869,1904,1909,1924,1932,1947,1955,1973,1976,1984,1990,1991,1994]
    tab2 = [23,33,51,57,70,78,80,81,84,85,90,104,108,127,133,134,141,149,159,171,187,192,193,200,203,204,213,218,225,230,238,250,286,291,299,306,308,310,317,365,370,384,390,403,406,432,437,447,453,457,458,461,463,477,478,489,490,491,516,518,523,527,529,537,556,566,569,582,587,593,594,602,605,613,639,653,665,668,677,678,683,691,710,712,719,754,755,760,765,772,808,809,818,830,838,842,849,857,891,898]

    print merge_tables_tuned(tab1, tab2)
    print "====="
    print merge_tables(tab1, tab2)


if __name__ == "__main__":
    main()