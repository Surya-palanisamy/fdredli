import requests
import sys
class name_ban:
    def banner(self):
        print("    TRACKING THE END FACE OF URLs\n   ")

    def help(self):
        print('flired v1.0')
        about = '''Have you ever wondered: Where does this link go? 
The flired it allows you to see the complete path a redirected URL goes through. 
It will show you the full redirection path of URLs, shortened links, or tiny URLs.'''
        print(about)
        print('\nRequirements: Python 3, requests and colorama libraries')
        print('To install the requirements run these commands')
        print('\tUpdate: apt-get update')
        print('\tPython 3: apt-get install python3')
        print('\tRequests: pip install requests')
        print('\tcolorama: pip install colorama')
        print('\nRun the tool: flired.py --track')
        print('Commands')
        print("--track or -t  -> Track the given URL's redirection path & find its end URL.")
        print('--help or -h  -> To display helpline how to use this tool & about tool. ')

    def cmdusage(self):
        print('Invalid command-line arguments!')
        print('Commands')
        print("--track or -t  -> Track the given URL's redirection path & find its end URL.")
        print('--help or -h  -> To display helpline how to use this tool & about tool. ')

class flired:
    def __init__(self, url):
        self.url = url
    def track_url(self):
        try:
            resp = requests.get(self.url)
            if resp.history:
                print('\nYes URL is Redirected or Shorten!')
                print('Here the following redirected chain...\n')
                for r in resp.history:
                    print(r.status_code, '|', r.url, '|', r.reason)
                print('\nEND URL :', resp.url)
                print('Status Code :', resp.status_code, resp.reason)
            else:
                print('\nURL is Not Redirected or Shorten!')
                print('END URL :', resp.url)
                print('Status Code :',resp.status_code, resp.reason)
        except BaseException as be:
            print('Tracking Failed! Check URL')
            print(be)
            exit()

if __name__=='__main__':
    intro = name_ban()
    intro.banner()
    if len(sys.argv) == 2:
        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            intro.help()
        elif sys.argv[1] == '--track' or sys.argv[1] == '-t':
            url = input('Enter URL to Track:')
            print('Tracking Redirection Of URL...')
            track = flired(url)
            track.track_url()
        else:
            intro.cmdusage()
    else:
        intro.cmdusage()
