# Claude Chatbot — Python + Vercel

A clean AI chatbot powered by Claude, deployed as a Python serverless function on Vercel.

## Project Structure

```
chatbot/
├── api/
│   └── chat.py          ← Python serverless function (handles Claude API calls)
├── public/
│   └── index.html       ← Frontend chat UI
├── vercel.json          ← Vercel deployment config
├── requirements.txt     ← Python dependencies (none needed!)
└── README.md
```

---

## Step 1 — Get Your Claude API Key

1. Go to **https://console.anthropic.com**
2. Sign up for a free account
3. Click **"Get API Keys"** in the left sidebar
4. Click **"Create Key"**, give it a name, copy it
5. Keep it safe — you'll need it in Step 3

---

## Step 2 — Deploy to Vercel

### Option A: Via GitHub (recommended)

1. Push this folder to a new GitHub repository:
   ```bash
   git init
   git add .
   git commit -m "Initial chatbot"
   gh repo create my-chatbot --public --push
   ```

2. Go to **https://vercel.com** → Sign up / Log in
3. Click **"Add New Project"** → Import your GitHub repo
4. Click **Deploy** (leave all settings as default)

### Option B: Via Vercel CLI

```bash
npm install -g vercel
vercel login
vercel --prod
```

---

## Step 3 — Add Your API Key to Vercel

After deploying:

1. Go to your project on **vercel.com**
2. Click **Settings** → **Environment Variables**
3. Add a new variable:
   - **Name:** `ANTHROPIC_API_KEY`
   - **Value:** `sk-ant-...` (your key from Step 1)
   - **Environment:** Production, Preview, Development (check all)
4. Click **Save**
5. Go to **Deployments** → click **Redeploy** (so it picks up the new env var)

---

## Step 4 — Test It!

Visit your Vercel URL (e.g. `https://my-chatbot.vercel.app`) — your chatbot is live!

---

## Running Locally (Optional)

```bash
# Install Vercel CLI
npm install -g vercel

# Set your API key locally
export ANTHROPIC_API_KEY=sk-ant-your-key-here

# Run local dev server
vercel dev
```

Then open **http://localhost:3000**

---

## Customizing the Bot

To change the bot's personality, edit `api/chat.py` — find this line:

```python
"system": "You are a helpful, friendly assistant. Be concise and clear.",
```

Change it to whatever you want, e.g.:
```python
"system": "You are a customer support agent for a clothing store. Be friendly and helpful.",
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| "API key not configured" | Add `ANTHROPIC_API_KEY` in Vercel → Settings → Environment Variables, then redeploy |
| "Claude API error" | Check your API key is correct and has credits |
| Blank page | Check browser console (F12) for errors |
| 404 on /api/chat | Make sure `vercel.json` is in the root folder |
