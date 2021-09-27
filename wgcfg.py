#!/usr/bin/python
import subprocess

#Generate Private Key for WG
def genKey():
    process=subprocess.run(["wg", "genkey"],
                             check=True,
                             capture_output=True)
    priv_key=process.stdout
    print("priv:  ", priv_key.decode("utf-8"))
    return(priv_key)

#Generate Public Key for Wireguard using a valid privatekey
def genPub(priv_key):
    process=subprocess.run(["wg", "pubkey"],
                             input=priv_key,
                             capture_output=True,)
    pub_key=process.stdout
    print("pub:  ", pub_key.decode("utf-8"))
    return(pub_key)


if __name__ == "__main__":
    genPub(genKey())
