##	JV having trouble properly getting modified CMS repo to install from modified selscan repo, so just include as a subdir and hack around scans.py
##	07.25.2019

basecmd = "/app/bin/linux/selscan"
	
import sys
import subprocess

def main():
	if len(sys.argv) != 5:
		print('call program as: python adhoc_runxp.py {in_tped1} {out1} {in_tped2} {out2}')
		sys.exit()
	in_tped1, out_popihh1, in_tped2, out_popihh2 = sys.argv[1:] 
	full_cmd = basecmd + " --xpehh --tped " + in_tped1 + " --out " + out_popihh1 + " --tped-ref " + in_tped2 + " --out2 " + out_popihh2 + " --maf 0.05 --gap-scale 20000 --threads 15 "
	print(full_cmd)
	subprocess.check_output(basecmd.split())

main()

