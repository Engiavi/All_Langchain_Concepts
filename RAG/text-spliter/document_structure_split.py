from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

# python code in class


text = """
class Student:
    def __init__(self, name, age, grade):
        self.name = name  # Field for the student's name
        self.age = age  # Field for the student's age
        self.grade = grade  # Field for the student's grade


"""
# # Example of creating a Student object and assigning fields
# student1 = Student("Alice", 20, "A")
# print(f"Name: {student1.name}, Age: {student1.age}, Grade: {student1.grade}")

spliter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=100, chunk_overlap=0
)

chunk = spliter.split_text(text)
print(len(chunk))
