def main():
    import sys
    from utils.transcript import get_transcript

    # Get the YouTube video URL from user input
    video_url = input("Enter the YouTube video URL: ")

    # Extract the video ID from the URL
    video_id = video_url.split("v=")[-1].split("&")[0]

    try:
        # Fetch the transcript
        transcript = get_transcript(video_id)

        # Save the transcript to a text file
        with open(f"{video_id}_transcript.txt", "w", encoding="utf-8") as f:
            f.write(transcript)

        print(f"Transcript saved to {video_id}_transcript.txt")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()