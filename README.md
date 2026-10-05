# Personal Travel Planner Agent

An AI-powered personal travel planner built with **Google Agent Development Kit (ADK)** and Gemini. It converts natural-language travel requests into practical, budget-aware travel plans.

## Features

- Understands destination, duration, budget, and interests.
- Creates personalized travel recommendations.
- Recommends historical places, attractions, and local food.
- Estimates accommodation, food, local transport, and activity costs.
- Produces a clear day-wise itinerary.
- Suggests practical travel tips and budget-saving options.
- Uses a custom ADK budget calculation tool.
- Supports natural-language travel planning.

## Tech Stack

- Python
- Google ADK
- Gemini
- Google AI API
- Python-dotenv

## Project Structure

```text
Personal-Travel-Planner-Agent/
│
├── agent.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── example_conversations.md
└── SUBMISSION_CHECKLIST.md


## Setup (Windows PowerShell)

Open a terminal in this folder.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Create `.env` in the same folder as `agent.py`:

```env
GOOGLE_API_KEY=YOUR_NEW_GEMINI_API_KEY
TRAVEL_AGENT_MODEL=gemini-3.8-flash
```

Do NOT commit or submit `.env`.

## Run

From the folder that contains the `travel_planner_agent` directory:

```powershell
adk web
```

If your ADK installation requires the agent directory explicitly:

```powershell
adk web travel_planner_agent
```

Open the localhost URL shown in the terminal.

Select `travel_planner_agent`.

## First test

```text
I want to visit Jaipur for 3 days with a budget of ₹15,000.
I am traveling alone and I like history and local food.
Create a complete day-wise itinerary.
```

## More tests

```text
Plan a 2-day Delhi trip under ₹8,000. I am interested in monuments and street food.
```

```text
I have ₹20,000 for 4 days in Goa. I like beaches, relaxing and seafood.
```

## Troubleshooting model errors

If an error says `gemini-2.5-flash is no longer available to new users`, check:

```powershell
echo $env:TRAVEL_AGENT_MODEL
```

If it prints `gemini-3.5-flash`, run:

```powershell
Remove-Item Env:TRAVEL_AGENT_MODEL -ErrorAction SilentlyContinue
```

Then close the terminal, open a new terminal, activate `.venv`, and run:

```powershell
adk web
```

The project default is `gemini-3.5-flash`.

## Security

Never put a real API key in `agent.py`, README, screenshots, ZIP files, GitHub, or chat messages. Store it only in `.env`.

If an API key has already been shared publicly, revoke it in Google AI Studio and create a new one.
#� �P�e�r�s�o�n�a�l�-�T�r�a�v�e�l�-�P�l�a�n�n�e�r�-�A�g�e�n�t�
�
�
