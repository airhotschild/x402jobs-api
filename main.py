"""
X402Jobs API - Main Application
FastAPI backend for X402 job processing system
"""

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List
import os
from datetime import datetime

# Create FastAPI app
app = FastAPI(
    title="X402Jobs API",
    description="Blockchain analytics and automation API powered by $JOBS token",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# PYDANTIC MODELS
# ============================================================================

class NFTFloorRequest(BaseModel):
    collection_address: str
    marketplace: str = "all"
    include_volume: bool = True

class TokenSafetyRequest(BaseModel):
    token_address: str
    blockchain: str = "solana"
    deep_scan: bool = False

class YieldOptimizerRequest(BaseModel):
    token_type: str
    amount: float
    risk_tolerance: str = "moderate"
    min_apy: float = 0.0

class WhaleMonitorRequest(BaseModel):
    action: str
    wallet_address: str
    time_range: str = "24h"

class TokenLaunchRequest(BaseModel):
    time_range: str = "1h"
    blockchain: str = "solana"
    min_liquidity_usd: float = 5000.0
    safety_filter: bool = True
    limit: int = 20

# ============================================================================
# ENDPOINTS
# ============================================================================

@app.get("/")
async def root():
    """Root endpoint - API info"""
    return {
        "service": "X402Jobs API",
        "version": "1.0.0",
        "status": "operational",
        "powered_by": "$JOBS Token",
        "endpoints": {
            "health": "/health",
            "pricing": "/pricing",
            "jobs": [
                "/nft-floor",
                "/token-safety",
                "/yield-optimizer",
                "/whale-monitor",
                "/token-launches"
            ]
        },
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "x402jobs-api",
        "uptime": "operational"
    }

@app.get("/pricing")
async def get_pricing():
    """Get pricing information for all jobs"""
    return {
        "currency": "$JOBS",
        "jobs": {
            "nft_floor_tracker": {
                "cost_per_request": 100,
                "description": "Real-time NFT floor price tracking"
            },
            "token_safety_scorer": {
                "cost_per_request": 50,
                "description": "Token safety analysis and risk scoring"
            },
            "yield_optimizer": {
                "cost_per_request": 200,
                "description": "DeFi yield optimization recommendations"
            },
            "whale_monitor": {
                "cost_per_request": 150,
                "description": "Whale wallet activity monitoring"
            },
            "token_launch_detector": {
                "cost_per_request": 250,
                "description": "New token launch detection and analysis"
            }
        },
        "note": "Payments processed via Solana blockchain"
    }

@app.post("/nft-floor")
async def nft_floor_tracker(request: NFTFloorRequest):
    """NFT Floor Price Tracker - Requires payment"""
    # Payment check (placeholder)
    raise HTTPException(
        status_code=402,
        detail={
            "error": "Payment Required",
            "job": "nft_floor_tracker",
            "cost": 100,
            "currency": "$JOBS",
            "payment_address": "JOBS_TREASURY_ADDRESS_HERE",
            "instructions": "Send 100 $JOBS to proceed"
        }
    )

@app.post("/token-safety")
async def token_safety_scorer(request: TokenSafetyRequest):
    """Token Safety Scorer - Requires payment"""
    raise HTTPException(
        status_code=402,
        detail={
            "error": "Payment Required",
            "job": "token_safety_scorer",
            "cost": 50,
            "currency": "$JOBS",
            "payment_address": "JOBS_TREASURY_ADDRESS_HERE",
            "instructions": "Send 50 $JOBS to proceed"
        }
    )

@app.post("/yield-optimizer")
async def yield_optimizer(request: YieldOptimizerRequest):
    """DeFi Yield Optimizer - Requires payment"""
    raise HTTPException(
        status_code=402,
        detail={
            "error": "Payment Required",
            "job": "yield_optimizer",
            "cost": 200,
            "currency": "$JOBS",
            "payment_address": "JOBS_TREASURY_ADDRESS_HERE",
            "instructions": "Send 200 $JOBS to proceed"
        }
    )

@app.post("/whale-monitor")
async def whale_monitor(request: WhaleMonitorRequest):
    """Whale Wallet Monitor - Requires payment"""
    raise HTTPException(
        status_code=402,
        detail={
            "error": "Payment Required",
            "job": "whale_monitor",
            "cost": 150,
            "currency": "$JOBS",
            "payment_address": "JOBS_TREASURY_ADDRESS_HERE",
            "instructions": "Send 150 $JOBS to proceed"
        }
    )

@app.post("/token-launches")
async def token_launch_detector(request: TokenLaunchRequest):
    """Token Launch Detector - Requires payment"""
    raise HTTPException(
        status_code=402,
        detail={
            "error": "Payment Required",
            "job": "token_launch_detector",
            "cost": 250,
            "currency": "$JOBS",
            "payment_address": "JOBS_TREASURY_ADDRESS_HERE",
            "instructions": "Send 250 $JOBS to proceed"
        }
    )

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.exception_handler(404)
async def not_found_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Endpoint not found",
            "path": str(request.url.path),
            "available_endpoints": ["/", "/health", "/pricing", "/nft-floor", "/token-safety", "/yield-optimizer", "/whale-monitor", "/token-launches"]
        }
    )

# ============================================================================
# STARTUP
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
