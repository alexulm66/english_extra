import streamlit as st

# Initialize session state to keep track of scores and feedback
if "score" not in st.session_state:
    st.session_state.score = 0
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

def check_answer(user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
        st.session_state.score += 1
        st.session_state.feedback = "Good!"
    else:
        st.session_state.feedback = f"Bad! The correct answer is: {correct_answer}."
    st.session_state.total_questions += 1

def reset_quiz():
    st.session_state.score = 0
    st.session_state.total_questions = 0
    st.session_state.feedback = ""

st.title("Understanding the Text: Exercises")

# Exercise 1: Fill in the Blanks
st.header("Exercise 1: Fill in the Blanks")
blank1 = st.text_input("BRIDGET told John that it's __________.")
if st.button("Submit Exercise 1", key="submit_ex1"):
    check_answer(blank1, "finished")
    st.success(st.session_state.feedback)

# Exercise 2: Multiple Choice
st.header("Exercise 2: Multiple Choice")
user_answer_ex2 = st.radio("Who does Bridget tell not to call her Gigi?", ["John", "Nick", "Hector", "Charley"], key="radio_ex2")
if st.button("Submit Exercise 2", key="submit_ex2"):
    check_answer(user_answer_ex2, "John")
    st.success(st.session_state.feedback)

# Exercise 3: True or False
st.header("Exercise 3: True or False")
user_answer_tf = st.radio("John sent flowers to Bridget.", ["True", "False"], key="radio_ex3")
if st.button("Submit Exercise 3", key="submit_ex3"):
    check_answer(user_answer_tf, "True")
    st.success(st.session_state.feedback)

# Exercise 4: Fill in the Blanks
st.header("Exercise 4: Fill in the Blanks")
blank2 = st.text_input("Hector was Bridget's __________ years ago.")
if st.button("Submit Exercise 4", key="submit_ex4"):
    check_answer(blank2, "pen pal")
    st.success(st.session_state.feedback)

# Exercise 5: Multiple Choice
st.header("Exercise 5: Multiple Choice")
user_answer_ex5 = st.radio("What does Hector want to know?", ["If he can stay", "If Bridget remembers him", "If John is coming", "If Charley is a good boy"], key="radio_ex5")
if st.button("Submit Exercise 5", key="submit_ex5"):
    check_answer(user_answer_ex5, "If he can stay")
    st.success(st.session_state.feedback)

# Exercise 6: True or False
st.header("Exercise 6: True or False")
user_answer_tf2 = st.radio("Bridget is excited about Hector's arrival.", ["True", "False"], key="radio_ex6")
if st.button("Submit Exercise 6", key="submit_ex6"):
    check_answer(user_answer_tf2, "False")
    st.success(st.session_state.feedback)

# Exercise 7: Fill in the Blanks
st.header("Exercise 7: Fill in the Blanks")
blank3 = st.text_input("Bridget's mother sent her a __________ from Argentina.")
if st.button("Submit Exercise 7", key="submit_ex7"):
    check_answer(blank3, "parcel")
    st.success(st.session_state.feedback)

# Exercise 8: Multiple Choice
st.header("Exercise 8: Multiple Choice")
user_answer_ex8 = st.radio("What does Annie think about Hector?", ["He is rude", "He is handsome", "He is old", "He is funny"], key="radio_ex8")
if st.button("Submit Exercise 8", key="submit_ex8"):
    check_answer(user_answer_ex8, "He is handsome")
    st.success(st.session_state.feedback)

# Exercise 9: True or False
st.header("Exercise 9: True or False")
user_answer_tf3 = st.radio("Annie has a dog named Charley.", ["True", "False"], key="radio_ex9")
if st.button("Submit Exercise 9", key="submit_ex9"):
    check_answer(user_answer_tf3, "True")
    st.success(st.session_state.feedback)

# Exercise 10: Fill in the Blanks
st.header("Exercise 10: Fill in the Blanks")
blank4 = st.text_input("The date Hector is coming is __________.")
if st.button("Submit Exercise 10", key="submit_ex10"):
    check_answer(blank4, "November 5th")
    st.success(st.session_state.feedback)

# Exercise 11: Matching
st.header("Exercise 11: Matching")
st.write("Match the character with their description:")
character1 = st.selectbox("Bridget", ["Tall", "Pen Pal", "Mother"], key="match1")
character2 = st.selectbox("John", ["Pen Pal", "Ex-boyfriend", "Dog Owner"], key="match2")
if st.button("Submit Exercise 11", key="submit_ex11"):
    if character1 == "Pen Pal" and character2 == "Ex-boyfriend":
        st.session_state.score += 2
        st.session_state.feedback = "Good!"
    else:
        st.session_state.feedback = "Bad! Correct matches: Bridget - Pen Pal, John - Ex-boyfriend."
    st.session_state.total_questions += 1
    st.success(st.session_state.feedback)

# Exercise 12: Fill in the Blanks
st.header("Exercise 12: Fill in the Blanks")
blank5 = st.text_input("Annie said, 'Oh, Latin Americans!', referring to __________.")
if st.button("Submit Exercise 12", key="submit_ex12"):
    check_answer(blank5, "Hector")
    st.success(st.session_state.feedback)

# Exercise 13: Multiple Choice
st.header("Exercise 13: Multiple Choice")
user_answer_ex13 = st.radio("What does Hector say about his English?", ["It's bad", "It's good", "It's excellent", "It's terrible"], key="radio_ex13")
if st.button("Submit Exercise 13", key="submit_ex13"):
    check_answer(user_answer_ex13, "It's good")
    st.success(st.session_state.feedback)

# Exercise 14: Fill in the Blanks
st.header("Exercise 14: Fill in the Blanks")
blank6 = st.text_input("Bridget is annoyed by John's __________.")
if st.button("Submit Exercise 14", key="submit_ex14"):
    check_answer(blank6, "calls")
    st.success(st.session_state.feedback)

# Exercise 15: Multiple Choice
st.header("Exercise 15: Multiple Choice")
user_answer_ex15 = st.radio("What does Bridget think about men?", ["They are great", "They are annoying", "They are funny", "They are interesting"], key="radio_ex15")
if st.button("Submit Exercise 15", key="submit_ex15"):
    check_answer(user_answer_ex15, "They are annoying")
    st.success(st.session_state.feedback)

# Exercise 16: True or False
st.header("Exercise 16: True or False")
user_answer_tf4 = st.radio("Bridget's birthday is in November.", ["True", "False"], key="radio_ex16")
if st.button("Submit Exercise 16", key="submit_ex16"):
    check_answer(user_answer_tf4, "False")
    st.success(st.session_state.feedback)

# Exercise 17: Fill in the Blanks
st.header("Exercise 17: Fill in the Blanks")
blank7 = st.text_input("Bridget's mother made her a __________.")
if st.button("Submit Exercise 17", key="submit_ex17"):
    check_answer(blank7, "gift")
    st.success(st.session_state.feedback)


# Show the total score
if st.button("Show Results", key="show_results"):
    st.write(f"You got {st.session_state.score} out of {st.session_state.total_questions} correct!")

# Reset button
if st.button("Reset Quiz", key="reset_quiz"):
    reset_quiz()
    st.success("Quiz reset!")
