## setup instructions

first dowload our repo and navigate there using your command line.

```sh
cd ~/Desktop/shopping-cart
```

create a virtual environment with the packages and modules you will need to run our app

```sh
conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
```

after creating this environment, go ahead and install all the packages found in our "requirements.txt" file

```sh
pip install -r requirements.txt
```
## running the app

at this point you should be able to run our application without any hiccups. We recommend that you research the ticker of your desired stock before commencing

```sh
python app/shopping_cart.py
```

Step 1: input your desired product identifier
Step 2: repeat until satisfied
additional note: when inputing new product identifier please input all requested information. Once you have added the new product please re-enter the identifier to add it to the receipt
Step 3: when you have finished checking out enter DONE as the product identifier

Enjoy your list