import unittest
import csv_json



class Test_csv_json_converter(unittest.TestCase):


    def test_convert(self):
        test1 = CsvToJsonConverter(['id,name\n','1,Ivan'])
        expected = [{ 'id':'1','name':'Ivan'}]
        self.assertEqual(test1.convert(), expected)


    def test_convert(self):
        test2 = CsvToJsonConverter(['id\n','1'])
        expected = ['id':'1']
        self.assertEqual(test2.convert(), expected)


    def test_convert(self):
        test3 = CsvToJsonConverter(['id, name, salary, birth\n','1, Ivan,,1999\n','2, AAA bbb, 100000, '])
        expected = '[{ "id":"1", "name":"Ivan",  "salary":"", "birth":"1999" },{  "id":"2", "name":"AAA bbb",  "salary":"100000", "birth":""}]'
        self.assertEqual(test3.convert(), expected)


        
if __name__== "__main__":
    unittest.main()
