# InfinityEKPayloadDecrypter

From [Diving into a Silverlight Exploit and Shellcode – Analysis and Techniques](http://www.checkpoint.com/downloads/partners/TCC-Silverlight-Jan2015.pdf):

> ... We decided to translate this Assembly code into a Python script and write a generic tool
> decrypting payloads from Infinity (using the encrypted payload and the key as parameters).

This is the Python script.

If you have the encrypted payload, let’s say from a PCAP file, it isn’t a problem to find the key also since it is hardcoded in the shellcode a few packets before. 


Usage:
```python
InfinityPayloadDecrypter.py <encoded_file> <output_file> <key>
```
