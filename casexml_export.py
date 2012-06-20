#conn = httplib.HTTPConnection("https://www.commcarehq.org/a/mvp/receiver/")
from urlparse import urlparse
import httplib
from django.conf import settings
settings.configure()


from forms import PregnancyForm

data ={}


class Main():
    
    def run(self):
    
        data['patient'] = ''
        form = PregnancyForm(data)
        self.transmit_form(form)

    def transmit_form(self, form):
        ''' Send data to commcare '''
        xml_form = form.render()

        headers = {"Content-type": "text/xml", "Accept": "text/plain"}

        url = "https://www.commcarehq.org/a/mvp/receiver/"

        up = urlparse(url)
        conn = httplib.HTTPSConnection(up.netloc) if url.startswith("https") else httplib.HTTPConnection(up.netloc) 
        conn.request('POST', up.path, xml_form, headers)
        resp =  conn.getresponse()
        responsetext = resp.read()
        print resp
        assert resp.status == 201, 'Bad HTTP Response'
        assert "Thanks for submitting" in responsetext, "Bad response text"
        
if __name__ == '__main__':
    main = Main()
    main.run()
