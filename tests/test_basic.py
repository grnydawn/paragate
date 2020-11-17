from paragate import Paragate
from tempfile import TemporaryDirectory

def test_basic():
    prj = Paragate()

    cmd = "input @1 --forward '@x=2'"
    ret, fwds = prj.run_command(cmd)

    assert ret == 0

def test_print(capsys):
    prj = Paragate()

    cmd = "-- input @1 --forward '@x=2' -- print @x @data[0]"
    ret, fwds = prj.run_command(cmd)

    assert ret == 0

    captured = capsys.readouterr()
    assert captured.out == "21\n"
    assert captured.err == ""

def test_default_init(capsys):
    prj = Paragate()

    with TemporaryDirectory() as tmp:
        import pdb; pdb.set_trace()
        cmd = "-- init " + tmp
        ret, fwds = prj.run_command(cmd)

        assert ret == 0

        captured = capsys.readouterr()
        assert captured.out == "default task is initialized.\n"
        assert captured.err == ""
