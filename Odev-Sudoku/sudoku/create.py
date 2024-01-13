from unittest import TestCase
import resource as resource
import createTest as sudoku
 
 
class CreateTest(TestCase):
    def setUp(self):
        self.status = "ok"
        self.validity = "Valid"

 
#     
#      Analysis
#     
#         Sad path.
#             test 910:    sting; level="two" 
#             test 920:    level = None
#             test 930:    level = ""; empty string
#             test 940:    level ="  " blank string
#             test 950:    level = -2  out of boundary where level is less than 1  
#             test 960:    level = 6   out of boundary where greater than 5
#             test 970:    level = 1.5 floating point

    def test200_910ShouldErrOnLevelBeingString(self):
        parms = {'level':'two'}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 1)
        self.assertIn('status', result)
        self.assertIn(result['status'][0:5], 'hata:')
    
    def test200_920ShouldErrOnLevelBeingNone(self):
        parms = {'level': "None"}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 1)
        self.assertIn('status', result)
        self.assertIn(result['status'][0:5], 'hata:')

    def test200_930ShouldErrOnLevelBeingEmptyStr(self):
        parms = {'level':""}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 1)
        self.assertIn('status', result)
        self.assertIn(result['status'][0:5], 'hata:')
        
    def test200_940ShouldErrOnLevelBeingBlankStr(self):
        parms = {'level':"    "}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 1)
        self.assertIn('status', result)
        self.assertIn(result['status'][0:5], 'hata:')
    
    def test200_950ShouldErrOnLevelLT1(self):
        parms = {'level':"0"}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 1)
        self.assertIn('status', result)
        self.assertIn(result['status'][0:5], 'hata:')
    
    def test200_960ShouldErrOnLevelGT5(self):
        parms = {'level':"10"}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 1)
        self.assertIn('status', result)
        self.assertIn(result['status'][0:5], 'hata:')
    
    def test200_970ShouldErrOnLevelBeingNotInteger(self):
        parms = {'level':"1.5"}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 1)
        self.assertIn('status', result)
        self.assertIn(result['status'][0:5], 'hata:')
    
    def test200_980ShouldErrOnLevelBeingNotInteger(self):
        parms = {'level':"2.0"}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 1)
        self.assertIn('status', result)
        self.assertIn(result['status'][0:5], 'hata:')
        
        
# Happy Path Test        
    def test200_100ShouldReturnValidGridOnLevel1(self):
        parms = {'level':"1"}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 3)
        self.assertEquals(result['status'], self.status)
        self.assertIn('grid', result)
        grid = result['grid']
        self.assertEquals(resource.gridLevel1, grid)
        
    def test200_110ShouldReturnValidIntegrityOnLevel1(self):
        parms = {'level':"1"}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 3)
        self.assertEquals(result['status'], self.status)
        self.assertIn('integrity', result)
        integrity = result['integrity']
        self.assertEquals(resource.integrityLevel1, integrity)
    
    def test200_120ShouldReturnValidGridOnLevel2(self):
        parms = {'level':"2"}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 3)
        self.assertEquals(result['status'], self.status)
        self.assertIn('grid', result)
        grid = result['grid']
        self.assertEquals(resource.gridLevel2, grid)
    
    def test200_130ShouldReturnValidIntegrityOnLevel2(self):
        parms = {'level':"2"}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 3)
        self.assertEquals(result['status'], self.status)
        self.assertIn('integrity', result)
        integrity = result['integrity']
        self.assertEquals(resource.integrityLevel2, integrity)
    
    def test200_140ShouldReturnValidGridOnLevel3(self):
        parms = {}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 3)
        self.assertEquals(result['status'], self.status)
        self.assertIn('grid', result)
        grid = result['grid']
        self.assertEquals(resource.gridLevel3, grid)
    
    def test200_150ShouldReturnValidIntegrityOnLevel3(self):
        parms = {'level':"3"}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 3)
        self.assertEquals(result['status'], self.status)
        self.assertIn('integrity', result)
        integrity = result['integrity']
        self.assertEquals(resource.integrityLevel3, integrity)
    
    def test200_160ShouldReturnValidGridOnLevel4(self):
        parms = {'level':"4"}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 3)
        self.assertEquals(result['status'], self.status)
        self.assertIn('grid', result)
        grid = result['grid']
        self.assertEquals(resource.gridLevel4, grid)
    
    def test200_170ShouldReturnValidIntegrityOnLevel4(self):
        parms = {'level':"4"}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 3)
        self.assertEquals(result['status'], self.status)
        self.assertIn('integrity', result)
        integrity = result['integrity']
        self.assertEquals(resource.integrityLevel4, integrity)

    def test200_180ShouldReturnValidGridOnLevel5(self):
        parms = {'level':"5"}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 3)
        self.assertEquals(result['status'], self.status)
        self.assertIn('grid', result)
        grid = result['grid']
        self.assertEquals(resource.gridLevel5, grid)
    
    def test200_190ShouldReturnValidIntegrityOnLevel5(self):
        parms = {'level':"5"}
        parms['op'] = 'create'
        result = sudoku._create(parms)
        self.assertEqual(len(result), 3)
        self.assertEquals(result['status'], self.status)
        self.assertIn('integrity', result)
        integrity = result['integrity']
        self.assertEquals(resource.integrityLevel5, integrity)
        
    #createTest.py

    def test300_210ShouldReturnUpdatedGridAndIntegrity(self):
        parms = {
            'op': 'insert',
            'cell': 'R1C1',
            'value': 5,
            'grid': {'grid': resource.gridLevel1},
            'integrity': {'integrity': resource.integrityLevel1}
        }
        result = sudoku.insert_operation(**parms)
        
        # Beklenen sonuçları kontrol et
        self.assertEqual(result['status'], 'ok')
        self.assertIn('grid', result)
        self.assertIn('integrity', result)
        
        # İhtiyaca göre grid ve integrity değerlerini kontrol et
        # (Örnek: self.assertEquals(result['grid'], beklenen_grid))
        # (Örnek: self.assertEquals(result['integrity'], beklenen_integrity))
