from abc import ABCMeta, abstractmethod
class Report():
    def __init__(self, title, text, formatter):
        self.title = title
        self.text = text
        self.formater = formatter

    def output_report(self):
        self.formater.output_report(self.title, self.text)

class Formatter(metaclass=ABCMeta):
    @abstractmethod
    def output_report(self, title, text):
        pass

class HTMLFormatter(Formatter):
    def output_report(self, title, text):
        print("<html>")
        print("<head>")
        print("<title>%s</title>" % (title,))
        print("</head>")
        print("<body>")
        for line in text:
            print("<p>%s</p>" % (line,))
        print("</body>")
        print("</html>")

class PlainFormatter(Formatter):
    def output_report(self, title, text):
        print("***%s***" % (title,))
        for line in text:
            print(line)

if __name__ == "__main__":
    report = Report(u"月次報告",[u"順調", u"最高"], PlainFormatter())
    report.output_report()
    print("-"*70)

    report = Report(u"月次報告", [u"順調", u"最高"], HTMLFormatter())
    report.output_report()
    print("-"*70)




