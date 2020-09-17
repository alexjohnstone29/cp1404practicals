

from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)
print(python)
print(visual_basic)

language_list = [ruby, python, visual_basic]

print("The dynamically typed languages are:")
for line in language_list:
    line.is_dynamic()
    if line.reflection == "True":
        print(line.name)
