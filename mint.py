<?php
require 'vendor/autoload.php';

use Web3\Web3;
use Web3\Contract;
use Web3p\EthereumTx\Transaction;

$rpcUrl = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID';
$web3 = new Web3($rpcUrl);

// Your wallet address and private key (handle securely!)
$fromAddress = '0xYourWalletAddress';
$privateKey = 'your_private_key';

// NFT contract address and ABI
$contractAddress = '0xYourNFTContractAddress';
$contractAbi = json_decode(file_get_contents('path_to_abi.json'), true);

$contract = new Contract($web3->provider, $contractAbi);

// Prepare mint transaction data (example mint function)
$toAddress = '0xRecipientAddress';
$tokenURI = 'ipfs://QmYourMetadataHash';

$mintData = $contract->getData('mint', $toAddress, $tokenURI);

// Get nonce
$web3->eth->getTransactionCount($fromAddress, function ($err, $nonce) use (&$nonceVal) {
    if ($err !== null) {
        throw new Exception($err->getMessage());
    }
    $nonceVal = $nonce;
});

// Build transaction
$txParams = [
    'nonce' => '0x' . dechex($nonceVal),
    'to' => $contractAddress,
    'gas' => '0x5208', // 21000 gas limit (adjust as needed)
    'gasPrice' => '0x3B9ACA00', // 1 Gwei (adjust as needed)
    'value' => '0x0',
    'data' => $mintData,
    'chainId' => 1 // Ethereum mainnet
];

// Sign and send transaction (use EthereumTx or similar library)
$transaction = new Transaction($txParams);
$signedTx = '0x' . $transaction->sign($privateKey);

// Send raw transaction
$web3->eth->sendRawTransaction($signedTx, function ($err, $txHash) {
    if ($err !== null) {
        echo 'Error: ' . $err->getMessage();
        return;
    }
    echo 'Transaction hash: ' . $txHash;
});
