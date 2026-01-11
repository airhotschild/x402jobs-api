# 🚀 X402JOBS API - DEPLOYMENT GUIDE

## 📋 TABLE OF CONTENTS
1. Quick Start
2. Local Testing
3. Deployment Options
4. API Usage
5. Real Data Integration
6. Troubleshooting

---

## ⚡ QUICK START (5 MINUTES)

### 1. Prepare Files
```bash
# Put all files in a folder:
x402jobs/
  ├── x402jobs_api.py
  ├── requirements.txt
  ├── Dockerfile
  └── .env.example
```

### 2. Create Python Virtual Environment
```bash
cd x402jobs
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run API
```bash
python x402jobs_api.py
```

✅ **API is now running:** https://x402jobs-api-production.up.railway.app

---

## 🧪 LOCAL TESTING

### Test 1: API Info
```bash
curl https://x402jobs-api-production.up.railway.app/
```

**Expected Output:**
```json
{
  "name": "X402Jobs Web3 API",
  "version": "1.0.0",
  "wallet": "8UT7S3acWenLuEuqFPwoAGDT6vFGrGiGz3JM6NK3rXKw",
  "jobs": ["nft-floor", "token-safety", "defi-yield", "whale-monitor", "token-launch"],
  "pricing": {
    "nft-floor": 0.02,
    "token-safety": 0.05,
    "defi-yield": 0.10,
    "whale-monitor": 0.15,
    "token-launch": 0.08
  }
}
```

### Test 2: Health Check
```bash
curl https://x402jobs-api-production.up.railway.app/health
```

### Test 3: NFT Floor Tracker (NO PAYMENT TEST)
```bash
curl -X POST https://x402jobs-api-production.up.railway.app/nft-floor \
  -H "Content-Type: application/json" \
  -d '{
    "collection_address": "test123",
    "marketplace": "all",
    "include_volume": true
  }'
```

**NOTE:** Payment verification is currently disabled (development mode). It will be automatically enabled when uploaded to x402jobs platform.

---

## 🌐 DEPLOYMENT OPTIONS

### OPTION 1: Railway.app (RECOMMENDED - FREE)

1. **Go to Railway.app:** https://railway.app
2. **Login with GitHub**
3. **"New Project" → "Deploy from GitHub"**
4. **Select your repo** (or upload files)
5. **Auto-deploy!**

✅ **Advantages:**
- Free tier available
- Automatic HTTPS
- Easy deployment
- Provides public URL

**Your Railway URL:** `https://your-project.up.railway.app`

### OPTION 2: Render.com (FREE)

1. **Go to Render.com:** https://render.com
2. **"New +" → "Web Service"**
3. **Connect GitHub repo**
4. **Build Command:** `pip install -r requirements.txt`
5. **Start Command:** `uvicorn x402jobs_api:app --host 0.0.0.0 --port $PORT`

### OPTION 3: Fly.io (FREE)

```bash
# Install Fly CLI
curl -L https://fly.io/install.sh | sh

# Login
fly auth login

# Deploy
fly launch
fly deploy
```

### OPTION 4: Docker (YOUR OWN SERVER)

```bash
# Build Docker image
docker build -t x402jobs-api .

# Run
docker run -p 8000:8000 x402jobs-api
```

---

## 📡 API USAGE

### 1. NFT Floor Tracker ($0.02)

**Endpoint:** `POST /nft-floor`

**Request:**
```json
{
  "collection_address": "J1S9H3QjnRtBbbuD4HjPV6RpRhwuk4zKbxsnCHuTgh9w",
  "marketplace": "all",
  "include_volume": true
}
```

**Response:**
```json
{
  "collection_name": "Mad Lads",
  "floor_price": 125.5,
  "floor_price_usd": 21335.0,
  "volume_24h": 450000.0,
  "total_supply": 10000,
  "unique_holders": 4521,
  "listed_count": 234,
  "price_change_24h": 3.2,
  "timestamp": "2026-01-11T20:00:00Z"
}
```

### 2. Token Safety Scorer ($0.05)

**Endpoint:** `POST /token-safety`

**Request:**
```json
{
  "token_address": "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
  "blockchain": "solana",
  "deep_scan": false
}
```

### 3. DeFi Yield Optimizer ($0.10)

**Endpoint:** `POST /yield-optimizer`

**Request:**
```json
{
  "token_type": "USDC",
  "amount": 10000,
  "risk_tolerance": "moderate",
  "min_apy": 5.0
}
```

### 4. Whale Monitor ($0.15)

**Endpoint:** `POST /whale-monitor`

**Request:**
```json
{
  "action": "track_wallet",
  "wallet_address": "9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM",
  "time_range": "24h"
}
```

### 5. Token Launch Detector ($0.08)

**Endpoint:** `POST /token-launches`

**Request:**
```json
{
  "time_range": "1h",
  "blockchain": "solana",
  "min_liquidity_usd": 5000,
  "safety_filter": true,
  "limit": 20
}
```

---

## 🔧 REAL DATA INTEGRATION

Currently API returns **placeholder data**. To integrate real data:

### NFT Floor Tracker - Real Implementation

```python
# Use Magic Eden API
import httpx

async def get_real_nft_floor(collection_address: str):
    async with httpx.AsyncClient() as client:
        # Magic Eden API
        response = await client.get(
            f"https://api-mainnet.magiceden.dev/v2/collections/{collection_address}/stats"
        )
        data = response.json()
        
        return {
            "floor_price": data["floorPrice"] / 1e9,  # Lamports to SOL
            "volume_24h": data["volumeAll"],
            # ... more data
        }
```

### Required API Keys:

1. **Magic Eden:** https://api.magiceden.dev
2. **Birdeye:** https://public-api.birdeye.so
3. **Helius:** https://helius.dev (Solana RPC)
4. **QuickNode:** https://quicknode.com (Multi-chain RPC)

### Add to .env file:
```bash
MAGIC_EDEN_API_KEY=your_key
BIRDEYE_API_KEY=your_key
HELIUS_RPC_URL=your_url
```

---

## 🎯 UPLOAD TO X402JOBS PLATFORM

### Step 1: Deploy API
Deploy API using Railway/Render/Fly and get public URL.

**Example:** `https://x402jobs-api.up.railway.app`

### Step 2: Update JSON Files
Replace `"url"` in each JSON file with your deployed URL:

```json
"endpoint": {
  "method": "POST",
  "url": "https://x402jobs-api.up.railway.app/nft-floor",
  "headers": {
    "Content-Type": "application/json"
  }
}
```

### Step 3: Upload to x402jobs Platform
1. Go to x402jobs.com
2. Click "Create Job"
3. Upload JSON files
4. Test
5. Publish!

---

## 🐛 TROUBLESHOOTING

### Problem: "Module not found"
```bash
pip install -r requirements.txt
```

### Problem: "Port already in use"
```bash
# Change port
uvicorn x402jobs_api:app --host 0.0.0.0 --port 8001
```

### Problem: "Payment verification failed"
- Will work automatically when testing on x402jobs platform
- Payment bypass enabled for local testing

### Problem: API is slow
- Add caching (Redis)
- Use database (PostgreSQL)
- Use CDN (Cloudflare)

---

## 📊 REVENUE TRACKING

### Simple Logging System:

```python
import logging
from datetime import datetime

# Log each job execution
logging.info(f"Job executed: {job_type} | Amount: ${amount} | Time: {datetime.now()}")
```

### Database Tracking (Optional):

```sql
CREATE TABLE job_executions (
    id SERIAL PRIMARY KEY,
    job_type VARCHAR(50),
    amount DECIMAL(10,2),
    wallet_address VARCHAR(100),
    timestamp TIMESTAMP DEFAULT NOW()
);
```

---

## 🚀 NEXT STEPS

1. ✅ **Local test** - Make sure it works
2. ✅ **Deploy to Railway** - Get public URL
3. ✅ **Update JSONs** - Add deploy URL
4. ✅ **Real data integration** - Get API keys
5. ✅ **Upload to x402jobs** - When hackathon starts
6. ✅ **Marketing** - Announce on Twitter, Discord

---

## 💰 REVENUE EXPECTATIONS

**CONSERVATIVE (Monthly):**
- 5 jobs × 100 executions/day × 30 days = 15,000 executions
- Average $0.08/call = **$1,200/month**

**MEDIUM (Platform grows):**
- 5 jobs × 500 executions/day × 30 days = 75,000 executions
- **$6,000/month**

**AGGRESSIVE (Goes viral):**
- 5 jobs × 2,000 executions/day × 30 days = 300,000 executions
- **$24,000/month**

---

## 📞 SUPPORT

For questions:
- Open GitHub Issues
- Join x402jobs Discord
- Tweet @x402jobs on Twitter

**Good luck! 🚀**
