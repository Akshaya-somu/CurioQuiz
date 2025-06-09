from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import random
import spacy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime 
from collections import defaultdict


app = Flask(__name__)
app.secret_key = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///curioquiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

nlp = spacy.load("en_core_web_sm")

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)



class UserAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question = db.Column(db.Text, nullable=False)
    selected_answer = db.Column(db.String(255), nullable=True)
    correct_answer = db.Column(db.String(255), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class MCQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    options = db.Column(db.Text, nullable=False)  # Stored as '||' separated string
    answer = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    difficulty = db.Column(db.String(10), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if User.query.filter_by(username=username).first():
            flash('Username already exists. Please choose another.', 'danger')
            return redirect(url_for('signup'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))

        login_user(user)
        flash('Logged in successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

@app.route('/generate', methods=['GET', 'POST'])
@login_required
def generate():
    questions = []

    if request.method == 'POST':
        text = request.form['text']
        difficulty = request.form.get('difficulty')


        doc = nlp(text)

        print("📥 Text received:", text)
        print("🎯 Difficulty selected:", difficulty)

        entities = [ent.text for ent in doc.ents if ent.label_ in ["PERSON", "ORG", "GPE", "LOC"]]
        entities = list(set(entities))
        print("🧠 Entities extracted:", entities)

        sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
        print("🧾 Sentences:", sentences)

        for sent in sentences:
            sent_doc = nlp(sent)
            sent_entities = [ent.text for ent in sent_doc.ents if ent.label_ in ["PERSON", "ORG", "GPE", "LOC"]]
            sent_entities = list(set(sent_entities))

            if sent_entities:
                answer = random.choice(sent_entities)
                question_text = sent.replace(answer, "______", 1)

                fake_pool = [opt for opt in entities if opt != answer]
                num_options = 3 if difficulty == "easy" else 4 if difficulty == "medium" else 5

                fake_options = random.sample(fake_pool, min(num_options, len(fake_pool)))
                options = fake_options[:num_options - 1] + [answer]
                random.shuffle(options)

                print(f"❓ Question: {question_text}")
                print(f"✅ Options: {options}")
                print(f"🔐 Answer: {answer}")

                questions.append({
                    'question': question_text,
                    'options': options,
                    'answer': answer
                })

                # Save to DB
                mcq = MCQ(
                    question=question_text,
                    options="||".join(options),
                    answer=answer,
                    user_id=current_user.id,
                    difficulty=difficulty
                )
                db.session.add(mcq)

        db.session.commit()

        if not questions:
            flash('No questions could be generated from the input text.', 'warning')

    # Fetch all MCQs for display
    mcqs = MCQ.query.filter_by(user_id=current_user.id).all()

    return render_template('generate.html', questions=questions, mcqs=mcqs)

@app.route('/save_mcqs', methods=['POST'])
@login_required
def save_mcqs():
    results = []
    question_keys = [key for key in request.form.keys() if key.startswith('question_')]
    num_questions = len(question_keys)

    for i in range(1, num_questions + 1):
        question = request.form.get(f'question_{i}')
        correct_answer = request.form.get(f'correct_answer_{i}')
        user_answer = request.form.get(f'answer_{i}')
        is_correct = (user_answer == correct_answer) if user_answer else False

        # ✅ Save to database
        ua = UserAnswer(
            user_id=current_user.id,
            question=question,
            selected_answer=user_answer,
            correct_answer=correct_answer,
            is_correct=is_correct
        )
        db.session.add(ua)

        results.append({
            'question': question,
            'correct_answer': correct_answer,
            'user_answer': user_answer,
            'is_correct': is_correct
        })

    db.session.commit()

    return render_template('results.html', results=results)

@app.route('/history')
@login_required
def history():
    # Optional filters from query parameters
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    difficulty = request.args.get('difficulty')
    print("Start Date from form:", start_date)
    print("End Date from form:", end_date)
    print("Difficulty from form:", difficulty)

    # Base query for MCQs created by the user
    query = MCQ.query.filter_by(user_id=current_user.id)

    # Apply filters if present
    if difficulty:
        query = query.filter(MCQ.difficulty == difficulty)
    if start_date:
        query = query.filter(MCQ.created_at >= datetime.strptime(start_date, '%Y-%m-%d'))

    if end_date:
        query = query.filter(MCQ.created_at <= datetime.strptime(end_date, '%Y-%m-%d'))


    mcqs = query.order_by(MCQ.created_at.desc()).all()

    # Group by creation date
    grouped_mcqs = defaultdict(list)
    for mcq in mcqs:
        date_str = mcq.created_at.strftime('%Y-%m-%d')
        grouped_mcqs[date_str].append(mcq)

    # Sort dates descending
    sorted_dates = sorted(grouped_mcqs.keys(), reverse=True)

    return render_template('history.html', grouped_mcqs=grouped_mcqs, sorted_dates=sorted_dates)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
