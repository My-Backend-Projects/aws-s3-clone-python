# AWS S3 Bucket Clone (Python)

---

# BucketManager

BucketManager is a Python project that simulates basic functionalities of AWS S3 buckets. This project includes two versions:
1. `BucketManager` without SQLite3: In-memory bucket management.
2. `BucketManager` with SQLite3: Persistent bucket management using an SQLite database.

## Features

- Create buckets with a specified name and region.
- Check the current capacity of buckets.
- Ensure the maximum capacity of 4 buckets.
- Delete a bucket by its index or ID (depending on the version).
- Create objects within buckets (only implemented in the in-memory version).

## Prerequisites

- Python 3.6 or higher

## Installation

Clone the repository:
```bash
git clone https://github.com/your-username/BucketManager.git
cd BucketManager
```

## Usage

### BucketManager without SQLite3

This version uses an in-memory list to manage buckets. Follow these steps to use it:

1. Open `bucket_manager_no_sqlite.py` and review the code.
2. Run the script:
    ```bash
    python bucket_manager_no_sqlite.py
    ```

```python
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
```

### BucketManager with SQLite3

This version uses SQLite3 for persistent storage. Follow these steps to use it:

1. Install SQLite3 if not already installed.
2. Open `bucket_manager_with_sqlite.py` and review the code.
3. Run the script:
    ```bash
    python bucket_manager_with_sqlite.py
    ```

```python
import sqlite3
from datetime import datetime

class BucketManager:
    def __init__(self, db_name='bucket_manager.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS buckets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                region TEXT NOT NULL,
                created_at TEXT NOT NULL,
                created_by TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def bucket_capacity(self) -> str:
        self.cursor.execute('SELECT COUNT(*) FROM buckets')
        count = self.cursor.fetchone()[0]
        if count == 0:
            return "Bucket is empty"
        else:
            return f"Bucket has {count} object(s)"

    def max_bucket_capacity(self) -> bool:
        self.cursor.execute('SELECT COUNT(*) FROM buckets')
        count = self.cursor.fetchone()[0]
        if count >= 4:
            print("You have reached the max Bucket Capacity")
            return False
        else:
            return True

    def create_bucket(self, bucket_name: str, region: str, created_by: str) -> str:
        if self.max_bucket_capacity():
            created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute('''
                INSERT INTO buckets (name, region, created_at, created_by)
                VALUES (?, ?, ?, ?)
            ''', (bucket_name, region, created_at, created_by))
            self.conn.commit()
            return "New Bucket created"
        else:
            return "No new Bucket created"

    def delete_bucket(self, bucket_id: int) -> str:
        self.cursor.execute('SELECT * FROM buckets WHERE id = ?', (bucket_id,))
        if self.cursor.fetchone():
            self.cursor.execute('DELETE FROM buckets WHERE id = ?', (bucket_id,))
            self.conn.commit()
            return f"Bucket with id {bucket_id} deleted"
        else:
            return "Bucket id not found"

    def __del__(self):
        self.conn.close()

# Example usage
bucket_manager = BucketManager()
print(bucket_manager.bucket_capacity())
print(bucket_manager.create_bucket("bucket1", "us-west-1", "ClientA"))
print(bucket_manager.bucket_capacity())
print(bucket_manager.create_bucket("bucket2", "us-west-2", "ClientB"))
print(bucket_manager.create_bucket("bucket3", "us-east-1", "ClientC"))
print(bucket_manager.create_bucket("bucket4", "us-east-2", "ClientD"))
print(bucket_manager.create_bucket("bucket5", "eu-west-1", "ClientE"))  # This should fail due to max capacity
print(bucket_manager.bucket_capacity())
print(bucket_manager.delete_bucket(2))
print(bucket_manager.bucket_capacity())
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributions

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Acknowledgments

- Inspired by AWS S3 bucket management.
- Built using Python and SQLite3.

---

Feel free to customize this README further to suit your project and personal preferences.
