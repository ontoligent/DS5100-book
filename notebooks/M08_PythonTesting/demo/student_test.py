from student import Student
import unittest

class EnrollInTestCase(unittest.TestCase): 
    
    def test_01_is_numCoursincremented_correctly(self):
        """
        Test if enrollInCourse() method successfully increments the
        num_courses attribute of the Student object 
        """
        
        student1 = Student('Katherine', ['DS 5100'])
        student1.enroll_in_course("CS 5050")
        student1.enroll_in_course("CS 5777")
        print('Course names:', student1.courses)
        print('Course count:', student1.num_courses)
        
        expected = 3
        self.assertEqual(student1.num_courses, expected)
                
        
if __name__ == '__main__':
    unittest.main()
