from url_shorten import app, db
from url_shorten.models import Urls
from url_shorten.forms import UrlForm
from flask import redirect, render_template, request, url_for, flash
from datetime import timedelta, datetime
import string
import random


# generate shorter url
def generate_short_url():
    chars = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_chars = random.choices(chars, k=7)
        rand_chars = "".join(rand_chars)
        short_url = Urls.query.filter_by(short=rand_chars).first()
        if not short_url:
            return rand_chars


@app.route('/', methods=['POST', 'GET'])
def home():
    # Check for expiries
    all_saved_urls = Urls.query.all()
    for url in all_saved_urls:
        url_date_time = url.expiry_date_time
        if url_date_time:
            if url_date_time <= datetime.now().replace(microsecond=0):
                db.session.delete(url)
                db.session.commit()
                flash('The old links have expired!', 'danger')
        
    # Handle form
    form = UrlForm()
    if request.method == "POST":
        # set exp_date_time
        exp_date_time = form.expiry_date_time.data
        
        # check name existence
        name = request.form['name']
        found_name = Urls.query.filter_by(name=name).first()
        if found_name:
            flash('Please use unique names for your short urls', 'danger')
            return render_template('home.html', title="Home Generate", form=form)

        url_long = request.form['long_url']
        found_url = Urls.query.filter_by(long=url_long).first()
        if found_url:
            flash('You already shortened this one: Here is your link:', 'warning')
            return redirect(url_for('display_short_url', url=found_url.short))
        else:
            shortened_url = generate_short_url()
            if exp_date_time:
                # exp_date_time check PAST
                if exp_date_time < datetime.now().replace(microsecond=0):
                    flash('Time travel to the past has not yet been invented!', 'danger')
                    return render_template('home.html', title="Home Generate", form=form)
                new_short_url = Urls(name, url_long, shortened_url, exp_date_time, datetime.now().replace(microsecond=0))
                db.session.add(new_short_url)
                db.session.commit()
                flash('Short url with custom expiry successfully generated!', 'success')
                return redirect(url_for('display_short_url', url=shortened_url))
            else:
                new_short_url = Urls(name, url_long, shortened_url, (datetime.now().replace(microsecond=0) + timedelta(days=3)), datetime.now().replace(microsecond=0))
                db.session.add(new_short_url)
                db.session.commit()
                flash('Short url successfully generated!', 'success')
                return redirect(url_for('display_short_url', url=shortened_url))
    else:
        return render_template('home.html', title="Home Generate", form=form)
 


@app.route('/display/<url>')
def display_short_url(url):
    return render_template('shortened_url.html', short_url_display=url, title="New shortened url")


@app.route('/<short_url>')
def redirection(short_url):
    long_url = Urls.query.filter_by(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    else:
        return f'<h1>The Url does not exist</h1>'


@app.route('/all')
def all():
    all_urls = Urls.query.order_by(Urls.id)
    return render_template('all-urls.html',
                           all_urls=all_urls, title="All Shortened Urls")


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    url = Urls.query.get_or_404(id)
    db.session.delete(url)
    db.session.commit()
    flash('The short link has been deleted!', 'success')
    return redirect(url_for('all'))
