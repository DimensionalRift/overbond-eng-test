import unittest
import main
class TestOverbond(unittest.TestCase):

    def test_parseLine_DIs_only(self):
        self.assertEqual({'DIs':"08-Jun-96" }, main.parseLine("BDBo;i8169;SiKOP_96_1A;s2;BTy1;DIs19960608;AOs700000000;DMa20211128;RCp5;DNc20211128;DCm1;Mv100;HaY;RDd0;RDt1;NRd2;CPFrN;LCOd20211128;Fv1;CFq2;Cc8;RIxCPI_IS;FCd19980528;VBa175.8;Vm5000000;MDo255;SSDaN;FIt3;DAd19960515;"
                                        , {}))
    def test_parseLine_Pl(self):
        self.assertEqual({'Pl':87.97 }, main.parseLine("m;i8221;t180000.336;Dt20210907;ISOcY;ISOtY;Pl87.97;LTd20130517;LPd20070711;"
                                            , {}) )

    def test_parseLine_All3(self):
        self.assertEqual({'BPr': 119.7, 'APl': 125.9, 'Pl':122.6 }, main.parseLine("m;i45168;t180000.336;Dt20210907;ISOcY;ISOtY;d0;BPr119.7;APl125.9;Pl122.6;HPm122.6;HPMd20210903;LPm122.0238;LPMd20210901;HPy123.0362;HPYd20210415;LPy120.39;LPYd20210824;LTd20210903;LPd20210903;"
                                        , {}))
    def test_parseLine_Nothing(self):
        self.assertEqual({}, main.parseLine("BDLi;i14720;SiICE_MUNICIPAL_AND_LSS_BONDS;s2;LSt434;PAi14718;NAmICE Municipal and LSS Bonds;LCyISK;TCeN;"
                                        , {}) )
    def test_parseRecords_One(self):
        file = open("one_test.txt", encoding="utf8")
        self.assertEqual([{'DIs': "07-Jul-04", 'BPr': 119.7, 'APl': 125.9, 'Pl':122.6 }], main.parseRecords(file))
        file.close()
    # Note, can add more test cases for more records if needed
    # However, I don't see the need to at this time as this is an assessment and I can't spend more time on it.
if __name__ == '__main__':

    unittest.main()
