import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load expanded dataset
data = pd.read_csv("dataset.csv")

# Preprocess: replace semicolons with spaces for better tokenization
data["skills"] = data["skills"].str.replace(";", " ")

# Combine features into a single text column
X = data["skills"] + " " + data["interest"] + " " + data["education"]
y = data["career"]

# Convert text to numeric features using TF-IDF (better than CountVectorizer)
vectorizer = TfidfVectorizer(
    lowercase=True,
    ngram_range=(1, 2),  # Use unigrams and bigrams
    max_features=500,
    min_df=1
)
X_vec = vectorizer.fit_transform(X)

# Encode career labels
encoder = LabelEncoder()
y_enc = encoder.fit_transform(y)

# Train classifier with better parameters
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=20,
    min_samples_split=2,
    random_state=42,
    class_weight='balanced'  # Handle imbalanced data
)
model.fit(X_vec, y_enc)

# Prediction function
def predict_career(skills, interest, education):
    # Preprocess input same way as training data
    skills_clean = skills.replace(",", " ").replace(";", " ")
    text = skills_clean + " " + interest + " " + education
    vec = vectorizer.transform([text])
    
    # Get prediction with probability
    pred = model.predict(vec)
    proba = model.predict_proba(vec)
    
    # Get top prediction
    career = encoder.inverse_transform(pred)[0]
    confidence = proba.max()
    
    return career
