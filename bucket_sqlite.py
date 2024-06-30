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

