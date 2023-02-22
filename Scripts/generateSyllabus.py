from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.text import WD_UNDERLINE

document = Document()
section = document.sections[0]
header = section.header

paragraph = header.paragraphs[0]
paragraph.text = "Course Syllabus\t\t[Insert semester]"
paragraph.style = document.styles["Header"]

title = document.add_paragraph('University Name')
title_format = title.paragraph_format
title_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

title2 = document.add_paragraph('[Program Name]')
title2_format = title2.paragraph_format
title2_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

title3 = document.add_paragraph('[Course Name]')
title3_format = title3.paragraph_format
title3_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

records = (
    ('Class Location: ', 'E-mail: '),
    ('Phone: ', 'Office hours: '),
    ('Lab location: ', 'Office location: '),
    ('Discussion seminar time: ', 'Discussion Seminar location: ')
)

table = document.add_table(rows=1, cols=2, style = "Table Grid")
row = table.rows[0].cells
row[0].text = 'Instructor: '
row[1].text = 'Class Time: '
for x, y in records:
    row_cells = table.add_row().cells
    row_cells[0].text = x
    row_cells[1].text = y
    
zoomMeeting = True 

if (zoomMeeting):
    row_cells = table.add_row().cells
    row_cells[0].text = 'Virtual office hours(Zoom)\nMeeting ID: \nPasscode: \n'
    row_cells[1].text = ''

paragraph2 = document.add_paragraph('\n')
run = paragraph2.add_run('Prerequisites')
run.underline = True
run.underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Insert Prerequisites]')

paragraph2.add_run('\n')
paragraph2.add_run('\nCourse Description').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Course Description]')

paragraph2.add_run('\n')
paragraph2.add_run('\nCourse Materials').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Textbook Title]')
paragraph2.add_run('\n[ISBN]')

paragraph2.add_run('\n')
paragraph2.add_run('\nLearning Objectives').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\nStudents who successfully complete this course will achieve the following learning objectives:')
paragraph2.add_run('\n[Insert learning objectives]')

paragraph2.add_run('\n')
paragraph2.add_run('\nLab Policy').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Course Description]')

paragraph2.add_run('\n')
paragraph2.add_run('\nAssignments').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Assignments]')

paragraph2.add_run('\n')
paragraph2.add_run('\nExpectations').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Expectations]')

paragraph2.add_run('\n')
paragraph2.add_run('\nQuiz').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Quiz]')

paragraph2.add_run('\n')
paragraph2.add_run('\nExam').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Exam]')

paragraph2.add_run('\n')
paragraph2.add_run('\nDiscussion Policy').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Discussion Policy]')

paragraph2.add_run('\n')
paragraph2.add_run('\nAttendance').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Attendance]')

paragraph2.add_run('\n')
paragraph2.add_run('\nGrading').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Grading]')

paragraph2.add_run('\n')
paragraph2.add_run('\nDisability Services').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Disability Services]')

paragraph2.add_run('\n')
paragraph2.add_run('\nHonor Code').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Honor Code]')

paragraph2.add_run('\n')
paragraph2.add_run('\nOnline Resources').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Online Resources]')

paragraph2.add_run('\n')
paragraph2.add_run('\nExtra Credit').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Extra Credit]')

paragraph2.add_run('\n')
paragraph2.add_run('\nFinal Exam').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Final Exam]')

paragraph2.add_run('\n')
paragraph2.add_run('\nInclement Weather').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Inclement Weather]')

paragraph2.add_run('\n')
paragraph2.add_run('\nWithdrawals').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Withdrawals]')

paragraph2.add_run('\n')
paragraph2.add_run('\nSyllabus Update').underline = WD_UNDERLINE.SINGLE
paragraph2.add_run('\n[Syllabus Update]')

paragraph2.add_run('\n')
paragraph2.add_run('\nLecture Schedule').underline = WD_UNDERLINE.SINGLE
schedule = (
    ('12/7', 'Mon', 'Lab1', 'Virus', 'Chapter 1', 'HW 1', '', '', '', ''),
    ('12/9', 'Wed', 'Lab1', 'Virus', '' ,'' ,'' ,'HW1' , '', 'Quiz 1')
)

table2 = document.add_table(rows=1, cols=10, style = "Table Grid")
row = table2.rows[0].cells
row[0].text = 'Date'
row[1].text = 'Lecture'
row[2].text = 'Lab'
row[3].text = 'Topic'
row[4].text = 'Reading'
row[5].text = 'HW'
row[6].text = 'HW Due'
row[7].text = 'Lab Due'
row[8].text = 'Exam'
row[9].text = 'Quiz'
for one, two, three, four, five, six, seven, eight, nine, ten in schedule:
    row_cells = table2.add_row().cells
    row_cells[0].text = one
    row_cells[1].text = two
    row_cells[2].text = three
    row_cells[3].text = four
    row_cells[4].text = five
    row_cells[5].text = six
    row_cells[6].text = seven
    row_cells[7].text = eight
    row_cells[8].text = nine
    row_cells[9].text = ten


document.save('syllabus.docx')