
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import re


class EthereumTransaction(BaseModel):
    hash: str = Field(..., description="Transaction hash")
    nonce: int = Field(...,
                       description="Number of transactions sent from this address")
    block_hash: str = Field(...,
                            description="Hash of the block containing this transaction")
    block_number: int = Field(...,
                              description="Number of the block containing this transaction")
    transaction_index: int = Field(...,
                                   description="Index of the transaction in the block")
    from_address: str = Field(..., description="Address of the sender")
    to_address: Optional[str] = Field(
        None, description="Address of the recipient (None for contract creation)")
    value: float = Field(..., description="Amount of Ether transferred")
    gas: int = Field(..., description="Gas provided for the transaction")
    gas_price: float = Field(..., description="Gas price in Gwei")
    gas_used: int = Field(...,
                          description="Amount of gas used by the transaction")
    transaction_fee: float = Field(...,
                                   description="Total transaction fee in Ether")
    input: str = Field(..., description="Data sent along with the transaction")
    status: int = Field(...,
                        description="Status of the transaction (1: success, 0: failure)")
    timestamp: datetime = Field(
        ..., description="Timestamp of the block containing the transaction")
    confirmations: int = Field(...,
                               description="Number of confirmations for the transaction")
