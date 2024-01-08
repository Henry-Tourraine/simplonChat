from services import UserService
from DAOs import Context


ctx = Context()
u_service = UserService(ctx.getSession())
print(u_service.find_all())