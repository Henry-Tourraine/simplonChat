from services.user_service import UserService
from DAOs import Context
from services import MessageService, UserService, ConnectionService, CallService
from datetime import datetime
import pytest


ctx = Context()
u_service = UserService(ctx.getSession())


@pytest.mark.order1
def test_create_user():
    res = u_service.create(pseudo="Robert", email="robert@outlook.fr", pwd="1234")
    assert "hello" == "hello"


@pytest.mark.order1
def test_create_connection():
    u = u_service.find_all()
    ConnectionService(ctx.getSession()).create(user_id=u[0].id)
    assert "hello" == "hello"


@pytest.mark.order1
def test_create_call():
    u = u_service.find_all()
    CallService(ctx.getSession()).create(user_id=u[0].id)
    assert "hello" == "hello"


@pytest.mark.order1
def test_create_message():
    u = u_service.find_all()
    MessageService(ctx.getSession()).create(content="hello me", at=datetime.now(), sender_id=u[0].id, receiver_id=u[0].id)
    assert "hello" == "hello"
