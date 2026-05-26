# AI Email Assistant

AI Email Assistant is a small Python project that analyzes an email with Google Gemini and returns structured JSON with the email category, priority, summary, action items, and a suggested reply.

## What it does

- Sends an email body to Gemini for analysis.
- Classifies the email into a category such as `job`, `meeting`, `spam`, `personal`, `work`, `finance`, or `other`.
- Assigns a priority of `low`, `medium`, or `high`.
- Produces a short summary, action items, and a suggested reply.
- Prints the model response to the terminal.

## Project structure

- `app.py` - simple entry point that passes a sample email to the analyzer.
- `email_processor.py` - loads environment variables, creates the Gemini client, and formats the analysis prompt.

## Requirements

- Python 3.10 or newer
- A Google Gemini API key

Python packages used by the project:

- `google-genai`
- `python-dotenv`

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install google-genai python-dotenv
   ```

3. Create a `.env` file in the project root and add your API key:

   ```env
   GENAI_API_KEY=your_api_key_here
   ```

## How to run

Run the app from the project folder:

```bash
python app.py
```

The script currently uses a sample email in `app.py`. To analyze a different email, replace the value of `sample_email` or call `analyze_email()` from your own code.

## Example output

The app prints a JSON response similar to this:

```json
{
  "category": "job",
  "priority": "high",
  "summary": "The email is about scheduling an interview for next Tuesday at 3 PM.",
  "action_items": ["Confirm availability for the interview"],
  "suggested_reply": "Thank you for reaching out. I am available next Tuesday at 3 PM and look forward to the interview."
}
```

## Notes

- The model call is currently configured to use `gemini-3.5-flash`.
- The analyzer expects the model to return only valid JSON.
- If you want stricter reliability, you can add JSON parsing and validation around the response in `email_processor.py`.

## Next improvements

- Add a `requirements.txt` file.
- Accept email text from user input or a file instead of a hardcoded sample.
- Parse and validate the JSON response before printing it.
- Add tests for the analyzer prompt and response handling.