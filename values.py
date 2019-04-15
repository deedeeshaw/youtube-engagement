import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from pprint import pprint

from config import config

import pymysql
pymysql.install_as_MySQLdb()

# FUNCTION TO CREATE THE DROPDOWN MENU OF CATEGORIES
def category_table():
    engine = create_engine(f'mysql://root:{config}@localhost:3306/youtube_db')

    # Create our session (link) from Python to the DB
    session = Session(engine)

    session.query('youtube')
    category_list= []
    with engine.connect() as con:
        records=  con.execute('select category_id, category_desc from youtube group by category_desc')
        for record in records:
            category_list.append({'cat_id':record[0], 'cat_desc': record[1]})

    session.close
    return category_list

# FUNCTION TO POPULATE FOR ALL CATEGORIES
def values():
    engine = create_engine(f'mysql://root:{config}@localhost:3306/youtube_db')

    # Create our session (link) from Python to the DB
    session = Session(engine)

    session.query('youtube')

    with engine.connect() as con:
        
        # total videos
        videos = con.execute('SELECT count(*) FROM youtube')
        for video in videos:
            print(video[0])
        # total subscribera
        subs = con.execute("select format(sum(subscriber), 2) from youtube")
        for sub in subs:
            print(sub[0])
        # total views
        views = con.execute("select format(sum(views), 2) from youtube")
        for view in views:
            print(view[0])
        # total engagement
        engages = con.execute("select format(sum(likes + dislikes + comment_count), 2) as engagement from youtube")
        for engage in engages:
            print(engage[0])

        ### Breakdown of Engagement metrics for bar graph
        likes = con.execute("select format(sum(likes), 2) from youtube")
        for like in likes:
            print(like[0])
        dislikes =con.execute("select format(sum(dislikes), 2) from youtube")
        for dislike in dislikes:
            print(dislike[0])
        comments =con.execute("select format(sum(comment_count), 2) from youtube")
        for comment in comments:
            print(comment[0])

    session.close

    values_dict = {"videos": video[0], "subscribers": sub[0], "view": view[0], "engagement": engage[0], "Likes": like[0], "Dislikes": dislike[0], "Comments": comment[0], "Likes": like[0], "Dislikes": dislike[0], "Comments": comment[0]}
    print(values_dict)
    return(values_dict)


# FUNCTION FOR WHEN A SPECIFIC CATEGORY IS PICKED
def category_id(cat_id):

    engine = create_engine(f'mysql://root:{config}@localhost:3306/youtube_db')

    # Create our session (link) from Python to the DB
    session = Session(engine)

    session.query('youtube')

    with engine.connect() as con:

        # category videos
        
        select_statement=f'SELECT count(*) FROM youtube where category_id = "{cat_id}"'
        print(select_statement)
        videos = con.execute(f'SELECT count(*) FROM youtube where category_id = "{cat_id}"')
        for video in videos:
            print(video[0])
        # category subscriber
        subs = con.execute(f"select format(sum(subscriber), 2) from youtube where category_id = '{cat_id}'")
        for sub in subs:
            print(sub[0])
        # category views
        views = con.execute(f"select format(sum(views), 2) from youtube where category_id = '{cat_id}'")
        for view in views:
            print(view[0])
        # category engagement
        engages = con.execute(f"select format(sum(likes + dislikes + comment_count), 2) as engagement from youtube where category_id= '{cat_id}'")
        for engage in engages:
            print(engage[0])

        ### Breakdown of Engagement metrics for bar graph
        likes = con.execute(f"select format(sum(likes), 2) from youtube where category_id = '{cat_id}'")
        for like in likes:
             print(like[0])
        dislikes =con.execute(f"select format(sum(dislikes), 2) from youtube where category_id = '{cat_id}'")
        for dislike in dislikes:
             print(dislike[0])
        comments =con.execute(f"select format(sum(comment_count), 2) from youtube where category_id = '{cat_id}'")
        for comment in comments:
            print(comment[0])

    session.close

    values_dict = {"videos": video[0], "subscribers": sub[0], "view": view[0], "engagement": engage[0], "Likes": like[0], "Dislikes": dislike[0], "Comments": comment[0], "Likes": like[0], "Dislikes": dislike[0], "Comments": comment[0]}
    print(values_dict)
    return(values_dict)

    
    