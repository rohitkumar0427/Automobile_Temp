import pandas as pd

File_Name="calc"
Function_Name="add"


f = open("Test_"+File_Name+".py", "w")
f.write("import unittest\n")
f.write("import "+File_Name+"\n")
f.write("f = open(\"Difference_Report_"+File_Name+"\", \"a\")\n")

f.write("class Test"+File_Name+"(unittest.TestCase):\n")
f.write("\tdef test"+Function_Name+"(self):\n")

df = pd.read_excel(open('Testing_Add.xlsx','rb'),sheet_name='Sheet1')

for i in df.index:
	f.write("\t\ttry:\n")
	f.write("\t\t\tself.assertEqual("+File_Name+"."+Function_Name+"("+str(df["Input"][i])+"),"+str(df["Output"][i])+")\n")
	f.write("\t\texcept AssertionError as e:\n")
	f.write("\t\t\tf.write(\"TestCase_no_"+str(i)+":\\n\\t\"+str(e)+\" \\n\")\n")

f.write("if __name__ == '__main__':\n")
f.write("\tunittest.main()")
f.close()
