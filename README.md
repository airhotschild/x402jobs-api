# x402jobs-api

**Pay-per-use Web3 Analytics API** powered by the x402 micropayment protocol.

Delivers 5 practical on-chain jobs with real utility through fair micropayments.

## 🎯 About This Project

x402jobs-api is a production-ready API that provides high-quality Web3 data and analytics. Users only pay for the jobs they use via the **x402 protocol** (HTTP 402 Payment Required) on Solana.

> **Payment Wallet:** `8UT7S3acWenLuEuqFPwoAGDT6vFGrGiGz3JM6NK3rXKw`  
> **Network:** Solana Mainnet

## 💎 Available Jobs

| Job                        | Price   | Description                                      |
|---------------------------|---------|--------------------------------------------------|
| **NFT Floor Tracker**     | $0.02  | Real-time NFT collection floor price tracking    |
| **Token Safety Scorer**   | $0.05  | Honeypot & rugpull detection                     |
| **DeFi Yield Optimizer**  | $0.10  | Smart yield opportunity suggestions              |
| **Whale Wallet Monitor**  | $0.15  | Track large/smart money wallet movements         |
| **Token Launch Detector** | $0.08  | Early detection of new token launches            |

## 🛠 Technologies

- Python + FastAPI
- x402 Micropayment Protocol
- Solana Web3
- Railway / Docker deployment

## ⚡ Quick Start

```bash
git clone https://github.com/airhotschild/x402jobs-api.git
cd x402jobs-api

python -m venv venv
source venv/bin/activate    # Mac/Linux
# venv\Scripts\activate     # Windows

pip install -r requirements.txt
cp env.example .env
# Fill your .env variables

python x402jobs_api.py
Live Demo → https://x402jobs-api-production.up.railway.app
Roadmap
•  AI-powered sentiment analysis jobs
•  Multi-chain support (Ethereum, Base…)
•  Web dashboard
•  Official SDKs (JS, Python)

Built with ❤️ for the Web3 ecosystem
Actively maintained by @airhotschild
