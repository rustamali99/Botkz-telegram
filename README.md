# Beauty Salon Booking with n8n

This repository demonstrates a simple Telegram bot and an example n8n workflow for managing appointments for a lash salon. The n8n workflow records bookings in Google Calendar and can respond through Telegram, WhatsApp and Instagram.

## Files

- `main.py` – example Telegram bot
- `beauty_salon_workflow.json` – sample n8n workflow

## n8n Workflow Overview

The workflow contains the following nodes:

1. **Telegram Trigger** – listens for new Telegram messages.
2. **Function (Parse Command)** – extracts the booking command and parameters.
3. **Switch** – routes create, update and delete actions.
4. **Google Calendar** – creates, updates or removes events.
5. **OpenAI Response** – generates a reply using an AI model (optional).
6. **Telegram**, **Twilio** and **HTTP Request** nodes – send confirmations to Telegram, WhatsApp and Instagram.

### Example Commands

Send messages via Telegram in one of these formats:

```
create YYYY-MM-DD HH:MM Service name
update EVENT_ID YYYY-MM-DD HH:MM Service name
delete EVENT_ID
```

### Setup

1. Install n8n and import `beauty_salon_workflow.json`.
2. Configure credentials for:
   - Telegram Bot
   - Google Calendar
   - Twilio (WhatsApp)
   - OpenAI (optional)
   - Instagram webhook URL
3. Adjust environment variables used in the workflow as needed.

### Running the Telegram bot

```
pip install pyTelegramBotAPI
BOT_TOKEN=<your-token> python main.py
```

This bot simply replies that it is running. Use the n8n workflow to handle bookings.
