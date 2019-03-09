import wmi
import paramiko
import os
import logging as log

class process_watcher:
    def __init__(self):
        self.proc_list = []
        log.basicConfig(format = '[ %(levelname)s ] %(message)s',
        level = log.INFO, stream = sys.stdout)
    
    def run_benchmark_on_all_machines(self, machine_list, server_ip,
                                      server_login, server_psw):
        for machine in machine_list:
            log.info('Run benchmark on {} machine'.format(machine.ip))
            run_benchmark(machine, server_ip, server_login,
                server_psw)
        log.info('Benchmark run on all machines')   

    def run_benchmark(self, machine, server_ip, server_login, server_psw):
        if machine.os_type == 'Windows':
            run_on_windows(machine, server_ip, server_login, server_psw)
        elif machine.os_type == 'Linux':
            run_on_linux(machine, server_ip, server_login, server_psw)


    def run_on_linux(self, machine, server_ip, server_login, server_psw): 
        paramiko_con = paramiko.SSHClient()
        paramiko_con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        paramiko_con.connect(hostname=machine.ip, username=machine.login,
            password=machine.psw)
        paramiko_con.exec_command(('python {} -ip {} -l {} -p {} -env {} -b {} ' +
            '-os {} --res_file {} --log_file {}').format(machine.path_to_ftp_client,
            server_ip, server_login, server_psw, machine.path_to_OpenVINO_env,
            machine.benchmark_config, machine.os_type, machine.res_file,
            machine.log_file))
        paramiko_con.close()


    def run_on_windows(self, machine, server_ip, server_login, server_psw):
        wmi_con = wmi.WMI(machine.ip, user=machine.login, password=machine.psw)
        process_startup = wmi_con.Win32_ProcessStartup.new()
        process_id, result = wmi_con.Win32_Process.Create(CommandLine=((
            'cmd.exe /c python {} -ip {} -l {} -p {} -env {} -b {} ' +
            '-os {} --res_file {} --log_file {}').format(machine.path_to_ftp_client,
            server_ip, server_login, server_psw, machine.path_to_OpenVINO_env,
            machine.benchmark_config, machine.os_type, machine.res_file,
            machine.log_file)), ProcessStartupInformation=process_startup)
        if result == 0:
            log.info('Process started successfully {}'.format(process_id))
        else:
            log.info('Problem creating process {}'.format(result))
