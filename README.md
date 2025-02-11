# YouTube Transcript Project

This project retrieves the transcript of a YouTube video and saves it to a text file. It utilizes the `youtube-transcript-api` library to fetch the transcript data.

## Project Structure

```
youtube-transcript-project
├── src
│   ├── main.py          # Entry point of the application
│   └── utils
│       └── transcript.py # Contains function to get transcript
├── environment.yml      # Conda environment configuration
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd youtube-transcript-project
   ```

2. **Create the conda environment:**
   ```
   conda env create -f environment.yml
   ```

3. **Activate the environment:**
   ```
   conda activate youtube-transcript-project
   ```

## Running the Application

1. **Run the application:**
   ```
   python src/main.py
   ```

2. **Follow the prompts to enter the YouTube video URL.**

3. **The transcript will be saved to a text file in the project directory.**

## Dependencies

- `youtube-transcript-api`: A library to fetch transcripts from YouTube videos.
- Any other necessary libraries specified in `environment.yml`.

## License

This project is licensed under the MIT License.