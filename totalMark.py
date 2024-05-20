# Program to calculate the final grade of students
#Abdullahi Sediq Ojonugwa 22CS1005
students = [
    {
    "name": "Sadiq",
    "exams":50,
    "assignments":30,
    "participation":10
    },

    {
    "name": "Emmanuel",
    "exams":40,
    "assignments":25,
    "participation":5
    },

    {
    "name": "Victor",
    "exams":70,
    "assignments":40,
    "participation":5
    }
]
def getFinalGrade():
   for i in range(len(students)):
      totalGrade = students[i]["exams"] + students[i]["assignments"] + students[i]["participation"]
      print("Total grade for", students[i]["name"], ":", totalGrade)

getFinalGrade()