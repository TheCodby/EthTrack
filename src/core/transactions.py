from web3 import Web3
from web3.exceptions import TransactionNotFound
from datetime import datetime
from typing import Optional
from src.schemas.transaction import EthereumTransaction
import os


class EthTransactionFetcher:
    def __init__(self, provider_url: str):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))

    def get_transaction_info(self, tx_hash: str) -> Optional[EthereumTransaction]:
        if not self.w3.is_connected():
            raise ConnectionError("Not connected to Ethereum network")

        if not tx_hash.startswith('0x'):
            tx_hash = '0x' + tx_hash

        try:
            tx = self.w3.eth.get_transaction(tx_hash)
            receipt = self.w3.eth.get_transaction_receipt(tx_hash)
            block = self.w3.eth.get_block(tx['blockNumber'])

            gas_used = receipt['gasUsed']
            gas_price = tx['gasPrice']
            transaction_fee = gas_used * gas_price

            return EthereumTransaction(
                hash=tx['hash'].hex(),
                nonce=tx['nonce'],
                block_hash=tx['blockHash'].hex(),
                block_number=tx['blockNumber'],
                transaction_index=tx['transactionIndex'],
                from_address=tx['from'],
                to_address=tx['to'],
                value=self.w3.from_wei(tx['value'], 'ether'),
                gas=tx['gas'],
                gas_price=self.w3.from_wei(gas_price, 'gwei'),
                gas_used=gas_used,
                transaction_fee=self.w3.from_wei(transaction_fee, 'ether'),
                input=tx['input'].hex() if isinstance(
                    tx['input'], (bytes, bytearray)) else str(tx['input']),
                status=receipt['status'],
                timestamp=datetime.fromtimestamp(block['timestamp']),
                confirmations=self.w3.eth.block_number - tx['blockNumber']
            )
        except TransactionNotFound:
            return None


def get_eth_fetcher():
    provider_url = os.getenv("ETHEREUM_PROVIDER_URL")
    if not provider_url:
        raise ValueError(
            "ETHEREUM_PROVIDER_URL environment variable is not set")
    return EthTransactionFetcher(provider_url)
