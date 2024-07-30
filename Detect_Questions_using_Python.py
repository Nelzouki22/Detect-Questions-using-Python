import nltk

# تحميل الموارد اللازمة
nltk.download('punkt')

def is_question(sentence):
    # تقسيم الجملة إلى كلمات
    words = nltk.word_tokenize(sentence)
    
    # عادة ما تبدأ الأسئلة بواحد من هذه الكلمات
    question_words = {'what', 'when', 'where', 'who', 'whom', 'which', 'why', 'how', 'is', 'are', 'do', 'does', 'did', 'can', 'could', 'would', 'will', 'shall', 'should'}
    
    # التحقق من أول كلمة في الجملة
    if words[0].lower() in question_words:
        return True
    # التحقق مما إذا كانت الجملة تنتهي بعلامة استفهام
    elif sentence.strip().endswith('?'):
        return True
    return False

# اختبار الكود
sentences = [
    "What is your name?",
    "This is a statement.",
    "Are you coming to the party?",
    "It's raining today."
]

for sentence in sentences:
    if is_question(sentence):
        print(f"'{sentence}' is a question.")
    else:
        print(f"'{sentence}' is not a question.")

