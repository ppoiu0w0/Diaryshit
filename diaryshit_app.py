import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import time
import os

root = tk.Tk()
root.title("Diaryshit")
root.minsize(400, 500)

root.iconbitmap(r"C:\\Users\\ryu0w\\Downloads\\diary.ico")

style = ttk.Style(root)
style.theme_use('clam')

style.configure('TButton', foreground='black', background='white', font=('Helvetica', 10))
style.configure('TLabel', foreground='black', background='white', font=('Helvetica', 10))
style.configure('TCombobox', foreground='black', background='white', font=('Helvetica', 10))

root.configure(bg="white")

DIARY_DIRECTORY = "C:\\Users\\ryu0w\\Diary"
os.makedirs(DIARY_DIRECTORY, exist_ok=True)

def open_diary_folder():
    try:
        os.startfile(DIARY_DIRECTORY)
    except Exception as e:
        messagebox.showerror("Error", f"파일 경로가 수정/삭제되었습니다. 'C:\\Users\\ryu0w' 경로에 'Diary' 폴더를 생성해주세요.\n{e}")

def save_to_file():
    mood = mood_combo.get()
    diary_entry = diary_text.get("1.0", tk.END).strip()

    if not mood:
        messagebox.showwarning("정보 미기입", "오늘의 기분을 선택해주세요.")
        return

    if not diary_entry:
        messagebox.showwarning("정보 미기입", "일기를 한 글자라도 입력해주세요.")
        return

    default_filename = time.strftime('%Y-%m-%d') + "_diary.txt"
    file_path = filedialog.asksaveasfilename(
        title="Save Diary Entry",
        initialdir=DIARY_DIRECTORY,
        initialfile=default_filename,
        filetypes=[("Text Files", "*.txt")],
        defaultextension=".txt"
    )

    if file_path:
        try:
            current_time = time.strftime('%Y.%m.%d')
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"작성 시각: {current_time}\n\n")
                file.write(f"오늘의 기분: {mood}\n\n")
                file.write(f"일기 >> \n{diary_entry}\n")
            messagebox.showinfo("성공", f"파일경로: \n{file_path}")

            try:
                os.startfile(file_path)
            except Exception as e:
                messagebox.showerror("Error", f"일기 파일을 열지 못했습니다.\n{e}")
            root.quit()
        except (IOError, OSError) as e:
            messagebox.showerror("Error", f"일기 파일을 저장하지 못했습니다.\n{e}")

button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=20)

mood_label = ttk.Label(root, text="오늘의 기분")
mood_label.pack(pady=10)
mood_combo = ttk.Combobox(root, values=["기쁨", "슬픔", "화남", "신남", "피곤함", "그저 그럼", "짜증남", "서운함", "기타(긍정적)", "기타(부정적)", "기타(중립)", "기타(X)"], state="readonly", width=28)
mood_combo.pack(pady=5)

diary_label = ttk.Label(root, text="오늘 있었던 일을 기록해 주세요:")
diary_label.pack(pady=10)
diary_text = tk.Text(root, width=40, height=10, wrap="word", bg="white", fg="black", insertbackground="black")
diary_text.configure(spacing1=10)
diary_text.pack(pady=5)

save_button = ttk.Button(button_frame, text="일기 저장하기", command=save_to_file)
save_button.grid(row=0, column=0, padx=10)
open_button = ttk.Button(button_frame, text="일기 보기", command=open_diary_folder)
open_button.grid(row=0, column=1, padx=10)

root.mainloop()
