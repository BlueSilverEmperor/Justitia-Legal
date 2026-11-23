import customtkinter 
import ollama
import threading
from collections import deque
import mysql.connector


prompt_history=deque(maxlen=100)   

##AI##
def get_law_context(query_text, country_name):
    """Searches your MySQL database for matching laws."""
    try:
        if not country_name:
            return "Please select a country from the menu first."
        table_name = f"law_{country_name.lower().replace(' ', '_')}"
        db = mysql.connector.connect(
            host="localhost", user="root", password="Sridhar1234$", database="law"
        )
        cursor = db.cursor()
        search_term = f"%{query_text}%"
        sql = f"SELECT title, description FROM {table_name} WHERE title LIKE %s OR description LIKE %s LIMIT 3"
        cursor.execute(sql, (search_term, search_term))
        results = cursor.fetchall()
        db.close()
        if not results: return f"No relevant laws found in database for {country_name}."
        return "\n\n".join([f"TITLE: {r[0]}\nCONTENT: {r[1]}" for r in results])
    except Exception as e:
        return f"Database Error: {str(e)}"

def get_response(user_input):
    selected_country = country_search_var.get()
    context = get_law_context(user_input, selected_country)
    system_prompt = (
        f"You are an expert Legal Consultant specialized in the Law of {selected_country if selected_country else 'the selected country'}. "
        "Your goal is to INTERPRET the provided database context to help the user. "
        "FOLLOW THESE RULES:\n"
        "1. Start by summarizing the specific Article/Section found in the database.\n"
        "2. Explain what it means in simple terms (Interpretation).\n"
        "3. If the user's question isn't fully covered by the database, use the database context as a starting point and explain what is missing.\n"
        "4. Always cite the title of the law found in the context.\n\n"
        f"CONTEXT FROM MYSQL:\n{context}"
    )
    response = ollama.chat(model="mistral-nemo", messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_input}
    ])
    return response['message']['content']

def on_submit():
    user_input = e1.get()
    if not user_input.strip():
        return
    b1.configure(state="disabled", text="Thinking...")
    def run_ai_task():
        
        response = get_response(user_input)
        
        
        prompt_history.append(f"YOU: {user_input}")
        prompt_history.append(f"AI: {response}\n{'-'*60}")
        
        
        full_chat = "\n\n".join(prompt_history)
        
        
        r1.after(0, lambda: text_box.delete("0.0", "end"))
        r1.after(0, lambda: text_box.insert("end", full_chat))
        r1.after(0, lambda: text_box.see("end")) 
        r1.after(0, lambda: b1.configure(state="normal", text="Submit"))
        r1.after(0, lambda: e1.delete(0, "end"))     
    threading.Thread(target=run_ai_task, daemon=True).start()

##Gui##
r1=customtkinter.CTk()
r1.geometry("900x800")
r1.update()
customtkinter.set_default_color_theme(r"C:\Users\sridh\OneDrive\Desktop\prj\Justitia\Untitled-1.json")
r1.title("Law")
r1.after(0, lambda: r1.state('zoomed'))

#Menu Sidebar Implementation
r1.grid_columnconfigure(1, weight=1)
r1.grid_rowconfigure(0, weight=1)
sidebar_frame = customtkinter.CTkFrame(r1, width=200, corner_radius=20)
sidebar_frame.grid(row=0, column=0,padx=10,pady=10, sticky="nsew")
logo_label = customtkinter.CTkLabel(sidebar_frame, text="My App", font=customtkinter.CTkFont(size=20, weight="bold", family="Times New Roman"))
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
btn_1 = customtkinter.CTkButton(sidebar_frame, text="Exit", anchor="w", command=lambda: r1.destroy(),font=("Times New Roman", 16))
btn_1.grid(row=1, column=0, padx=20, pady=10)
btn_2 = customtkinter.CTkButton(sidebar_frame, text="Settings", anchor="w",font=("Times New Roman", 16))
btn_2.grid(row=2, column=0, padx=20, pady=10)
mode_menu = customtkinter.CTkOptionMenu(sidebar_frame, values=["Dark", "Light", "System"],
                               command=lambda m: customtkinter.set_appearance_mode(m),font=("Times New Roman", 16))
mode_menu.grid(row=3, column=0, padx=20, pady=(100, 20))
search_label = customtkinter.CTkLabel(sidebar_frame, text="Select Country:", font=("Times New Roman", 14))
search_label.grid(row=4, column=0, padx=20, pady=(10, 0), sticky="w")
country_search_var = customtkinter.StringVar()
country_search_entry = customtkinter.CTkEntry(sidebar_frame, textvariable=country_search_var, placeholder_text="Search country...", font=("Times New Roman", 14))
country_search_entry.grid(row=5, column=0, padx=20, pady=(5, 10), sticky="ew")
country_list_frame = customtkinter.CTkScrollableFrame(sidebar_frame, width=180, height=250)
country_list_frame.grid(row=6, column=0, padx=20, pady=10, sticky="nsew")
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 
             'Antigua And Barbuda', 'Argentina', 'Armenia', 'Australia', 
             'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 
             'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan',
             'Bolivia', 'Bosnia Herzegovina', 'Botswana', 'Brazil', 'Brunei', 
             'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 
             'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 
             'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 
             'Cote Divoire', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 
             'Democratic Republic Of The Congo', 'Denmark', 'Djibouti', 
             'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 
             'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 
             'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 
             'Georgia', 'German Federal Republic', 'Ghana', 'Greece', 
             'Grenada', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Hungary',
             'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 
             'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 
             'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyz Republic', 
             'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 
             'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 
             'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Malta', 
             'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 
             'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 
             'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 
             'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 
             'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 
             'Papua New Guinea', 'Paraguay', 'Peoples Republic Of Korea', 
             'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 
             'Republic Of Korea', 'Romania', 'Russia', 'Rwanda', 'Samoa',
             'Sao Tome And Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
             'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 
             'Slovenia', 'Socialist Republic Of Vietnam', 'Solomon Islands',
             'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 
             'St Kitts And Nevis', 'St Lucia', 'St Vincent And The Grenadines',
             'Sudan', 'Surinam', 'Swaziland', 'Sweden', 'Switzerland', 
             'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo',
             'Tonga', 'Trinidad And Tobago', 'Tunisia', 'Turkey', 
             'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
             'United Arab Emirates', 'United Kingdom',
             'United States Of America', 'Uruguay', 'Usa', 'Uzbekistan', 
             'Vanuatu', 'Venezuela', 'Yemen', 'Zambia', 'Zimbabwe']
country_buttons = []

def select_country(country):
    print(f"Selected country: {country}")
    country_search_var.set(country)
    

def update_list(*args):
    search_term = country_search_var.get().lower()
    for btn in country_buttons:
        btn.destroy()
    country_buttons.clear()
    
    filtered_countries = [c for c in countries if search_term in c.lower()]
    for country in filtered_countries:
        btn = customtkinter.CTkButton(country_list_frame, text=country, 
                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                      hover_color=("white", "gray30"), anchor="w",
                                      command=lambda c=country: select_country(c))
        btn.pack(fill="x", padx=5, pady=2)
        country_buttons.append(btn)

country_search_var.trace_add("write", update_list)
update_list() 

def toggle_country_lock():
    current_text = lock_country_btn.cget("text")
    if current_text == "Lock Country":
        country_search_entry.configure(state="disabled")
        for btn in country_buttons:
            btn.configure(state="disabled")
        lock_country_btn.configure(text="Change Country")
    else:
        country_search_entry.configure(state="normal")
        for btn in country_buttons:
            btn.configure(state="normal")
        lock_country_btn.configure(text="Lock Country")

lock_country_btn = customtkinter.CTkButton(sidebar_frame, text="Lock Country", command=toggle_country_lock, font=("Times New Roman", 14))
lock_country_btn.grid(row=7, column=0, padx=20, pady=(10, 20), sticky="ew")

model_label = customtkinter.CTkLabel(sidebar_frame, text="Model: mistral-nemo", font=("Times New Roman", 12), text_color="gray50")
model_label.grid(row=8, column=0, padx=20, pady=(0, 20), sticky="s")
#End of Menu Sidebar Implementation

#Main Frame And search bar implementation
main_frame = customtkinter.CTkFrame(r1, corner_radius=20)
main_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure((0, 4), weight=1) 
l1 = customtkinter.CTkLabel(main_frame, text="Laws", font=("Times New Roman", 40))
l1.grid(row=1, column=0, pady=(0, 20)) # Put in column 0
e1 = customtkinter.CTkEntry(
    main_frame, 
    width=1000,
    height=80, 
    placeholder_text="How Can I help you?", 
    font=("Times New Roman", 25), 
    corner_radius=10
)
e1.grid(row=2, column=0, padx=40, pady=20) 
b1= customtkinter.CTkButton(
    main_frame,
    text="Submit",
    command=on_submit,
    width=200,
    corner_radius=10,
    height=50,
    font=("Times New Roman", 20)
)
b1.grid(row=3, column=0, padx=40, pady=20)  
#End of Main Frame And search bar implementation

res_frame = customtkinter.CTkFrame(main_frame, corner_radius=10)
res_frame.grid(row=4, column=0, padx=20, pady=20, sticky="nsew")
res_frame.grid_columnconfigure(0, weight=10) 
text_box = customtkinter.CTkTextbox(res_frame, font=("Times New Roman", 20), corner_radius=10,height=400)
text_box.grid(row=0, column=0, padx=20, pady=20, sticky="nsew") 
scr1= customtkinter.CTkScrollbar(res_frame, orientation="vertical", command=text_box.yview)
scr1.grid(row=0, column=1, sticky="ns")
text_box.configure(yscrollcommand=scr1.set)






r1.mainloop()