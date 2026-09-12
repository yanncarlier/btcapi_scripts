

https://iancoleman.io/bip39/  

https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html  

https://mempool.space/  

https://bitinfocharts.com/bitcoin/address/  



bc1q8tet66yh0jf7eauv7k22sd7jx0qa9wq36acdev

bc1qxuy8c9t8anc33wya6lxzk29dkctud6sxqr88ud




```
python create_transaction.py \
  --private-key 41f41d69260df4cf277826a9b65a3717e4eeddbeedf637f212ca096576479361 \
  --source bc1p5cyxnuxmeuwuvkwfem96lqzszd02n6xdcjrs20cac6yqjjwudpxqkedrcr \
  --txid PREVIOUS_TRANSACTION_ID \
  --vout 0 \
  --input-sats 100000 \
  --destination bc1qa3tjj9fc7n0j3lnfuc56tqdhlqrt0uw0czrkm6 \
  --amount-sats 90000 \
  --fee-sats 1000 \
  --change-address bc1qa3tjj9fc7n0j3lnfuc56tqdhlqrt0uw0czrkm6
```


```
# Auto-fetch UTXO from mempool.space (uses largest UTXO)
python create_transaction.py --private-key <key> --source <addr> --destination <dest> --amount-sats 1000 --fee-sats 250 --network testnet

# Auto-fetch but use 2nd largest UTXO
python create_transaction.py ... --utxo-index 1

# Manual UTXO specification (old behavior still works)
python create_transaction.py ... --txid <txid> --vout 0 --input-sats 5000 ...
```

