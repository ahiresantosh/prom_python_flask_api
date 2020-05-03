from flask import render_template, request, redirect
from app import app, db
from app.models import Entry
from promapi import prometheus

jedi = "of the jedi"

@app.route('/')
@app.route('/index')
def index():
    # entries = [
    #     {
    #         'id' : 1,
    #         'title': 'test title 1',
    #         'description' : 'test desc 1',
    #         'status' : True
    #     },
    #     {
    #         'id': 2,
    #         'title': 'test title 2',
    #         'description': 'test desc 2',
    #         'status': False
    #     }
    # ]
    entries = Entry.query.all()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        description = form.get('description')
        if not title or description:
            entry = Entry(title = title, description = description)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')

    return "of the jedi"

@app.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            return render_template('update.html', entry=entry)

    return "of the jedi"

@app.route('/update', methods=['POST'])
def update():
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return "of the jedi"



@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return "of the jedi"

@app.route('/turn/<int:id>')
def turn(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            entry.status = not entry.status
            db.session.commit()
        return redirect('/')

    return "of the jedi"


@app.route('/rangequery', methods=['POST'])
def rangequery():
    # Set Prometheus Endpoint
    prometheus.set_endpoint("http://localhost", 9090)

    if request.method == 'POST':
        form = request.form
        jobname = form.get('jobname')

        #if not jobname:
        # result = prometheus.query_range("rate(process_cpu_seconds_total{job=\""+jobname+"\"}[5m])",
        #                                 start=1588501129,
        #                                 end=1588508129, step=60)
        result = prometheus.query_range("rate(prometheus_sd_kubernetes_events_total{event=\"" + jobname + "\"}[5m])",
                                        start=1588501129,
                                        end=1588508129, step=60)
        print(jobname)
        print(result)
        #return redirect('/')
        return str(result)

    return "of the jedi"

# @app.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"