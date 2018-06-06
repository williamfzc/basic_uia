from basic_uia import runner, device, utils

if __name__ == '__main__':
    device.connect_all_device()
    utils.load_all_cases()
    runner.run_all()
