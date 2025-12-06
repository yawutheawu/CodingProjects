'''
Student:
Name - !
Age - !
ID - !
Grades
GPA
Courses

Teacher:
Courses
Age - !
ID - !
Name - !
Salary
Department

'''
import random as r

class Teacher:
    TeacherIDs = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        potentialID = r.randint(0, 9999)
        while potentialID in Teacher.TeacherIDs:
            potentialID = r.randint(0, 9999)
        self.id = potentialID
        Teacher.TeacherIDs.append(potentialID)
        self.salary = None
        self.department = None
        self.courses = []
    def setSalary(self, salary):
        self.salary = salary
    def TeacherIDs():
        return Teacher.TeacherIDs
    def setDepartment(self, department):
        self.department = department
    def addCourse(self, course):
        self.courses.append(course)
    def removeCourse(self, courseID):
        failFlag = True
        for i in self.courses:
            if i.courseID == courseID:
                failFlag = False
                self.courses.remove(i)
        if failFlag:
            return False
        else:
            return True

class Course:
    CourseIDs = []
    def __init__(self, courseName, section, meetingTime, department):
        self.courseName = courseName
        potentialID = r.randint(0, 9999999)
        while potentialID in Course.CourseIDs:
            potentialID = r.randint(0, 9999999)
        self.courseID = potentialID
        self.MeetingTime = meetingTime
        self.Deptartment = department
        self.section = section
        Course.CourseIDs.append(potentialID)
    def CourseIDs():
        return Course.CourseIDs
    def getID(self):
        return self.courseID