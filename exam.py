# --------------------------------------------------
# 國中資訊三年級期中考_python
# Streamlit 線上測驗系統
# 功能：
# 1. 單選題 20 題
# 2. 輸入班級、座號、姓名
# 3. 同一「班級＋座號」最多作答 2 次
# 4. 自動輸出 results.xlsx 成績檔
# --------------------------------------------------

import streamlit as st
import pandas as pd
from datetime import datetime
import os

# ===== 基本設定 =====
st.set_page_config(
    page_title="國中資訊三年級期中考_python",
    layout="centered"
)

st.title("國中資訊三年級期中考_python")
st.caption("請確實填寫班級、座號、姓名。同一座號最多可作答 2 次。")

RESULT_FILE = "results.xlsx"
MAX_ATTEMPTS = 2

# ===== 題庫（20 題）=====
questions = [
    {
        "q": "1. Python 中用來顯示文字到畫面的指令是？",
        "options": ["input()", "print()", "show()", "write()"],
        "ans": "print()"
    },
    {
        "q": "2. 下列哪一個是正確的變數命名方式？",
        "options": ["1name", "my-name", "my_name", "my name"],
        "ans": "my_name"
    },
    {
        "q": "3. 執行下列程式後，畫面會顯示什麼？ print(5 + 3)",
        "options": ["5+3", "8", "53", "錯誤"],
        "ans": "8"
    },
    {
        "q": "4. input() 指令的主要功能是？",
        "options": ["顯示文字", "讓使用者輸入資料", "輸出結果", "計算數值"],
        "ans": "讓使用者輸入資料"
    },
    {
        "q": "5. 下列哪一個屬於整數（int）型態？",
        "options": ["3.5", "'7'", "7", "True"],
        "ans": "7"
    },
    {
        "q": "6. 如果 a = 10，下列哪一行可以讓 a 變成 15？",
        "options": ["a == 15", "a + 5", "a = a + 5", "a += 0"],
        "ans": "a = a + 5"
    },
    {
        "q": "7. 用來判斷條件是否成立的指令是？",
        "options": ["for", "if", "print", "range"],
        "ans": "if"
    },
    {
        "q": "8. 條件不成立時要執行的指令是？",
        "options": ["elif", "else", "while", "break"],
        "ans": "else"
    },
    {
        "q": "9. 下列哪一個是正確的比較運算子？",
        "options": ["=", "==", "=>", "=<"],
        "ans": "=="
    },
    {
        "q": "10. for 迴圈的主要用途是？",
        "options": ["判斷條件", "重複執行程式", "輸入資料", "顯示結果"],
        "ans": "重複執行程式"
    },
    {
        "q": "11. range(3) 會產生哪些數值？",
        "options": ["1,2,3", "0,1,2", "0,1,2,3", "3"],
        "ans": "0,1,2"
    },
    {
        "q": "12. 下列哪一項是清單（list）的正確寫法？",
        "options": ["(1,2,3)", "{1,2,3}", "[1,2,3]", "<1,2,3>"],
        "ans": "[1,2,3]"
    },
    {
        "q": "13. list.append(5) 的作用是？",
        "options": ["刪除 5", "將 5 加入清單", "取得第 5 個元素", "排序清單"],
        "ans": "將 5 加入清單"
    },
    {
        "q": "14. 若 lst = [10, 20, 30]，lst[1] 的值是？",
        "options": ["10", "20", "30", "錯誤"],
        "ans": "20"
    },
    {
        "q": "15. while 迴圈通常在什麼情況下使用？",
        "options": ["次數已知", "依條件反覆執行", "只執行一次", "不能停止"],
        "ans": "依條件反覆執行"
    },
    {
        "q": "16. # 在 Python 中的功能是？",
        "options": ["除法", "註解", "結束程式", "輸入資料"],
        "ans": "註解"
    },
    {
        "q": "17. True 與 False 屬於哪一種資料型態？",
        "options": ["int", "str", "bool", "list"],
        "ans": "bool"
    },
    {
        "q": "18. 將數字 12 轉成字串的指令是？",
        "options": ["int(12)", "str(12)", "bool(12)", "float(12)"],
        "ans": "str(12)"
    },
    {
        "q": "19. len([1,2,3,4]) 的結果是？",
        "options": ["3", "4", "5", "錯誤"],
        "ans": "4"
    },
    {
        "q": "20. Python 程式通常依什麼順序執行？",
        "options": ["由下往上", "由右往左", "由上往下", "隨機"],
        "ans": "由上往下"
    }
]

# ===== 學生資料 =====
st.subheader("學生資料")
class_name = st.text_input("班級")
seat_no = st.text_input("座號")
name = st.text_input("姓名")

# ===== 作答次數檢查 =====
if class_name and seat_no and os.path.exists(RESULT_FILE):
    df_exist = pd.read_excel(RESULT_FILE)
    attempts = len(
        df_exist[
            (df_exist["班級"] == class_name) &
            (df_exist["座號"].astype(str) == seat_no)
        ]
    )
    if attempts >= MAX_ATTEMPTS:
        st.error("此座號已達最大作答次數（2 次），無法再次作答。")
        st.stop()

# ===== 題目區 =====
st.subheader("測驗題目")
answers = []

for item in questions:
    ans = st.radio(item["q"], item["options"], key=item["q"])
    answers.append(ans)

# ===== 送出測驗 =====
if st.button("送出測驗"):
    if not class_name or not seat_no or not name:
        st.error("請先填寫完整學生資料。")
    else:
        score = sum(
            1 for i, item in enumerate(questions)
            if answers[i] == item["ans"]
        )

        result = {
            "班級": class_name,
            "座號": seat_no,
            "姓名": name,
            "分數": score,
            "作答時間": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        if os.path.exists(RESULT_FILE):
            df = pd.read_excel(RESULT_FILE)
            df = pd.concat([df, pd.DataFrame([result])], ignore_index=True)
        else:
            df = pd.DataFrame([result])

        df.to_excel(RESULT_FILE, index=False)

        st.success(f"作答完成！你的分數是 {score} / 20")
        st.info("同一座號最多可作答 2 次。")