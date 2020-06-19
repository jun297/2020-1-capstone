# 2020-1-capstone
Yonsei University Team Acafela 2020-1 Software Capstone Design Repository

## Testing NPU architectures via measuring integrated trade-offs
This repository is about 2020-1 capstone design, implementing WS- and OS-architecture NPU on PyNQ-Z2 using Vivado HLS and Vivado and measuring integrated trade-offs

### Vivado HLS

![HLS_C](https://user-images.githubusercontent.com/49740083/84996254-f8bc1b00-b187-11ea-876f-6f6d94aa2a82.JPG "weight stationary architecture implemeted by C in Vivado HLS")

We implemented weight stationary architecture and output stationary architecture using C language. Vivado HLS converts the C source code to IP Core.
### Vivado

![Vivado](https://user-images.githubusercontent.com/49740083/85006258-d977ba80-b194-11ea-8b44-4e98a9e7843e.JPG "IP Core of ws architecture and black design in Vivado")

Vivado converts the IP Core to bitstream. 
![powerre](https://user-images.githubusercontent.com/49740083/85008108-763b5780-b197-11ea-8e89-2231cc0a8b54.JPG "power report")
Power report of Vivado shows the power estimation according to the logic implented by us.
### Jupyter notebook
We overlaied the bitstream to the PyNQ-Z2 using python module and measured the processing time of 1-D convolution operation which is accelerated by ws- and os- architecture NPU.
## Contributors
Junhyeok Kim (Yonsei University)<br>
Yoonsuk Jung (Yonsei University)<br>
Hyeonkyu Kim (Yonsei University)<br>
<br>
Jounghoo Lee (TA for Capstone Design, High Performance Computing Platform Lab (https://hpcp.yonsei.ac.kr/), Yonsei Univeristy) <br>
Prof. Youngsok Kim (High Performance Computing Platform Lab (https://hpcp.yonsei.ac.kr/), Yonsei Univeristy) <br>

