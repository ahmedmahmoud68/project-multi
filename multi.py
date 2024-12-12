import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play_text():
    text = text_entry.get("1.0", tk.END).strip()  # الحصول على النص المدخل
    if text:
        try:
            tts = gTTS(text, lang='ar')  # تعديل اللغة إلى العربية (أو الإنجليزية إذا كنت تفضل)
            tts.save("output.mp3")
            # التعامل مع التشغيل على أنظمة التشغيل المختلفة
            if os.name == "nt":  # نظام ويندوز
                os.system("start output.mp3")
            else:  # أنظمة macOS أو Linux
                os.system("open output.mp3" if os.name == "posix" else "xdg-open output.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please enter some text to play.")

def clear_text():
    text_entry.delete("1.0", tk.END)  # مسح النص المدخل

def exit_app():
    root.destroy()  # إغلاق التطبيق

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("تطبيق تحويل النص إلى كلام")
root.geometry("400x300")

# إنشاء واجهة إدخال النص
text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=40)
text_entry.pack(pady=18)

# إنشاء الأزرار
play_button = tk.Button(root, text="play", command=play_text) #زر التشغيل
play_button.pack(pady=5)

clear_button = tk.Button(root, text="set", command=clear_text)  # تعديل النص إلى "مسح"
clear_button.pack(pady=5)

# زر الخروج من البرنامج 
exit_button = tk.Button(root, text="Exit", command=exit_app, bg="red") 
exit_button.pack(pady=5)

# تشغيل التطبيق
root.mainloop()
