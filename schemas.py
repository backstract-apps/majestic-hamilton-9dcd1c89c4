from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple,Union

import re

class Categories(BaseModel):
    user_id: Optional[Union[int, float]]=None
    name: str
    color: Optional[str]=None
    created_at_dt: Optional[Any]=None
    updated_at_dt: Optional[Any]=None


class ReadCategories(BaseModel):
    user_id: Optional[Union[int, float]]=None
    name: str
    color: Optional[str]=None
    created_at_dt: Optional[Any]=None
    updated_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Tags(BaseModel):
    user_id: Optional[Union[int, float]]=None
    name: str
    created_at_dt: Optional[Any]=None


class ReadTags(BaseModel):
    user_id: Optional[Union[int, float]]=None
    name: str
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class TaskTags(BaseModel):
    task_id: Optional[Union[int, float]]=None
    tag_id: Optional[Union[int, float]]=None


class ReadTaskTags(BaseModel):
    task_id: Optional[Union[int, float]]=None
    tag_id: Optional[Union[int, float]]=None
    class Config:
        from_attributes = True


class Tasks(BaseModel):
    user_id: Optional[Union[int, float]]=None
    category_id: Optional[Union[int, float]]=None
    title: str
    description: Optional[str]=None
    status: Optional[str]=None
    priority: Optional[str]=None
    due_date_dt: Optional[Any]=None
    created_at_dt: Optional[Any]=None
    updated_at_dt: Optional[Any]=None


class ReadTasks(BaseModel):
    user_id: Optional[Union[int, float]]=None
    category_id: Optional[Union[int, float]]=None
    title: str
    description: Optional[str]=None
    status: Optional[str]=None
    priority: Optional[str]=None
    due_date_dt: Optional[Any]=None
    created_at_dt: Optional[Any]=None
    updated_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class UserPreferences(BaseModel):
    user_id: Optional[Union[int, float]]=None
    theme: Optional[str]=None
    default_sort: Optional[str]=None
    notifications_enabled: Optional[Union[int, float]]=None
    updated_at_dt: Optional[Any]=None


class ReadUserPreferences(BaseModel):
    user_id: Optional[Union[int, float]]=None
    theme: Optional[str]=None
    default_sort: Optional[str]=None
    notifications_enabled: Optional[Union[int, float]]=None
    updated_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Users(BaseModel):
    email: str
    password: str
    created_at_dt: Optional[Any]=None


class ReadUsers(BaseModel):
    email: str
    password: str
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    email: str = Field(..., max_length=255)
    password: str = Field(..., max_length=255)
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostUserPreferences(BaseModel):
    user_id: Optional[Union[int, float]]=None
    theme: Optional[str]=None
    default_sort: Optional[str]=None
    notifications_enabled: Optional[Union[int, float]]=None
    updated_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutUserPreferencesId(BaseModel):
    id: str = Field(..., max_length=100)
    user_id: Optional[Union[int, float]]=None
    theme: Optional[str]=None
    default_sort: Optional[str]=None
    notifications_enabled: Optional[Union[int, float]]=None
    updated_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostTasks(BaseModel):
    user_id: Optional[Union[int, float]]=None
    category_id: Optional[Union[int, float]]=None
    title: str = Field(..., max_length=255)
    description: Optional[str]=None
    status: Optional[str]=None
    priority: Optional[str]=None
    due_date_dt: Optional[str]=None
    created_at_dt: Optional[str]=None
    updated_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutTasksId(BaseModel):
    id: str = Field(..., max_length=100)
    user_id: Optional[Union[int, float]]=None
    category_id: Optional[Union[int, float]]=None
    title: str = Field(..., max_length=255)
    description: Optional[str]=None
    status: Optional[str]=None
    priority: Optional[str]=None
    due_date_dt: Optional[str]=None
    created_at_dt: Optional[str]=None
    updated_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostTags(BaseModel):
    user_id: Optional[Union[int, float]]=None
    name: str = Field(..., max_length=50)
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutTagsId(BaseModel):
    id: str = Field(..., max_length=100)
    user_id: Optional[Union[int, float]]=None
    name: str = Field(..., max_length=50)
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostCategories(BaseModel):
    user_id: Optional[Union[int, float]]=None
    name: str = Field(..., max_length=100)
    color: Optional[str]=None
    created_at_dt: Optional[str]=None
    updated_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutCategoriesId(BaseModel):
    id: str = Field(..., max_length=100)
    user_id: Optional[Union[int, float]]=None
    name: str = Field(..., max_length=100)
    color: Optional[str]=None
    created_at_dt: Optional[str]=None
    updated_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: str = Field(..., max_length=100)
    email: str = Field(..., max_length=255)
    password: str = Field(..., max_length=255)
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostPlatformAuthPackageMaysonAuthUserLogin(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostPlatformAuthPackageMaysonAuthUserRegister(BaseModel):
    email: str = Field(..., max_length=100)
    password: str = Field(..., max_length=100)

    class Config:
        from_attributes = True



class PostTaskTags(BaseModel):
    task_id: Optional[Union[int, float]]=None
    tag_id: Optional[Union[int, float]]=None

    class Config:
        from_attributes = True



class PutTaskTagsId(BaseModel):
    id: str = Field(..., max_length=100)
    task_id: Optional[Union[int, float]]=None
    tag_id: Optional[Union[int, float]]=None

    class Config:
        from_attributes = True



# Query Parameter Validation Schemas

class GetUsersIdQueryParams(BaseModel):
    """Query parameter validation for get_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetUserPreferencesIdQueryParams(BaseModel):
    """Query parameter validation for get_user_preferences_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetTasksIdQueryParams(BaseModel):
    """Query parameter validation for get_tasks_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetTagsIdQueryParams(BaseModel):
    """Query parameter validation for get_tags_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetCategoriesIdQueryParams(BaseModel):
    """Query parameter validation for get_categories_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteUsersIdQueryParams(BaseModel):
    """Query parameter validation for delete_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteTagsIdQueryParams(BaseModel):
    """Query parameter validation for delete_tags_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteTasksIdQueryParams(BaseModel):
    """Query parameter validation for delete_tasks_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteUserPreferencesIdQueryParams(BaseModel):
    """Query parameter validation for delete_user_preferences_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteCategoriesIdQueryParams(BaseModel):
    """Query parameter validation for delete_categories_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetTaskTagsIdQueryParams(BaseModel):
    """Query parameter validation for get_task_tags_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteTaskTagsIdQueryParams(BaseModel):
    """Query parameter validation for delete_task_tags_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True
