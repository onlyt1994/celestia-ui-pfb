# celestia-ui-pfb

Send data to the Celestia Network using your own node and a beautiful UI solution.

To use this solution, you need to run [Celestia Node](https://docs.celestia.org/nodes/light-node/).

Testing on Blockspace Race network.

## How to install?

1) Install the required dependencies:
```
pip install -r requirements.txt
```
2) Specify in the ```envi.py``` in vartiable ```DEFAULT_NODE_URL``` address of the local node
3) Run script:
```
python main.py
```
4) Go to http://127.0.0.1:8000/ and create PayForBlob transaction.