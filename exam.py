Streamlit 線上測驗：國中資訊科技三年級 Python
功能：學生線上作答 → 依座號輸出 Excel 成績檔
import streamlit as st import pandas as pd from datetime import datetime
st.set_page_config(page_title="Python 線上測驗", layout="centered")
st.title("國中生活科技三年級－Python 單選測驗") st.caption("請輸入基本資料後作答，送出後會記錄成績。")
===== 題庫 =====
questions = [ { "q": "1. Python 用來在畫面上顯示文字的指令是？", "options": ["input()", "print()", "show()", "display()"], "ans": "print()" }, { "q": "2. 下列哪一項是正確的變數命名？", "options": ["2score", "my score", "my_score", "my-score"], "ans": "my_score" }, { "q": "3. 用來讓使用者輸入資料的指令是？", "options": ["print()", "type()", "input()", "write()"], "ans": "input()" }, { "q": "4. 下列哪一項是整數資料型態？", "options": ["3.14", "'10'", "10", "True"], "ans": "10" }, { "q": "5. 判斷條件是否成立時，會使用哪一個指令？", "options": ["for", "while", "if", "print"], "ans": "if" }, { "q": "6. 若條件不成立時要執行的指令為？", "options": ["elif", "else", "then", "do"], "ans": "else" }, { "q": "7. 用來重複執行程式碼的結構是？", "options": ["if", "print", "loop", "for"], "ans": "for" }, { "q": "8. range(5) 會產生哪些數字？", "options": ["1 到 5", "0 到 5", "0 到 4", "1 到 4"], "ans": "0 到 4" }, { "q": "9. 哪一個符號代表相等？", "options": ["=", "==", "!=", ">="], "ans": "==" }, { "q": "10. len() 指令的作用是？", "options": ["加法", "計算長度", "轉換型態", "輸入資料"], "ans": "計算長度" }, { "q": "11. 清單（list）的符號是？", "options": ["{}", "()", "[]", "<>"], "ans": "[]" }, { "q": "12. 下列哪一項可以存放多個資料？", "options": ["int", "float", "list", "bool"], "ans": "list" }, { "q": "13. append() 指令的用途是？", "options": ["刪除資料", "新增資料", "排序資料", "取代資料"], "ans": "新增資料" }, { "q": "14. 若要取得清單第一個元素，索引值為？", "options": ["1", "0", "-1", "2"], "ans": "0" }, { "q": "15. while 迴圈的特色是？", "options": ["固定次數", "依條件重複", "只執行一次", "不能停止"], "ans": "依條件重複" }, { "q": "16. # 在 Python 中代表？", "options": ["除法", "結尾", "註解", "錯誤"], "ans": "註解" }, { "q": "17. True 與 False 屬於哪一種資料型態？", "options": ["int", "string", "bool", "float"], "ans": "bool" }, { "q": "18. 將字串轉成整數的指令是？", "options": ["str()", "float()", "bool()", "int()"], "ans": "int()" }, { "q": "19. 程式發生錯誤時，畫面顯示的訊息稱為？", "options": ["警告", "錯誤訊息", "輸出", "結果"], "ans": "錯誤訊息" }, { "q": "20. Python 程式是一行一行依什麼順序執行？", "options": ["隨機", "由下往上", "由左往右", "由上往下"], "ans": "由上往下" } ]
===== 基本資料 =====
st.subheader("學生資料") seat_no = st.text_input("座號") name = st.text_input("姓名") class_name = st.text_input("班級")
st.subheader("測驗題目") answers = [] for item in questions: ans = st.radio(item["q"], item["options"], key=item["q"]) answers.append(ans)
if st.button("送出測驗"): if not seat_no or not name or not class_name: st.error("請先填寫完整學生資料。") else: score = 0 for i, item in enumerate(questions): if answers[i] == item["ans"]: score += 1
    result = {
        "班級": class_name,
        "座號": seat_no,
        "姓名": name,
        "分數": score,
        "作答時間": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        df = pd.read_excel("results.xlsx")
        df = pd.concat([df, pd.DataFrame([result])], ignore_index=True)
    except:
        df = pd.DataFrame([result])

    df.to_excel("results.xlsx", index=False)

    st.success(f"作答完成！你的分數是 {score} / 20")
    st.info("老師可下載 results.xlsx 查看全班成績。")
