from fastapi import HTTPException, status


post_object_not_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Post object not found"
)
