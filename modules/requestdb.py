import sqlite3
import os.path
# import pandas # cf pretty_print
from IPython.display import display, HTML

__version__ = (1,1)
##  Règle le pb des noms de colonnes identiques
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        basename = col[0]
        name = basename
        k = 2
        while name in d:
            name = "{}({:1d})".format(basename, k)
            k += 1
        d[name] = row[idx]
    return d

class RequestDB():
    LIMIT_OUTPUT_ = 100

    def __init__(self, databasename):
        if not os.path.isfile(databasename):
            print("No such file : {}".format(databasename))
            self.db = None
        else:
            self.db = databasename

    def _make_a_request(self, request, params=None):
        if self.db is None:
            print("No database")
            return None
        with sqlite3.connect(self.db) as cnx:
            cnx.row_factory = dict_factory
            c = cnx.cursor()
            try:
                if params is None:
                    c.execute(request)
                else:
                    c.execute(request, params)
            except sqlite3.OperationalError as e:
                print("OperationalError : {}".format(e))
                return None
            data = [dict(row) for row in c.fetchall()]
        return data

    @staticmethod
    def _prettyprint_table_with_pandas(data):
        df = pandas.DataFrame(data)
        return df.to_html()

    @staticmethod
    def _prettyprint_table(data):
        if not data:
            return ""
        lines = ["<table class='dataframe' border='1'><thead><tr>"]
        keys = list(data[0].keys())
        lines.extend("<td><b>{}</b></td>".format(k) for k in keys)
        lines.append("</tr></thead><tbody>")
        for row in data:
            lines.append("<tr>")
            lines.extend("<td>{}</td>".format(row[k]) for k in keys)
            lines.append("</tr>")
        lines.append("</tbody></table>")
        return "\n".join(lines)


    def query(self, request, *, force=False):
        res = self._make_a_request(request)
        if res is None or len(res) == 0:
            print("No results")
        else:
            header = "<p>Number of rows : <b>{}</b></p>".format(len(res))
            if len(res) <= self.LIMIT_OUTPUT_ or force:
                return HTML(header + self._prettyprint_table(res))
            else:
                header += "<p><b>Output too large...</b></p>"
                footer = "<p>You can force output with query(&lt;your_query&gt;, force=True) if you know what you are doing</p>"
                return HTML(header + footer)

    def infos(self):
        lines = []
        res  = self._make_a_request("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [_['name'] for _ in res]
        for table in tables:
            lines.append("<p><b>Table {}</b><br/>".format(table))
            res  = self._make_a_request("PRAGMA table_info({})".format(table));
            resf = [{'name': _["name"], "type": _['type'], 'notnull': _['notnull']} for _ in res]
            lines.append(self._prettyprint_table(resf))
        return HTML("\n".join(lines))

print("requestdb v", __version__)
