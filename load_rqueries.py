#!/usr/bin/python3
"""
"""

# USAGE: cat load_queries.py | python3 manage.py shell

import sqlite3

from query_compendium.models import RedditQuery, ContentCreator

querystr = "SELECT ama_index.url_id, cc_name, fan_name, question_text, answer_text FROM ama_queries INNER JOIN ama_index ON ama_index.url_id = ama_queries.url_id;"

with sqlite3.connect("../output/ama_database.db") as cnxn:
    cnxn.row_factory = sqlite3.Row
    cur = cnxn.cursor()
    ama_queries = cur.execute(querystr).fetchall()

for cc in ContentCreator.objects.all():
    cc_name = cc.display_name
    for myrow in filter(lambda row: row['cc_name'] == cc_name, ama_queries):
        myrow = dict(myrow)
        myrow.pop('cc_name')
        rquery = RedditQuery(content_creator=cc, **myrow)
        rquery.save()


if __name__ == '__main__':
    pass
