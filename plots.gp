set terminal png
set output "plot.png"
unset key
plot 'ASLR-test-parsed.dat'
set output "plot2.png"
plot [2e6:2e7] 'ASLR-test-parsed.dat'
