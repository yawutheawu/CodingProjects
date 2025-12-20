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
    Teachers = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        potentialID = r.randint(0, 9999)
        while potentialID in Teacher.TeacherIDs:
            potentialID = r.randint(0, 9999)
        self.id = potentialID
        Teacher.TeacherIDs.append(potentialID)
        Teacher.Teachers.append(self)
        self.salary = None
        self.department = None
        self.courses = []
    def setSalary(self, salary):
        self.salary = salary
    def getTeacherIDs():
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
    def getTeacherfromID(teacherID):
        for i in Teacher.Teachers:
            if i.id == teacherID:
                return i
        return None
    
class Student:
    StudentIDs = []
    Students = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        potentialID = r.randint(0, 9999)
        while potentialID in Student.StudentIDs:
            potentialID = r.randint(0, 9999)
        self.id = potentialID
        Student.StudentIDs.append(potentialID)
        Student.Students.append(self)
        self.grades = {}
        self.GPA = None
        self.courses = []
    def addCourse(self, course):
        self.courses.append(course)
        self.grades[course] = 0
        return True
    def removeCourse(self, courseID):
        failFlag = True
        for i in self.courses:
            if i.courseID == courseID:
                failFlag = False
                self.courses.remove(i)
                del self.grades[courseID]
        if failFlag:
            return False
        else:
            return True
    def calcGPA(self):
        gradeList = []
        for i in self.grades.values():
            gradeList.append(i)
        self.GPA = sum(gradeList)/len(gradeList)
        return self.GPA
            
    def setGrade(self, courseID, grade):
        if courseID in self.grades:
            self.grades[courseID] = grade
            return True
        else:
            return False
    def getStudentID():
        return Student.StudentIDs
    def getStudents():
        return Student.Students
    def getStudentfromID(studentID):
        for i in Student.Students:
            if i.id == studentID:
                return i
        return None

class Course:
    CourseIDs = []
    Courses = []
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
        Course.Courses.append(self)
    def getCourseIDs():
        return tuple(Course.CourseIDs)
    def getID(self):
        return self.courseID
    def getCoursefromID(courseID):
        for i in Course.Courses:
            if i.courseID == courseID:
                return i
        return None
    def getStudentsEnrolled(self):
        enrolledStudents = []
        for i in Student.Students:
            for j in i.courses:
                if j == self.courseID:
                    enrolledStudents.append(i)
        return enrolledStudents
    def getTeacher(self):
        for i in Teacher.Teachers:
            for j in i.courses:
                if j == self.courseID:
                    return i
        return None
    def getClasslist(self):
        classList = {}
        studentList = []
        for i in Student.Students:
            for j in i.courses:
                if j == self.courseID:
                    studentList.append(i.name)
        classList["Students"] = studentList
        for i in Teacher.Teachers:
            for j in i.courses:
                if j == self.courseID:
                    classList["Teacher"] = i.name
        return classList
    def getClasslistIDs(self):
        classList = {}
        studentList = []
        for i in Student.Students:
            for j in i.courses:
                if j == self.courseID:
                    studentList.append(i.id)
        classList["Students"] = studentList
        for i in Teacher.Teachers:
            for j in i.courses:
                if j == self.courseID:
                    classList["Teacher"] = i.id
        return classList

if __name__ == "__main__":
    #Teachers
    johnSmith = Teacher("John Smith", 45)
    johnSmith.setDepartment("History")
    johnSmith.setSalary(55000)
    MarleneJones = Teacher("Marlene Jones", 39)
    MarleneJones.setDepartment("Mathematics")
    MarleneJones.setSalary(55000)
    
    #Students
    aliceBrown = Student("Alice Brown", 20)
    bobDavis = Student("Bob Davis", 22)
    charlieEvans = Student("Charlie Evans", 19)
    dianaFoster = Student("Diana Foster", 21)
    krisGarcia = Student("Kris Garcia", 23)
    ellaHarris = Student("Ella Harris", 20)
    liamJohnson = Student("Liam Johnson", 22)
    derekKing = Student("Derek King", 24)
    ninaLopez = Student("Nina Lopez", 21)
    oscarMartinez = Student("Oscar Martinez", 23)
    #Courses
    history101 = Course("History 101", "1", "MWF 9-10AM", "History")
    math101 = Course("Math 101", "1", "TTh 11-12:30PM", "Mathematics")
    
    #Assign Teachers to Courses
    johnSmith.addCourse(history101.courseID)
    MarleneJones.addCourse(math101.courseID)
    
    #Enroll Students in Courses
    aliceBrown.addCourse(history101.courseID)
    bobDavis.addCourse(history101.courseID)
    charlieEvans.addCourse(history101.courseID)
    dianaFoster.addCourse(history101.courseID)
    krisGarcia.addCourse(history101.courseID)
    ellaHarris.addCourse(history101.courseID)
    liamJohnson.addCourse(history101.courseID)
    ellaHarris.addCourse(math101.courseID)
    liamJohnson.addCourse(math101.courseID)
    derekKing.addCourse(math101.courseID)
    ninaLopez.addCourse(math101.courseID)
    oscarMartinez.addCourse(math101.courseID)
    
    print(history101.getClasslist())
    print(math101.getClasslist())
    #Add function that gets classlist with IDs of students and teachers
    historyClass = history101.getClasslistIDs()
    mathClass = math101.getClasslistIDs()
    
    print(Student.getStudentfromID(historyClass["Students"][0]).grades)
    print(Student.getStudentfromID(historyClass["Students"][0]).calcGPA())