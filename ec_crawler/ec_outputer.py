class Outputer(object):

    def __init__(self):
        super().__init__()
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        fout = open("output.html", 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<head>")
        fout.write("<meta charset='utf-8'>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("<tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
