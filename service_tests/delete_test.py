from services.user_service import UserService
from DAOs import Context
from services import MessageService, UserService, ConnectionService, CallService
from datetime import datetime
import pytest

ctx = Context()


@pytest.mark.order3
def test_delete_user():
    u_service = UserService(ctx.getSession())
    users = u_service.find_all()
    for i in range(len(users)):
        u_service.delete(users[i])
    assert "hello" == "hello"


@pytest.mark.order3
def test_delete_connection():
    u_service = ConnectionService(ctx.getSession())
    connections = u_service.find_all()
    for i in range(len(connections)):
        u_service.delete( connections[i])
    assert "hello" == "hello"


@pytest.mark.order3
def test_delete_call():
    u_service = CallService(ctx.getSession())
    calls = u_service.find_all()
    for i in range(len(calls)):
        u_service.delete( calls[i])
    assert "hello" == "hello"


@pytest.mark.order3
def test_delete_message():
    u_service = MessageService(ctx.getSession())
    messages = u_service.find_all()
    for i in range(len(messages)):
        u_service.delete(messages[i])
    assert "hello" == "hello"
