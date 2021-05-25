import requests
from faker import Faker



from requests.auth import HTTPBasicAuth
user = 'admin'
password = 'rewq4321'
fake = Faker()
def getSession(user, password):
    hostname = 'http://127.0.0.1:8000/api-auth/login/'
    session = requests.Session()
    session.auth = (user, password)
    auth = session.post( hostname )
    return session


def createTasks(quatity, session):
    i = 0
    for _ in range(quatity):

        try:
            payload = {
                "title": fake.sentence(nb_words=3),
                "description": fake.sentence(nb_words=10),
                "status": "open",
                "assign": 1
            }
            session.post("http://127.0.0.1:8000/tasks/", data=payload)
            i += 1
            print('Crater Task: {}/{}'.format(i,quatity))
        except:
            print('not work')

def createLogs(session):
    i = 0
    listTask = requests.get("http://127.0.0.1:8000/tasks/").json()
    for task_id in listTask:

        try:
            payload = {'task': task_id['id'], 'duration': 0}
            session.post("http://127.0.0.1:8000/logs/", data=payload)
            i += 1
            print('Crater log: {}/{}'.format(i,len(listTask)))

        except:
            print('not work')




session =  getSession(user, password)
createTasks(200, session)
createLogs(session)
