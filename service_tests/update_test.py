from services.user_service import UserService
from DAOs import Context
from services import MessageService, UserService, ConnectionService, CallService
from datetime import datetime
import pytest

ctx = Context()


@pytest.mark.order2
def test_update_user():
    u_service = UserService(ctx.getSession())
    users = u_service.find_all()
    for i in range(len(users)):
        users[i].pseudo = "Jean-Bobby"
    u_service.update()
    assert "hello" == "hello"


@pytest.mark.order2
def test_update_connection():
    u_service = ConnectionService(ctx.getSession())
    connections = u_service.find_all()
    for i in range(len(connections)):
        connections[i].end = datetime.now()
    u_service.update()
    assert "hello" == "hello"


@pytest.mark.order2
def test_update_call():
    u_service = CallService(ctx.getSession())
    calls = u_service.find_all()
    for i in range(len(calls)):
        calls[i].end = datetime.now()
    u_service.update()
    assert "hello" == "hello"


@pytest.mark.order2
def test_update_message():
    u_service = MessageService(ctx.getSession())
    messages = u_service.find_all()
    for i in range(len(messages)):
        messages[i].content = "good bye"
    u_service.update()
    assert "hello" == "hello"
