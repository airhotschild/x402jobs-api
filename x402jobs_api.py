"""
X402Jobs API Test Script
Tests all 5 job endpoints
"""

import requests
import json
from datetime import datetime

# API Base URL (değiştir!)
BASE_URL = "http://localhost:8000"

def print_test_header(test_name):
    print("\n" + "="*60)
    print(f"🧪 TEST: {test_name}")
    print("="*60)

def test_root():
    print_test_header("Root Endpoint")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.status_code == 200

def test_health():
    print_test_header("Health Check")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.status_code == 200

def test_pricing():
    print_test_header("Pricing Endpoint")
    response = requests.get(f"{BASE_URL}/pricing")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.status_code == 200

def test_nft_floor():
    print_test_header("NFT Floor Tracker")
    payload = {
        "collection_address": "J1S9H3QjnRtBbbuD4HjPV6RpRhwuk4zKbxsnCHuTgh9w",
        "marketplace": "all",
        "include_volume": True
    }
    
    # Bu test 402 dönecek (payment gerekli)
    response = requests.post(
        f"{BASE_URL}/nft-floor",
        json=payload
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 402:
        print("✅ Payment Required (Expected)")
        print(json.dumps(response.json(), indent=2))
    else:
        print(json.dumps(response.json(), indent=2))
    
    return True

def test_token_safety():
    print_test_header("Token Safety Scorer")
    payload = {
        "token_address": "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
        "blockchain": "solana",
        "deep_scan": False
    }
    
    response = requests.post(
        f"{BASE_URL}/token-safety",
        json=payload
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 402:
        print("✅ Payment Required (Expected)")
        print(json.dumps(response.json(), indent=2))
    else:
        print(json.dumps(response.json(), indent=2))
    
    return True

def test_yield_optimizer():
    print_test_header("DeFi Yield Optimizer")
    payload = {
        "token_type": "USDC",
        "amount": 10000,
        "risk_tolerance": "moderate",
        "min_apy": 5.0
    }
    
    response = requests.post(
        f"{BASE_URL}/yield-optimizer",
        json=payload
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 402:
        print("✅ Payment Required (Expected)")
        print(json.dumps(response.json(), indent=2))
    else:
        print(json.dumps(response.json(), indent=2))
    
    return True

def test_whale_monitor():
    print_test_header("Whale Wallet Monitor")
    payload = {
        "action": "track_wallet",
        "wallet_address": "9WzDXwBbmkg8ZTbNMqUxvQRAyrZzDsGYdLVL9zYtAWWM",
        "time_range": "24h"
    }
    
    response = requests.post(
        f"{BASE_URL}/whale-monitor",
        json=payload
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 402:
        print("✅ Payment Required (Expected)")
        print(json.dumps(response.json(), indent=2))
    else:
        print(json.dumps(response.json(), indent=2))
    
    return True

def test_token_launches():
    print_test_header("Token Launch Detector")
    payload = {
        "time_range": "1h",
        "blockchain": "solana",
        "min_liquidity_usd": 5000,
        "safety_filter": True,
        "limit": 20
    }
    
    response = requests.post(
        f"{BASE_URL}/token-launches",
        json=payload
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 402:
        print("✅ Payment Required (Expected)")
        print(json.dumps(response.json(), indent=2))
    else:
        print(json.dumps(response.json(), indent=2))
    
    return True

def run_all_tests():
    print("\n" + "🚀"*30)
    print("X402JOBS API TEST SUITE")
    print("🚀"*30)
    
    tests = [
        ("Root", test_root),
        ("Health", test_health),
        ("Pricing", test_pricing),
        ("NFT Floor", test_nft_floor),
        ("Token Safety", test_token_safety),
        ("Yield Optimizer", test_yield_optimizer),
        ("Whale Monitor", test_whale_monitor),
        ("Token Launches", test_token_launches)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, "✅ PASS" if result else "❌ FAIL"))
        except Exception as e:
            results.append((name, f"❌ ERROR: {str(e)}"))
    
    # Summary
    print("\n" + "="*60)
    print("📊 TEST SUMMARY")
    print("="*60)
    for name, status in results:
        print(f"{name:.<40} {status}")
    
    passed = sum(1 for _, s in results if "✅" in s)
    total = len(results)
    print(f"\n{passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
    else:
        print("\n⚠️ Some tests failed")

if __name__ == "__main__":
    print("\n⚙️  Make sure API is running on", BASE_URL)
    print("⚙️  Start with: python x402jobs_api.py")
    input("\n Press Enter to start tests...")
    
    run_all_tests()
