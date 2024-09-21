import unitest
from multiply import multiplication
class multiplyTestcase(unitest.Testcase):

 def test_1(self):
  
    result = multiplication(3,4)

    self.assertEqual(result, 12)

 def test_2(self):
  
    result = multiplication(3,-4)

    self.assertEqual(result, 3)

   if__name__'__main__':
   unitest.main()
