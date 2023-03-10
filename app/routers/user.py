from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from controllers.auth import AuthController
from controllers.user import UserController
from schemas.users import AuthTokenSchema, UserSchema

router = APIRouter()


@router.post("/user", summary="Create a user")
async def user_create(data: UserSchema):
    return await UserController.create(user=data)


@router.post(
    "/authentication",
    summary="User authentication",
    response_model=AuthTokenSchema,
)
async def user_authentication(data: OAuth2PasswordRequestForm = Depends()):
    return await AuthController.authenticate(credentials=data, method=UserController)
