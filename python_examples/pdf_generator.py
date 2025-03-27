# Recreate the PDF with text-based arrows instead of special characters
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="6-Week C++ + CP + Robotics Master Plan", ln=True, align="C")
pdf.ln(10)

# Week 1-2: Master C
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Week 1-2: Master C", ln=True)
pdf.multi_cell(0, 10, txt="Pointers & Memory - Practice pointer arithmetic, malloc, calloc, free\n"
                           "Structures & File I/O - Build a mini contact book using structs & file handling\n"
                           "5 Beginner CP Problems - Solve basic math & loops problems on Codeforces/AtCoder\n")
pdf.ln(5)

# Week 3-4: Power Up with C++
pdf.cell(200, 10, txt="Week 3-4: Power Up with C++", ln=True)
pdf.multi_cell(0, 10, txt="OOP Basics - Create simple classes (Bank Account, Student Database)\n"
                           "STL Mastery - Learn vector, map, set, priority_queue, sort()\n"
                           "5 Beginner CP Problems in C++ - Codeforces Div. 3 or Leetcode Easy\n")
pdf.ln(5)

# Week 5-6: CP + Robotics Blend
pdf.cell(200, 10, txt="Week 5-6: CP + Robotics Blend", ln=True)
pdf.multi_cell(0, 10, txt="Graph Basics (BFS/DFS) - Solve 3 graph traversal problems\n"
                           "Arduino + C - Blink LED, read sensor values, control a servo motor\n"
                           "5 Medium CP Problems - Start learning binary search, recursion, DP\n")
pdf.ln(5)

# Long-Term Weekly Plan
pdf.cell(200, 10, txt="Long-Term Weekly Plan (After 6 Weeks)", ln=True)
pdf.multi_cell(0, 10, txt="Monday-Tuesday - Learn a new CP concept (e.g., DP, bit manipulation)\n"
                           "Wednesday - Watch 1 Robotics tutorial + try an Arduino project\n"
                           "Thursday-Friday - Solve 3 medium CP problems\n"
                           "Saturday - Revise STL & algorithms + learn an advanced CP topic\n"
                           "Sunday - Free day or work on a robotics simulation\n")
pdf.ln(5)

# Extra Resources
pdf.cell(200, 10, txt="Extra Resources to Speed Up Learning", ln=True)
pdf.multi_cell(0, 10, txt="C & C++ - GeeksForGeeks | CPP Reference\n"
                           "CP Practice - Codeforces | AtCoder\n"
                           "Robotics & Arduino - SparkFun | ROS Tutorials\n")
pdf.ln(5)

# Footer
pdf.set_font("Arial", 'I', 10)
pdf.cell(200, 10, txt="Now go dominate CP and Robotics!", ln=True, align="C")

# Save the PDF
file_path = "/mnt/data/6_Week_C_Plus_Plus_CP_Robotics_Plan_v3.pdf"
pdf.output(file_path)

file_path
