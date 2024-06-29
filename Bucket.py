
bucket = []


def bucket_capacity()-> str:
    """
        bucket_capacity method is for checking
        the length of the over all buckets
        created in the system.

        Args:
            Empty
            
        Return:
            String
    """
    
    if len(bucket) <= 0: # check if bucket length is empty
        return "Bucket is empty"
    else:
        return f"Bucket has {len(bucket)} object"


def max_bucket_capacity()-> bool:
    """
        max_bucket_capacity method is for
        checking if a user has reach the max level
        of buckets they allow to create.

        Args:
            Empty

        Return:
            Boolean: True | False
    """
    
    if len(bucket) == 4:
        print("You have reach the max Bucket Capacity")
        return False
    else:
        return True


def create_bucket(bucket_name: str, region: str):
    empty_obj = [
        {
            f'{bucket_name}': [
                {
                    'region': f'{region}'
                },
                {
                    'obj': {
                        'key': 'value'
                    }
                }
            ]
        }
    ]
    
    if max_bucket_capacity() == True:
        bucket.append(empty_obj)
        return "New Bucket created"
    else:
        return "No new Bucket created"
    

def delete_bucket(index: int)-> str | int:
    """
        delete_bucket method give user
        the chance to delete a bucket by index.

        Args:
            int: index

        Return:
            int: If index is valid.
            str: If index is not vaild.
            
    """
    if index == True:
        bucket.pop(index)
        return index
    else:
        return "Index invalid"


print(bucket)






