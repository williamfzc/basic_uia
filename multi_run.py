import config as cf
import argparse
import subprocess


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--device', help="YOUR DEVICE ID LIST")
parser.add_argument('-t', '--task', help="YOUR TASK NAME")


if __name__ == '__main__':
    outside_args = parser.parse_args()
    device_list = outside_args.device.split(',')
    task_name = outside_args.task
    print(device_list, task_name)
    process_list = list()
    for each_device in device_list:
        each_task_name = '{}_{}'.format(task_name, each_device)
        cmd_list = ['python', cf.ENTRY_PYTHON_FILE,
                    '-d', each_device,
                    '-t', each_task_name]
        cmd_str = ' '.join(cmd_list)
        each_process = subprocess.Popen(cmd_str)
        process_list.append(each_process)
        print('Device {} start test now.'.format(each_device))
    for _ in process_list:
        try:
            _.communicate()
        except subprocess.TimeoutExpired:
            _.terminate()
    print('all test end.')
