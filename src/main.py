import os

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

        # Convert the transcript list to a string
        transcript_str = "\n".join([item['text'] for item in transcript])

        # Define the directory to save the transcripts
        output_dir = "transcripts"
        os.makedirs(output_dir, exist_ok=True)

        # Save the transcript to a text file in the specified directory
        output_path = os.path.join(output_dir, f"{video_id}_transcript.txt")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(transcript_str)

        print(f"Transcript saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()