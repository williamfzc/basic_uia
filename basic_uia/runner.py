from basic_uia import device, logger, utils


def run_all():
    case_dict = utils.CASE_MODULE_DICT
    device_dict = device.DEVICE_INSTANCE_DICT
    for case_name, case_item in case_dict.items():
        for each_device_id, each_device in device_dict.items():
            logger.info(
                'start case {} on device: {}'.format(
                    case_name,
                    each_device_id,
                )
            )
            # case_item.__dict__['device'] = each_device
            case_item.device = each_device
            case_item.before()
            case_item.run()
            case_item.after()
    logger.info('test end')
