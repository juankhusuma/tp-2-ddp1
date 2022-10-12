import subprocess

case = ['python ./grep.py "mat_pag" mydir',
        'python ./grep.py "mat_pag" mydir/file1.txt',
        'python ./grep.py -w "olahraga" mydir',
        'python ./grep.py -i "PaGi" mydir/file1.txt',
        'python ./grep.py -i "MaT_PaG" mydir/file1.txt',
        'python ./grep.py -i "olahraga" mydir',
        'python ./grep.py -w "Bul*kis" mydir',
        'python ./grep.py -w "bul*kis" mydir',
        'python ./grep.py -w "Bulutangkis*" mydir',
        'python ./grep.py "hariberjalan" mydir',
        'python ./grep.py -i "Ol*gA" mydir',
        'python ./grep.py -w "albuminoid" mydir2', ]

for i, c in enumerate(case):
    title = f"[Testing case {i + 1}]"
    print(f"{title:^100s}")
    print(f"\n{''.join(c)}\n")
    print("="*100)
    subprocess.run([k.replace("_", " ").replace("\"", "") for k in c.split()])
    print("\n")
