import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    if not videos:
        print("No videos available.")
    else:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. Name: {video['name']}, Time: {video['time']}")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print(f"Video '{name}' added successfully!")

def update_video(videos):
    list_all_videos(videos)
    if not videos:
        print("Nothing to update.")
        return
    try:
        index = int(input("Enter the video number to update: "))
        if 1 <= index <= len(videos):
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            videos[index-1] = {"name": name, "time": time}
            save_data_helper(videos)
            print(f"Video {index} updated successfully!")
        else:
            print(f"Invalid index selected. Please enter a number between 1 and {len(videos)}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_video(videos):
    list_all_videos(videos)
    if not videos:
        print("Nothing to delete.")
        return
    try:
        index = int(input("Enter the video number to be deleted: "))
        if 1 <= index <= len(videos):
            del videos[index-1]
            save_data_helper(videos)
            print(f"Video {index} deleted successfully!")
        else:
            print(f"Invalid video index selected. Please enter a number between 1 and {len(videos)}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def export_to_pdf(videos):
    if not videos:
        print("No videos to export.")
        return
    pdf_file = "youtube_videos.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.setFont("Helvetica", 12)
    
    # Title
    c.drawString(100, 750, "YouTube Video List")
    c.drawString(100, 735, "-" * 50)
    
    # List videos
    y = 700  # Starting y-position
    for index, video in enumerate(videos, start=1):
        text = f"{index}. Name: {video['name']}, Time: {video['time']}"
        c.drawString(100, y, text)
        y -= 20  # Move down for the next line
        if y < 50:  # If we run out of space, start a new page
            c.showPage()
            c.setFont("Helvetica", 12)
            y = 750
    
    c.save()
    print(f"Video list exported to '{pdf_file}' successfully!")

def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        print("6. Export video list to PDF")
        choice = input("Enter your choice: ")
        # print(videos)  # Uncomment for debugging
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting the app. Goodbye!")
                break
            case "6":
                export_to_pdf(videos)
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()
