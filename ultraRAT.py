#If you need to run one or a few simple commands and do not mind if their output goes to the console, you can use the os.system() command. If you want to manage the input and output of a shell command, use subsystem.run(). If you want to run a command and continue doing other work while it's being executed, use subprocess.Popen.

import subprocess

def runcommand (cmd):
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True,
                            universal_newlines=True)
    std_out, std_err = proc.communicate()
    return proc.returncode, std_out, std_err

def main():
    print("==================================================");
    print('Check connection"...');
    print("==================================================");
    code, out, err = runcommand("runcommand");
    print("Return code: {}".format(code));
    print("--------------------------------------------------");
    print("stdout:");
    print(out);
    print("--------------------------------------------------");
    print("stderr:");
    print(err);
    print("--------------------------------------------------");


if __name__ == '__main__':
    main()
