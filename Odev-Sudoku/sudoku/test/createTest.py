
'''
    The file contains the test code for create function
    Created on oct 16, 2019
    @author:    Uma Athikala
'''

# -*- coding: utf-8 -*-

from unittest import TestCase
import sudoku.create as sudoku 



# acceptance Tests
# 
# input: dictionary parms
#            op: "create",  key-value pair, string , validated by dispatch
#            level : [1,5],  string of an integer 
# 
# output: dictionary outputCreate
#            grid : list of 81 integers
# 
# HAPPY PATH
#     Test010 : string of nominal value of 'level'
#     Test020 : no instance of 'level' 
#     Test030 : string of low bound of 'level'
#     Test040 : string of upper bound of 'level'
#
#
# SAD PATH
#     Test910 : string of non-integer value of 'level'
#     Test920 : non-string value of 'level'
#     Test930 : string of integer value less than lower bound of 'level'
#     Test940 : string of integer value above the upper bound of 'level'
#     Test950 : string without a value given to level

class CreateTest(TestCase):
        
        
    #def testIfReturnsDict_withokstatus(self):
    #    expectedResult = {'status' : 'ok'}
    #    parms = {'op': 'create'}
    #    actualResult = sudoku._create(parms)
    #    self.assertEqual(expectedResult, actualResult)
        
    #def testIfHexDigestReturnsStringValue(self):
    #    expectedResult = {'integrity' : 'randomvalue', 'status' : 'ok'}
    #    params = {'op': 'create'}
    #    actualResult = sudoku._create(params)
    #    self.assertEqual(expectedResult, actualResult)
        
    #def testIfHexDigestReturnsConcatenatedStringValueofAGrid(self):
    #    expectedResult = '0-40-80-50000000-700-1-2-3-7-8-200-50-400-9-50-70-6-10000-8-600-7-7-5-6000-9000-3-7-6-100-2-5-2000-500-8000-1-40-9-600'
    #    actualResult = sudoku._integrity([0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, -1, -7, 0, -5, 0, 0])
    #    self.assertEqual(expectedResult, actualResult)
        
    #def testIfHexDigestReturnsSHA256HexDigestofAGrid(self):
    #    expectedResult = 'b594924588d873f60df054a64a7bfaa1d4196ab1d2000f1788a453c1765b05b8'
    #    actualResult = sudoku._integrity([0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, -1, -7, 0, -5, 0, 0])
    #    self.assertEqual(expectedResult, actualResult)
    
    #def testIfHexDigestReturnsSHA256HexDigestofAGrid_UpperBound(self):
    #    expectedResult = '110a79143bc7c2b66faff5e8fe895320d402e4f91dbbe6b969931228abb84242'
    #    actualResult = sudoku._integrity([-2, 0, 0, 0, -5, 0, -9, -1, 0, -6, 0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, -2, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0, 0, -7, 0, -9, -3, 0, -1, 0, -5, 0, 0, 0, 0, 0, 0, 0, -7, 0, 0, -2, 0, -1, 0, 0, -3, 0, 0, -5, 0, -4, 0, 0, -6, 0, 0, 0, 0, 0])
    #    self.assertEqual(expectedResult, actualResult)
        
    #def testIfHexDigestReturnsSHA256HexDigestofAGrid_LowerBound(self):
    #    expectedResult = '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5'
    #    actualResult = sudoku._integrity([-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0])
    #    self.assertEqual(expectedResult, actualResult)
        
    def testForNominalValueoflevel(self):
        expectedResult = { 'grid': [0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, -1, -7, 0, -5, 0, 0],
                            'integrity': 'b594924588d873f60df054a64a7bfaa1d4196ab1d2000f1788a453c1765b05b8', 
                                'status': 'ok'}
        params = {'op': 'create','level': '3'}
        actualResult = sudoku._create(params)
        self.assertEqual(expectedResult, actualResult)
        
    def testForUpperboundValueoflevel(self):
        expectedResult = { 'grid' : [-2, 0, 0, 0, -5, 0, -9, -1, 0, -6, 0, 0, 0, 0, -8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -3, 0, 0, -2, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, -4, 0, 0, 0, 0, -7, 0, -9, -3, 0, -1, 0, -5, 0, 0, 0, 0, 0, 0, 0, -7, 0, 0, -2, 0, -1, 0, 0, -3, 0, 0, -5, 0, -4, 0, 0, -6, 0, 0, 0, 0, 0],
                            'integrity' : '110a79143bc7c2b66faff5e8fe895320d402e4f91dbbe6b969931228abb84242',
                                'status' : 'ok'}
        params = {'op': 'create', 'level' : '5'}
        actualResult = sudoku._create(params)
        self.assertEqual(expectedResult, actualResult)
        
    def testForLowerboundValueoflevel(self):
        expectedResult = { 'grid' : [-8, -1, -5, -7, -6, -9, -3, -2, 0, -4, -9, 0, 0, 0, -5, -8, -7, 0, 0, 0, -6, 0, -4, -8, 0, -9, -5, 0, -8, -1, 0, 0, -3, 0, 0, -2, 0, -5, 0, -1, -8, 0, -9, 0, -7, -7, -3, -9, -5, -2, -4, -6, -8, -1, -9, -4, 0, 0, 0, -7, 0, -1, -8, -5, -2, 0, -8, -9, 0, -4, -6, -3, -1, -6, 0, -4, -3, -2, -7, 0, 0],
                            'integrity' : '634dd6769e9b9a53ee4416edb9790684ac18dcbde5b879260610ff27794b66f5',
                                'status' : 'ok'}
        params={ 'op':'create','level':'1'}
        actualResult = sudoku._create(params)
        self.assertEqual(expectedResult, actualResult)
        
    def testForValueoflevel2(self):
        expectedResult = { 'grid' : [0, -3, 0, 0, 0, -2, 0, -6, -5, -5, -8, 0, -1, -3, -4, 0, -2, -9, 0, -2, -7, 0, -5, 0, 0, 0, -1, 0, 0, -2, 0, 0, -9, 0, -1, -3, -8, -5, -9, 0, -7, -1, 0, -4, -2, -1, 0, 0, -6, -2, 0, 0, 0, -7, 0, 0, 0, 0, -4, -7, -2, -5, 0, -6, -7, -5, 0, 0, -8, 0, -9, 0, 0, -9, -4, -5, -6, 0, 0, -7, -8],
                            'integrity' : '39a4fbe2283d82b8dff98f36e6fcb09e6071653a77795e9527b26f90b4ad0d26',
                                'status' : 'ok'}
        params={ 'op':'create','level':'2'}
        actualResult = sudoku._create(params)
        self.assertEqual(expectedResult, actualResult)
        
    def testForValueoflevel4(self):
        expectedResult = { 'grid' : [0, -6, -7, 0, -2, 0, 0, 0, -3, 0, -8, 0, -7, 0, -3, 0, 0, -6, -1, 0, 0, 0, 0, 0, 0, -7, 0, 0, -5, 0, 0, -3, 0, 0, 0, -8, -8, 0, 0, 0, -4, 0, 0, 0, -1, -4, 0, 0, 0, -6, 0, 0, -5, 0, -3, 0, 0, 0, 0, 0, 0, 0, -2, -6, 0, 0, -2, 0, -4, 0, -3, 0, -5, 0, 0, 0, -9, 0, -8, -4, 0],
                            'integrity' : '0ea83ad27c27241477102e2377f1bb14cc2f8c6125fbc85fab972c9ab0661319',
                                'status' : 'ok'}
        params={ 'op':'create','level':'4'}
        actualResult = sudoku._create(params)
        self.assertEqual(expectedResult, actualResult)
        
    
        
    def testForNoMentionOfLevelGiven(self):
        expectedResult = { 'grid': [0, 0, -3, 0, 0, -7, 0, -2, 0, -4, 0, -7, 0, 0, -5, -3, 0, 0, 0, 0, -8, -9, 0, -6, -7, 0, -1, -8, 0, -2, -5, 0, 0, -6, 0, -4, 0, -7, 0, 0, -8, 0, -1, -5, 0, -5, 0, 0, -7, -6, 0, 0, 0, -9, 0, 0, -5, 0, 0, -9, 0, 0, -6, 0, -1, 0, -6, 0, 0, -2, -8, 0, 0, -2, -4, -1, -7, 0, -5, 0, 0],
                            'integrity': 'b594924588d873f60df054a64a7bfaa1d4196ab1d2000f1788a453c1765b05b8', 
                                'status': 'ok'}
        params = {'op': 'create'}
        actualResult = sudoku._create(params)
        self.assertEqual(expectedResult, actualResult)
        
        
    #SAD PATH
    
    def testForAboveUpperBoundLevel(self):
        expectedResult = {'status':'error: invalid level'}
        params = {'op': 'create', 'level' : '6'}
        actualResult = sudoku._create(params)
        self.assertEqual(expectedResult, actualResult)
        
    def testForBelowLowerBoundLevel(self):
        expectedResult = {'status':'error: invalid level'}
        params = {'op': 'create', 'level' : '0'}
        actualResult = sudoku._create(params)
        self.assertEqual(expectedResult, actualResult)
     
    # The below function is taken off since it is not relevant to the requirements    
    #def testForNonStringLevel(self):
    #    expectedResult = {'status':'error: invalid DataType of level'}
    #    params = {'op': 'create', 'level' : 3}
    #    actualResult = sudoku._create(params)
    #    self.assertEqual(expectedResult, actualResult)
        
    def testForStringofNonIntegerLevel(self):
        expectedResult = {'status':'error: invalid DataType for value of level'}
        params = {'op': 'create', 'level' : 'three'}
        actualResult = sudoku._create(params)
        self.assertEqual(expectedResult, actualResult)
        
    def testForEmptyStringofLevel(self):
        expectedResult = {'status':'error: no value given for level'}
        params = {'op': 'create', 'level' : ''}
        actualResult = sudoku._create(params)
        self.assertEqual(expectedResult, actualResult)
        

        
        
        
        
    
        
    
         
