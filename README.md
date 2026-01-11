# 🚀 X402Jobs Web3 API

**Pay-per-use Web3 data and analytics jobs powered by x402 protocol**

> Wallet: `8UT7S3acWenLuEuqFPwoAGDT6vFGrGiGz3JM6NK3rXKw`  
> Network: Solana Mainnet  
> Protocol: x402 (HTTP 402 Payment Required)

---

## 🎯 About This Project

Comprehensive API system with 5 different Web3 jobs. Each job operates with micropayments via x402 protocol.

### 💎 Jobs and Pricing

| Job | Price | Description |
|-----|-------|-------------|
| **NFT Floor Tracker** | $0.02 | Real-time NFT collection floor price tracking |
| **Token Safety Scorer** | $0.05 | Token security analysis (honeypot, rugpull detection) |
| **DeFi Yield Optimizer** | $0.10 | Find best APY opportunities across protocols |
| **Whale Wallet Monitor** | $0.15 | Track large wallets and smart money |
| **Token Launch Detector** | $0.08 | Real-time detection of new token launches |

---

## ⚡ Quick Start

### 1. Installation

```bash
# Clone repository
git clone https://github.com/airhotschild/x402jobs-api
cd x402jobs-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Run

```bash
python x402jobs_api.py
```

API is now running at: https://x402jobs-api-production.up.railway.app

### 3. Test

```bash
python test_api.py
```

---

## 📡 API Endpoints

### Genel Bilgi
```bash
GET /              # API info
GET /health        # Health check
GET /pricing       # Fiyat listesi
```

### Jobs
```bash
POST /nft-floor         # NFT Floor Tracker ($0.02)
POST /token-safety      # Token Safety Scorer ($0.05)
POST /yield-optimizer   # Yield Optimizer ($0.10)
POST /whale-monitor     # Whale Monitor ($0.15)
POST /token-launches    # Launch Detector ($0.08)
```

---

## 📖 Usage Examples

### NFT Floor Price
```bash
curl -X POST https://x402jobs-api-production.up.railway.app/nft-floor \
  -H "Content-Type: application/json" \
  -d '{
    "collection_address": "J1S9H3QjnRtBbbuD4HjPV6RpRhwuk4zKbxsnCHuTgh9w",
    "marketplace": "all"
  }'
```

### Token Safety Check
```bash
curl -X POST https://x402jobs-api-production.up.railway.app/token-safety \
  -H "Content-Type: application/json" \
  -d '{
    "token_address": "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
    "blockchain": "solana"
  }'
```

---

## 🌐 Deployment

### Railway (Recommended)
1. Go to https://railway.app
2. "New Project" → "Deploy from GitHub"
3. Auto-deploy!

### Render
1. Go to https://render.com
2. "New Web Service"
3. Connect GitHub repo
4. Deploy!

### Docker
```bash
docker build -t x402jobs-api .
docker run -p 8000:8000 x402jobs-api
```

Detailed deployment guide: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

---

## 📁 Project Structure

```
x402jobs-api/
├── x402jobs_api.py          # Main API code
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker config
├── .env.example            # Environment variables
├── test_api.py             # Test script
├── DEPLOYMENT_GUIDE.md     # Detailed deployment guide
├── README.md               # This file
└── jobs/                   # JSON job definitions
    ├── nft-floor-tracker.json
    ├── token-safety-scorer.json
    ├── defi-yield-optimizer.json
    ├── whale-wallet-monitor.json
    └── token-launch-detector.json
```

---

## 🔧 Development

### Real Data Integration

Currently API returns placeholder data. To integrate real data, get API keys:

1. **Magic Eden:** https://api.magiceden.dev
2. **Birdeye:** https://public-api.birdeye.so
3. **Helius:** https://helius.dev
4. **QuickNode:** https://quicknode.com

Add to `.env` file:
```bash
MAGIC_EDEN_API_KEY=your_key
BIRDEYE_API_KEY=your_key
HELIUS_RPC_URL=your_url
```

---

## 💰 Revenue Potential

| Scenario | Executions/Day | Monthly Revenue |
|---------|----------------|-----------------|
| **Conservative** | 100/job | $1,200 |
| **Medium** | 500/job | $6,000 |
| **Aggressive** | 2,000/job | $24,000 |

---

## 🎯 Hackathon Strategy

1. ✅ **Deploy API** (Railway/Render)
2. ✅ **Update JSON files** (add deploy URL)
3. ✅ **Upload to x402jobs platform**
4. ✅ **Test**
5. ✅ **Marketing** (Twitter, Discord)

---

## 📄 Lisans

MIT License

---

## 🤝 Contributing

Pull requests are welcome!

1. Fork the repo
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📞 Contact

- GitHub: [@airhotschild](https://github.com/airhotschild)
- Twitter/X: [@airhotschild](https://twitter.com/airhotschild)
- Discord: airhotschild
- Telegram: [@airhotschild](https://t.me/airhotschild)
- Email: airhotschild@gmail.com

---

## 🙏 Thanks

- Coinbase x402 team
- Solana Foundation
- x402jobs platform

---

**⭐ Star this repo if you find it useful!**

Made with ❤️ for Web3
