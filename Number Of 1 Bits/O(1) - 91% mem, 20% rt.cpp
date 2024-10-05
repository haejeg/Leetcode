class Solution {
public:
    int hammingWeight(int n) {
        int mask = 0x01;
        mask = mask | mask<<4;
        mask = mask | mask<<8;
        mask = mask | mask<<16;
        int col1 = n & mask; //first column
        // only requires shifting 3 times. since 0x1 is already at the first column
        mask = mask<<1;
        int col2 = n & mask;
        mask = mask<<1;
        int col3 = n & mask;
        mask = mask<<1;
        int col4 = n & mask;
        //needs to shift back the amount it was originally shifted in mask
        int finalcol = col1 + (col2>>1) + (col3>>2) + (col4>>3); 
        return (finalcol & 0xF) + ((finalcol>>4) & 0xF) + ((finalcol>>8) & 0xF) + ((finalcol>>12) & 0xF) + ((finalcol>>16) & 0xF) + ((finalcol>>20) & 0xF) + ((finalcol>>24) & 0xF) + ((finalcol>>28) & 0xF);
    }
};