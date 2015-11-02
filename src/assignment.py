from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('assignment.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
  if request.method == 'POST':
    print request.form
    name = request.form['name']
    return "Hello %s" %  name
  else:
    page = '''
    <html><body>
      <form action="" method="post" name="form">
        <label for="name">Team: </label>
        <input type="text" name="name" id="name"/>
        <input type="submit" name="submit" id="submit"/>
      </form>
      </body><html>'''

    return page

@app.route('/bpl/')
def bplLink():
  teamName = ['AFC Bournemouth', 'Arsenal', 'Aston Villa', 'Chelsea',
  'Crystal Palace', 'Everton', 'Leicester City', 'Liverpool', 'Manchester City',
  'Manchester United', 'Newcastle United', 'Norwich City', 'Southampton',
  'Stoke City', 'Sunderland', 'Swansea City', 'Tottenham Hotspur',
  'Watford', 'West Bromwich Albion', 'West Ham United']
  return render_template('bplteams.html', teamName=teamName)

@app.route('/bpl/<team>')
def team(team):
  index = int(request.args.get('index', 0))
  stadium = ['Dean Court', 'Emirates Stadium', 'Villa Park', 'Stamford Bridge',
  'Selhurst Park', 'Goodison Park', 'King Power Stadium', 'Anfield',
  'Etihad Stadium', 'Old Trafford', 'St James Park', 'Carrow Road',
  'St Marys Stadium', 'Britannia Stadium', 'Stadium of Light',
  'Liberty Stadium', 'White Hart Lane', 'Vicarage Road', 'The Hawthorns',
  'Boleyn Ground']
  badge = ['bournemouth.png', 'arsenal.png', 'aston-villa.png', 'chelsea.png',
  'crystal-palace.png', 'everton.png', 'leicester.png', 'liverpool.png',
  'man-city.png', 'man-united.png', 'newcastle.png', 'norwich.png',
  'southampton.png', 'stoke.png', 'sunderland.png', 'swansea.png',
  'tottenham.png', 'watford.png', 'west-brom.png', 'west-ham.png']
  capacity = ['11,464', '60,260', '42,660', '41,798', '25,073', '39,571',
  '32,312', '44,742', '55,097', '75,653', '52,338', '27,010', '32,505',
  '27,740', '48,707', '20,909', '36,284', '21,500', '26,850', '35,345']
  manager = ['Eddie Howe', 'Arsene Wenger', 'Kevin MacDonald (caretaker)',
  'Jose Mourinho', 'Alan Pardew', 'Roberto Martinez', 'Claudio Ranieri',
  'Jurgen Klopp', 'Manuel Pellegrini', 'Louis van Gaal', 'Steve McClaren',
  'Alex Neil', 'Ronald Koeman', 'Mark Hughes', 'Sam Allardyce', 'Garry Monk',
  'Mauricio Pochettino', 'Quique Flores', 'Tony Pulis', 'Slaven Bilic']
  nickname = ['Cherries', 'Gunners', 'Villans', 'Blues', 'Eagles', 'Toffees',
  'Foxes', 'Reds', 'City', 'Red Devils', 'Magpies', 'Canaries', 'Saints',
  'Potters', 'Black Cats', 'Swans', 'Spurs', 'Hornets', 'Baggies', 'Irons']
  return render_template('details.html', team=team, stadium=stadium,
  badge=badge, capacity=capacity, manager=manager, nickname=nickname,
  index=index)

@app.route('/admin')
def members():
  return redirect(url_for('index'))

@app.route('/upload', methods=['POST', 'GET'])
def memberspage():
  if request.method == 'POST':
    f = request.files['datafile']
    f.save('static/uploads/image.png')
    return '<p>Hi</p><img src="'+url_for('static', filename='uploads/image.png')+'"/>'
  else:
    page='''
    <html>
    <head><link rel="stylesheet" type="text/css"
    href="/static/style.css"/></head>
    <body>
    <div id="header">
    <h1>BPL Teams</h1>
    <div id="nav">
    <ul id="navMenu">
      <li><a href="/">Home</a></li>
      <li><a href="/bpl">BPL Teams</a></li>
      <li><a href="/upload">Upload</a></li>
      </ul>
     </div>
    </div>
    <form action="" id="uploadform"  method="post" name="form" enctype="multipart/form-data">
    <input type="file" name="datafile" />
    <input type="submit" name="submit" id="submit"/>
    </form>
    <div id="footer">
    <h1>Liam Rawsthorne</h1>
    <div id="nav">
    <ul id="navMenu">
    <li><a href="/">Home</a></li>
    <li><a href="/bpl">BPL Teams</a></li>
    <li><a href="/upload">Upload</a></li>
    </ul>
    </div>
    </div>
    </body>
    </html>
    '''

    return page, 200

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html') 

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)



