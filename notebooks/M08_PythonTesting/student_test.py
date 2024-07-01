from student import Student
import unittest

class EnrollInTestCase(unittest.TestCase): 
    
    def test_01_is_numCoursincremented_correctly(self):
        # Create student instance, adding some courses
        student1 = Student('Katherine', ['DS 5100'])
        student1.enroll_in_course("CS 5050")
        student1.enroll_in_course("CS 5777")
        print(student1.courses)
        print(student1.num_courses)
        
        # Test
        expected = 3
        # unittest.TestCase brings in the assertEqual() method
        self.assertEqual(student1.num_courses, expected)
                
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
