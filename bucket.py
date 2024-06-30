class BucketManager:
    def __init__(self):
        """
        Initializes a new instance of BucketManager with an empty bucket list.
        """
        self.bucket = []

    def bucket_capacity(self) -> str:
        """
        Returns the current capacity of the bucket list.
        :return: A string indicating the number of buckets or if the bucket list is empty.
        """
        if len(self.bucket) == 0:
            return "Bucket is empty"
        else:
            return f"Bucket has {len(self.bucket)} object(s)"

    def max_bucket_capacity(self) -> bool:
        """
        Checks if the bucket list has reached its maximum capacity.
        :return: False if the bucket list has 4 or more buckets, True otherwise.
        """
        if len(self.bucket) >= 4:
            print("You have reached the max Bucket Capacity")
            return False
        else:
            return True

    def create_bucket(self, bucket_name: str, region: str) -> str:
        """
        Creates a new bucket with the given name and region if the max capacity is not reached.
        :param bucket_name: The name of the bucket to create.
        :param region: The region of the bucket to create.
        :return: A string indicating if the bucket was created successfully or not.
        """
        empty_obj = {
            'name': bucket_name,
            'region': region,
            'objects': []
        }

        if self.max_bucket_capacity():
            self.bucket.append(empty_obj)
            return "New Bucket created"
        else:
            return "No new Bucket created"

    def delete_bucket(self, index: int) -> str:
        """
        Deletes the bucket at the specified index.
        :param index: The index of the bucket to delete.
        :return: A string indicating if the bucket was deleted successfully or if the index was invalid.
        """
        if 0 <= index < len(self.bucket):
            self.bucket.pop(index)
            return f"Bucket at index {index} deleted"
        else:
            return "Index invalid"

    def create_object(self, bucket_index: int, object_key: str, object_value: str) -> str:
        """
        Creates a new object in the specified bucket.
        :param bucket_index: The index of the bucket to add the object to.
        :param object_key: The key of the object to create.
        :param object_value: The value of the object to create.
        :return: A string indicating if the object was created successfully or if the bucket index was invalid.
        """
        if 0 <= bucket_index < len(self.bucket):
            self.bucket[bucket_index]['objects'].append({object_key: object_value})
            return f"Object '{object_key}' created in bucket at index {bucket_index}"
        else:
            return "Bucket index invalid"

# Example usage
bucket_manager = BucketManager()
print(bucket_manager.bucket)  # Prints the initial empty bucket list
print(bucket_manager.create_bucket("bucket1", "us-west-1"))  # Creates a new bucket
print(bucket_manager.bucket_capacity())  # Prints the current capacity of the bucket list
print(bucket_manager.create_bucket("bucket2", "us-west-2"))  # Creates another bucket
print(bucket_manager.create_bucket("bucket3", "us-east-1"))  # Creates another bucket
print(bucket_manager.create_bucket("bucket4", "us-east-2"))  # Creates another bucket
print(bucket_manager.create_bucket("bucket5", "eu-west-1"))  # This should fail due to max capacity
print(bucket_manager.bucket_capacity())  # Prints the current capacity of the bucket list
print(bucket_manager.delete_bucket(1))  # Deletes the bucket at index 1
print(bucket_manager.bucket_capacity())  # Prints the current capacity of the bucket list
print(bucket_manager.create_object(0, "file1.txt", "Hello World"))  # Creates a new object in the first bucket
print(bucket_manager.create_object(0, "file2.txt", "Another File"))  # Creates another object in the first bucket
print(bucket_manager.bucket)  # Prints the current state of the bucket list
