bucket = []

def bucket_capacity() -> str:
    """
    bucket_capacity method is for checking the length of the overall buckets
    created in the system.

    Args:
        Empty

    Return:
        String
    """
    if len(bucket) == 0:  # check if bucket length is empty
        return "Bucket is empty"
    else:
        return f"Bucket has {len(bucket)} object(s)"

def max_bucket_capacity() -> bool:
    """
    max_bucket_capacity method is for checking if a user has reached the max level
    of buckets they are allowed to create.

    Args:
        Empty

    Return:
        Boolean: True | False
    """
    if len(bucket) >= 4:
        print("You have reached the max Bucket Capacity")
        return False
    else:
        return True

def create_bucket(bucket_name: str, region: str) -> str:
    empty_obj = {
        'name': bucket_name,
        'region': region,
        'objects': []
    }
    
    if max_bucket_capacity():
        bucket.append(empty_obj)
        return "New Bucket created"
    else:
        return "No new Bucket created"

def delete_bucket(index: int) -> str:
    """
    delete_bucket method gives user the chance to delete a bucket by index.

    Args:
        index (int): Index of the bucket to delete.

    Return:
        str: Result of the deletion.
    """
    if 0 <= index < len(bucket):
        bucket.pop(index)
        return f"Bucket at index {index} deleted"
    else:
        return "Index invalid"

def create_object(bucket_index: int, object_key: str, object_value: str) -> str:
    """
    create_object method adds an object to a specified bucket.

    Args:
        bucket_index (int): Index of the bucket where the object should be created.
        object_key (str): Key of the object.
        object_value (str): Value of the object.

    Return:
        str: Result of the object creation.
    """
    if 0 <= bucket_index < len(bucket):
        bucket[bucket_index]['objects'].append({object_key: object_value})
        return f"Object '{object_key}' created in bucket at index {bucket_index}"
    else:
        return "Bucket index invalid"

# Example usage
print(bucket)
print(create_bucket("bucket1", "us-west-1"))
print(bucket_capacity())
print(create_bucket("bucket2", "us-west-2"))
print(create_bucket("bucket3", "us-east-1"))
print(create_bucket("bucket4", "us-east-2"))
print(create_bucket("bucket5", "eu-west-1"))  # This should fail due to max capacity
print(bucket_capacity())
print(delete_bucket(1))
print(bucket_capacity())
print(create_object(0, "file1.txt", "Hello World"))
print(create_object(0, "file2.txt", "Another File"))
print(bucket)



