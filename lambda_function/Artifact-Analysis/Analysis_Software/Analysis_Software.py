import os
import sys

def upload_s3(instance_id,case_time):
    os.system(f"aws s3 cp /home/ec2-user/volatility3/result.txt s3://cumulus-analysis-result/{instance_id}/{case_time}/result.txt")

def write_first_line(output_file,type):
    with open(output_file, 'a',encoding='utf-8') as file:
        file.write(f"\n+- {type}")

def write_second_line(output_file,type):
    with open(output_file, 'a',encoding='utf-8') as file:
        file.write(f"\n+-- {type}\n")

def ascii_art(output_file):
    with open(output_file, 'w',encoding='utf-8') as file:
        file.write(open('/home/ec2-user/volatility3/ascii_art.txt','r').read())

def run_command_and_save_result(command, output_file):
    try:
        result = '|    '
        result += os.popen(command).read()

        formatted_result = '|    '.join(result.splitlines(True))

        with open(output_file, 'a', encoding='utf-8') as file:
            file.write(f"+--- {command}{formatted_result}")
            file.write(f"|\n")
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        print(f"Skipping command execution for: {command}")

def run_vola_and_save_result(command, output_file):
    result = '|    '
    result += os.popen(command).read()

    formatted_result = '|    '.join(result.splitlines(True))

    with open(output_file, 'a',encoding='utf-8') as file:
        file.write(f"+--- {command}{formatted_result}")
        file.write(f"|\n")

def download_lime_file(instance_id,case_time):
    command = f'aws s3 cp s3://cumulus-forensic-artifact/{instance_id}/{case_time}/memory/{instance_id}.lime /home/ec2-user/volatility3/tmp.lime'    
    os.system(command)
 
def command_artifact(output_file):
    s3 = f'aws s3 cp s3://cumulus-forensic-artifact/{instance_id}/{case_time}/command/'
    command_output = [
        'date.txt',
        'uname_output.txt',
        'ifconfig_output.txt',
        'ps_ef_output.txt',
        'netstat_output.txt',
        'lsof_output.txt',
        'netstat_rn_route_output.txt',
        'df_mount_output.txt',
        'free_output.txt',
        'w_output.txt',
        'last_output.txt',
        'lsmod_output.txt',
        'passwd_output.txt',
        'shadow_output.txt',
        'find_output.txt',
        'history_output.txt',
        'lastlog_output.txt',
        'ps_aux_output.txt'
    ]
    command = [
        'date',
        'uname -a',
        'ifconfig -a || ip a',
        'ps -ef',
        'netstat -anp',
        'lsof -V',
        'netstat -rn && route',
        'df && mount',
        'free',
        'w',
        'last -Faiwx',
        'lsmod',
        'cat /etc/passwd',
        'cat /etc/shadow',
        'find /directory -type f -mtime -1 -print',
        'history | less',
        'lastlog',
        'ps aux'
    ]
    
    with open(output_file, 'a',encoding='utf-8') as file:
        for cmd_output, cmd in zip(command_output, command):
            result ='\n'
            result += os.popen(f'{s3}{cmd_output} -').read()
            formatted_result = '|    '.join(result.splitlines(True))
            file.write(f"+--- {cmd}{formatted_result}")
            file.write(f"|")


if __name__ == "__main__":
    output_file_name = f"/home/ec2-user/volatility3/result.txt" # 결과 TXT
    vola_command_file = f"/home/ec2-user/volatility3/vola_line.txt" # 볼라틸리티 치트시트
    command_file = f"/home/ec2-user/volatility3/command_line.txt" # 커맨트 치트시트

    #인스턴스 ID랑 TIME 인자로 받기
    instance_id = sys.argv[1]
    case_time= sys.argv[2]
    
    #아스키 아트
    ascii_art(output_file_name)

    #메모리 채증한거 다운로드
    download_lime_file(instance_id,case_time)

    #그냥 선 긋기
    write_first_line(output_file_name,"Volatile Artifact Analysis")
    write_second_line(output_file_name,"Analyzing Memory Dump")

    #볼라 명령어 내용 적기
    with open(vola_command_file, 'r',encoding='utf-8') as file:
        for line in file:
            run_vola_and_save_result(line, output_file_name)

    write_second_line(output_file_name,"Analyzing Network, history, log")

    command_artifact(output_file_name)

    write_first_line(output_file_name,"Non-volatile Artifacts analysis")
    write_second_line(output_file_name,"Analyzing Log")

    #런커맨드 명령어 내용 적기
    with open(command_file, 'r',encoding='utf-8') as file:
        for line in file:
            run_command_and_save_result(line, output_file_name)

    upload_s3(instance_id,case_time)
