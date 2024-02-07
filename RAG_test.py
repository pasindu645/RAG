import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    tokens = word_tokenize(text.lower())  # Tokenize and lowercase
    stopwords_removed = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    return stopwords_removed

landmark_corpus = [
    "The Eiffel Tower is a wrought-iron lattice tower located on the Champ de Mars in Paris.",
    "The Statue of Liberty is a colossal neoclassical sculpture on Liberty Island in New York Harbor.",
    " chathura is work in hatch building 4th floor"
    # Add more landmark descriptions
]

preprocessed_landmarks = [preprocess_text(description) for description in landmark_corpus]

def retrieve_landmark(question, landmark_corpus):
    question_tokens = preprocess_text(question)
    best_match = None
    max_overlap = 0
    
    for description in landmark_corpus:
        overlap = len(set(description) & set(question_tokens))
        if overlap > max_overlap:
            best_match = description
            max_overlap = overlap
    
    return best_match

question = "where is chathura?"
retrieved_description = retrieve_landmark(question, preprocessed_landmarks)
print("Retrieved Description:", " ".join(retrieved_description))


def generate_answer(question, retrieved_description):
    return " ".join(retrieved_description)

answer = generate_answer(question, retrieved_description)
print("Generated Answer:", answer)

