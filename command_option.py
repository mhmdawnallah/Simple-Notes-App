from notebook import Note, Notebook

notebook = Notebook()
notebook.new_note("Hello world")
notebook.new_note("Hello again")


print(notebook.notes)