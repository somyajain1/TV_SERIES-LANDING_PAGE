from flask import Flask, render_template, abort
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change this in production
csrf = CSRFProtect(app)

# Sample TV series data with images and detailed summaries
tv_series = [
    {
        "id": "breaking-bad",
        "title": "Breaking Bad",
        "description": "A high school chemistry teacher turned methamphetamine manufacturer.",
        "image": "https://image.tmdb.org/t/p/w500/ggFHVNu6YYI5L9pCfOacjizRGt.jpg",
        "summary": """Breaking Bad follows protagonist Walter White, a chemistry teacher who lives in New Mexico with his wife and teenage son who has cerebral palsy. White is diagnosed with Stage III cancer and given a prognosis of two years left to live. With a new sense of fearlessness based on his medical prognosis, and a desire to secure his family's financial security, White chooses to enter a dangerous world of drugs and crime and ascends to power in this world. The series explores how a fatal diagnosis such as White's releases a typical man from the daily concerns and constraints of normal society and follows his transformation from mild family man to a kingpin of the drug trade.""",
        "seasons": 5,
        "rating": "9.5/10",
        "genre": ["Crime", "Drama", "Thriller"]
    },
    {
        "id": "stranger-things",
        "title": "Stranger Things",
        "description": "A group of kids encounter supernatural forces and secret government exploits.",
        "image": "https://image.tmdb.org/t/p/w500/49WJfeN0moxb9IPfGn8AIqMGskD.jpg",
        "summary": """In a small town where everyone knows everyone, a peculiar incident starts a chain of events that leads to the disappearance of a child, which begins to tear at the fabric of an otherwise peaceful community. Dark government agencies and seemingly malevolent supernatural forces converge on the town, while a few locals begin to understand that there's more going on than meets the eye.""",
        "seasons": 4,
        "rating": "8.7/10",
        "genre": ["Drama", "Fantasy", "Horror"]
    },
    {
        "id": "the-crown",
        "title": "The Crown",
        "description": "Chronicles the life of Queen Elizabeth II from the 1940s to modern times.",
        "image": "https://image.tmdb.org/t/p/w500/7IbRNKqhIZVZ7WVL1VXfEsqR5jl.jpg",
        "summary": """This drama follows the political rivalries and romance of Queen Elizabeth II's reign and the events that shaped the second half of the 20th century. As the decades pass, personal intrigues, romances, and political rivalries are revealed that played a big role in events that shaped the later years of the American century.""",
        "seasons": 6,
        "rating": "8.7/10",
        "genre": ["Biography", "Drama", "History"]
    },
    {
        "id": "the-mandalorian",
        "title": "The Mandalorian",
        "description": "A lone bounty hunter makes his way through the outer reaches of the galaxy.",
        "image": "https://image.tmdb.org/t/p/w500/sWgBv7LV2PRoQgkxwlibdGXKz1S.jpg",
        "summary": """After the stories of Jango and Boba Fett, another warrior emerges in the Star Wars universe. The Mandalorian is set after the fall of the Empire and before the emergence of the First Order. We follow the travails of a lone gunfighter in the outer reaches of the galaxy far from the authority of the New Republic.""",
        "seasons": 3,
        "rating": "8.7/10",
        "genre": ["Action", "Adventure", "Fantasy"]
    },
    {
        "id": "game-of-thrones",
        "title": "Game of Thrones",
        "description": "Noble families fight for control over the mythical lands of Westeros.",
        "image": "https://image.tmdb.org/t/p/w500/u3bZgnGQ9T01sWNhyveQz0wH0Hl.jpg",
        "summary": """Nine noble families fight for control over the lands of Westeros, while an ancient enemy returns after being dormant for millennia. Political and sexual intrigue abound as seven noble families fight for control of the mythical land of Westeros. Friction between the houses leads to full-scale war. All while a very ancient evil awakens in the farthest north.""",
        "seasons": 8,
        "rating": "9.3/10",
        "genre": ["Action", "Adventure", "Drama"]
    },
    {
        "id": "the-office",
        "title": "The Office",
        "description": "A mockumentary on a group of typical office workers at a paper company.",
        "image": "https://image.tmdb.org/t/p/w500/qWnJzyZhyy74gjpSjIXWmuk0ifX.jpg",
        "summary": """The Office is a mockumentary that documents the exploits of a paper supply company in Scranton, Pennsylvania. Made up of head chief Michael Scott, a harmlessly deluded boss who cares about the welfare of his employees while trying to put his own spin on company policy. With an office including the likes of various peers who have their own hangups, The Office takes a look at the lives of its co-workers.""",
        "seasons": 9,
        "rating": "8.9/10",
        "genre": ["Comedy"]
    }
]

@app.route('/')
def index():
    return render_template('index.html', series=tv_series)

@app.route('/show/<show_id>')
def show_details(show_id):
    show = next((show for show in tv_series if show['id'] == show_id), None)
    if show is None:
        abort(404)
    return render_template('show_details.html', show=show)

if __name__ == '__main__':
    app.run(debug=True) 