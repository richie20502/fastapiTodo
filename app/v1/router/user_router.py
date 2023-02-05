from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.v1.schema import user_schema
from app.v1.service import user_service

from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/user/",
    tags=["users"],
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Crea un nuevo usuario"
)
def create_user(user: user_schema.UserRegister = Body(...)):
    """
    ## Crea un nuevo usuario en la aplicacio

    ### Args
    La aplicacion recibe los siguientes parametros en JSON
    - email: valida un correo
    - username: nombre de usuario unico
    - password: contraseña fuerte para autentificacion

    ### Returns
    - user: informacion del usuario
    """
    return user_service.create_user(user)