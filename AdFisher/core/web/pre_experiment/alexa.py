import unittest
import os, sys


def collect_sites(make_browser, output_file="out.txt", num_sites=5,
                  alexa_link="http://www.alexa.com/topsites"):
    file_path = "./" + output_file
    if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
        response = input("This will overwrite file {}... Continue? (Y/n)".format(output_file))
        if response == 'n':
            sys.exit(0)
    fo = open(output_file, "w")
    fo.close()
    print("Beginning Collection")

    class Test(unittest.TestCase):
        def setUp(self):
            self.unit = make_browser(-1, -1)

        def runTest(self):
            self.unit.collect_sites_from_alexa(alexa_link, output_file, num_sites)

        def tearDown(self):
            self.unit.quit()

    test = Test()
    suite = unittest.TestSuite()
    suite.addTest(test)
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)

    print("Collection Complete. Results stored in ", output_file)
