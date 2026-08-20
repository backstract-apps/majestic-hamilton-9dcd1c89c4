from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Query, Form, File
from sqlalchemy.orm import Session
from typing import List, Annotated, Optional
import service, models, schemas
from database import SessionLocal
from middleware.application_middleware import platform_auth_platform_auth_middleware_group_dependency, default_dependency


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_users(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id/')
async def get_users_id(request: Request, query: schemas.GetUsersIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_users_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(request: Request, raw_data: schemas.PostUsers, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.post_users(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_preferences/')
async def get_user_preferences(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_user_preferences(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_preferences/id/')
async def get_user_preferences_id(request: Request, query: schemas.GetUserPreferencesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_user_preferences_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user_preferences/')
async def post_user_preferences(request: Request, raw_data: schemas.PostUserPreferences, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.post_user_preferences(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user_preferences/id/')
async def put_user_preferences_id(request: Request, raw_data: schemas.PutUserPreferencesId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.put_user_preferences_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/')
async def get_tasks(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_tasks(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/id/')
async def get_tasks_id(request: Request, query: schemas.GetTasksIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_tasks_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/tasks/')
async def post_tasks(request: Request, raw_data: schemas.PostTasks, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.post_tasks(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/tasks/id/')
async def put_tasks_id(request: Request, raw_data: schemas.PutTasksId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.put_tasks_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tags/')
async def get_tags(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_tags(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tags/id/')
async def get_tags_id(request: Request, query: schemas.GetTagsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_tags_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/tags/')
async def post_tags(request: Request, raw_data: schemas.PostTags, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.post_tags(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/tags/id/')
async def put_tags_id(request: Request, raw_data: schemas.PutTagsId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.put_tags_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/categories/')
async def get_categories(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_categories(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/categories/id/')
async def get_categories_id(request: Request, query: schemas.GetCategoriesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_categories_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/categories/')
async def post_categories(request: Request, raw_data: schemas.PostCategories, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.post_categories(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/categories/id/')
async def put_categories_id(request: Request, raw_data: schemas.PutCategoriesId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.put_categories_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(request: Request, raw_data: schemas.PutUsersId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.put_users_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id/')
async def delete_users_id(request: Request, query: schemas.DeleteUsersIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.delete_users_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/platform_auth_package/mayson/auth/user/login')
async def post_platform_auth_package_mayson_auth_user_login(request: Request, raw_data: schemas.PostPlatformAuthPackageMaysonAuthUserLogin, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.post_platform_auth_package_mayson_auth_user_login(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/tags/id/')
async def delete_tags_id(request: Request, query: schemas.DeleteTagsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.delete_tags_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/platform_auth_package/mayson/auth/user/register')
async def post_platform_auth_package_mayson_auth_user_register(request: Request, raw_data: schemas.PostPlatformAuthPackageMaysonAuthUserRegister, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.post_platform_auth_package_mayson_auth_user_register(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/tasks/id/')
async def delete_tasks_id(request: Request, query: schemas.DeleteTasksIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.delete_tasks_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user_preferences/id/')
async def delete_user_preferences_id(request: Request, query: schemas.DeleteUserPreferencesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.delete_user_preferences_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/categories/id/')
async def delete_categories_id(request: Request, query: schemas.DeleteCategoriesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.delete_categories_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/task_tags/')
async def get_task_tags(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_task_tags(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/task_tags/id/')
async def get_task_tags_id(request: Request, query: schemas.GetTaskTagsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_task_tags_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/task_tags/')
async def post_task_tags(request: Request, raw_data: schemas.PostTaskTags, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.post_task_tags(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/task_tags/id/')
async def put_task_tags_id(request: Request, raw_data: schemas.PutTaskTagsId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.put_task_tags_id(request, db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/task_tags/id/')
async def delete_task_tags_id(request: Request, query: schemas.DeleteTaskTagsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.delete_task_tags_id(request, db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/platform_auth_package/mayson/sso/auth/login/google')
async def get_platform_auth_package_mayson_sso_auth_login_google(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_platform_auth_package_mayson_sso_auth_login_google(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/platform_auth_package/mayson/sso/auth/callback/')
async def get_platform_auth_package_mayson_sso_auth_callback(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_platform_auth_package_mayson_sso_auth_callback(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/platform_auth_package/mayson/sso/auth/me')
async def get_platform_auth_package_mayson_sso_auth_me(request: Request, db: Session = Depends(get_db), protected_deps_1: dict = Depends(platform_auth_platform_auth_middleware_group_dependency), protected_deps_2: dict = Depends(default_dependency),  ):
    try:
        return await service.get_platform_auth_package_mayson_sso_auth_me(request, db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

