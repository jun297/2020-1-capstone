# 2020-1-capstone
Yonsei University Team Acafela 2020-1 Software Capstone Design Repository

## Testing NPU architectures via measuring integrated trade-offs
This repository is about 2020-1 capstone design, implementing WS- and OS-architecture NPU on PyNQ-Z2 using Vivado HLS and Vivado and measuring integrated trade-offs

### Vivado HLS

![HLS_C](https://user-images.githubusercontent.com/49740083/84996254-f8bc1b00-b187-11ea-876f-6f6d94aa2a82.JPG "weight stationary architecture implemeted by C in Vivado HLS")

We implemented weight stationary architecture and output stationary architecture using C language. Vivado HLS converts the C source code to IP Core.
### Vivado
Vivado converts the IP Core to bitstream. 
### Jupyter notebook
We overlay the bitstream to the PyNQ-Z2 using python module.
