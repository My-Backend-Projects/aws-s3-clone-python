class BucketManager:
    def __init__(self):
        self.bucket = []

    def bucket_capacity(self) -> str:
        if len(self.bucket) == 0:
            return "Bucket is empty"
        else:
            return f"Bucket has {len(self.bucket)} object(s)"

    def max_bucket_capacity(self) -> bool:
        if len(self.bucket) >= 4:
            print("You have reached the max Bucket Capacity")
            return False
        else:
            return True

    def create_bucket(self, bucket_name: str, region: str) -> str:
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
        if 0 <= index < len(self.bucket):
            self.bucket.pop(index)
            return f"Bucket at index {index} deleted"
        else:
            return "Index invalid"

    def create_object(self, bucket_index: int, object_key: str, object_value: str) -> str:
        if 0 <= bucket_index < len(self.bucket):
            self.bucket[bucket_index]['objects'].append({object_key: object_value})
            return f"Object '{object_key}' created in bucket at index {bucket_index}"
        else:
            return "Bucket index invalid"

# Example usage
bucket_manager = BucketManager()
print(bucket_manager.bucket)
print(bucket_manager.create_bucket("bucket1", "us-west-1"))
print(bucket_manager.bucket_capacity())
print(bucket_manager.create_bucket("bucket2", "us-west-2"))
print(bucket_manager.create_bucket("bucket3", "us-east-1"))
print(bucket_manager.create_bucket("bucket4", "us-east-2"))
print(bucket_manager.create_bucket("bucket5", "eu-west-1"))  # This should fail due to max capacity
print(bucket_manager.bucket_capacity())
print(bucket_manager.delete_bucket(1))
print(bucket_manager.bucket_capacity())
print(bucket_manager.create_object(0, "file1.txt", "Hello World"))
print(bucket_manager.create_object(0, "file2.txt", "Another File"))
print(bucket_manager.bucket)

