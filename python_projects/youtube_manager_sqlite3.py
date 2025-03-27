import sqlite3

con = sqlite3.connect('youtube_videos.db')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS VIDEOS (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    try:
        cursor.execute("SELECT * FROM videos")
        rows = cursor.fetchall()
        print('\n')
        print('*' * 70)
        if not rows:
            print("No videos in the database")
        else:
            for row in rows:
                print(row)
        print('\n')
        print('*' * 70)
    except sqlite3.Error as e:
        print(f"Database error: {e}")

def add_video(name, time):
    try:
        cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
        con.commit()
        print("Video added successfully")
    except sqlite3.Error as e:
        print(f"Error adding video: {e}")

def update_video(video_id, new_name, new_time):
    try:
        cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
        if cursor.fetchone() is None:
            print(f"No video found with ID {video_id}")
            return
        cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", 
                      (new_name, new_time, video_id))
        con.commit()
        print("Video updated successfully")
    except sqlite3.Error as e:
        print(f"Error updating video: {e}")

def delete_video(video_id):
    try:
        cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
        if cursor.fetchone() is None:
            print(f"No video found with ID {video_id}")
            return
        cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
        con.commit()
        print("Video deleted successfully")
    except sqlite3.Error as e:
        print(f"Error deleting video: {e}")

def main():
    while True:
        print("\nYouTube Manager App with DB")
        print("1. List all videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter video ID to update: ")
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5")
    
    con.close()
    print("Database connection closed")

if __name__ == "__main__":
    main()