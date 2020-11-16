"""main entry for paragate command-line interface"""

def main():
    from paragate import Paragate
    ret, fwds = Paragate().run_command()
    return ret

if __name__ == "__main__":
    main()
