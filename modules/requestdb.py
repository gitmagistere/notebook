import sqlite3
import os.path
# import pandas # cf pretty_print
from IPython.display import display, HTML

class RequestDB():
    
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
        cnx = sqlite3.connect(self.db)
        cnx.row_factory = sqlite3.Row
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
        cnx.close()
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
            

    def query(self, request, size=20):
        res = self._make_a_request(request)
        if res is None or len(res) == 0:
            print("No results")
        else:
            header = "<p>Number of rows : <b>{}</b></p>".format(len(res))
            if len(res) <= size:
                return HTML(header + self._prettyprint_table(res))
            else:
                header += "<p><b>First lines only...</b></p>"
                footer = "<p>...</p>You can try : query(&lt;your_query&gt;, size={}) if you know what you are doing".format(len(res))
                return HTML(header + self._prettyprint_table(res[:size]) + footer)
        
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

