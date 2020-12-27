from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable, ComplexModel, String
from spyne.protocol.json import JsonDocument
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import threading

students = dict()


class Student(ComplexModel):
    std_id = Integer
    name = String
    major = String
    level = String

    def __init__(self, std_id, name, major, level):
        students[std_id] = self

        self.std_id = std_id
        self.name = name
        self.major = major
        self.level = level


class RegisterStudentService(ServiceBase):
    @rpc(Integer, Unicode, Unicode, Unicode, _returns=Unicode)
    def register(self, std_id, name, major, level):
        Student(std_id, name, major, level)
        return 'Registration Successful'


class GetStudentService(ServiceBase):
    @rpc(Integer, _returns=Student)
    def get_student(self, std_id):
        return students[std_id]


def create_server(service, port, protocol):
    wsgi_app = WsgiApplication(Application([service], 'sa.course', in_protocol=protocol(), out_protocol=protocol()))
    server = make_server('0.0.0.0', port, wsgi_app)
    return threading.Thread(target=server.serve_forever)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    services = ({
                    'service': RegisterStudentService,
                    'port': 8000,
                    'protocol': JsonDocument},
                {
                    'service': GetStudentService,
                    'port': 8001,
                    'protocol': Soap11})
    for service in services:
        create_server(**service).start()
