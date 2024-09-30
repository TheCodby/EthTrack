from fastapi import APIRouter, Depends, HTTPException, Path
from src.schemas.transaction import EthereumTransaction
from src.core.transaction import get_eth_fetcher, EthTransactionFetcher

router = APIRouter()


@router.get("/{tx_hash}", response_model=EthereumTransaction)
def get_transaction(tx_hash: str = Path(..., description="Ethereum transaction hash", regex="^0x[a-fA-F0-9]{64}$"), fetcher: EthTransactionFetcher = Depends(get_eth_fetcher)):
    transaction = fetcher.get_transaction_info(tx_hash)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction
