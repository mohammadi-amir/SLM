
import openai
import tkinter
from tkinter import Tk,  Entry
import requests

root = Tk()
root.title("Chatboot")
root.geometry("300x650")
root.minsize(width=200, height=250)



e = Entry(root, width=20, bg="gray")
e.pack()

root.mainloop()

client = openai.OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="nokeyneeded",
)


response = client.chat.completions.create(
    model="phi3",
    temperature=0.7,
    n=1,
    messages=[
        {"role": "system", "content": "Please of German Language "},
        {"role": "user", "content":"wo liegt Frankfurt ?"},
    ],
)
label = tkinter.Label(root, text= response.choices[0].message.content)
label.pack(pady=10)
output_label = tkinter.Label(root, text="Hi", wraplength=400, justify="left", fg="green")
output_label.pack(pady=10)

root.mainloop()
#print("Response:")
print(e.get())