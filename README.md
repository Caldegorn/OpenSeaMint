
# OpenSeaMint

Automated NFT minting process on OpenSea using Python.

## Overview

OpenSeaMint is a Python-based tool to automate the minting of NFTs on OpenSea-compatible blockchains. This repository provides a simple and extensible script to interact with NFT smart contracts, upload metadata, and mint NFTs programmatically.

## Features

- Automated NFT minting via smart contract interaction
- Upload and manage NFT metadata (compatible with OpenSea standards)
- Support for Ethereum and compatible networks
- Easy to customize for your own NFT collection

## Prerequisites

- Python 3.7+
- An Ethereum wallet private key with sufficient funds for gas fees
- Access to an Ethereum RPC endpoint (e.g., Infura, Alchemy)
- NFT smart contract deployed on Ethereum or compatible chain
- Metadata and asset files prepared and hosted (e.g., IPFS)

## Installation

1. Clone the repository:

```
git clone https://github.com/Caldegorn/OpenSeaMint.git
cd OpenSeaMint
```

2. (Optional) Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install required dependencies:

```
pip install -r requirements.txt
```

*(If `requirements.txt` is not provided, install manually:)*

```
pip install web3 requests
```

## Usage

1. Configure your wallet private key, RPC endpoint, and NFT contract details inside `mint.py`.

2. Prepare your NFT metadata JSON files and host them on IPFS or another decentralized storage.

3. Run the minting script:

```
python mint.py
```

4. The script will:

- Connect to the Ethereum network
- Interact with your NFT smart contract to mint tokens
- Use the provided metadata URIs for the minted NFTs
- Output transaction hashes and minting status

## Example

```
# Example snippet from mint.py
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

private_key = 'YOUR_PRIVATE_KEY'
contract_address = 'YOUR_NFT_CONTRACT_ADDRESS'
metadata_uri = 'ipfs://QmYourMetadataHash'

# Mint NFT by calling smart contract mint function with metadata_uri
```

## Notes

- Ensure your wallet has enough ETH (or native token) to cover gas fees.
- This script assumes you have a mint function in your smart contract that accepts a metadata URI.
- OpenSea automatically indexes NFTs minted on supported chains; no additional steps needed to list.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve functionality or add features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


