//filter 25 ofmap 25
void ws_25_25(float ifMap[49], float ofMap[25], float filter[25],int H, int R) {
    #pragma HLS INTERFACE s_axilite port=ifMap
    #pragma HLS INTERFACE s_axilite port=ofMap
    #pragma HLS INTERFACE s_axilite port=filter
    #pragma HLS INTERFACE s_axilite port=H
    #pragma HLS INTERFACE s_axilite port=R
    #pragma HLS INTERFACE ap_ctrl_none port=return
   float PEWeight[25];
   float PEPsum[25];
   #pragma HLS array_partition variable=PEWeight complete
   #pragma HLS array_partition variable=PEPsum complete
   for (int i=0;i<25;i++)
   {
      PEWeight[i]=filter[i];
   }
         for (int cycle = 0; cycle < 49; cycle++)
      {
         const float iact = ifMap[cycle];
         for (int j = 24; j >=1; j--)
         {
            #pragma HLS unroll
            PEPsum[j] = PEPsum[j - 1] + (iact*PEWeight[j]);
         }
         PEPsum[0]=iact*PEWeight[0];
         if (cycle + 1 >= 25)
         {
            ofMap[cycle-24] = PEPsum[24];
         }
      }
}
