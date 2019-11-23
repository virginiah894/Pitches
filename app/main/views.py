from flask_login import login_required

@main.route('/')
def index():
  @login_required

  return render_template('index.html')