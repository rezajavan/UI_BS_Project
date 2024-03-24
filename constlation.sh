cd code;

sudo ./pdsch_enodeb -o float_d.bin -n 5  -m 9 >/dev/null 2>&1;
cp float_d.bin data_c.bin;
sudo ./pdsch_ue  -i data_c.bin  -r 1234  ;
