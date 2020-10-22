---
title: "Linux: Fail to signing GPG commit"
date: 2019-09-24T00:15:39+07:00
showDate: true
draft: false
toc: true
comments: true
categories:
- linux
tags:
- repair
---

## Overview
I get error while signing commit to my Github repository

![](https://res.cloudinary.com/bimagv/image/upload/v1603375939/2019-09/2019-09-24img1_xlyj6o.png)

Let's check

- my public & private gpg key
- expiration date of key

  $ git commit -m "initial post"
  error: gpg failed to sign the data
  fatal: failed to write commit object

## Prerequisite
I using **gnupg** program

  $ sudo pacman -S gnupg


## How to?
First, check with **gpg --list-key**

  $ gpg --list-keys
  /home/bima/.gnupg/pubring.kbx
  -----------------------------
  pub   rsa2048 2017-08-27 [SC] [expires: 2019-01-07]
        SF2H3HV35DF35UKC4Q27JKMHGRDR421VBNHTY632A
  uid           [ unknown] Maria Bermon <public@enpore.de>
  sub   rsa2048 2017-08-27 [E]

And this is default gpg key used by system. Make sure your key validation, expiration.

In case your key has expired or don't have an existing GPG key, you can try to create new key

### Generate GPG key 

generate a new GPG key to use for signing commits and tags

    $ gpg --full-gen-key

At the prompt, specify the kind of key you want or press Enter to accept the default RSA and RSA

    Please select what kind of key you want:
        (1) RSA and RSA (default)
        (2) DSA and Elgamal
        (3) DSA (sign only)
        (4) RSA (sign only)
    Your selection? 1

Enter the desired key size. Your key must be at least 4096 bits

    RSA keys may be between 1024 and 4096 bits long.
    What keysize do you want? (2048) 4096
    Requested keysize is 4096 bits

Enter the length of time the key should be valid. Press Enter to specify the default selection, indicating that the key doesn't expire

    Please specify how long the key should be valid.
        0 = key does not expire
        <n>  = key expires in n days
        <n>w = key expires in n weeks
        <n>m = key expires in n months
        <n>y = key expires in n years
    Key is valid for? (0) 0
    Key does not expire at all

Verify that your selections are correct

    Is this correct? (y/N) y

Enter your user ID information

    GnuPG needs to construct a user ID to identify your key.

    Real name: Bima

    Email address: bima@kokom.com
    Comment: my new secret key

    You selected this USER-ID:
        "Bima <bima@kokom.com>"

    Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O

    (Input password)

finish

    gpg: key TH33DG6NVCSFTY3S marked as ultimately trusted
    gpg: revocation certificate stored as '/home/bima/.gnupg/openpgp-revocs.d/SG3GDNFGHDWERTYFSACS32TYUI7TJRJNFTURE43DB.rev'
    public and secret key created and signed.

    pub   rsa4096 2019-09-23 [SC]
          SG3GDNFGHDWERTYFSACS32TYUI7TJRJNFTURE43DBD
    uid                      Bima <bima@kokom.com>
    sub   rsa4096 2018-09-23 [E]

git file config you can find on ~/.gitconfig

    $ vi ~/.gitconfig

Then update signingkey and User ID information

    [user]
      name = bima
      email = bima@kokom.com
      #signingkey = SF2H3HV35DF35UKC4Q27JKMHGRDR421VBNHTY632A
      signingkey = SG3GDNFGHDWERTYFSACS32TYUI7TJRJNFTURE43DB
    [github]
      user = bimagv

Done!

Thats all you need.

### Export GPG key

The optional steps, you can add GPG key to Github for signing commit. 

Check this out:

https://help.github.com/en/enterprise/2.16/user/articles/adding-a-new-gpg-key-to-your-github-account

So, you need to export gpg public key. This command to show gpg public key

    $ gpg --list-secret-keys --keyid-format LONG
    sec   rsa4096/TH33DG6NVCSFTY3S 2019-09-23 [SC]
           SG3GDNFGHDWERTYFSACS32TYUI7TJRJNFTURE43DBD
    uid                 [ultimate] Bima <bima@kokom.com>
    ssb   rsa4096/DS2SGHJ3DFGH43IK 2019-09-23 [E]

and command to export GPG Public Key with the name of ID in section **sec**

    $ gpg --armor --export TH33DG6NVCSFTY3S

    -----BEGIN PGP PUBLIC KEY BLOCK-----

    mQINBFRUAGoBEACuk6ze2V2pZtScf1Ul25N2CX19AeL7sVYwnyrTYuWdG2FmJx4x
    DLTLVUazp2AEm/JhskulL/7VCZPyg7ynf+o20Tu9/6zUD7p0rnQA2k3Dz+7dKHHh
    eEsIl5EZyFy1XodhUnEIjel2nGe6f1OO7Dr3UIEQw5JnkZyqMcbLCu9sM2twFyfa
    a8JNghfjltLJs3/UjJ8ZnGGByMmWxrWQUItMpQjGr99nZf4L+IPxy2i8O8WQewB5

    [... snip - full example below ...]

    fvfidBGruUYC+mTw7CusaCOQbBuZBiYduFgH8hRW97KLmHn0xzB1FV++KI7syo8q
    XGo8Un24WP40IT78XjKO
    =nUop
    -----END PGP PUBLIC KEY BLOCK-----

### Import GPG key
Or you can just import your key.

In additional purposes using the key from internet for check their digital signature against their public key on your keyring. 

You can also importing other people's keys to your keyring. 

When use Archstrike repository, I have to import someone's public key.

![import](https://res.cloudinary.com/bimagv/image/upload/v1603375936/2019-09/fail-to-signing-commit-01_ilyhuf.png)
